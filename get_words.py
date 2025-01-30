import requests
from bs4 import BeautifulSoup

# target website URL
urls = [f"https://www.koolearn.com/dict/tag_1958_{i}.html" for i in range(1, 12)]

# set header
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}
all_words = []
for url in urls:
    try:
        # send request
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()  # check request status

        # decode response content
        soup = BeautifulSoup(response.text, "html.parser")

        # find word-box element
        word_box = soup.find(class_="word-box")
        if word_box:
            words = [a.text.strip() for a in word_box.find_all("a")]
            all_words.extend(words)
        else:
            print(f"'word-box' element not found（{url}）")

    except requests.exceptions.RequestException as e:
        print(f"request failed（{url}）: {e}")

# write words to file
with open("words.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(reversed(all_words)))