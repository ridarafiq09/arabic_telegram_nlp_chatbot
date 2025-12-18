import sys
import os
import requests
from flask import Flask, request, jsonify

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


from model.test_inference import predict_intent
from nlp.entities import extract_entities
from core.logic import handle_intent


app = Flask(__name__)

TELEGRAM_TOKEN = ""
TELEGRAM_API_URL = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"


CONFIDENCE_RULES = {
    "GREETING": 0.0,
    "PRICE_INQUIRY": 0.45,
    "BUSINESS_HOURS": 0.30,
    "DELIVERY_INFO": 0.30,
    "PRODUCT_INFO": 0.45
}


# CHAT API (for testing / Streamlit)

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()

    if not data or "message" not in data:
        return jsonify({"error": "No message provided"}), 400

    text = data["message"].strip().replace("؟", "")

    #  RULES 
    if any(word in text for word in ["تفتح", "تفتحون", "دوام", "متى", "تقفل"]):
        reply = "نفتح من 9 صباحاً إلى 5 مساءً"

    elif "توصيل" in text:
        reply = "نعم، نوفر خدمة التوصيل داخل المدينة"

    else:
        intent, confidence = predict_intent(text)
        entities = extract_entities(text)
        reply = handle_intent(intent, entities)

    return jsonify({"reply": reply})


# TELEGRAM WEBHOOK

@app.route("/telegram", methods=["POST"])
def telegram_webhook():
    data = request.get_json()

    if not data or "message" not in data:
        return "ok"

    chat_id = data["message"]["chat"]["id"]
    text = data["message"].get("text", "")

    # reuse SAME 
    intent, confidence = predict_intent(text)
    entities = extract_entities(text)
    reply = handle_intent(intent, entities)

    # send reply back to Telegram
    requests.post(
        TELEGRAM_API_URL,
        json={
            "chat_id": chat_id,
            "text": reply
        }
    )

    return "ok"


if __name__ == "__main__":
    app.run(debug=True)
