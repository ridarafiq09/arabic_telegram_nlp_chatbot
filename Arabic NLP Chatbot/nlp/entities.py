def extract_entities(text):
    entities = {}

    products = ["فستان", "حذاء", "جاكيت"]
    for p in products:
        if p in text:
            entities["product"] = p
            break

    if any(w in text for w in ["مقاسات", "المقاسات"]):
        entities["sizes"] = True

    if any(w in text for w in ["ألوان", "الألوان"]):
        entities["colors"] = True

    return entities
