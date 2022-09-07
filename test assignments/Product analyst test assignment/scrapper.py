#!/usr/bin/env python3
import requests
import random
import csv
import warnings
from typing import List
from bs4 import BeautifulSoup
from time import sleep
from tqdm import tqdm
from fake_useragent import UserAgent
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from argparse import ArgumentParser

ua = UserAgent()
URL = 'https://www.kinopoisk.ru/lists/movies/top250/'
URL_MAIN_PAGE = 'https://www.kinopoisk.ru'

def getdatafromhtml(soup : BeautifulSoup) -> List:
    """
    Extract data from html
    Args:
        soup (BeautifulSoup)
    Raises:
        ValueError: Rising when a bad response is received
    Returns:
        List: List of film data lists
    """
    data = []
    films = soup.findAll('div', {'class' : 'styles_root__ti07r'})
    if len(films) == 0:
        raise ValueError('Can not find any film')
    
    for film in films:
        title = film.find('span', {'class' : 'styles_mainTitle__IFQyZ'}).text
        alltime_raiting = float(film.find('div', {'class' : 'styles_rating__ni2L0'}).text)
        lastyear_raiting = float(film.find('span', {'class' : 'styles_kinopoiskValuePositive__vOb2E'}).text)
        data.append([title, alltime_raiting, lastyear_raiting])
    
    return data


def getnextpage(soup : BeautifulSoup) -> str:
    """
    Args:
        soup (BeautifulSoup)
    Returns:
        str: Return next page url
        If next button does not exists return None
    """
    nextbutton = soup.find('a', {'class':'styles_end__aEsmB'})
    if nextbutton:
        return URL_MAIN_PAGE + nextbutton.get('href')
    else:
        return

def stealthrequest(url : str) -> requests.Response:
    """
    Makes a request that is recognized by the system as human request
    Args:
        url (str): url
    Returns:
        requests.Response: response
    """
    sleep(random.randint(5,10))
    
    session = requests.session()
    retry = Retry(connect=3, backoff_factor=0.5)
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('http://', adapter)
    session.mount('https://', adapter)

    # Clear cookies
    # session.cookies.clear()
    # Set headers
    headers = {'user-agent': ua.chrome}
    
    # Paste all your Request Headers here if not working with simple headers.
    # headers = {
    #     "accept": "",
    #     "accept-encoding": "gzip, deflate, br",
    #     "accept-language": "ru",
    #     "cache-control": "max-age=0",
    #     "cookie": "",
    #     "referer": "",
    #     "sec-ch-ua": "",
    #     "sec-ch-ua-mobile": "?0",
    #     "sec-ch-ua-platform": "",
    #     "sec-fetch-dest": "document",
    #     "sec-fetch-mode": "navigate",
    #     "sec-fetch-site": "same-origin",
    #     "sec-fetch-user": "?1",
    #     "upgrade-insecure-requests": "1",
    #     "user-agent": "",
    # }  
    # Make request
    r = session.get(url, headers=headers)
    return r

def getalldata(url : str, faultrequests : int = 5) -> List:
    data = []
    
    with tqdm(total=250, position=0, leave=True) as pbar:
        while len(data) < 250:
            
            #Make request      
            r = stealthrequest(url)
            soup = BeautifulSoup(r.text, 'html.parser')
            
            # Getting data
            try:
                pagedata = getdatafromhtml(soup)
            except:
                faultrequests -= 1
                warnings.warn(f"Warning: Data not found. Attempts left {faultrequests}")
                if faultrequests > 0:
                    continue
                else:
                    raise ValueError("Can not get data")
            
            #Append page data
            pbar.update(len(pagedata))
            data.extend(pagedata)
            
            # Getting new page
            url = getnextpage(soup)
            if url is None and len(data) < 250:
                raise ValueError('Next page not faund')
            
    return data

def savetocsv(data, path : str = "out.csv") -> None:
    with open(path, "w", newline = "", encoding="utf8") as f:
        writer = csv.writer(f)
        writer.writerows(data)

def loadandsave(savepath) -> None:
    data = getalldata(URL)
    savetocsv(data, savepath)
    
def process_cli_arguments(arguments):
    loadandsave(arguments.path)

def setup_parser(parser):
    parser.add_argument("-p", "--savepath", dest="path", type=str, required=True)
    parser.set_defaults(callback=process_cli_arguments)

def main():
    parser = ArgumentParser(
        prog="scrapper",
        description="Tool for scraping kinopoisk top 250 films site",
    )
    setup_parser(parser)
    arguments = parser.parse_args()
    arguments.callback(arguments)

if __name__ == "__main__":
    main()