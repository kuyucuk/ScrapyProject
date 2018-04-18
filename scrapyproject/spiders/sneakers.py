 # -*- coding: utf-8 -*-
import scrapy
from scrapy import Selector
import sqlite3

conn = sqlite3.connect('linkler.db')
c = conn.cursor()



class ToScrapeCSSSpider(scrapy.Spider):
    c.execute("CREATE TABLE IF NOT EXISTS stuffToPlot(link TEXT)")

    c.execute('SELECT * FROM stuffToPlot')
    data = c.fetchall()


    name = "sneakers"
    start_urls = [

    ]

    start_urls = data
    print(start_urls)
    c.close()
    conn.close()


    start_urls = [
        ('https://www.sportscheck.com/nike-arrowz-sneaker-herren-p260419-F052/white-black/'),
        'https://www.sportscheck.com/adidas-questar-byd-sneaker-herren-p280290-F040/core-black/',
        'https://www.sportscheck.com/puma-basket-heart-patent-sneaker-damen-p266770-F004/marshmallow-marshmallow/',
        'https://www.sportscheck.com/tom-tailor-boyfriend-jeans-damen-p277474-F007/mid-stone-wash-denim/',
        'https://www.sportscheck.com/adidas-cf-lite-racer-cc-sneaker-herren-p280298-F052/ftwr-white/',
        'https://www.sportscheck.com/nike-air-max-thea-sneaker-damen-p282416-F034/barely-rose/',
        'https://www.sportscheck.com/nike-md-runner2-sneaker-herren-p282308-F041/black-black-white/',
        'https://www.sportscheck.com/nike-internationalist-sneaker-damen-p282415-F034/particle-rose-vast-grey/',
        'https://www.sportscheck.com/project-delray-wavey-sneaker-damen-p291470-F004/stone-dusty-pink/',
        'https://www.sportscheck.com/reebok-trilux-sneaker-damen-p280049-F007/blau-rosa/'
    ]


    def parse(self, response):
        with open("sneakers.txt", "a", encoding = "utf-8") as file:
            for marka in response.css("span.product__brand"):
                doc = marka.xpath('//*[@id="productdetail"]/section[1]/div[1]/div/div/div[2]/div/div[1]/div[1]/h1/span[1]').extract()
                sel = Selector(text=str(doc), type="html")
                yazar = sel.xpath('//span//node()').extract()
            file.write("********************************************************************************************************************************")
            file.write("\nMarka:" + str(yazar) + "\n")

            for model in response.css("span.product__brand"):
                doc = model.xpath('//*[@id="productdetail"]/section[1]/div[1]/div/div/div[2]/div/div[1]/div[1]/h1/span[2]').extract()
                sel = Selector(text=str(doc), type="html")
                yazar2 = sel.xpath('//span//node()').extract()
            file.write("________________________________________________________________________________________________________________________________")
            file.write("\nModel:" + str(yazar2) + "\n")

            for cins in response.css("span.product__brand"):
                doc = cins.xpath('//*[@id="productdetail"]/section[1]/div[1]/div/div/div[2]/div/div[1]/div[1]/h1/span[3]').extract()
                sel = Selector(text=str(doc), type="html")
                yazar3 = sel.xpath('//span//node()').extract()
            file.write("________________________________________________________________________________________________________________________________")
            file.write("\nCins:" + str(yazar3) + "\n")

            for renk in response.css("span.color-desc"):
                doc = renk.xpath('//*[@id="productdetail"]/section[1]/div[1]/div/div/div[2]/div/div[3]/div[1]/div/div/div/span').extract()
                sel = Selector(text=str(doc), type="html")
                yazar4 = sel.xpath('//span//node()').extract()
            file.write("________________________________________________________________________________________________________________________________")
            file.write("\nRenk:" + str(yazar4) + "\n")

            for numara in response.css("div.select"):
                doc = numara.xpath('//*[@id="secondary-select"]').extract()
                sel = Selector(text=str(doc), type="html")
                yazar5 = sel.xpath('//option//@value').extract()
            file.write("________________________________________________________________________________________________________________________________")
            file.write("\nAyakkabı Numaraları:" + str(yazar5) + "\n")

            for img in response.css("div.viewer__image"):
                yazar6 = img.xpath('//div[@class="viewer__image"]/img[1]/@src').extract()
            file.write("________________________________________________________________________________________________________________________________")
            file.write("\nIMG URL:" + str(yazar6) + "\n")

            for stok in response.css("div.row"):
                yazar7 = stok.xpath('//*[@id="productdetail"]/section[1]/div[1]/div/div/div[2]/div/div[4]/div[2]/div[1]/div/span/node()').extract()[2]
            file.write("________________________________________________________________________________________________________________________________")
            file.write("\nStok durumu:" + str(yazar7))

            for URL in response.xpath("/html/head"):
                yazar8 = URL.xpath('//link/@href').extract()[7]
            file.write("________________________________________________________________________________________________________________________________")
            file.write("\nURL:" + str(yazar8) + "\n")

            for title in response.css('ul.product-description__list'):
                yazar9 = title.xpath('//*[@id="productdetail"]/section[1]/section/section/div/div/article/div[1]/ul/li/text()').extract()
            file.write("________________________________________________________________________________________________________________________________")
            file.write("\nÖzellikler:" + str(yazar9) + "\n")

            for title in response.css('span.product-description__text'):
                yazar10 = title.xpath('//*[@id="productdetail"]/section[1]/section/section/div/div/article/div[2]/span/p/text()').extract()
            file.write("________________________________________________________________________________________________________________________________")
            file.write("\nAçıklama:" + str(yazar10) + "\n")

            for eskifiyat in response.css("span.nobreak"):
                yazar11 = eskifiyat.xpath('//*[@id="productdetail"]/section[1]/div[1]/div/div/div[2]/div/div[4]/div[1]/div/div/span/span/span/node()').extract()[0]
            if str(response.xpath('//*[@id="productdetail"]/section[1]/div[1]/div/div/div[2]/div/div[4]/div[1]/div/@class').extract()[0]) != "overall-price row":
                file.write("________________________________________________________________________________________________________________________________")
                file.write("\nEski Fiyat:" + str(yazar11) + "\n")

            for yenifiyat in response.xpath('//*[@id="productdetail"]/section[1]/div[1]/div/div/div[2]/div/div[4]/div[1]/div'):
                if str(response.xpath('//*[@id="productdetail"]/section[1]/div[1]/div/div/div[2]/div/div[4]/div[1]/div/@class').extract()[0])!= "overall-price row":
                    yazar12 = yenifiyat.xpath('//*[@id="productdetail"]/section[1]/div[1]/div/div/div[2]/div/div[4]/div[1]/div/div/span/span/span/node()').extract()[1]
                else:
                    yazar12 = yazar11
            if yazar12 != yazar11:
                file.write("________________________________________________________________________________________________________________________________")
                file.write("\nYeni Fiyat:" + str(yazar12) + "\n")
            else:
                file.write("________________________________________________________________________________________________________________________________")
                file.write("\nFiyat:" + str(yazar12) + "\n")
            file.write("********************************************************************************************************************************\n\n\n\n\n")


