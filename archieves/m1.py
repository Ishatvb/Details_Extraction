import numpy as np
from transformers import BertTokenizerFast, BertForTokenClassification, Trainer, TrainingArguments
from datasets import load_dataset, Dataset, DatasetDict
from sklearn.metrics import precision_recall_fscore_support, accuracy_score

# Load pre-trained model and tokenizer
model_name = "bert-base-uncased"
tokenizer = BertTokenizerFast.from_pretrained(model_name)
model = BertForTokenClassification.from_pretrained(model_name, num_labels=3)

# Load dataset
dataset = load_dataset("conll2003")

# Tokenize and align labels
def tokenize_and_align_labels(examples, label_all_tokens=True):
    tokenized_inputs = tokenizer(examples["tokens"], truncation=True, padding='max_length', is_split_into_words=True)
    
    labels = examples["ner_tags"]
    new_labels = []
    for i, label in enumerate(labels):
        word_ids = tokenized_inputs.word_ids(batch_index=i)
        label_ids = []
        previous_word_idx = None
        for word_idx in word_ids:
            if word_idx is None:
                label_ids.append(-100)
            elif word_idx != previous_word_idx:
                label_ids.append(label[word_idx])
            else:
                label_ids.append(label[word_idx] if label_all_tokens else -100)
            previous_word_idx = word_idx
        new_labels.append(label_ids)
    
    tokenized_inputs["labels"] = new_labels
    return tokenized_inputs

# Map the function to the dataset
tokenized_datasets = dataset.map(lambda examples: tokenize_and_align_labels(examples, label_all_tokens=True), batched=True)

# Split dataset into training and validation
train_dataset = tokenized_datasets["train"]
eval_dataset = tokenized_datasets["validation"]

# Define Trainer arguments
training_args = TrainingArguments(
    output_dir="./results",
    evaluation_strategy="epoch",
    learning_rate=2e-5,
    per_device_train_batch_size=16,
    per_device_eval_batch_size=16,
    num_train_epochs=3,
    weight_decay=0.01,
)

# Initialize Trainer
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset,
    eval_dataset=eval_dataset,
    tokenizer=tokenizer,
    compute_metrics=lambda p: {
        "accuracy": accuracy_score(p.label_ids, np.argmax(p.predictions, axis=2)),
        **precision_recall_fscore_support(p.label_ids, np.argmax(p.predictions, axis=2), average="weighted"),
    }
)

# Train and evaluate model
trainer.train()
trainer.evaluate()
