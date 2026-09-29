import requests
import time
import json
import os
from datetime import datetime


# HackerNews API URLs
TOP_STORIES_URL = "https://hacker-news.firebaseio.com/v0/topstories.json"
ITEM_URL = "https://hacker-news.firebaseio.com/v0/item/{}.json"


# Keywords used to classify stories into categories
CATEGORY_KEYWORDS = {
    "technology": [
        "ai", "software", "tech", "code", "computer",
        "data", "cloud", "api", "gpu", "llm"
    ],

    "worldnews": [
        "war", "government", "country", "president",
        "election", "climate", "attack", "global"
    ],

    "sports": [
        "nfl", "nba", "fifa", "sport", "game",
        "team", "player", "league", "championship"
    ],

    "science": [
        "research", "study", "space", "physics",
        "biology", "discovery", "nasa", "genome"
    ],

    "entertainment": [
        "movie", "film", "music", "netflix", "game",
        "book", "show", "award", "streaming"
    ]
}


def fetch_story_ids():
    """Fetch the first 500 top story IDs from HackerNews."""

    headers = {"User-Agent": "TrendPulse/1.0"}

    try:
        response = requests.get(
            TOP_STORIES_URL,
            headers=headers,
            timeout=10
        )

        response.raise_for_status()

        story_ids = response.json()

        return story_ids[:500]

    except requests.RequestException as error:
        print(f"Failed to fetch top story IDs: {error}")
        return []


def fetch_story(story_id):
    """Fetch details for one HackerNews story."""

    headers = {"User-Agent": "TrendPulse/1.0"}

    try:
        url = ITEM_URL.format(story_id)

        response = requests.get(
            url,
            headers=headers,
            timeout=10
        )

        response.raise_for_status()

        return response.json()

    except requests.RequestException as error:
        print(f"Failed to fetch story {story_id}: {error}")
        return None


def collect_stories(story_ids):
    """Collect up to 25 stories for each category."""

    collected = []

    for category, keywords in CATEGORY_KEYWORDS.items():

        category_count = 0

        for story_id in story_ids:

            if category_count >= 25:
                break

            story = fetch_story(story_id)

            if not story:
                continue

            title = story.get("title", "")
            title_lower = title.lower()

            # Check whether the title contains a keyword
            # belonging to the current category.
            if not any(keyword.lower() in title_lower for keyword in keywords):
                continue

            collected_story = {
                "post_id": story.get("id"),
                "title": title,
                "category": category,
                "score": story.get("score", 0),
                "num_comments": story.get("descendants", 0),
                "author": story.get("by", ""),
                "collected_at": datetime.now().isoformat()
            }

            collected.append(collected_story)

            category_count += 1

        print(f"Collected {category_count} stories for {category}")

        # Wait two seconds before processing the next category.
        time.sleep(2)

    return collected


def save_to_json(stories):
    """Save stories into the data folder."""

    os.makedirs("data", exist_ok=True)

    date_string = datetime.now().strftime("%Y%m%d")

    file_path = f"data/trends_{date_string}.json"

    with open(file_path, "w", encoding="utf-8") as file:

        json.dump(
            stories,
            file,
            indent=4,
            ensure_ascii=False
        )

    return file_path


def main():

    print("Fetching top HackerNews stories...")

    story_ids = fetch_story_ids()

    if not story_ids:
        print("No story IDs were fetched.")
        return

    print(f"Fetched {len(story_ids)} story IDs.")

    stories = collect_stories(story_ids)

    file_path = save_to_json(stories)

    print(f"Collected {len(stories)} stories.")

    print(f"Saved to {file_path}")


if __name__ == "__main__":
    main()