import os
from dotenv import load_dotenv

def load_env():
    load_dotenv()
    return {
        "SERPAPI_KEY": os.getenv("SERPAPI_KEY"),
        "GEMINI_API_KEY": os.getenv("GEMINI_API_KEY")
    }
