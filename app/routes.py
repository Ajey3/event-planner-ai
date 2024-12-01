import os
from flask import Blueprint, request, jsonify
import openai
from dotenv import load_dotenv

load_dotenv()

main = Blueprint('main', __name__)

openai.api_key = os.getenv("OPENAI_API_KEY")

@main.route('/')
def home():
    return "Welcome to the Event Planner AI!"

@main.route('/plan-event', methods=['POST'])
def plan_event():
    data = request.json
    user_query = data.get("query", "")

    if not user_query:
        return jsonify({"error": "Query is required"}), 400

    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=f"Help me plan an event: {user_query}",
            max_tokens=150,
            temperature=0.7
        )
        return jsonify({"response": response['choices'][0]['text'].strip()})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
