from google import genai
import os
from dotenv import load_dotenv
from PIL import Image

load_dotenv()

class ImageAgent:
    def __init__(self):
        self.client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

    def analyze_image(self, image_path):
        print(f"\n🖼️ [ImageAgent] Analyzing image: {image_path}")

        # Load image
        try:
            image = Image.open(image_path)
        except Exception as e:
            print(f"[ImageAgent] ❌ Error opening image: {e}")
            return None

        # Send to Gemini for understanding
        resp = self.client.models.generate_content(
            model="gemini-2.5-flash",
            contents=[
                "Look at this image or screenshot and describe what fact or claim is being made in one short sentence suitable for fact-checking.",
                image
            ]
        )

        extracted_query = resp.text.strip()
        print(f"[ImageAgent] 🧠 Extracted query from image: '{extracted_query}'")
        return extracted_query
