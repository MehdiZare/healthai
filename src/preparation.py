import json
from tqdm import tqdm

from src.api import fetch_data
from src.config import settings
from src.logger import logger

keywords = [
	'medical', 'health', 'pharma', 'hospital', 'doctor', 'nurse', 'patient', 'medicine', 'vaccine', 'disease',
	'illness', 'healthcare'
]


def prepare_training_data() -> None:
	training_data = []
	for idx, keyword in tqdm(enumerate(keywords)):
		logger.info(f"Fetching data for {keyword}")
		response = fetch_data(
			access_key=settings.API_KEY,
			keywords=keyword,
			countries="us"
		)

		tmp = [
			f"{news.get('title')} - {news.get('description')}" for news in response if news.get('language') == 'en'
		]
		training_data.extend(tmp)

	with open(settings.TRAINING_DATA_FILE, 'w', encoding='utf-8') as file:
		json.dump(training_data, file)


def load_training_data() -> list:
	with open(settings.TRAINING_DATA_FILE, 'r', encoding='utf-8') as file:
		training_data = json.load(file)
	return training_data
