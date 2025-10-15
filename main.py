from agents.image_agent import ImageAgent
from agents.search_agent import SearchAgent
from agents.verify_agent import VerifyAgent
from agents.writer_agent import WriterAgent
import os
from dotenv import load_dotenv

load_dotenv()

def main():
    print("🤖 Welcome to Fact-Check Agent!")
    choice = input("Do you want to analyze a (1) text claim or (2) image? Enter 1 or 2: ")

    image_agent = ImageAgent()
    search_agent = SearchAgent(api_key=os.getenv("SERPAPI_KEY"))
    verify_agent = VerifyAgent()
    writer_agent = WriterAgent()

    if choice.strip() == "2":
        image_path = input("Enter path to your image file: ").strip()
        query = image_agent.analyze_image(image_path)
        if not query:
            print("❌ Could not extract query from image. Exiting.")
            return
    else:
        query = input("Enter a claim to fact-check: ").strip()

    # Run normal 3-step pipeline
    search_results = search_agent.search(query)
    verification = verify_agent.verify(query, search_results)
    final_output = writer_agent.write_output(query, verification)

    print("\n--- Final Fact Check ---")
    print(final_output["result"])

if __name__ == "__main__":
    main()
