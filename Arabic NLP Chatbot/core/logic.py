from db.queries import get_product

def handle_intent(intent, entities, text=None):
    text = text or ""

    # RULES
    if any(w in text for w in ["متى", "تفتح", "تفتحون", "دوام", "تقفل"]):
        return "نفتح من 9 صباحاً إلى 5 مساءً"

    if any(w in text for w in ["توصيل", "توصلون", "شحن"]):
        return "نعم، نوفر خدمة التوصيل داخل المدينة"

    if any(w in text for w in ["مرحبا", "السلام", "هلا"]):
        return "أهلاً وسهلاً! كيف أقدر أساعدك؟"

    if any(w in text for w in ["شكرا", "شكرًا", "يعطيك"]):
        return "العفو! يسعدني خدمتك 🌸"

    # DATA + INTENT
    product = entities.get("product")
    data = get_product(product)

    # PRODUCT DETAILS FIRST 
    if data:
       if entities.get("colors"):
        return f"الألوان المتوفرة: {data['colors']}"

    if entities.get("sizes"):
        return f"المقاسات المتوفرة: {data['sizes']}"

# PRICE LAST
    if intent == "PRICE_INQUIRY":
       if not product:
        return "عذرًا، هذا المنتج غير موجود"
    data = get_product(product)
    if data:
        return f"سعر {data['name']} هو {data['price']} ريال"
    return "عذرًا، هذا المنتج غير موجود"
  


    if intent == "PRODUCT_INFO":
        if not data:
            return "المنتج غير موجود"

        if "sizes" in entities:
            return f"المقاسات المتوفرة: {data['sizes']}"

        if "colors" in entities:
            return f"الألوان المتوفرة: {data['colors']}"

        return "نعم، المنتج متوفر حالياً"

    return "ممكن توضح طلبك أكثر؟ مثل السعر أو التوصيل"
