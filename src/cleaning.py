import spacy

# Initialize spacy 'en' model, downloading the model if necessary
try:
	nlp = spacy.load("en_core_web_md")
except:
	spacy.cli.download("en_core_web_md")
	nlp = spacy.load("en_core_web_md")


def clean_text(text):
	doc = nlp(text.lower())  # Convert text to lowercase and create a spaCy Doc object
	cleaned_text = []

	for token in doc:
		if not token.is_stop and token.is_alpha:  # Remove stop words and non-alphabetic tokens
			cleaned_text.append(token.lemma_)  # Lemmatize the token

	return ' '.join(cleaned_text)


# Example usage
sample_text = "The quick brown fox jumps over the lazy dog!"
cleaned_sample = clean_text(sample_text)
print(cleaned_sample)
