import json
import requests
from typing import List, Dict

from src.config import settings


def fetch_data(access_key: str, keywords: str, countries: str) -> List[Dict]:
	"""Fetch data from the mediastack API."""
	base_url = "https://api.mediastack.com/v1/news"
	params = {
		"access_key": access_key,
		"keywords": keywords,
		"countries": countries
	}

	response = requests.get(base_url, params=params)
	response.raise_for_status()

	data = response.json().get('data')
	return data




