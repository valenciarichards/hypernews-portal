import requests

from bs4 import BeautifulSoup

# link = input().strip()
link = "https://www.who.int/health-topics"
r = requests.get(link)
soup = BeautifulSoup(r.content, "html.parser")

topics = []

for a_tag in soup.find_all("a"):
    topic = a_tag.text
    if topic.startswith("S") and len(topic) > 1:
        if "topic" in a_tag["href"] or "entity" in a_tag["href"]:
            topics.append(topic)

print(topics)