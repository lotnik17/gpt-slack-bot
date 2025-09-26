import os
from flask import Flask, request, jsonify
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
import openai

app = Flask(__name__)

openai.api_key = os.environ.get("OPENAI_API_KEY")
slack_token = os.environ.get("SLACK_BOT_TOKEN")
client = WebClient(token=slack_token)

@app.route("/")
def home():
    return "GPT Slack Bot działa."

@app.route("/slack/events", methods=["POST"])
def slack_events():
    data = request.get_json()
    event = data.get("event", {})
    text = event.get("text", "")
    channel = event.get("channel", "")

    if "bot_id" not in event:
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": text}]
            )
            reply = response["choices"][0]["message"]["content"]
            client.chat_postMessage(channel=channel, text=reply)
        except SlackApiError as e:
            print("Slack API error:", e.response["error"])

    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
