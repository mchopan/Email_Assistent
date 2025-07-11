from dotenv import load_dotenv
import os

load_dotenv()

EMAIL_ADDRESS = os.getenv("EMAIL_USERNAME")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
GOOGLE_MODEL = os.getenv("GOOGLE_MODEL")


# Optionally raise error if not loaded
if not EMAIL_ADDRESS or not EMAIL_PASSWORD:
    raise ValueError("Missing EMAIL_ADDRESS or EMAIL_PASSWORD in .env")