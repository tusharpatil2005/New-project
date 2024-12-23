from flask import Flask, request, jsonify, render_template
import openai

# Initialize Flask app
app = Flask(__name__)

# Replace with your OpenAI API key
openai.api_key = "YOUR_OPENAI_API_KEY"

# Default route to serve the index.html
@app.route("/")
def home():
    return render_template("index.html")

# API route to process input and get a response from OpenAI
@app.route("/api", methods=["POST"])
def chat_api():
    try:
        # Get input data from POST request
        user_input = request.json.get("message", "")
        if not user_input:
            return jsonify({"error": "Message parameter is required"}), 400

        # Send the user input to OpenAI's API
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # or "gpt-4"
            messages=[
                {"role": "system", "content": "You are an expert agricultural advisor."},
                {"role": "user", "content": user_input}
            ]
        )

        # Extract the bot's response
        bot_message = response["choices"][0]["message"]["content"]

        # Return the bot's response
        return jsonify({"reply": bot_message})

    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"error": "Something went wrong"}), 500

# Run the Flask server
if __name__ == "__main__":
    app.run(debug=True)
