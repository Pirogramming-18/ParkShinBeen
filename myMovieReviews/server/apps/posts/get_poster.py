import requests
from bs4 import BeautifulSoup as bs

def search(name):
    try:
        url = f'https://movie.naver.com/movie/search/result.naver?query={name}&section=all&ie=utf8'
        response = requests.get(url)
        soup = bs(response.text, "html.parser")
        raw_code = soup.select_one('.search_list_1 p a').get("href")
        code = raw_code[30:]
        movie_url = f"https://movie.naver.com/movie/bi/mi/basic.naver?code={code}"

        movie_response = requests.get(movie_url)
        movie_soup = bs(movie_response.text, "html.parser")
        src = movie_soup.select_one('.poster > a > img').get("src")
        print(src)
        return src
    except:
        return "https://ssl.pstatic.net/static/movie/2012/06/dft_img77x110_1.png"