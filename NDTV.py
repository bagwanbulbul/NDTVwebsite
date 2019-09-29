#NDTV Website from Scrape the Data

import requests
from bs4 import BeautifulSoup
from pprint import pprint

def getUrl():
    url="https://www.ndtv.com/india?pfrom=home-mainnavgation"
    response=requests.get(url)
    soup=BeautifulSoup(response.text,"html.parser")

    main_div=soup.find("div",class_="ins_left_rhs")
    find_lis=main_div.findAll("li")
    dictionary={}
    newsPageUrl=[]
    for index in find_lis:
        try:
            url=index.find("div",class_="new_storylising_img").a["href"]
            newsPageUrl.append(url)
        except AttributeError:
            continue
    return newsPageUrl
url_list=getUrl()

def Url_detail(urls):
    NdtvDetails=[]
    WholeNdtvData={}
    for index in urls:
        NdtvParagraph=[]
        dictionary={}
        res=requests.get(index)
        soup=BeautifulSoup(res.text,"html.parser")

        headline=soup.find("div",class_="ins_lftcont640 clr")
        try:
            title=headline.find("div",class_="ins_headline").h1.get_text()

            newsDateList=soup.find("div",class_="ins_dateline").get_text()
            newsDate=newsDateList.split("|")
            wholeDate=(newsDate[2])

            newsOuther=(newsDate[1])

            pragraph=soup.find("div",class_="ins_lftcont640 clr")
            pra=pragraph.findAll("p")
            for i in pra:
                pragraphs = i.get_text()
                NdtvParagraph.append(pragraphs)
                            
            dictionary["pragraph"]=NdtvParagraph
            dictionary["heading"]=title
            dictionary["aouther"]=newsOuther
            dictionary["date"]=wholeDate
            NdtvDetails.append(dictionary)
        
        except AttributeError:
            continue
        except TypeError:
            continue
    WholeNdtvData["NDTV_DATA"]=NdtvDetails
    return WholeNdtvData
pprint(Url_detail(url_list))