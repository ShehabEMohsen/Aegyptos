import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import torch
import torchvision.transforms as transforms
from PIL import Image
from PIL import ImageFile
import werkzeug
import matching_algorithm as ma
import googletrans
from googletrans import *

app = Flask(__name__)

# load pkl model
model = pickle.load(open("squeezenetuntrained.pkl", "rb"))

@app.route('/predict', methods=['POST'])
def predict():
    if(request.method == 'POST'):
        imageFile = request.files['image']
        filename = werkzeug.utils.secure_filename(imageFile.filename)
        imageFile.save(filename)
        input_image = Image.open(filename).convert('RGB')
        preprocess = transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
        ])
        input_tensor = preprocess(input_image)
        input_batch = input_tensor.unsqueeze(0)
        if torch.cuda.is_available():
            input_batch = input_batch.to('cuda')
            model.to('cuda')

        with torch.no_grad():
            output = model(input_batch)
        probabilities = torch.nn.functional.softmax(output[0], dim=0)

    with open("classes_names.txt") as f:
        categories = [s.strip() for s in f.readlines()]
    top5_prob, top5_catid = torch.topk(probabilities, 5)
    for i in range(top5_prob.size(0)):
        print(categories[top5_catid[i]], top5_prob[i].item())
    
    top1 = categories[top5_catid[0]]
    
    matchingText=ma.dictionary_matching(top1)
    translator = googletrans.Translator()
    translate=translator.translate(matchingText,dest='arabic')
    matchingTranslation = translate.text
    
    matchingTextPronunciation=ma.dictionary_matching_pronunciation(top1)
    
    return jsonify({'prediction': matchingText,'gardinerCode':matchingTextPronunciation,'translation': matchingTranslation})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000,debug=True)