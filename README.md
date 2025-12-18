# Arabic Transformer-Powered Telegram Chatbot

## Overview

This project is an **applied Arabic NLP chatbot system** built using **Python** and **Telegram**.

The chatbot is designed to handle customer support–style queries in Arabic, such as questions about products, prices, sizes, colors, delivery, and business hours.
It combines a **transformer-based intent classification model (MARBERT)** with **rule-based logic** and a **SQLite database** to provide accurate, controlled, and reliable responses.

The project demonstrates how **modern NLP models are integrated into real software systems**, rather than used in isolation.

---

## Key Features

* Arabic Telegram chatbot interface
* Transformer-based intent classification (MARBERT)
* Rule-based entity extraction for products and attributes
* SQLite database for structured business data
* Multi-turn conversation memory (context awareness)
* Modular, maintainable project structure

---

## System Architecture

```
User (Telegram)
      ↓
Telegram Bot Interface
      ↓
Transformer Model (Intent Classification)
      ↓
Entity Extraction (Rule-Based)
      ↓
Business Logic
      ↓
SQLite Database
      ↓
Response to User
```

This hybrid design ensures:

* **Language understanding** is handled by the transformer model
* **Business decisions** remain deterministic and safe

---

## Technologies Used

* Python
* Hugging Face Transformers
* MARBERT (Arabic Transformer Model)
* PyTorch
* SQLite
* Telegram Bot API

---

## Project Structure

```
Arabic NLP Chatbot/
│
├── telegram_bot.py        # Telegram bot entry point
├── core/                 # Business logic and rules
├── nlp/                  # Entity extraction
├── model/                # Transformer inference code
├── training/             # Model training / fine-tuning
├── data/                 # Training data
├── db/                   # SQLite database & queries
├── requirements.txt
└── README.md
```

---

## Example Interaction

**User**

```
كم سعر الفستان؟
```

**Bot**

```
سعر الفستان هو 120 ريال
```

**User**

```
ما هي المقاسات؟
```

**Bot**

```
المقاسات المتوفرة: S, M, L
```

> The chatbot correctly remembers the previously mentioned product and continues the conversation naturally.

---

## Model Training (Optional)

The transformer model can be trained or fine-tuned using:

```bash
python training/train_marbert.py
```

The trained model is then loaded for **intent inference** inside the Telegram chatbot.

> Note: Trained model weights are excluded from the repository due to GitHub file size limits.

---

## Demo

🎥 **Demo Video:**
https://drive.google.com/file/d/1NO3RjTMCGEk2SKcgWBWzcPHFAdeX_93d/view?usp=sharing

---

## Project Type

**Applied NLP / AI-Powered Software System**

This project focuses on **practical NLP integration**, showing how transformer models work together with rule-based logic and databases in production-style applications.

---

## Design Notes

* Transformer models are used **only for intent understanding**
* Entity extraction and business logic are rule-based for stability
* Large model files and videos are intentionally excluded from version control
* The system is designed to be easily extensible

---

## Author

Built as an **applied NLP and software engineering project**, demonstrating real-world usage of transformer-based Arabic language models in a production-style chatbot system.

---

