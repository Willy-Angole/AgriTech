from django.urls import path
from . import views
# from .views import scan_image

urlpatterns = [
    path('', views.home, name='home'),
    path('packages/', views.packages, name='packages'),
    path('404/', views.not_found, name='not_found'),
   
]


    # path('leaf_detection/', views.leaf_detection, name='leaf_detection'),
    # path('inputcotton/', views.inputcotton, name='inputcotton'),
    # path('inputcorn/', views.inputcorn, name='inputcorn'),
    # path('inputgrape/', views.inputgrape, name='inputgrape'),
    # path('inputpotato/', views.inputpotato, name='inputpotato'),
    # path('inputtomato/', views.inputtomato, name='inputtomato'),
    # path('input_crop_recommendation/', views.input_crop_recommendation, name='input_crop_recommendation'),
    # path('data/', views.submit, name='submit'),
    # path('predictioncotton/', views.predictioncotton, name='predictioncotton'),
    # path('predictioncorn/', views.predictioncorn, name='predictioncorn'),
    # path('predictiongrape/', views.predictiongrape, name='predictiongrape'),
    # path('predictionpotato/', views.predictionpotato, name='predictionpotato'),
    # path('predictiontomato/', views.predictiontomato, name='predictiontomato'),
    # path('crop_recommendation/', views.crop_recommendation, name='crop_recommendation'),
    # path('load_img/', views.load_img, name='load_img'),
    # path('scan-image/', views.scan_image, name='scan_image'),
