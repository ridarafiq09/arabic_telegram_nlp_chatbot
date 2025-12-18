import os
from telegram.ext import Updater, MessageHandler, Filters
from model.test_inference import predict_intent
from nlp.entities import extract_entities
from core.logic import handle_intent


# MEMORY STORE
user_memory = {}

BOT_TOKEN = os.getenv("BOT_TOKEN")

if not BOT_TOKEN:
    raise RuntimeError("BOT_TOKEN environment variable is not set")


def handle_message(update, context):
    text = update.message.text
    chat_id = update.message.chat_id


    intent, confidence = predict_intent(text)
    entities = extract_entities(text)

   
    print("=" * 50)
    print(f"[USER] {text}")
    print(f"[AI ] Intent: {intent}")
    print(f"[AI ] Confidence: {round(confidence, 3)}")
    print(f"[NLP] Entities: {entities}")

    # remember product if mentioned
    if entities.get("product"):
        user_memory[chat_id] = entities["product"]

    # reuse memory if product not mentioned
    if (
        chat_id in user_memory
        and not entities.get("product")
        and any(w in text for w in ["مقاسات", "ألوان", "الألوان"])
    ):
        entities["product"] = user_memory[chat_id]

   
    reply = handle_intent(intent, entities, text)

   
    print(f"[BOT ] Reply: {reply}")
    print("=" * 50)

    update.message.reply_text(reply)



def main():
    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    print("Bot is running...")
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
