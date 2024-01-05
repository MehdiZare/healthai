from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained("distilgpt2")
tokenizer.pad_token = tokenizer.eos_token

model = AutoModelForCausalLM.from_pretrained("distilgpt2")


def tokenize_and_prepare_labels(text):
	tokenized_inputs = tokenizer(text["text"], padding="max_length", truncation=True, max_length=512)
	# Create labels by shifting input_ids to the right
	tokenized_inputs["labels"] = tokenized_inputs["input_ids"].copy()
	return tokenized_inputs
