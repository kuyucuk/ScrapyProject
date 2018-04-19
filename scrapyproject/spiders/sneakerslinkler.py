# -*- coding: utf-8 -*-
import scrapy
from scrapy import Selector
import sqlite3

conn = sqlite3.connect('linkler.db')
c = conn.cursor()


class MySpider(scrapy.Spider):
    name = "sneakerslinkler"
    start_urls = [
        'https://www.sportscheck.com/schuhe/herren/',
        'https://www.sportscheck.com/s/sneakers/'
    ]

    linksayisi = len(start_urls)
    print(linksayisi)

    def parse(self, response):

        with open("sneakerslinkler.txt", "a", encoding="utf-8") as file:

            for hey in response.xpath("//html/body"):
                liste = hey.xpath("//main/div[4]/div/div/div[3]/div/div[1]/a/@href").extract()
                elemansayisi = (len(liste) + 1) * self.linksayisi

            dizi = [1]
            links = dizi * (elemansayisi)


            for title in response.xpath("//html/body"):

                for x in range(1, elemansayisi):
                    links[x] = title.xpath("//main/div[4]/div[" + str(x) + "]/div/div[3]/div/div[1]/a/@href").extract()[
                        0]
                    file.write(
                        "________________________________________________________________________________________________________________________________")
                    file.write("\n" + "link" + str(x) + ": " + str(links[x]) + "\n")

                    c.execute("CREATE TABLE IF NOT EXISTS stuffToPlot(link TEXT)")

                    c.execute('SELECT * FROM stuffToPlot')
                    data = c.fetchall()
                    print(data)
                    for row in data:
                        print(row)

                    c.execute("INSERT INTO stuffToPlot VALUES('" + str(links[x]) + "')")
                    conn.commit()
                c.close()
                conn.close()
