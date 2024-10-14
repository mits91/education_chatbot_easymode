# education_chatbot_easymode
A chatbot for teachers easy to modify
# Scientific Assistant Chatbot

## Overview
The Scientific Assistant Chatbot is an educational chatbot powered by OpenAI's API and built with Flask. It answers scientific questions and is designed to be easily customized for different educational purposes.
Powered by OpenAI’s API and built using Flask, this chatbot answers students' questions based on predefined scientific keywords. The chatbot is easy to modify, allowing teachers to adapt it to various subjects and lessons.

## App Structure
1. app.py – Backend Logic
This Python file contains the core logic of the chatbot. It connects to the OpenAI API, filters relevant questions based on specific keywords, and serves the web interface using Flask.

Key Components:
OpenAI API Integration: Handles requests to the OpenAI API to generate responses.
Keyword Filtering: Ensures the chatbot only responds to specific topics by checking user inputs for relevant keywords.
Flask Web Server: Hosts the web application locally or on a server.

How to Customize app.py:
Change the API Key:

In app.py, you will find the following line:

openai.api_key = 'your-api-key-here'
Replace 'your-api-key-here' with your own OpenAI API key, which you can get from OpenAI's platform.
This allows the chatbot to use your account to generate answers.
Modify the Keywords:

The chatbot only responds to questions that include predefined keywords in Greek, located in the is_science_question function:
 ```bash
science_keywords = ["περιοδικός", "χημεία", "στοιχείο", "ενέργεια", "επιστήμη", ...]
 ```
To customize the chatbot for different topics (e.g., biology or physics), add or replace the keywords in this list. For example, to add biology-related keywords:
 ```bash
science_keywords = ["DNA", "κύτταρο", "αναπαραγωγή", "όργανο", "χλωροφύλλη", ...]
 ```
You can modify this list to suit any lesson or subject area.

## Adjust the System Prompt:

The chatbot’s behavior and personality are determined by the system message in the conversation:
 ```bash
{"role": "system", "content": "Είσαι ένας φιλικός επιστημονικός βοηθός. Απαντάς μόνο σε ερωτήσεις σχετικές με την επιστήμη. Δίνεις πλήρεις απαντήσεις."}
 ```
You can change the chatbot's role by updating this message to fit your teaching context. For example:
 ```bash
{"role": "system", "content": "Είσαι ένας φιλικός βοηθός μαθηματικών. Απαντάς μόνο σε ερωτήσεις σχετικές με τα μαθηματικά."}
 ```
2. index.html – Frontend Interface
This file contains the basic web interface that users interact with. It includes an input field for questions and a section to display the chatbot’s responses.

Customizing index.html:
Change the Logo or Image:

The chatbot interface includes a placeholder for an image (e.g., a logo):
 ```bash
<img src="{{ url_for('static', filename='logo.png') }}" alt="Chatbot Image">
 ```
To replace this image, upload a new one in the /static folder and update the filename in the src attribute.

Update the Chatbox Style:
The appearance of the chat interface (e.g., colors, fonts) can be modified in the <style> section of index.html. 
Feel free to update these to match your school's branding or your lesson's theme.


## Running the Chatbot Locally

### Steps to Set Up and Run
1. Clone the repository:  
   Download the chatbot files by running the following command in your terminal or command prompt:
   ```bash
   git clone https://github.com/mits91/education_chatbot_easymode.git
   cd education_chatbot_easymode
Set up Python and install requirements:
#Make sure you have Python 3 installed. Then, run the following commands:
 ```bash
pip install -r requirements.txt
```

## Get your OpenAI API key:
Go to OpenAI's platform and create an account (if you don’t have one already). Then, get your API key.

Set up your API key:
In your terminal, set the API key as an environment variable. Replace your-api-key-here with your actual key:

For Linux/macOS:
```bash
export OPENAI_API_KEY='your-api-key-here'
```

For Windows:
```bash
set OPENAI_API_KEY='your-api-key-here'
```

# Run the chatbot:
Now, you’re ready to run the app. Use this command to start it:
```bash
flask run
```
Access the chatbot:
Open your web browser and go to http://127.0.0.1:5000. You should see the chatbot ready to answer questions!


## Deploying the Chatbot on a Server (e.g., Heroku)
Steps to Deploy
Set up a Heroku account:
If you don’t have a Heroku account, sign up at heroku.com. Install the Heroku CLI on your computer.

Log in to Heroku:
Open your terminal or command prompt and log in to Heroku:
```bash
heroku login
```

Create a Heroku app:
Inside the folder where the chatbot files are stored, run this command to create a new app on Heroku:
```bash
heroku create
```

Add your OpenAI API key to Heroku:
Set your OpenAI API key as an environment variable on Heroku:
```bash
heroku config:set OPENAI_API_KEY='your-api-key-here'
```

Deploy the code to Heroku:
Push your code to Heroku’s servers using these commands:
```bash
git add .
git commit -m "Initial commit"
git push heroku main
```

Start the app on Heroku:
Make sure your app is running:
```bash
heroku ps:scale web=1
```
Access the chatbot:
Heroku will provide a URL for your live chatbot. Open that link in your browser to start using the chatbot




