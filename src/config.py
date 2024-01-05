from pathlib import Path
from dotenv import load_dotenv
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
	DEBUG: bool = True
	LOG_LEVEL: str = "INFO"
	API_KEY: str
	TRAINING_FOLDER: str = "training_data"
	MODEL_FOLDER: str = "distilgpt2_finetuned"
	MODEL_WEIGHT_FOLDER: str = "distilgpt2_finetuned"
	LOG_FOLDER: str = "logs"

	def __init__(self, **values):
		super().__init__(**values)
		self._ensure_directories_exist()

	def _ensure_directories_exist(self):
		for path in [self.TRAINING_PATH, self.MODEL_PATH, self.MODEL_WEIGHT_PATH, self.LOG_PATH]:
			path.mkdir(parents=True, exist_ok=True)

	@property
	def TRAINING_PATH(self):
		return Path(__file__).parent.parent / self.TRAINING_FOLDER

	@property
	def TRAINING_DATA_FILE(self):
		return Path(__file__).parent.parent / self.TRAINING_FOLDER / 'training_data.json'

	@property
	def MODEL_PATH(self):
		return Path(__file__).parent.parent / self.MODEL_FOLDER

	@property
	def MODEL_WEIGHT_PATH(self):
		return Path(__file__).parent.parent / self.MODEL_WEIGHT_FOLDER

	@property
	def LOG_PATH(self):
		return Path(__file__).parent.parent / self.LOG_FOLDER

	class Config:
		case_sensitive = True


env_file = '.env'
env_path = Path(__file__).parent.parent / env_file

load_dotenv(env_path)

settings = Settings()
