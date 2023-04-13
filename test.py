import matching_algorithm as ma

input_array = ['O004', 'V031', 'D021', 'A040','O001', 'D021', 'D054']

def find_last_true_string(input_array):
    resArray=[]
    last_true_string = ""
    last_meaning =""
    for i,input_element in enumerate(input_array):
        if i != 0 :
            if iter+1 < len(input_array):
                i = iter + 1
            else: 
                break
        input_str = str(input_array[i])
        meaning,result = ma.dictionary_matching(input_str)
        iter=i
        # x =""
        while result:
            if input_array[iter] != input_array[-1]:
                temp=input_str +" "+ str(input_array[iter+1])
                meaning,result = ma.dictionary_matching(temp)
                if result:
                    print("b:" + meaning)
                    input_str = input_str +" "+ str(input_array[iter+1])
                    last_true_string = input_str
                    last_meaning = meaning
                    iter+=1
            else:
                last_true_string=input_str
                last_meaning = meaning
                break
        
    
        resArray.append(last_meaning)
    # resArray2,_=ma.dictionary_matching(resArray)
    return resArray


arr = find_last_true_string(input_array)
print("-------------------------------------------------------")
for i in arr:
    print (i)
