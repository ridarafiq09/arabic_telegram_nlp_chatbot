import sys
import os

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, ROOT_DIR)


import streamlit as st

from model.infer import predict_intent
from nlp.entities import extract_entities
from core.logic import handle_intent

CONFIDENCE_RULES = {
    "GREETING": 0.0,
    "PRICE_INQUIRY": 0.45,
    "BUSINESS_HOURS": 0.30,
    "DELIVERY_INFO": 0.30,
    "PRODUCT_INFO": 0.45
}

st.set_page_config(page_title="Arabic Business Chatbot", layout="centered")
st.title("🛍️ Arabic Business Chatbot")

if "history" not in st.session_state:
    st.session_state.history = []

# INPUT
user_text = st.text_input("اكتب رسالتك هنا:")

if st.button("إرسال") and user_text.strip():
    text = user_text.strip().replace("؟", "").strip()



    # Business hours
    if "تفتح" in text or "دوام" in text or "تقفل" in text:
        reply = "نفتح من 9 صباحاً إلى 5 مساءً"

    # Delivery
    elif "توصيل" in text:
        reply = "نعم، نوفر خدمة التوصيل داخل المدينة"

    
    else:
        intent, confidence = predict_intent(text)
        required_conf = CONFIDENCE_RULES.get(intent, 0.5)

        # Vague greeting → clarify
        if intent == "GREETING" and confidence < 0.4:
            reply = "هل يمكنك توضيح طلبك أكثر؟"

        elif confidence < required_conf:
            reply = "هل يمكنك توضيح طلبك أكثر؟"

        else:
            entities = extract_entities(text)
            reply = handle_intent(intent, entities)

    st.session_state.history.append(("أنت", user_text))
    st.session_state.history.append(("البوت", reply))
