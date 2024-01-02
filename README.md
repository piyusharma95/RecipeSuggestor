# Recipe Suggestor

## Introduction
Recipe Suggestor is a web application built with Django and JavaScript, integrating the Spoonacular API. It allows users to input ingredients they have and suggests recipes that can be made with those ingredients. Users can click on any suggested recipe to view detailed steps for preparation in a modal popup.

## Features
- Ingredient input with autocomplete functionality.
- Recipe suggestions based on provided ingredients.
- Clickable recipes with detailed preparation steps in a modal popup.

## Setup and Installation

To get the project up and running on your local machine, follow these steps:

### Prerequisites
- Python 3.8 or higher
- Django 3.2 or higher
- Requests library for Python
- A Spoonacular API key

### Installation

#### 1. Clone the Repository
git clone https://github.com/your-username/recipe-suggestor.git
cd recipe-suggestor

#### 2. Set Up a Virtual Environment (Optional)
For Unix or MacOS:
python -m venv venv
source venv/bin/activate
For Windows:
python -m venv venv
venv\Scripts\activate

#### 3. Install Dependencies
pip install django requests

#### 4. Set Up Spoonacular API Key
Create a `API_KEY` variable in the project settings file and add your Spoonacular API key:
API_KEY = 'your_api_key_here'

#### 5. Run the Development Server
python manage.py runserver
The application should now be running on [http://localhost:8000](http://localhost:8000).

## Usage
Start by entering ingredients in the input box on the homepage. The application will suggest recipes based on the entered ingredients. Click on any recipe title to view detailed steps and information.

## Contributing
Contributions to the Recipe Suggestor are welcome! Start submitting pull requests.
