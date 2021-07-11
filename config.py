import os
import pathlib
import uuid


class Config:
    DEFAULT_CONFIG_PATH = '/storage/images'
    DEFAULT_UUID_GENERATOR = uuid.uuid4
    DEFAULT_MIN_THUMB_SIZE = 64
    DEFAULT_LOG_DIRECTORY = '/logs'
    DEFAULT_RESPONSE_LOG_FILE = os.path.join(DEFAULT_LOG_DIRECTORY, 'www.log')
    DEFAULT_APP_LOG_FILE = os.path.join(DEFAULT_LOG_DIRECTORY, 'app.log')

    def __init__(self):
        self.storage_path = pathlib.Path(os.environ.get('IMAGE_STORAGE_PATH', self.DEFAULT_CONFIG_PATH))
        self.storage_path.mkdir(parents=True, exist_ok=True)

        self.uuid_generator = Config.DEFAULT_UUID_GENERATOR
        self.min_thumb_size = self.DEFAULT_MIN_THUMB_SIZE
        self.www_log = pathlib.Path(os.environ.get('WWW_LOG_FILE', self.DEFAULT_RESPONSE_LOG_FILE))
        self.app_log = pathlib.Path(os.environ.get('APP_LOG_FILE', self.DEFAULT_APP_LOG_FILE))
