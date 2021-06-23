from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from collections.abc import Set

book_num_chapters = {
    'MAT': 28,
    'MRK': 16,
    'LUK': 24,
    'JHN': 21,
    'ACT': 28,
    'ROM': 16,
    '1CO': 16,
    '2CO': 13,
    'GAL': 16,
    'EPH': 6,
    'PHP': 4,
    'COL': 4,
    '1TH': 5,
    '2TH': 3,
    '1TI': 6,
    '2TI': 4,
    'TIT': 3,
    'PHM': 1,
    'HEB': 13,
    'JAS': 5,
    '1PE': 5,
    '2PE': 3,
    '1JN': 5,
    '2JN': 1,
    '3JN': 1,
    'JUD': 1,
    'REV': 22
}

words = []

with open('JCR_words.txt', 'w') as f:
    for book, num_chapters in book_num_chapters.items():
        for chapter in range(1, num_chapters + 1):
            url = f"https://www.bible.com/bible/476/{book}.{str(chapter)}.JNT"
            req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            page = urlopen(req).read()
            soup = BeautifulSoup(page, 'html.parser')
            verse_elems = soup.find_all('span', class_='content')

            for verse_elem in verse_elems:
                verse_text = verse_elem.text.split()
                for word in verse_text:
                    words.append(''.join(filter(str.isalnum, word.lower())))

    words = sorted(list(set(words)))

    for word in words:
        f.write(word + "\n")

# TODO
# Print time
# Print number of words
# Show progress
