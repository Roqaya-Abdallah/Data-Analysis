import requests
import csv
from bs4 import BeautifulSoup
res = []
Md = []

date = input("please enter the date of matches MM/DD/YY:  ")
page = requests.get(f"https://www.yallakora.com/match-center?date={date}")
src = page.content
soup = BeautifulSoup(src, "lxml")

champs = soup.find_all("div", {"class": "matchCard"})
for i in range(len(champs)):
    champ = champs[i].find("div", {"class": "title"}).find("h2").text.strip()
    matches = champs[i].find_all("li")
    for i in range(len(matches)):
        teamA = matches[i].find(
            "div", {"class": "teamA"}).find("p").text.strip()
        teamB = matches[i].find(
            "div", {"class": "teamB"}).find("p").text.strip()
        res = matches[i].find("div", {"class": "MResult"}).find_all(
            "span", {"class": "score"})
        score = f"{res[0].text.strip()}-{res[1].text.strip()}"
        # add the inf of every matches
        Md.append({"البطولة": champ, "الفريق الاول": teamA,
                  "الفريق الثاني": teamB, "النتيجة": score})
keys = Md[0].keys()
with open("E:\Data Analysis/Matches.csv", "w", encoding='utf')as scraping:
    dict_writer = csv.DictWriter(scraping, keys)
    dict_writer.writeheader()
    dict_writer.writerows(Md)


print("file created")
