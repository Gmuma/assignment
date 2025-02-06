                                                                          **Chatbot Application**

**Overview**

This project demonstrates how to build a simple chatbot application using Flask, OpenAI API, HTML, CSS, and JavaScript. The chatbot serves as a customer support assistant capable of handling basic customer queries.

**Features**
Responsive user interface

Backend powered by Flask

AI-generated responses using OpenAI's GPT-3.5 Turbo

Interactive chat experience

**Prerequisites**

Ensure you have the following installed:

Python 3.x

Pip package manager

Installation Steps

cd chatbot-app

2. Install Required Libraries

**pip install openai flask python-dotenv**

3. Set Up OpenAI API Key

Sign up for an account at OpenAI.

Obtain your API key.

**Create a .env file in the project root directory and add your API key:**

**OPENAI_API_KEY=your_openai_api_key**

Folder Structure

chatbot-app/

├── app.py            # Main Flask application

├── templates/

│   └── index.html    # Frontend HTML

├── static/

│   └── style.css     # Frontend CSS

└── .env              # API key configuration

**Usage**

1. Run the Application

python app.py

2. Access the Chatbot

Open a web browser and navigate to:

http://127.0.0.1:5000

How It Works

**Backend**

The Flask application serves the frontend and provides a /chat endpoint to process user queries.

The endpoint uses OpenAI’s GPT-3.5 Turbo model to generate responses.

**Frontend**

The user interface is built using HTML, CSS, and JavaScript.

User messages are sent to the backend via a POST request.

Bot responses are displayed dynamically on the webpage.

**File Descriptions**

1. app.py

Handles routing and interaction with the OpenAI API.

2. index.html

Defines the structure of the user interface.

3. style.css

Provides the styling for the chatbot interface.

4. .env

Stores sensitive environment variables such as the OpenAI API key.

Example Interaction

User: What are your support hours?

Bot: Our support hours are from 9 AM to 6 PM, Monday to Friday.

**Technologies Used**

Backend: Flask, Python

AI: OpenAI GPT-3.5 Turbo

Frontend: HTML, CSS, JavaScript

**Troubleshooting**

If the application doesn't start, ensure all libraries are installed correctly using pip install.

If the chatbot fails to respond, verify your OpenAI API key in the .env file.

Future Enhancements

Add user authentication.

Implement persistent chat history.

Expand chatbot functionality for domain-specific queries.

**License**

This project is open source and free to use. Contributions are welcome!

