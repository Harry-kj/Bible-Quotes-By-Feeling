<<<<<<< HEAD
import requests
from bs4 import BeautifulSoup
import json
import time

# List of emotions (topics) you want to scrape
emotions = [
    "happiness",
    "sadness",
    "fear",
    "anger",
    "peace",
    "love"
]

base_url = "https://www.openbible.info/topics/"

def scrape_emotion_verses(emotion):
    url = base_url + emotion
    print(f"Scraping {emotion} from {url}")
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to retrieve {url}")
        return []

    soup = BeautifulSoup(response.text, "html.parser")
    verses = []

    for verse_div in soup.find_all("div", class_="verse"):
        # Get verse reference and link
        a_tag = verse_div.find("h3").find("a", class_="bibleref")
        if not a_tag:
            continue
        reference = a_tag.text.strip()
        link = a_tag['href']

        # Get verse text from <p>
        verse_text_p = verse_div.find("p")
        if not verse_text_p:
            continue
        verse_text = verse_text_p.get_text(strip=True).replace('\u201c', '"').replace('\u201d', '"')

        verses.append({
            "reference": reference,
            "link": link,
            "text": verse_text
        })

    return verses

def main():
    all_verses = {}
    for emotion in emotions:
        verses = scrape_emotion_verses(emotion)
        all_verses[emotion] = verses
        time.sleep(1)  # Be polite, avoid hammering the server

    # Save results to JSON file
    with open("emotion_verses.json", "w", encoding="utf-8") as f:
        json.dump(all_verses, f, indent=2, ensure_ascii=False)

    print("Scraping complete. Data saved to emotion_verses.json")

if __name__ == "__main__":
    main()
=======
import requests
from bs4 import BeautifulSoup
import json
import time

# List of emotions (topics) you want to scrape
emotions = [
    "happiness",
    "sadness",
    "fear",
    "anger",
    "peace",
    "love"
]

base_url = "https://www.openbible.info/topics/"

def scrape_emotion_verses(emotion):
    url = base_url + emotion
    print(f"Scraping {emotion} from {url}")
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to retrieve {url}")
        return []

    soup = BeautifulSoup(response.text, "html.parser")
    verses = []

    for verse_div in soup.find_all("div", class_="verse"):
        # Get verse reference and link
        a_tag = verse_div.find("h3").find("a", class_="bibleref")
        if not a_tag:
            continue
        reference = a_tag.text.strip()
        link = a_tag['href']

        # Get verse text from <p>
        verse_text_p = verse_div.find("p")
        if not verse_text_p:
            continue
        verse_text = verse_text_p.get_text(strip=True).replace('\u201c', '"').replace('\u201d', '"')

        verses.append({
            "reference": reference,
            "link": link,
            "text": verse_text
        })

    return verses

def main():
    all_verses = {}
    for emotion in emotions:
        verses = scrape_emotion_verses(emotion)
        all_verses[emotion] = verses
        time.sleep(1)  # Be polite, avoid hammering the server

    # Save results to JSON file
    with open("emotion_verses.json", "w", encoding="utf-8") as f:
        json.dump(all_verses, f, indent=2, ensure_ascii=False)

    print("Scraping complete. Data saved to emotion_verses.json")

if __name__ == "__main__":
    main()
>>>>>>> d9a72738d026b7896c8c5261de303b03c492d8e8
