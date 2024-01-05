import logging

from src.config import settings

# Configure the logger
logging.basicConfig(
	level=settings.LOG_LEVEL,
	format="%(asctime)s - %(levelname)s - %(message)s",
	handlers=[
		logging.StreamHandler()
	]
)
logger = logging.getLogger()
