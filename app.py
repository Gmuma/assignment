from flask import Flask, request, jsonify, render_template
import openai
import os
from dotenv import load_dotenv

# Load API key from .env
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    # Ensure the request contains JSON and is a valid request
    if not request.is_json:
        return jsonify({"error": "Request must be in JSON format"}), 400
    
    user_message = request.json.get("message")
    if not user_message:
        return jsonify({"error": "No message provided"}), 400

    try:
        # OpenAI API request
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a customer support assistant."},
                {"role": "user", "content": user_message},
            ],
        )
        bot_reply = response['choices'][0]['message']['content']
        return jsonify({"reply": bot_reply})
    
    except openai.error.OpenAIError as e:
        # Catch OpenAI specific errors
        return jsonify({"error": f"OpenAI API error: {str(e)}"}), 500
    except Exception as e:
        # Catch any other exceptions
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(debug=True)
