import os
import pathlib
import uuid


class Config:
    DEFAULT_CONFIG_PATH = '/storage/images'
    DEFAULT_UUID_GENERATOR = uuid.uuid4
    DEFAULT_MIN_THUMB_SIZE = 64

    def __init__(self):
        self.storage_path = pathlib.Path(os.environ.get('IMAGE_STORAGE_PATH', self.DEFAULT_CONFIG_PATH))
        self.storage_path.mkdir(parents=True, exist_ok=True)

        self.uuid_generator = Config.DEFAULT_UUID_GENERATOR
        self.min_thumb_size = self.DEFAULT_MIN_THUMB_SIZE
