from urllib import request
from bs4 import BeautifulSoup
import json
import sqlite3

conn = sqlite3.connect(r'R:\WorkSpace\databases\douban.db')
cur = conn.cursor()

def get_html(page_num):
    resp1 = request.urlopen('https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=20&page_start=' + str(page_num))
    json_data = resp1.read().decode('utf-8')
    #print(json_data)
    return json_data

def parse_info(basic_json):
    for i in range(20):
        try:
            this_json = json.loads(basic_json)
            title = this_json['subjects'][i]['title']
            rate = this_json['subjects'][i]['rate']
            url = this_json['subjects'][i]['url']
            is_new = this_json['subjects'][i]['is_new']

            resp = request.urlopen(url)
            html_data = resp.read().decode('utf-8')
            soup = BeautifulSoup(html_data, "html.parser")

            director = soup.find('a',rel='v:directedBy').string

            scriptwriter_list = soup.find('span', text='编剧').next_sibling.next_sibling.contents
            scriptwriter = ""
            for sw in scriptwriter_list:
                scriptwriter += sw.string
            
            actors_list = soup.find('span', text='主演').next_sibling.next_sibling.contents
            actors = ""
            for ac in actors_list:
                actors += ac.string

            types_list = soup.find_all('span', property="v:genre")
            types = ""
            for tp in types_list:
                types += tp.string
                types += ' '
            
            regions = soup.find('span', text='制片国家/地区:').next_sibling.string

            languages = soup.find('span', text='语言:').next_sibling.string

            releaseTime = soup.find('span', property="v:initialReleaseDate").string

            runTime = soup.find('span', property="v:runtime").string

            starsRate_list = soup.find_all('span', class_="rating_per")
            fiveStar = starsRate_list[0].string
            fourStar = starsRate_list[1].string
            threeStar = starsRate_list[2].string
            twoStar = starsRate_list[3].string
            oneStar = starsRate_list[4].string


            print('title: ', title)
            print('regions: ',regions)
            print('languages: ',languages)
            print('releaseTime: ',releaseTime)
            print('runTime: ',runTime)
            print('type: ',types)
            print('director: ',director)
            print('scriptwritter: ',scriptwriter)
            print('actors: ',actors)
            print('rate: ',rate)
            print('is_new: ',is_new)
            print('url: ',url)
            print('FiveStar: ', fiveStar)
            print('\n')
            cur.execute("Insert Into movies(title,regions,languages,releasetime, \
                         runtime,type,director,scriptwritter,actors,rate,is_new,url,fivestar,fourstar,threestar,twostar,onestar) \
                         Values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?);", (title,regions,languages,releaseTime,runTime,types,director,scriptwriter,actors,rate,is_new,url,fiveStar,fourStar,threeStar,twoStar,oneStar))
            conn.commit()
        except IndexError:
            break
        except AttributeError:
            continue



if __name__ == "__main__":
    i = 0
    while i <=320:
        parse_info(get_html(i))
        i = i + 20
    conn.close()
    print("Data Record Finished...")

