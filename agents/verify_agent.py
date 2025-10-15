from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

class VerifyAgent:
    def __init__(self):
        self.client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

    def verify(self, query, search_results):
        print(f"[VerifyAgent] 🧠 Analyzing search results for: '{query}'")
        combined_text = "\n".join([
            f"Source: {r['source']}\nTitle: {r['title']}\nSnippet: {r['snippet']}\nLink: {r['link']}\n"
            for r in search_results
        ])

        print(f"[VerifyAgent] 🧾 Combined search text sent to Gemini:\n{'-'*60}\n{combined_text}\n{'-'*60}\n")

        prompt = f"""
You are a fact-checking AI. Verify this claim based on the sources below.

Claim: "{query}"

Sources:
{combined_text}

Answer clearly whether the claim is TRUE, FALSE, or AMBIGUOUS,
and explain briefly why.
"""
        resp = self.client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        print(f"[VerifyAgent] ✅ Gemini raw output:\n{resp.text}\n{'='*60}\n")
        return resp.text
