import pandas as pd
import bs4
from bs4 import BeautifulSoup

def get_ratings_table(ratings_page):
    ts = ratings_page.find_all("table")
    rows = ts[0].find_all("tr")
    df = pd.DataFrame()
    scores = []
    nvotes = []
    for (i, row) in enumerate(rows):
        if i == 0:
            continue
        score = int(row.find_all("div", {"class": "rightAligned"})[0].text)
        nvote = int(row.find_all("div", {"class": "leftAligned"})[0].text.replace(",", ""))
        scores.append(score)
        nvotes.append(nvote)
        # df[i, :] = [score.text, nvotes.text]
    df = pd.DataFrame(list(zip(scores, nvotes)),columns =['score', 'nvotes'])
    return df