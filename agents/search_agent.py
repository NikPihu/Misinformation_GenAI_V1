from serpapi import GoogleSearch

class SearchAgent:
    def __init__(self, api_key):
        self.api_key = api_key

    def search(self, query):
        print(f"\n🔍 [SearchAgent] Searching '{query}' via DuckDuckGo and Google...")

        # --- DuckDuckGo Search ---
        ddg_params = {
            "engine": "duckduckgo",
            "q": query,
            "api_key": self.api_key
        }
        ddg_search = GoogleSearch(ddg_params)
        ddg_results = ddg_search.get_dict()
        ddg_organic = ddg_results.get("organic_results", [])

        duckduckgo_links = [
            {
                "source": "DuckDuckGo",
                "title": r.get("title"),
                "snippet": r.get("snippet"),
                "link": r.get("link")
            }
            for r in ddg_organic[:2]
        ]

        print(f"[SearchAgent] DuckDuckGo results ({len(duckduckgo_links)}):")
        for r in duckduckgo_links:
            print(f"  • {r['title']} → {r['link']}")

        # --- Google Search ---
        google_params = {
            "engine": "google",
            "q": query,
            "api_key": self.api_key
        }
        google_search = GoogleSearch(google_params)
        google_results = google_search.get_dict()
        google_organic = google_results.get("organic_results", [])

        google_links = [
            {
                "source": "Google",
                "title": r.get("title"),
                "snippet": r.get("snippet"),
                "link": r.get("link")
            }
            for r in google_organic[:3]
        ]

        print(f"[SearchAgent] Google results ({len(google_links)}):")
        for r in google_links:
            print(f"  • {r['title']} → {r['link']}")

        combined_results = duckduckgo_links + google_links
        print(f"[SearchAgent] ✅ Retrieved {len(combined_results)} total results.\n")
        return combined_results
