""" import os
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
 """

# from flask import Flask, Blueprint, request, jsonify

# main = Blueprint('main', __name__)

# @main.route('/')
# def home():
#     return "Welcome to the Event Planner AI!"

# @main.route('/plan-event', methods=['POST'])
# def plan_event():
#     data = request.json
#     user_query = data.get("query", "")

#     if not user_query:
#         return jsonify({"error": "Query is required"}), 400

#     # Mocked response
#     mocked_responses = {
#         "birthday party": "Plan a superhero-themed birthday party with costumes, a cake, and fun games for kids.",
#         "team-building event": "Organize an outdoor team-building event with trust exercises, obstacle courses, and collaborative problem-solving activities.",
#         "wedding": "Plan a wedding with a beautiful outdoor ceremony, floral decorations, and a dinner reception with live music."
#     }

#     # Find a response or use a default
#     response = mocked_responses.get(
#         user_query.lower(), 
#         "I'm sorry, I don't have a response for that event type."
#     )

#     return jsonify({"response": response})


import openai
from flask import Blueprint, request, jsonify

# Set your OpenAI API key
openai.api_key = 'w5CcX2aqXL30bZdDKM3vH3CiSPrPAh3ziKJhcQ9hKNmZd1UlhBPqkaKKPP3fTMIosX5-oIHnT3BlbkFJn1Iws2uB8NsfrJF9Q_UKKEMxj7PDYZ_oj9YN0E_dpMyrPEUedXAQ9JZj84wtxmc3AkmvW1oBsA'

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return "Welcome to the Event Planner AI!"

@main.route('/plan-event', methods=['POST'])
def plan_event():
    data = request.json
    user_query = data.get("query", "")

    if not user_query:
        return jsonify({"error": "Query is required"}), 400

    # Create a prompt for the AI
    prompt = f"Suggest event ideas for a {user_query}."

    try:
        # Make the request to OpenAI's API to generate a response
        response = openai.Completion.create(
            engine="text-davinci-003",  # You can use GPT-4 if you have access
            prompt=prompt,
            max_tokens=150  # You can adjust the number of tokens to fit your needs
        )

        # Extract the response from OpenAI
        ai_response = response.choices[0].text.strip()

        return jsonify({"response": ai_response})

    except Exception as e:
        return jsonify({"error": str(e)}), 500
