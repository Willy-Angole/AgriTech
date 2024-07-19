from django.shortcuts import render
from django.http import HttpResponse
import cv2
import numpy as np
from keras.models import load_model
import pickle
import joblib

# Load models
model_corn = load_model("AG_Corn_Plant_VGG19.h5")
model_cotton = load_model("AG_COTTON_plant_VGG19.h5")
model_grape = load_model("AI_Grape.h5")
model_potato = load_model("AI_Potato_VGG19.h5")
model_tomato = load_model("AI_Tomato_model_inception.h5")

COUNT = 0

def home(request):
    return render(request, 'index.html')

def leaf_detection(request):
    return render(request, 'leaf_detection.html')

def inputcotton(request):
    return render(request, 'prediction_cotton.html')

def inputcorn(request):
    return render(request, 'prediction_Corn.html')

def inputgrape(request):
    return render(request, 'prediction_Grape.html')

def inputpotato(request):
    return render(request, 'prediction_potato.html')

def inputtomato(request):
    return render(request, 'prediction_tomato.html')

def input_crop_recommendation(request):
    return render(request, 'crop_recommendation.html')

def submit(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = int(request.POST.get('phone'))
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        print("Name Of User:", name)
        print("Phone no:", phone)
        print("Email:", email)
        print("subject:", subject)
        print("message:", message)

        return render(request, 'index.html')
    else:
        return render(request, 'index.html')

def predictioncotton(request):
    global COUNT
    if request.method == 'POST':
        img = request.FILES['image']
        with open(f'static/img/{COUNT}.jpg', 'wb+') as destination:
            for chunk in img.chunks():
                destination.write(chunk)

        img_arr = cv2.imread(f'static/img/{COUNT}.jpg')
        img_arr = cv2.resize(img_arr, (224, 224))
        img_arr = img_arr / 255.0
        img_arr = img_arr.reshape(1, 224, 224, 3)
        predictions = model_cotton.predict(img_arr)
        prediction = np.argmax(predictions, axis=1)
        print(prediction[0])
        COUNT += 1
        if prediction[0] == 0:
            return render(request, 'Output.html', {'data': ["diseased cotton leaf", 'green']})
        elif prediction[0] == 1:
            return render(request, 'Output.html', {'data': ["diseased cotton plant", 'red']})
        elif prediction[0] == 2:
            return render(request, 'Output.html', {'data': ["fresh cotton leaf", 'red']})
        else:
            return render(request, 'Output.html', {'data': ["fresh cotton plant", 'red']})

# Similar view functions for predictioncorn, predictiongrape, predictionpotato, predictiontomato

def crop_recommendation(request):
    if request.method == 'POST':
        Nitrogen = float(request.POST['Nitrogen'])
        Phosphorus = float(request.POST['Phosphorus'])
        Potassium = float(request.POST['Potassium'])
        temperature = float(request.POST['temperature'])
        humidity = float(request.POST['humidity'])
        rainfall = float(request.POST['rainfall'])
        ph = float(request.POST['ph'])

        print(Nitrogen, Phosphorus, Potassium, temperature, humidity, rainfall, ph)

        with open("Crop_Recomandation_RF.pkl", 'rb') as file:
            Pickled_RF_Model = pickle.load(file)
        result = Pickled_RF_Model.predict([[Nitrogen, Phosphorus, Potassium, temperature, humidity, ph, rainfall]])
        crops = ["rice", "maize", "chickpea", "kidneybeans", "pigeonpeas", "mothbeans", "mungbean", "blackgram", "lentil",
                 "pomegranate", "banana", "mango", "grapes", "watermelon", "muskmelon", "apple", "orange", "papaya",
                 "coconut", "cotton", "jute", "coffee"]
        return render(request, 'crop_recommendation.html', {'data': [crops[result[0]], 'green']})
    else:
        return render(request, 'crop_recommendation.html')

def load_img(request):
    global COUNT
    return HttpResponse(open(f'static/img/{COUNT - 1}.jpg', 'rb'), content_type='image/jpeg')

