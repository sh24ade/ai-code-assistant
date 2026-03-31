from flask import Flask, request, jsonify, render_template
from openai import OpenAI
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Home route
@app.route("/")
def home():
    return render_template("index.html")


# Generate code from prompt
@app.route("/generate", methods=["POST"])
def generate_code():
    user_input = request.json.get("prompt")

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": "You are an expert software engineer. Generate clean, efficient, well-structured code with brief explanation."
                },
                {
                    "role": "user",
                    "content": user_input
                }
            ]
        )

        return jsonify({
            "output": response.choices[0].message.content
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Improve existing code
@app.route("/improve", methods=["POST"])
def improve_code():
    code = request.json.get("code")

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": "Improve this code for readability, performance, and best practices. Return improved version with explanation."
                },
                {
                    "role": "user",
                    "content": code
                }
            ]
        )

        return jsonify({
            "output": response.choices[0].message.content
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Explain code clearly
@app.route("/explain", methods=["POST"])
def explain_code():
    code = request.json.get("code")

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": "Explain this code clearly and simply so a developer can understand it quickly."
                },
                {
                    "role": "user",
                    "content": code
                }
            ]
        )

        return jsonify({
            "output": response.choices[0].message.content
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Run the app
if __name__ == "__main__":
    app.run(debug=True)
