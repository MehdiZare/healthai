from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline

from src.config import settings

tokenizer = AutoTokenizer.from_pretrained(settings.MODEL_WEIGHT_PATH)
tokenizer.pad_token = tokenizer.eos_token

model = AutoModelForCausalLM.from_pretrained(settings.MODEL_WEIGHT_PATH)

text_generator = pipeline("text-generation", model=model, tokenizer=tokenizer)

input_prompt = "Today is a beautiful day"
generated_texts = text_generator(input_prompt, max_length=50, num_return_sequences=1)
