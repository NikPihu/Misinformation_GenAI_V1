import json
from datetime import datetime

class WriterAgent:
    def write_output(self, query, verification_result):
        print("[WriterAgent] 📝 Writing structured output...")

        output = {
            "claim": query,
            "result": verification_result,
            "timestamp": datetime.now().isoformat()
        }

        with open("fact_check_output.json", "w", encoding="utf-8") as f:
            json.dump(output, f, indent=4)

        print("[WriterAgent] ✅ Output saved to fact_check_output.json")
        return output
