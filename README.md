# education_chatbot_easymode
A chatbot for teachers easy to modify
# Scientific Assistant Chatbot

## Overview
The **Scientific Assistant Chatbot** is an educational chatbot powered by OpenAI's API and built with Flask. It answers scientific questions and is designed to be easily customized for different educational purposes.

## Running the Chatbot Locally

### Steps to Set Up and Run
1. **Clone the repository**:  
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




