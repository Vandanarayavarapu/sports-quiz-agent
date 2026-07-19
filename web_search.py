from duckduckgo_search import DDGS

def search_sports_news(query):
    results = []

    with DDGS() as ddgs:
        for result in ddgs.text(query, max_results=3):
            results.append(result["body"])

    return results


query = "latest cricket news"

news = search_sports_news(query)

print("Latest Sports Information:")

for item in news:
    print("-", item)