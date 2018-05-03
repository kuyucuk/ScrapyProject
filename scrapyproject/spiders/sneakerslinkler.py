# -*- coding: utf-8 -*-
import scrapy
from scrapy import Selector
import sqlite3

conn = sqlite3.connect('database.db')
c = conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS PRODUCTS(marka TEXT, model TEXT, cins TEXT, renk TEXT, numaralar TEXT, IMG_url TEXT, stok TEXT, url TEXT, ozelliker TEXT, aciklama TEXT, eski_fiyat TEXT, yeni_fiyat TEXT)")


class MySpider(scrapy.Spider):
    name = "sneakerslinkler"
    start_urls = [
        #'https://www.sportscheck.com/schuhe/herren/',
        #'https://www.sportscheck.com/badminton/'
        'https://www.sportscheck.com/s/sneakers/',
        'https://www.sportscheck.com/s/sneakers/2',
        'https://www.sportscheck.com/s/sneakers/3',
        'https://www.sportscheck.com/s/sneakers/4',
        'https://www.sportscheck.com/s/sneakers/5',
        'https://www.sportscheck.com/s/sneakers/6',
        'https://www.sportscheck.com/s/sneakers/7',
        'https://www.sportscheck.com/s/sneakers/8',
        'https://www.sportscheck.com/s/sneakers/9',
        'https://www.sportscheck.com/s/sneakers/10',
        'https://www.sportscheck.com/s/sneakers/11',
        'https://www.sportscheck.com/s/sneakers/12',
        'https://www.sportscheck.com/s/sneakers/13',
        'https://www.sportscheck.com/s/sneakers/14',
        'https://www.sportscheck.com/s/sneakers/15',
        'https://www.sportscheck.com/s/sneakers/16',
        'https://www.sportscheck.com/s/sneakers/17',
        'https://www.sportscheck.com/s/sneakers/18',
        'https://www.sportscheck.com/s/sneakers/18',
        'https://www.sportscheck.com/s/sneakers/20',
        'https://www.sportscheck.com/s/sneakers/21',
        'https://www.sportscheck.com/s/sneakers/22',
        'https://www.sportscheck.com/s/sneakers/23',
        'https://www.sportscheck.com/s/sneakers/24',
        'https://www.sportscheck.com/s/sneakers/25',
        'https://www.sportscheck.com/s/sneakers/26',
        'https://www.sportscheck.com/s/sneakers/27',
        'https://www.sportscheck.com/s/sneakers/28',
        'https://www.sportscheck.com/s/sneakers/28',
        'https://www.sportscheck.com/s/sneakers/29',
        'https://www.sportscheck.com/s/sneakers/30',
        'https://www.sportscheck.com/s/sneakers/31',
        'https://www.sportscheck.com/s/sneakers/32'

    ]

    linksayisi = len(start_urls)
    print(linksayisi)
    linksirasi = 1

    def parse(self, response):

        with open("sneakerslinkler.txt", "a", encoding="utf-8") as file:

            for hey in response.xpath("//html/body"):
                liste = hey.xpath("//main/div[5]/div/div/div[3]/div/div[1]/a/@href").extract()
                elemansayisi = (len(liste) + 1) * self.linksayisi



            dizi = [1]
            links = dizi * (elemansayisi)

            for title in response.xpath("//html/body"):

                for x in range(1, elemansayisi):
                    links[x] = title.xpath("//main/div[5]/div[" + str(x) + "]/div/div[3]/div/div[1]/a/@href").extract()[0]
                    file.write("________________________________________________________________________________________________________________________________")
                    file.write("\n" + "link" + str(self.linksirasi) + ": " + str(links[x]) + "\n")

                    self.linksirasi += 1

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
