from flask import Flask, request
import requests

app = Flask(__name__)

PAGE_ACCESS_TOKEN = "PUT_PAGE_ACCESS_TOKEN_HERE"

def reply(comment_id, text):
    url = f"https://graph.facebook.com/v19.0/{comment_id}/comments"
    data = {
        "access_token": PAGE_ACCESS_TOKEN,
        "message": text
    }
    requests.post(url, data=data)

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json()

    try:
        value = data["entry"][0]["changes"][0]["value"]
        comment_text = value["message"].lower()
        comment_id = value["comment_id"]

        if "السعر" in comment_text or "الثمن" in comment_text:
            reply(comment_id, "مرحبا، السعر موضح في الخاص")

        elif "كيف" in comment_text or "طريقة" in comment_text:
            reply(comment_id, "مرحبا، طريقة التسجيل سهلة ومذكورة في الإعلان")

    except Exception as e:
        print(e)

    return "ok", 200
