import os


BASE_DIR = os.path.dirname(__file__)

DATABASE_URI = f"sqlite:///{os.path.join(BASE_DIR, 'golden-bell.db')}"
DATABASE_TRACK_MODIFICATIONS = False