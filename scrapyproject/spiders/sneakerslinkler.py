 # -*- coding: utf-8 -*-
import scrapy
from scrapy import Selector
import sqlite3

conn = sqlite3.connect('linkler.db')
c = conn.cursor()



class MySpider(scrapy.Spider):
    name = "sneakerslinkler"
    start_urls = [
        'https://www.sportscheck.com/schuhe/herren/'
    ]

    def parse(self, response):

        with open("sneakerslinkler.txt", "a", encoding = "utf-8") as file:

            for hey in response.xpath("/html"):
                liste = hey.xpath("//body/div[4]/main/div[4]/div/div/div/a/@href").extract()
                elemansayisi=len(liste)+1

            dizi = [1]
            links = dizi * (elemansayisi)

            for title in response.xpath("/html"):

                for x in range (1,elemansayisi):
                    links[x] = title.xpath("//body/div[4]/main/div[4]/div[" +str(x)+ "]/div/div/a/@href").extract()[0]
                    file.write("________________________________________________________________________________________________________________________________")
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