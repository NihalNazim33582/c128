import time
import csv
import requests
from bs4 import BeautifulSoup
from selenium import webdriver

Start_url = "https://exoplanets.nasa.gov/discovery/exoplanet-catalog/"
browswer = webdriver.Chrome("/Users/naseemahusain/Downloads/chromedriver")
browswer.get(Start_url)
time.sleep(10)

header = ["name", "light_years_from_earth", "planet_mass", "stellar_magnitude", "discovery_date", "HyperLink",
          "Planet_Type", "Discovery_Date", "Planet_Radius", "Orbital_Radius", "Orbital_Period", "Eccentricity"]
planetData = []
newData = []


def Scrapping2():

    for i in range(1, 441):
        while True:
            time.sleep(2)
            soup = BeautifulSoup(browser.page_source, "html.parser")
            currentPageNum = int(soup.find_all(
                'input', attrs={'class', "page_num"})[0]).get("value")
            if currentPageNum < i:
                browser.find_element_by_xpath(
                    '//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a')
            elif currentPageNum > i:
                browser.find_element_by_xpath(
                    '//*[@id="primary_column"]/footer/div/div/div/nav/span[1]/a')
            else:
                break

        for ul_tag in soup.find_all('ul', attrs=['class', 'exoplanet']):
            li_tag = ul_tag.find_all('li')
            allData = []
            for index, li_tag in enumerate(li_tag):
                if index == 0:
                    allData.append(li_tag.find_all('a')[0].contents[0])
                else:
                    try:
                        allData.append(li_tag.contents[0])

                    except:
                        addData.append('')

            hyperLink = li_tag[0]
            allData.append('https://exoplanets.nasa.gov/' +
                           hyperLink.find_all('a', href=True)[0]['href'])

        planetData.append(allData)
        browser.find_element_by_xpath(
            '//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a')
        print(f'{i}Page Finished.')


def HyperLinks(hyperLink):
    try:
        page = requests.get(hyperLink)
        soup = BeautifulSoup(page.content, 'html.parser')
        allData = []

        for tr_tags in soap.find_all('tr', attrs={'class', 'fact_row'}):
            td_tag = tr_tags.find_all('td')
            for i in td_tag:
                try:
                    allData.append(i.find_all(
                        'div', attrs={'class', 'value'})[0].contents[0])
                except:
                    allData.append('')
        newData.appned(allData)
    except:
        HyperLinks(hyperLink)

Scrapping2()

for index,item in enumerate(planetData):
    HyperLinks(item[5])

finalData=[]
for index,item in enumerate(planetData):
    finalData_index=newData[index]
    finalData.append(item+finalData[index])

with open('save.csv', 'w') as f:
    csvWriter = csv.writer(f)
    csvWriter.writerow(headers)
    csvWriter.writerows(finalData)