#!/usr/bin/env python3

from bs4 import BeautifulSoup
import requests
import re
import json
import datetime

def scrapePopularData():
    
    url = "https://www.imdb.com/chart/moviemeter/?ref_=nv_mv_mpm"
    response = requests.get(url, timeout=5)
    content = BeautifulSoup(response.content, "html.parser")

    movie_list = []

    for movie_container in content.findAll('tr'):
    
        title_col_cont = str(movie_container.find('td', attrs={"class":"titleColumn"}))
        year_cont = str(movie_container.find('span', attrs={"class":"secondaryInfo"}))
        rating_cont = str(movie_container.find('td', attrs={"class":"ratingColumn"}))

        matches_title = re.search(r">(.*)</a>", title_col_cont)
        matches_year = re.search(r">\((\d+)\)</span>", year_cont)
        matches_rating = re.search(r"<strong title=\"(.*)\">", rating_cont)

        if matches_title:
            movie_title = matches_title.group(1)

        if matches_year:
            movie_year = matches_year.group(1)

        if matches_rating:
            movie_rating = matches_rating.group(1)

            movieObject = {

                "title": movie_title,
                "year": movie_year,
                "rating": movie_rating
            }

            movie_list.append(movieObject)

    with open("mostPopularMovieData.json", "w+") as outfile:
        json.dump(movie_list, outfile)


def getDateAndTime():
    now = datetime.datetime.now()
    currentDate = now.strftime("%Y/%m/%d %H:%M:%S")
    return str(currentDate)

def readPopularData():

    counter = 1

    with open("mostPopularMovieData.json", "r") as json_data:
        popularData = json.load(json_data)

    print("\n\n\t\t\t---------------Most Popular Movies as of "+getDateAndTime()+"---------------\n\n")
    print("\t\t\tTITLE-----------------------------YEAR-----------------------------USER RATING\n\n")
    
    for movieInfo in popularData:
        print("\t\t"+str(counter)+". "+movieInfo["title"]+"--------------------"+movieInfo["year"]+"--------------------"+movieInfo["rating"]+"\n")
        counter += 1

def stripArticle(article_cont):
    
    article_cont_stripped = re.sub(r"div class=\"news-article__content\">|<a.*?>|</a>|</div>", "", article_cont)
    article_cont_stripped = re.sub(r"<br/><br/>", "\n", article_cont_stripped)
    article_cont_stripped = re.sub(r"<", "", article_cont_stripped)
    article_cont_stripped = re.sub(r"&amp;", "&", article_cont_stripped)

    return article_cont_stripped

def scrapeNewsData():

    url = "https://www.imdb.com/news/movie/?ref_=nv_nw_mv"
    response = requests.get(url, timeout=5)
    content = BeautifulSoup(response.content, "html.parser")

    article_list = []

    for article_container in content.findAll('article', attrs={"class":"ipl-zebra-list__item news-article"}):
        
        title_col_cont = str(article_container.find('a'))
        date_cont = str(article_container.find('li', attrs={"class":"ipl-inline-list__item news-article__date"}))
        author_cont = str(article_container.find('li', attrs={"class":"ipl-inline-list__item news-article__author"}))
        source_cont = str(article_container.find('li', attrs={"class":"ipl-inline-list__item news-article__source"}))
        article_cont = str(article_container.find('div', attrs={"class":"news-article__content"}))
        url_cont = str(article_container.find('a', attrs={"class":"news-content__offsite-link"}))

        #print(url_cont + "\n\n")

        matches_title = re.search(r">(.*)</a>", title_col_cont)
        matches_date = re.search(r">(.*)</li>", date_cont)
        matches_author = re.search(r">(.*)</li>", author_cont)
        matches_source = re.search(r">(.*)</a>", source_cont)
        matches_url = re.search(r"href=\"(.*?)\"", url_cont)

        if matches_title:
            article_title = matches_title.group(1)

        if matches_date:
            article_date = matches_date.group(1)
        
        if matches_author:
            article_author = matches_author.group(1)
        
        if matches_source:
            article_source = matches_source.group(1)
        
        if matches_url:
            article_url = matches_url.group(1)
            print(article_url+"\n\n")

        article_text = stripArticle(article_cont)
        
        articleObject = {
                
                "title": article_title,
                "date": article_date,
                "author": article_author,
                "source": article_source,
                "content": article_text
            }
        
        article_list.append(articleObject)
    
    with open("movieNewsData.json", "w+") as outfile:
        json.dump(article_list, outfile)

scrapeNewsData()
def readNewsData():
    
    with open("movieNewsData.json", "r") as json_data:
        newsData = json.load(json_data)

    print("\n\n\t\t\t---------------Movie News Snippets as of "+getDateAndTime()+"---------------\n\n")

    for articleInfo in newsData:
        print(articleInfo["title"]+"\n"+articleInfo["date"]+"\n\n"+articleInfo["content"].lstrip()+"\n"+articleInfo["author"]+"\n"+articleInfo["source"]+"\n\n")
        print("------------------------------------------------------------------------------------------------")


