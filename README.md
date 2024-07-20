# AgriAlert - Leaf Detection and Crop Recommendation System

## Project Overview

AgriAlert is a Django-based web application designed to help farmers with leaf disease detection and crop recommendations. The application uses pre-trained machine learning models to identify diseases in various crops and provide appropriate recommendations.

## Features

- **Leaf Detection:** Identify diseases in leaves of various crops like corn, cotton, grape, potato, and tomato.....    we are focusing on corn(maize first)
- **Crop Recommendation:** Get crop recommendations based on soil and environmental conditions.

## Setup Instructions

### Prerequisites

Ensure you have the following installed on your machine:

- Python 3.8 or higher
- pip
- virtualenv (optional but recommended)
- Git

### Clone the Repository

Clone the project repository from GitHub to your local machine:

### Git bash or Terminal for mac/linux users
git clone git@github.com:Willy-Angole/AgriTech.git

cd agrialert

### Create a virtual environment
python -m venv venv

### Activate the virtual environment
### On Windows
venv\Scripts\activate

### On macOS/Linux
source venv/bin/activate

### Install Dependencies
pip install -r requirements.txt

### Configure the Database
python manage.py makemigrations
python manage.py migrate

### Start the Django development server:
python manage.py runserver


### Project Structure
agrialert/
    AgriTech/
        __init__.py
        ...
    detection/
        __init__.py
        admin.py
        apps.py
        migrations/
        models.py
        models/
            AG_Corn_Plant_VGG19.h5
            AG_COTTON_plant_VGG19.h5
            AI_Grape.h5
            AI_Potato_VGG19.h5
            AI_Tomato_model_inception.h5
        tests.py
        urls.py
        views.py
    manage.py
    static/
        css/
            tooplate-style.css
        images/
            cotton-plant-leaves-1.jpg
    templates/
        leaf_detection.html
        ...
    README.md
    requirements.txt
    venv/
        ...



