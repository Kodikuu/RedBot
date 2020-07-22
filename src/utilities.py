import logging
import os


def init_logging(debug):
	logger = logging.getLogger(__name__)
	logger.addHandler(logging.StreamHandler())
	logger.setLevel(logging.DEBUG if debug else logging.INFO)
	return logger


def env(key, default=None):
	return os.environ.get(key, default)
