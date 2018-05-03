# -*- coding: utf-8 -*-
import sqlite3
import csv
import os

def convert ():
    bagla = sqlite3.connect('database.db')

    sec = bagla.cursor()
    sec.execute('SELECT * FROM PRODUCTS')

    with open("out.csv", "w", newline='') as csv_file:  # Python 3 version
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow([i[0] for i in sec.description])  # write headers
        csv_writer.writerows(sec)

    f = open('out.csv')
    csv_f = csv.reader(f)
    data = []

    for row in csv_f:
        data.append(row)
    f.close()

    def convert_row(row):
        return """  <row>
        <marka>%s</marka>
        <model>%s</model>
        <cins>%s</cins>
        <renk>%s</renk>
        <numaralar>%s</numaralar>
        <IMG_url>%s</IMG_url>
        <stok>%s</stok>
        <url>%s</url>
        <ozelliker>%s</ozelliker>
        <aciklama>%s</aciklama>
        <eski_fiyat>%s</eski_fiyat>
        <yeni_fiyat>%s</yeni_fiyat>
      </row>""" % (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11])

    data = """<?xml version="1.0" encoding="UTF-8"?>
    <root>
    """ + '\n'.join([convert_row(row) for row in data[1:]]) + """
    </root>"""

    file = open("output.xml", "w", encoding="utf-8")

    veri = str(data).replace("&h=", "&amp;h=")
    file.write(veri)
    file.close()

    file = open("output.xml", "w", encoding="utf-8")
    veri = veri.replace("&qlt=", "&amp;qlt=")
    file.write(veri)
    file.close()

    file = open("output.xml", "w", encoding="utf-8")
    veri = veri.replace("&unsharp=", "&amp;unsharp=")
    file.write(veri)
    file.close()

    file = open("output.xml", "w", encoding="utf-8")
    veri = veri.replace("&nbsp", "")
    file.write(veri)
    file.close()

    file = open("output.xml", "w", encoding="utf-8")
    veri = veri.replace("&", "&amp;")
    file.write(veri)
    file.close()

    # print (veri)

    file = open("output.xml", "r", encoding="utf-8")

    dosya = file.read()
    print(dosya)

    file = open("dataX.xml", "w", encoding="utf-8")
    degisim = str(dosya).replace("FIELD1>", "ProductName>")
    file.write(degisim)
    file.close()

    os.remove("out.csv")
    os.remove("output.xml")
    try:
        os.remove("sneakerslinkler.txt")
    except:
        a = 1
    try:
        os.remove("sneakers.txt")
    except:
        a = 1

    file = open("dataX.xml", "w", encoding="utf-8")
    degisim = degisim.replace("FIELD2", "Model")
    file.write(degisim)
    file.close()
    file = open("dataX.xml", "w", encoding="utf-8")
    degisim = degisim.replace("FIELD3", "Brand")
    file.write(degisim)
    file.close()
    file = open("dataX.xml", "w", encoding="utf-8")
    degisim = degisim.replace("FIELD4", "Color")
    file.write(degisim)
    file.close()
    file = open("dataX.xml", "w", encoding="utf-8")
    degisim = degisim.replace("FIELD5", "AvailableSizes")
    file.write(degisim)
    file.close()
    file = open("dataX.xml", "w", encoding="utf-8")
    degisim = degisim.replace("FIELD6", "ImageURL1")
    file.write(degisim)
    file.close()
    file = open("dataX.xml", "w", encoding="utf-8")
    degisim = degisim.replace("FIELD7", "Stock")
    file.write(degisim)
    file.close()
    file = open("dataX.xml", "w", encoding="utf-8")
    degisim = degisim.replace("FIELD8", "ProductURL")
    file.write(degisim)
    file.close()
    file = open("dataX.xml", "w", encoding="utf-8")
    degisim = degisim.replace("FIELD9", "Material")
    file.write(degisim)
    file.close()
    file = open("dataX.xml", "w", encoding="utf-8")
    degisim = degisim.replace("FIELD10", "Description")
    file.write(degisim)
    file.close()
    file = open("dataX.xml", "w", encoding="utf-8")
    degisim = degisim.replace("FIELD11", "OldPrice")
    file.write(degisim)
    file.close()
    file = open("dataX.xml", "w", encoding="utf-8")
    degisim = degisim.replace("FIELD12", "NewPrice")
    file.write(degisim)
    file.close()

    file = open("dataX.xml", "w", encoding="utf-8")
    degisim = str(dosya).replace("marka>", "ProductName>")
    file.write(degisim)
    file.close()
    file = open("dataX.xml", "w", encoding="utf-8")
    degisim = degisim.replace("model>", "Model>")
    file.write(degisim)
    file.close()
    file = open("dataX.xml", "w", encoding="utf-8")
    degisim = degisim.replace("cins>", "Brand>")
    file.write(degisim)
    file.close()
    file = open("dataX.xml", "w", encoding="utf-8")
    degisim = degisim.replace("renk>", "Color>")
    file.write(degisim)
    file.close()
    file = open("dataX.xml", "w", encoding="utf-8")
    degisim = degisim.replace("numaralar>", "AvailableSizes>")
    file.write(degisim)
    file.close()
    file = open("dataX.xml", "w", encoding="utf-8")
    degisim = degisim.replace("IMG_url>", "ImageURL1>")
    file.write(degisim)
    file.close()
    file = open("dataX.xml", "w", encoding="utf-8")
    degisim = degisim.replace("stok>", "Stock>")
    file.write(degisim)
    file.close()
    file = open("dataX.xml", "w", encoding="utf-8")
    degisim = degisim.replace("url>", "ProductURL>")
    file.write(degisim)
    file.close()
    file = open("dataX.xml", "w", encoding="utf-8")
    degisim = degisim.replace("ozelliker>", "Material>")
    file.write(degisim)
    file.close()
    file = open("dataX.xml", "w", encoding="utf-8")
    degisim = degisim.replace("aciklama>", "Description>")
    file.write(degisim)
    file.close()
    file = open("dataX.xml", "w", encoding="utf-8")
    degisim = degisim.replace("eski_fiyat>", "OldPrice>")
    file.write(degisim)
    file.close()
    file = open("dataX.xml", "w", encoding="utf-8")
    degisim = degisim.replace("yeni_fiyat>", "NewPrice>")
    file.write(degisim)
    file.close()

    file = open("dataX.xml", "w", encoding="utf-8")
    degisim = degisim.replace("""    <ProductName>marka</ProductName>
        <Model>model</Model>
        <Brand>cins</Brand>
        <Color>renk</Color>
        <AvailableSizes>numaralar</AvailableSizes>
        <ImageURL1>IMG_url</ImageURL1>
        <Stock>stok</Stock>
        <ProductURL>url</ProductURL>
        <Material>ozelliker</Material>
        <Description>aciklama</Description>
        <OldPrice>eski_fiyat</OldPrice>
        <NewPrice>yeni_fiyat</NewPrice>""", "")
    file.write(degisim)
    file.close()

    file = open("dataX.xml", "w", encoding="utf-8")
    degisim = degisim.replace("""  <row>

      </row>""", "")
    file.write(degisim)
    file.close()

    file = open("dataX.xml", "w", encoding="utf-8")
    degisim = degisim.replace("""<root>

      <row>""", """<root>
      <row>""")
    file.write(degisim)
    file.close()

    file = open("dataX.xml", "w", encoding="utf-8")
    degisim = degisim.replace("""
    </Stock>""", "</Stock>")
    file.write(degisim)
    file.close()

    file = open("dataX.xml", "w", encoding="utf-8")
    degisim = degisim.replace("""<Stock>
    """, "<Stock>")
    file.write(degisim)
    file.close()

    file = open("dataX.xml", "w", encoding="utf-8")
    degisim = degisim.replace("&apos;", "")
    file.write(degisim)
    file.close()

    file = open("dataX.xml", "w", encoding="utf-8")
    degisim = degisim.replace("[, ", "")
    file.write(degisim)
    file.close()

    file = open("dataX.xml", "w", encoding="utf-8")
    degisim = degisim.replace(", ]", "")
    file.write(degisim)
    file.close()

    file = open("dataX.xml", "w", encoding="utf-8")
    degisim = degisim.replace(" 2/3", "")
    file.write(degisim)
    file.close()

    file = open("dataX.xml", "w", encoding="utf-8")
    degisim = degisim.replace(" 1/3", "")
    file.write(degisim)
    file.close()

    file = open("dataX.xml", "w", encoding="utf-8")
    degisim = degisim.replace(" 1/2", "")
    file.write(degisim)
    file.close()

    file = open("dataX.xml", "w", encoding="utf-8")
    degisim = degisim.replace(", ,", ",")
    file.write(degisim)
    file.close()

    file = open("dataX.xml", "w", encoding="utf-8")
    degisim = degisim.replace("]</Av", "</Av")
    file.write(degisim)
    file.close()

    file = open("dataX.xml", "w", encoding="utf-8")
    degisim = degisim.replace("['', ", "")
    file.write(degisim)
    file.close()

    file = open("dataX.xml", "w", encoding="utf-8")
    degisim = degisim.replace("'', ", "")
    file.write(degisim)
    file.close()

    file = open("dataX.xml", "w", encoding="utf-8")
    degisim = degisim.replace(",''", "")
    file.write(degisim)
    file.close()

    for i in range(0, 50):
        file = open("dataX.xml", "w", encoding="utf-8")
        degisim = degisim.replace("'" + str(i) + "'", str(i))
        file.write(degisim)
        file.close()

    for i in range(0, 50):
        file = open("dataX.xml", "w", encoding="utf-8")
        degisim = degisim.replace(str(i) + ", " + str(i) + ", ", "" + str(i) + ",")
        file.write(degisim)
        file.close()

    file = open("dataX.xml", "w", encoding="utf-8")
    degisim = degisim.replace(" €", "")
    file.write(degisim)
    file.close()

    for i in range(0, 50):
        file = open("dataX.xml", "w", encoding="utf-8")
        degisim = degisim.replace(str(i) + ", ", str(i) + ",")
        file.write(degisim)
        file.close()

    file = open("dataX.xml", "w", encoding="utf-8")
    degisim = degisim.replace(",''", "")
    file.write(degisim)
    file.close()

    file = open("dataX.xml", "w", encoding="utf-8")
    degisim = degisim.replace("<Material>[", "<Material>")
    file.write(degisim)
    file.close()

    file = open("dataX.xml", "w", encoding="utf-8")
    degisim = degisim.replace("]</Material>", "</Material>")
    file.write(degisim)
    file.close()

    file = open("dataX.xml", "w", encoding="utf-8")
    degisim = degisim.replace("<Description>[", "<Description>")
    file.write(degisim)
    file.close()

    file = open("dataX.xml", "w", encoding="utf-8")
    degisim = degisim.replace("]</Description>", "</Description>")
    file.write(degisim)
    file.close()

    file = open("dataX.xml", "w", encoding="utf-8")
    degisim = degisim.replace("""</Brand>
        """, """</Brand>
        <Category>Sneakers</Category>
        """)
    file.write(degisim)
    file.close()

    file = open("dataX.xml", "w", encoding="utf-8")
    degisim = degisim.replace("""</Category>
        """, """</Category>
        <Subcategory>Sport</Subcategory>
        <CPC>0.35</CPC>
        <ShippingCost>4.9</ShippingCost>
        """)
    file.write(degisim)
    file.close()

    file = open("dataX.xml", "w", encoding="utf-8")
    degisim = degisim.replace("""
        <ProductName>""", """
        <SKU>001</SKU>
        <ProductName>""")
    file.write(degisim)
    file.close()
    print(degisim)

convert()
