import json
from datasets import Dataset
from transformers import Trainer, TrainingArguments
from transformers import AutoTokenizer, AutoModelForCausalLM

from src.config import settings
from src.preparation import load_training_data

tokenizer = AutoTokenizer.from_pretrained("distilgpt2")
tokenizer.pad_token = tokenizer.eos_token

model = AutoModelForCausalLM.from_pretrained("distilgpt2")


def tokenize_and_prepare_labels(examples):
	tokenized_inputs = tokenizer(examples["text"], padding="max_length", truncation=True, max_length=512)
	# Create labels by shifting input_ids to the right
	tokenized_inputs["labels"] = tokenized_inputs["input_ids"].copy()
	return tokenized_inputs


# Assuming 'texts' is a list of strings
# dataset = Dataset.from_dict({"text": texts})
# tokenized_dataset = dataset.map(tokenize_and_prepare_labels, batched=True)
#
# training_args = TrainingArguments(
# 	output_dir=settings.MODEL_FOLDER,
# 	num_train_epochs=3,
# 	per_device_train_batch_size=2,
# 	warmup_steps=500,
# 	weight_decay=0.01,
# 	logging_dir=settings.LOG_PATH,
# )
#
# trainer = Trainer(
# 	model=model,
# 	args=training_args,
# 	train_dataset=tokenized_dataset,
# )
#
# # Train the model
# trainer.train()
#
# model.save_pretrained(settings.MODEL_WEIGHT_PATH)
# tokenizer.save_pretrained(settings.MODEL_WEIGHT_PATH)
