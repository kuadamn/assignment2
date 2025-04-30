import requests
from bs4 import BeautifulSoup
from datetime import datetime

def fetch_wired_titles():
    headlines = []
    seen_titles = set()  # ✅ To prevent duplicates

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:113.0) Gecko/20100101 Firefox/113.0"
    }

    for page in range(1, 30):  # Fetch first 30 pages
        url = f"https://www.wired.com/most-recent/?page={page}"
        try:
            res = requests.get(url, headers=headers)
            soup = BeautifulSoup(res.text, 'html.parser')

            article_tags = soup.find_all("h3", class_="SummaryItemHedBase-hiFYpQ dzwliP summary-item__hed")

            for tag in article_tags:
                try:
                    title = tag.text.strip()
                    if title in seen_titles:  # ✅ Skip duplicates
                        continue
                    seen_titles.add(title)

                    link_tag = tag.find_parent("a")
                    if not link_tag:
                        continue

                    link = "https://www.wired.com" + link_tag["href"]

                    headlines.append({
                        "title": title,
                        "link": link,
                        "date": datetime.now()
                    })
                except Exception as e:
                    print(f"Error parsing article tag: {e}")
                    continue

        except Exception as e:
            print(f"Error fetching page {page}: {e}")
            continue

    return headlines
