# from genericpath import isdir
import bs4
from bs4 import BeautifulSoup
import requests as r
import os
import pandas as pd
import numpy as np

def download_imdb_dataset(data_link: bs4.element.Tag):
    fn = data_link.text
    data_url = data_link["href"]
    path = os.path.join(datadir, fn)
    tsv_path = os.path.splitext(path)[0] # since gunzip deletes, we need to remove the .gz extension to check if we already grabbed the dataset
    os.path.isfile(tsv_path) or os.system(f'wget -O {path} {data_url}')
    os.system(f'gunzip {path}') # this deletes the .gz file
    return path

if __name__ == "__main__":
    url = "https://datasets.imdbws.com/"
    req = r.get(url)
    p = BeautifulSoup(req.text, 'html.parser')
    links = p.find_all('a')
    data_links = links[1:] # ignore the first one, since it links to http://www.imdb.com/interfaces/
    assert len(data_links)==7 # check that there are 7 datasets

    datadir = 'data'
    os.path.isdir(datadir) or os.mkdir(datadir)
    for l in data_links:
        download_imdb_dataset(l)
