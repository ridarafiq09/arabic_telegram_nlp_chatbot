import pandas as pd
import numpy as np
from datasets import Dataset
from transformers import (
    AutoTokenizer,
    AutoModelForSequenceClassification,
    TrainingArguments,
    Trainer
)
from sklearn.metrics import accuracy_score, f1_score


MODEL_NAME = "UBC-NLP/MARBERT"
DATA_PATH = "data/train.csv"
OUTPUT_DIR = "model/marbert-intent"
MAX_LENGTH = 64
EPOCHS = 3
BATCH_SIZE = 8
LR = 2e-5


# LOAD DATA
df = pd.read_csv(DATA_PATH)

assert "text" in df.columns and "label" in df.columns, \
    "CSV must contain 'text' and 'label' columns"

# Create label mappings
labels = sorted(df["label"].unique())
label2id = {l: i for i, l in enumerate(labels)}
id2label = {i: l for l, i in label2id.items()}

df["label_id"] = df["label"].map(label2id)

dataset = Dataset.from_pandas(df[["text", "label_id"]])

# TOKENIZER
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)

def tokenize(batch):
    return tokenizer(
        batch["text"],
        truncation=True,
        padding="max_length",
        max_length=MAX_LENGTH
    )

dataset = dataset.map(tokenize, batched=True)
dataset = dataset.rename_column("label_id", "labels")
dataset.set_format("torch")


model = AutoModelForSequenceClassification.from_pretrained(
    MODEL_NAME,
    num_labels=len(labels),
    label2id=label2id,
    id2label=id2label
)


# METRICS
def compute_metrics(eval_pred):
    logits, labels = eval_pred
    preds = np.argmax(logits, axis=1)
    return {
        "accuracy": accuracy_score(labels, preds),
        "f1_macro": f1_score(labels, preds, average="macro")
    }

# TRAINING ARGS
training_args = TrainingArguments(
    output_dir=OUTPUT_DIR,
    num_train_epochs=EPOCHS,
    per_device_train_batch_size=BATCH_SIZE,
    learning_rate=LR,
    logging_steps=50,

    save_strategy="no",   # no checkpoints
    report_to="none"
)


trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=dataset,
    tokenizer=tokenizer,
    compute_metrics=compute_metrics
)


trainer.train()


# SAVE MODEL
trainer.save_model(OUTPUT_DIR)
tokenizer.save_pretrained(OUTPUT_DIR)

print("✅ Training complete")
print("✅ Model saved to:", OUTPUT_DIR)
