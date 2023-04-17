import os
import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import torch
import torchvision.transforms as transforms
from PIL import Image
from PIL import ImageFile
import werkzeug
import matching_algorithm as ma
import matching_algorithm_pronunciation as pronunciation
import googletrans
from googletrans import *
import cv2
from imutils import contours
from skimage.filters import threshold_otsu

app = Flask(__name__)

# load pkl model
model = pickle.load(open("new squeezenet(finetuned).pkl", "rb"))

image_array = []

# def Otsu(myImage):
#   sample_image = cv2.imread(myImage)
#   img = cv2.cvtColor(sample_image,cv2.COLOR_BGR2RGB)

#   # plt.axis('off')
#   # plt.imshow(img)

#   img_gray=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)

#   thresh = threshold_otsu(img_gray)
#   img_otsu  = img_gray < thresh

#   # plt.imshow(img_otsu)

#   filtered = filter_image(img, img_otsu)
#   filteredBW=cv2.cvtColor(filtered,cv2.COLOR_RGB2GRAY)
#   return filteredBW



# def filter_image(image, mask):

#     r = image[:,:,0] * mask
#     g = image[:,:,1] * mask
#     b = image[:,:,2] * mask

#     return np.dstack([r,g,b])
# global deleteCounterImage
# deleteCounterImage=0
def cropping(myImage):
    global deleteCounterImage 
    deleteCounterImage = 0  # default value
    # Load the YOLOv3 network
    net = cv2.dnn.readNet("yolov3.weights", "yolov3.cfg")

    # Set confidence threshold and non-maximum suppression threshold for YOLO
    conf_threshold = 0.5
    nms_threshold = 0.4

    # Load the input image
    image = cv2.imread(myImage)

    # Convert image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Threshold image
    _, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)

    # Find contours
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)


    # Iterate over the contours
    for i, contour in enumerate(contours):
        deleteCounterImage=deleteCounterImage+1
        # Get bounding box coordinates
        x, y, w, h = cv2.boundingRect(contour)

        # Crop the image using the bounding box coordinates
        crop_img = image[y:y+h, x:x+w]

        # Create a blob from the cropped image
        blob = cv2.dnn.blobFromImage(crop_img, 1 / 255.0, (416, 416), swapRB=True, crop=False)

        # Pass the blob through the network to perform object detection
        net.setInput(blob)
        layer_names = net.getLayerNames()
        output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers()]
        outputs = net.forward(output_layers)

        boxes = []
        confidences = []

        # Iterate over the output layers
        for output in outputs:
            # Iterate over the detected objects
            for detection in output:
                # Extract the class ID and confidence score
                scores = detection[5:]
                class_id = np.argmax(scores)
                confidence = scores[class_id]

                # Check if the detected object is above the confidence threshold
                if confidence > conf_threshold:
                    # Compute the bounding box coordinates of the detected object
                    center_x = int(detection[0] * w)
                    center_y = int(detection[1] * h)
                    box_width = int(detection[2] * w)
                    box_height = int(detection[3] * h)
                    left = int(center_x - box_width / 2)
                    top = int(center_y - box_height / 2)

                    # Apply non-maximum suppression to remove overlapping boxes
                    box = [left, top, box_width, box_height]
                    
                    boxes.append(box)
                    confidences.append(float(confidence))
        
        # Apply non-maximum suppression to remove overlapping boxes
        indices = cv2.dnn.NMSBoxes(boxes, confidences, conf_threshold, nms_threshold)

        # Draw the final bounding boxes on the cropped image
        for i in indices:
            i = i[0]
            box = boxes[i]
            x, y, w, h = box
            cv2.rectangle(crop_img, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Save the cropped image to a file
        filename = f"crop_{i}.png"
        cv2.imwrite(filename, crop_img)
        

    for i, contour in enumerate(contours):
        print("bassem")
        # Load the input image
        image = cv2.imread(f"crop_{i}.png")

        # Get the original dimensions of the image
        height, width, _ = image.shape

        # Calculate the aspect ratio of the image
        aspect_ratio = width / height

        # Set the desired output size (height or width)
        output_size = 224

        # Calculate the other dimension based on the aspect ratio
        if width > height:
            new_width = output_size
            new_height = int(new_width / aspect_ratio)
        else:
            new_height = output_size
            new_width = int(new_height * aspect_ratio)

        # Resize the image
        resized_image = cv2.resize(image, (new_width, new_height))
        
        # Calculate the coordinates to copy the resized image onto the new image
        x_offset = int((output_size - new_width) / 2)
        y_offset = int((output_size - new_height) / 2)

        # Save the resized image to a file
        cv2.imwrite(f"resize{i}.png", resized_image)

        # Load the resized image from file
        resized_image = cv2.imread(f"resize{i}.png")

        # Convert the image to grayscale
        gray = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)

        # Apply Otsu's thresholding method to get a binary image
        thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU + cv2.THRESH_BINARY)[1]

        # Invert the binary image
        inv = cv2.bitwise_not(thresh)

        # Save the segmented image to a file
        cv2.imwrite(f"seg_img{i}.png", inv)

        # Load the segmented image from file
        seg_img = cv2.imread(f"seg_img{i}.png")

        # Create a new blank image with the desired output size
        new_image = np.zeros((output_size, output_size, 3), np.uint8)
        new_image[:, :] = (0, 0, 0)  # fill with black pixels

        # Copy the segmented image onto the new image with black pixels
        new_image[y_offset:y_offset+new_height, x_offset:x_offset+new_width] = seg_img

        # Save the final image to a file
        cv2.imwrite(f"final{i}.png", new_image)

        image_array.append(new_image)

        # # Create a new blank image with the desired output size
        # new_image = np.zeros((output_size, output_size, 3), np.uint8)
        # new_image[:, :] = (255, 255, 255)  # fill with black pixels

        # # Calculate the coordinates to copy the resized image onto the new image
        # x_offset = int((output_size - new_width) / 2)
        # y_offset = int((output_size - new_height) / 2)

        # # Copy the resized image onto the new image with black pixels
        # new_image[y_offset:y_offset+new_height, x_offset:x_offset+new_width] = resized_image

        # # Save the final image to a file
        # cv2.imwrite(f"resize{i}.png", new_image)

        # image = cv2.imread(f"resize{i}.png")
        # gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        # thresh = cv2.threshold(gray,0,255,cv2.THRESH_OTSU + cv2.THRESH_BINARY)[1]
        # inv = cv2.bitwise_not(thresh)
        # seg_img = cv2.imwrite(f"seg_img{i}.png", inv)
        # image_array.append(seg_img)



@app.route('/predict', methods=['POST'])
def predict():
    if(request.method == 'POST'):
        
        imageFile = request.files['image']
        filename = werkzeug.utils.secure_filename(imageFile.filename)
        imageFile.save(filename)
        cropping(filename)
        results = ""
        for i in range(deleteCounterImage):
            # cv2.imwrite('segmented_image.png', image)
            # input_image = Image.open('segmented_image.png').convert('RGB')
            input_image = Image.open(f'final{i}.png').convert('RGB')

            preprocess = transforms.Compose([
                transforms.Resize(256),
                transforms.CenterCrop(224),
                transforms.ToTensor(),
                transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
                # transforms.Pad(50),
            ])
            input_tensor = preprocess(input_image)
            # input_tensor = preprocess(Image.fromarray(i))
            input_batch = input_tensor.unsqueeze(0)
            if torch.cuda.is_available():
                input_batch = input_batch.to('cuda')
                model.to('cuda')

            with torch.no_grad():
                output = model(input_batch)

            # Tensor of shape 1000, with confidence scores over Aegyptos' 1072 classes
            print(output[0])
            # The output has unnormalized scores. To get probabilities, you can run a softmax on it.
            probabilities = torch.nn.functional.softmax(output[0], dim=0)

            # Read the categories
            #Basma
            with open("classes_names.txt", "r") as f:

            #Bassem
            # with open("D:/Ahmed Bassem/MIU\Year 4/Graduation Project/classes_names.txt", "r") as f:
                categories = [s.strip() for s in f.readlines()]
            # Show top categories per image
            top5_prob, top5_catid = torch.topk(probabilities, 5)
            for i in range(top5_prob.size(0)):
                print(categories[top5_catid[i]], top5_prob[i].item())

            top1 = categories[top5_catid[0]]
            print(top1)
            # results = results + top1 + " "
            results += " "+ top1
    
        updated_results = results.replace(" ", "", 1)

        matchingText=ma.dictionary_matching(updated_results)
        translator = googletrans.Translator()
        translate=translator.translate(matchingText,dest='arabic')
        matchingTranslation = translate.text
        
        matchingTextPronunciation=pronunciation.dictionary_matching_pronunciation(updated_results)
        
        os.remove(filename)
        for i in range(deleteCounterImage):
            removeCrop = f"crop_{i}.png"
            removeSegImg = f"seg_img{i}.png"
            removeFinal = f"final{i}.png"
            removeResize = f"resize{i}.png"
            try:
                os.remove(removeCrop)
                os.remove(removeSegImg)
                os.remove(removeFinal)
                os.remove(removeResize)
            except FileNotFoundError:
                pass
            
        return jsonify({'prediction': matchingText,'translation': matchingTranslation,'gardinerCodePronunciation':matchingTextPronunciation})



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000,debug=True)