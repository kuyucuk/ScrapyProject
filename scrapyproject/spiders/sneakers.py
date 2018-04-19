 # -*- coding: utf-8 -*-
import scrapy
from scrapy import Selector
import sqlite3

conn = sqlite3.connect('linkler.db')
c = conn.cursor()

connection = sqlite3.connect('products.db')
cursor = connection.cursor()

eleman=0
x=0

class ToScrapeCSSSpider(scrapy.Spider):
    c.execute("CREATE TABLE IF NOT EXISTS stuffToPlot(link TEXT)")
    c.execute('SELECT link FROM stuffToPlot')
    data = c.fetchall()

    name = "sneakers"

    for row in data:
        eleman = len(data)

    dizi = [1]
    seri = dizi * (eleman)

    for row in data:
        seri[x]=row[0]
        x=x+1

    start_urls = seri
    print(start_urls)

    c.close()
    conn.close()

    linksirasi=1

    def parse(self, response):
        with open("sneakers.txt", "a", encoding = "utf-8") as file:
            cursor.execute("CREATE TABLE IF NOT EXISTS PRODUCTS(marka TEXT, model TEXT, cins TEXT, renk TEXT, numaralar TEXT, IMG_url TEXT, stok TEXT, url TEXT, ozelliker TEXT, aciklama TEXT, eski_fiyat TEXT, yeni_fiyat TEXT)")

            for marka in response.css("span.product__brand"):
                yazar = marka.xpath('//*[@id="productdetail"]/section[1]/div[1]/div/div/div[2]/div/div[1]/div[1]/h1/span[1]//node()').extract()[0]
            file.write("*************************************************************************(" + str(self.linksirasi) + ")*************************************************************************")
            file.write("\nMarka:" + str(yazar) + "\n")

            for model in response.css("span.product__brand"):
                yazar2 = model.xpath('//*[@id="productdetail"]/section[1]/div[1]/div/div/div[2]/div/div[1]/div[1]/h1/span[2]//node()').extract()[0]
            file.write("_____________________________________________________________________________________________________________________________________________________")
            file.write("\nModel:" + str(yazar2) + "\n")

            for cins in response.css("span.product__brand"):
                yazar3 = cins.xpath('//*[@id="productdetail"]/section[1]/div[1]/div/div/div[2]/div/div[1]/div[1]/h1/span[3]//node()').extract()[0]
            file.write("_____________________________________________________________________________________________________________________________________________________")
            file.write("\nCins:" + str(yazar3) + "\n")

            for renk in response.css("span.color-desc"):
                yazar4 = renk.xpath('//*[@id="productdetail"]/section[1]/div[1]/div/div/div[2]/div/div[3]/div[1]/div/div/div/span//node()').extract()[0]
            file.write("_____________________________________________________________________________________________________________________________________________________")
            file.write("\nRenk:" + str(yazar4) + "\n")

            for numara in response.css("div.select"):
                doc = numara.xpath('//*[@id="secondary-select"]').extract()
                sel = Selector(text=str(doc), type="html")
                yazar5 = sel.xpath('//option//@value').extract()
            file.write("_____________________________________________________________________________________________________________________________________________________")
            file.write("\nAyakkabı Numaraları:" + str(yazar5) + "\n")

            for img in response.css("div.viewer__image"):
                yazar6 = img.xpath('//div[@class="viewer__image"]/img[1]/@src').extract()[0]
            file.write("_____________________________________________________________________________________________________________________________________________________")
            file.write("\nIMG URL:" + str(yazar6) + "\n")

            for stok in response.css("div.row"):
                yazar7 = stok.xpath('//*[@id="productdetail"]/section[1]/div[1]/div/div/div[2]/div/div[4]/div[2]/div[1]/div/span/node()').extract()[2]
            file.write("_____________________________________________________________________________________________________________________________________________________")
            file.write("\nStok durumu:" + str(yazar7))

            for URL in response.xpath("/html/head"):
                yazar8 = URL.xpath('//link/@href').extract()[7]
            file.write("_____________________________________________________________________________________________________________________________________________________")
            file.write("\nURL:" + str(yazar8) + "\n")

            if str(response.xpath('//*[@id="productdetail"]/section[1]/section/section/div/div/article/div[1]/div[2]/div[1]/@*').extract()) != str(['product-description__table']):
                for title in response.css('ul.product-description__list'):
                    yazar9 = title.xpath('//*[@id="productdetail"]/section[1]/section/section/div/div/article/div[1]/ul/li/text()').extract()
                file.write("_____________________________________________________________________________________________________________________________________________________")
                file.write("\nÖzellikler:" + str(yazar9) + "\n")
            else:
                for title in response.css('div.product-description__table'):
                    yazar9 = title.xpath('//*[@id="productdetail"]/section[1]/section/section/div/div/article/div[1]/div/div//span/text()').extract()
                file.write("_____________________________________________________________________________________________________________________________________________________")
                file.write("\nÖzellikler:" + str(yazar9) + "\n")

            for title in response.css('span.product-description__text'):
                yazar10 = title.xpath('//*[@id="productdetail"]/section[1]/section/section/div/div/article/div[2]/span/p/text()').extract()
            file.write("_____________________________________________________________________________________________________________________________________________________")
            file.write("\nAçıklama:" + str(yazar10) + "\n")

            for eskifiyat in response.css("span.nobreak"):
                yazar11 = eskifiyat.xpath('//*[@id="productdetail"]/section[1]/div[1]/div/div/div[2]/div/div[4]/div[1]/div/div/span/span/span/node()').extract()[0]
            if str(response.xpath('//*[@id="productdetail"]/section[1]/div[1]/div/div/div[2]/div/div[4]/div[1]/div/@class').extract()[0]) != "overall-price row":
                file.write("_____________________________________________________________________________________________________________________________________________________")
                file.write("\nEski Fiyat:" + str(yazar11) + "\n")

            for yenifiyat in response.xpath('//*[@id="productdetail"]/section[1]/div[1]/div/div/div[2]/div/div[4]/div[1]/div'):
                if str(response.xpath('//*[@id="productdetail"]/section[1]/div[1]/div/div/div[2]/div/div[4]/div[1]/div/@class').extract()[0])!= "overall-price row":
                    yazar12 = yenifiyat.xpath('//*[@id="productdetail"]/section[1]/div[1]/div/div/div[2]/div/div[4]/div[1]/div/div/span/span/span/node()').extract()[1]
                else:
                    yazar12 = yazar11
            if yazar12 != yazar11:
                file.write("_____________________________________________________________________________________________________________________________________________________")
                file.write("\nYeni Fiyat:" + str(yazar12) + "\n")
            else:
                file.write("_____________________________________________________________________________________________________________________________________________________")
                file.write("\nFiyat:" + str(yazar12) + "\n")
            print("*************************************************************************(" + str(self.linksirasi) + ")*************************************************************************\n\n\n\n\n")

            cursor.execute('SELECT * FROM PRODUCTS')
            cursor.execute("INSERT INTO PRODUCTS VALUES (?,?,?,?,?,?,?,?,?,?,?,?)", (str(yazar),str(yazar2),str(yazar3),str(yazar4),str(yazar5),str(yazar6),str(yazar7),str(yazar8),str(yazar9),str(yazar10),str(yazar11),str(yazar12)))
            connection.commit()
        self.linksirasi+=1



