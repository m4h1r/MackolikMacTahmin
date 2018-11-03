# Maçkolik Maç Tahmin v0.6 (28.10.2018)
# Written by Mahir Yıldızhan
# e-mail: info@mahiryildizhan.com
# site: www.mahiryildizhan.com

from sklearn import tree
import pandas
from selenium import webdriver
import csv
import numpy as np
from decimal import *

print("Please enter Mackolik link=")
url = input()
#url = "http://www.mackolik.com/Match/Default.aspx?id=2843827"
chrome_path = r"C:\Python36\chromedriver.exe"
driver = webdriver.Chrome(chrome_path)
driver.get(url)

EvSahibiTakim = (driver.find_element_by_xpath("""//*[@id="match-details"]/div/div[1]/div/div[2]/div[1]/div[1]/a""")).text
if EvSahibiTakim=='Aytemiz Alanyaspor': #Son 5 maçtaki isim ile takım adı uyuşmazlığı çözmek için.
	EvSahibiTakim='Alanyaspor'
elif EvSahibiTakim=='Akhisar Belediyespor': #Son 5 maçtaki isim ile takım adı uyuşmazlığı çözmek için.
	EvSahibiTakim='Akhisarspor'
elif EvSahibiTakim=='Karabükspor': #Son 5 maçtaki isim ile takım adı uyuşmazlığı çözmek için.
	EvSahibiTakim='Kardemir Karabükspor'
elif EvSahibiTakim=='Medicana Sivasspor': #Son 5 maçtaki isim ile takım adı uyuşmazlığı çözmek için.
	EvSahibiTakim='Sivasspor'
elif EvSahibiTakim=='Torku Konyaspor': #Son 5 maçtaki isim ile takım adı uyuşmazlığı çözmek için.
	EvSahibiTakim='Atiker Konyaspor'

DeplasmanTakimi = (driver.find_element_by_xpath("""//*[@id="match-details"]/div/div[1]/div/div[2]/div[3]/div[1]/a""")).text
if DeplasmanTakimi=='Aytemiz Alanyaspor': #Son 5 maçtaki isim ile takım adı uyuşmazlığı çözmek için.
	DeplasmanTakimi='Alanyaspor'
elif DeplasmanTakimi=='Akhisar Belediyespor': #Son 5 maçtaki isim ile takım adı uyuşmazlığı çözmek için.
	DeplasmanTakimi='Akhisarspor'
elif DeplasmanTakimi=='Karabükspor': #Son 5 maçtaki isim ile takım adı uyuşmazlığı çözmek için.
	DeplasmanTakimi='Kardemir Karabükspor'
elif DeplasmanTakimi=='Medicana Sivasspor': #Son 5 maçtaki isim ile takım adı uyuşmazlığı çözmek için.
	DeplasmanTakimi='Sivasspor'
elif DeplasmanTakimi=='Torku Konyaspor': #Son 5 maçtaki isim ile takım adı uyuşmazlığı çözmek için.
	DeplasmanTakimi='Atiker Konyaspor'

EvSahibiTakimD1 = (driver.find_element_by_xpath("""//*[@id="match-details"]/div/div[1]/div/div[2]/div[1]/div[4]/span""")).text

if len(EvSahibiTakimD1)==12:
	EvSahibiTakimD2=EvSahibiTakimD1[0:2]+EvSahibiTakimD1[3:6]
if len(EvSahibiTakimD1)==13:
	EvSahibiTakimD2=EvSahibiTakimD1[0:3]+EvSahibiTakimD1[4:7]

A0=Decimal(int(EvSahibiTakimD2)/100000).quantize(Decimal('1.0000'))

DeplasmanTakimD1 = (driver.find_element_by_xpath("""//*[@id="match-details"]/div/div[1]/div/div[2]/div[3]/div[4]/span""")).text

if len(DeplasmanTakimD1)==12:
	DeplasmanTakimD2=DeplasmanTakimD1[0:2]+DeplasmanTakimD1[3:6]
if len(DeplasmanTakimD1)==13:
	DeplasmanTakimD2=DeplasmanTakimD1[0:3]+DeplasmanTakimD1[4:7]

A9=Decimal(int(DeplasmanTakimD2)/100000).quantize(Decimal('1.0000'))

EvSahibiAvarajArti = 0
EvSahibiAvarajEksi = 0
Son5e1 = driver.find_element_by_xpath("""//*[@id="match-details"]/div/div[1]/div/div[2]/div[1]/div[3]/div[2]""").get_attribute("title")

if Son5e1[0:len(EvSahibiTakim)]==EvSahibiTakim : #Ev sahibi ilk sırada mı değil mi algılar.
	EvSahibiAvarajArti = EvSahibiAvarajArti + int(Son5e1[len(EvSahibiTakim)+1]) #İlk sırada ise + avaraja değer toplanır.
	EvSahibiAvarajEksi = EvSahibiAvarajEksi + int(Son5e1[len(EvSahibiTakim)+3])
elif Son5e1[0:len(EvSahibiTakim)]!=EvSahibiTakim :
	EvSahibiAvarajArti = EvSahibiAvarajArti + int(Son5e1[-((len(EvSahibiTakim))+15)])
	EvSahibiAvarajEksi = EvSahibiAvarajEksi + int(Son5e1[-((len(EvSahibiTakim))+17)])

if Son5e1[0:len(EvSahibiTakim)]==EvSahibiTakim : #Ev sahibi ilk sırada mı değil mi algılar.
	a1 = int(Son5e1[len(EvSahibiTakim)+1]) #İlk sırada ise + avaraja değer toplanır.
	b1 = int(Son5e1[len(EvSahibiTakim)+3])
elif Son5e1[0:len(EvSahibiTakim)]!=EvSahibiTakim :
	a1 = int(Son5e1[-((len(EvSahibiTakim))+15)])
	b1 = int(Son5e1[-((len(EvSahibiTakim))+17)])

if a1>b1:
	A1=1
elif a1==b1:
	A1=0
elif a1<b1:
	A1=-1

Son5e2 = driver.find_element_by_xpath("""//*[@id="match-details"]/div/div[1]/div/div[2]/div[1]/div[3]/div[3]""").get_attribute("title")

if Son5e2[0:len(EvSahibiTakim)]==EvSahibiTakim : #Ev sahibi ilk sırada mı değil mi algılar.
	EvSahibiAvarajArti = EvSahibiAvarajArti + int(Son5e2[len(EvSahibiTakim)+1]) #İlk sırada ise + avaraja değer toplanır.
	EvSahibiAvarajEksi = EvSahibiAvarajEksi + int(Son5e2[len(EvSahibiTakim)+3])
elif Son5e2[0:len(EvSahibiTakim)]!=EvSahibiTakim :
	EvSahibiAvarajArti = EvSahibiAvarajArti + int(Son5e2[-((len(EvSahibiTakim))+15)])
	EvSahibiAvarajEksi = EvSahibiAvarajEksi + int(Son5e2[-((len(EvSahibiTakim))+17)])

if Son5e2[0:len(EvSahibiTakim)]==EvSahibiTakim : #Ev sahibi ilk sırada mı değil mi algılar.
	a2 = int(Son5e2[len(EvSahibiTakim)+1]) #İlk sırada ise + avaraja değer toplanır.
	b2 = int(Son5e2[len(EvSahibiTakim)+3])
elif Son5e2[0:len(EvSahibiTakim)]!=EvSahibiTakim :
	a2 = int(Son5e2[-((len(EvSahibiTakim))+15)])
	b2 = int(Son5e2[-((len(EvSahibiTakim))+17)])

if a2>b2:
	A2=1
elif a2==b2:
	A2=0
elif a2<b2:
	A2=-1

Son5e3 = driver.find_element_by_xpath("""//*[@id="match-details"]/div/div[1]/div/div[2]/div[1]/div[3]/div[4]""").get_attribute("title")

if Son5e3[0:len(EvSahibiTakim)]==EvSahibiTakim : #Ev sahibi ilk sırada mı değil mi algılar.
	EvSahibiAvarajArti = EvSahibiAvarajArti + int(Son5e3[len(EvSahibiTakim)+1]) #İlk sırada ise + avaraja değer toplanır.
	EvSahibiAvarajEksi = EvSahibiAvarajEksi + int(Son5e3[len(EvSahibiTakim)+3])
elif Son5e3[0:len(EvSahibiTakim)]!=EvSahibiTakim :
	EvSahibiAvarajArti = EvSahibiAvarajArti + int(Son5e3[-((len(EvSahibiTakim))+15)])
	EvSahibiAvarajEksi = EvSahibiAvarajEksi + int(Son5e3[-((len(EvSahibiTakim))+17)])

if Son5e3[0:len(EvSahibiTakim)]==EvSahibiTakim : #Ev sahibi ilk sırada mı değil mi algılar.
	a3 = int(Son5e3[len(EvSahibiTakim)+1]) #İlk sırada ise + avaraja değer toplanır.
	b3 = int(Son5e3[len(EvSahibiTakim)+3])
elif Son5e3[0:len(EvSahibiTakim)]!=EvSahibiTakim :
	a3 = int(Son5e3[-((len(EvSahibiTakim))+15)])
	b3 = int(Son5e3[-((len(EvSahibiTakim))+17)])

if a3>b3:
	A3=1
elif a3==b3:
	A3=0
elif a3<b3:
	A3=-1

Son5e4 = driver.find_element_by_xpath("""//*[@id="match-details"]/div/div[1]/div/div[2]/div[1]/div[3]/div[5]""").get_attribute("title")

if Son5e4[0:len(EvSahibiTakim)]==EvSahibiTakim : #Ev sahibi ilk sırada mı değil mi algılar.
	EvSahibiAvarajArti = EvSahibiAvarajArti + int(Son5e4[len(EvSahibiTakim)+1]) #İlk sırada ise + avaraja değer toplanır.
	EvSahibiAvarajEksi = EvSahibiAvarajEksi + int(Son5e4[len(EvSahibiTakim)+3])
elif Son5e4[0:len(EvSahibiTakim)]!=EvSahibiTakim :
	EvSahibiAvarajArti = EvSahibiAvarajArti + int(Son5e4[-((len(EvSahibiTakim))+15)])
	EvSahibiAvarajEksi = EvSahibiAvarajEksi + int(Son5e4[-((len(EvSahibiTakim))+17)])

if Son5e4[0:len(EvSahibiTakim)]==EvSahibiTakim : #Ev sahibi ilk sırada mı değil mi algılar.
	a4 = int(Son5e4[len(EvSahibiTakim)+1]) #İlk sırada ise + avaraja değer toplanır.
	b4 = int(Son5e4[len(EvSahibiTakim)+3])
elif Son5e4[0:len(EvSahibiTakim)]!=EvSahibiTakim :
	a4 = int(Son5e4[-((len(EvSahibiTakim))+15)])
	b4 = int(Son5e4[-((len(EvSahibiTakim))+17)])

if a4>b4:
	A4=1
elif a4==b4:
	A4=0
elif a4<b4:
	A4=-1

Son5e5 = driver.find_element_by_xpath("""//*[@id="match-details"]/div/div[1]/div/div[2]/div[1]/div[3]/div[6]""").get_attribute("title")

if Son5e5[0:len(EvSahibiTakim)]==EvSahibiTakim : #Ev sahibi ilk sırada mı değil mi algılar.
	EvSahibiAvarajArti = EvSahibiAvarajArti + int(Son5e5[len(EvSahibiTakim)+1]) #İlk sırada ise + avaraja değer toplanır.
	EvSahibiAvarajEksi = EvSahibiAvarajEksi + int(Son5e5[len(EvSahibiTakim)+3])
elif Son5e5[0:len(EvSahibiTakim)]!=EvSahibiTakim :
	EvSahibiAvarajArti = EvSahibiAvarajArti + int(Son5e5[-((len(EvSahibiTakim))+15)])
	EvSahibiAvarajEksi = EvSahibiAvarajEksi + int(Son5e5[-((len(EvSahibiTakim))+17)])

if Son5e5[0:len(EvSahibiTakim)]==EvSahibiTakim : #Ev sahibi ilk sırada mı değil mi algılar.
	a5 = int(Son5e5[len(EvSahibiTakim)+1]) #İlk sırada ise + avaraja değer toplanır.
	b5 = int(Son5e5[len(EvSahibiTakim)+3])
elif Son5e5[0:len(EvSahibiTakim)]!=EvSahibiTakim :
	a5 = int(Son5e5[-((len(EvSahibiTakim))+15)])
	b5 = int(Son5e5[-((len(EvSahibiTakim))+17)])

if a5>b5:
	A5=1
elif a5==b5:
	A5=0
elif a5<b5:
	A5=-1

A6 = int(EvSahibiAvarajArti)
A7 = -(int(EvSahibiAvarajEksi))

DeplasmanAvarajArti = 0
DeplasmanAvarajEksi = 0

Son5d1 = driver.find_element_by_xpath("""//*[@id="match-details"]/div/div[1]/div/div[2]/div[3]/div[3]/div[2]""").get_attribute("title")

if Son5d1[0:len(DeplasmanTakimi)]==DeplasmanTakimi : #Ev sahibi ilk sırada mı değil mi algılar.
	DeplasmanAvarajArti = DeplasmanAvarajArti + int(Son5d1[len(DeplasmanTakimi)+1]) #İlk sırada ise + avaraja değer toplanır.
	DeplasmanAvarajEksi = DeplasmanAvarajEksi + int(Son5d1[len(DeplasmanTakimi)+3])
elif Son5d1[0:len(DeplasmanTakimi)]!=DeplasmanTakimi :
	DeplasmanAvarajArti = DeplasmanAvarajArti + int(Son5d1[-((len(DeplasmanTakimi))+15)])
	DeplasmanAvarajEksi = DeplasmanAvarajEksi + int(Son5d1[-((len(DeplasmanTakimi))+17)])

if Son5d1[0:len(DeplasmanTakimi)]==DeplasmanTakimi : #Ev sahibi ilk sırada mı değil mi algılar.
	c1 = int(Son5d1[len(DeplasmanTakimi)+1]) #İlk sırada ise + avaraja değer toplanır.
	d1 = int(Son5d1[len(DeplasmanTakimi)+3])
elif Son5d1[0:len(DeplasmanTakimi)]!=DeplasmanTakimi :
	c1 = int(Son5d1[-((len(DeplasmanTakimi))+15)])
	d1 = int(Son5d1[-((len(DeplasmanTakimi))+17)])

if c1>d1:
	A10=1
elif c1==d1:
	A10=0
elif c1<d1:
	A10=-1

Son5d2 = driver.find_element_by_xpath("""//*[@id="match-details"]/div/div[1]/div/div[2]/div[3]/div[3]/div[3]""").get_attribute("title")

if Son5d2[0:len(DeplasmanTakimi)]==DeplasmanTakimi : #Ev sahibi ilk sırada mı değil mi algılar.
	DeplasmanAvarajArti = DeplasmanAvarajArti + int(Son5d2[len(DeplasmanTakimi)+1]) #İlk sırada ise + avaraja değer toplanır.
	DeplasmanAvarajEksi = DeplasmanAvarajEksi + int(Son5d2[len(DeplasmanTakimi)+3])
elif Son5d2[0:len(DeplasmanTakimi)]!=DeplasmanTakimi :
	DeplasmanAvarajArti = DeplasmanAvarajArti + int(Son5d2[-((len(DeplasmanTakimi))+15)])
	DeplasmanAvarajEksi = DeplasmanAvarajEksi + int(Son5d2[-((len(DeplasmanTakimi))+17)])

if Son5d2[0:len(DeplasmanTakimi)]==DeplasmanTakimi : #Ev sahibi ilk sırada mı değil mi algılar.
	c2 = int(Son5d2[len(DeplasmanTakimi)+1]) #İlk sırada ise + avaraja değer toplanır.
	d2 = int(Son5d2[len(DeplasmanTakimi)+3])
elif Son5d2[0:len(DeplasmanTakimi)]!=DeplasmanTakimi :
	c2 = int(Son5d2[-((len(DeplasmanTakimi))+15)])
	d2 = int(Son5d2[-((len(DeplasmanTakimi))+17)])

if c2>d2:
	A11=1
elif c2==d2:
	A11=0
elif c2<d2:
	A11=-1

Son5d3 = driver.find_element_by_xpath("""//*[@id="match-details"]/div/div[1]/div/div[2]/div[3]/div[3]/div[4]""").get_attribute("title")

if Son5d3[0:len(DeplasmanTakimi)]==DeplasmanTakimi : #Ev sahibi ilk sırada mı değil mi algılar.
	DeplasmanAvarajArti = DeplasmanAvarajArti + int(Son5d3[len(DeplasmanTakimi)+1]) #İlk sırada ise + avaraja değer toplanır.
	DeplasmanAvarajEksi = DeplasmanAvarajEksi + int(Son5d3[len(DeplasmanTakimi)+3])
elif Son5d3[0:len(DeplasmanTakimi)]!=DeplasmanTakimi :
	DeplasmanAvarajArti = DeplasmanAvarajArti + int(Son5d3[-((len(DeplasmanTakimi))+15)])
	DeplasmanAvarajEksi = DeplasmanAvarajEksi + int(Son5d3[-((len(DeplasmanTakimi))+17)])

if Son5d3[0:len(DeplasmanTakimi)]==DeplasmanTakimi : #Ev sahibi ilk sırada mı değil mi algılar.
	c3 = int(Son5d3[len(DeplasmanTakimi)+1]) #İlk sırada ise + avaraja değer toplanır.
	d3 = int(Son5d3[len(DeplasmanTakimi)+3])
elif Son5d3[0:len(DeplasmanTakimi)]!=DeplasmanTakimi :
	c3 = int(Son5d3[-((len(DeplasmanTakimi))+15)])
	d3 = int(Son5d3[-((len(DeplasmanTakimi))+17)])

if c3>d3:
	A12=1
elif c3==d3:
	A12=0
elif c3<d3:
	A12=-1

Son5d4 = driver.find_element_by_xpath("""//*[@id="match-details"]/div/div[1]/div/div[2]/div[3]/div[3]/div[5]""").get_attribute("title")

if Son5d4[0:len(DeplasmanTakimi)]==DeplasmanTakimi : #Ev sahibi ilk sırada mı değil mi algılar.
	DeplasmanAvarajArti = DeplasmanAvarajArti + int(Son5d4[len(DeplasmanTakimi)+1]) #İlk sırada ise + avaraja değer toplanır.
	DeplasmanAvarajEksi = DeplasmanAvarajEksi + int(Son5d4[len(DeplasmanTakimi)+3])
elif Son5d4[0:len(DeplasmanTakimi)]!=DeplasmanTakimi :
	DeplasmanAvarajArti = DeplasmanAvarajArti + int(Son5d4[-((len(DeplasmanTakimi))+15)])
	DeplasmanAvarajEksi = DeplasmanAvarajEksi + int(Son5d4[-((len(DeplasmanTakimi))+17)])

if Son5d4[0:len(DeplasmanTakimi)]==DeplasmanTakimi : #Ev sahibi ilk sırada mı değil mi algılar.
	c4 = int(Son5d4[len(DeplasmanTakimi)+1]) #İlk sırada ise + avaraja değer toplanır.
	d4 = int(Son5d4[len(DeplasmanTakimi)+3])
elif Son5d4[0:len(DeplasmanTakimi)]!=DeplasmanTakimi :
	c4 = int(Son5d4[-((len(DeplasmanTakimi))+15)])
	d4 = int(Son5d4[-((len(DeplasmanTakimi))+17)])

if c4>d4:
	A13=1
elif c4==d4:
	A13=0
elif c4<d4:
	A13=-1

Son5d5 = driver.find_element_by_xpath("""//*[@id="match-details"]/div/div[1]/div/div[2]/div[3]/div[3]/div[6]""").get_attribute("title")

if Son5d5[0:len(DeplasmanTakimi)]==DeplasmanTakimi : #Ev sahibi ilk sırada mı değil mi algılar.
	DeplasmanAvarajArti = DeplasmanAvarajArti + int(Son5d5[len(DeplasmanTakimi)+1]) #İlk sırada ise + avaraja değer toplanır.
	DeplasmanAvarajEksi = DeplasmanAvarajEksi + int(Son5d5[len(DeplasmanTakimi)+3])
elif Son5d5[0:len(DeplasmanTakimi)]!=DeplasmanTakimi :
	DeplasmanAvarajArti = DeplasmanAvarajArti + int(Son5d5[-((len(DeplasmanTakimi))+15)])
	DeplasmanAvarajEksi = DeplasmanAvarajEksi + int(Son5d5[-((len(DeplasmanTakimi))+17)])

if Son5d5[0:len(DeplasmanTakimi)]==DeplasmanTakimi : #Ev sahibi ilk sırada mı değil mi algılar.
	c5 = int(Son5d5[len(DeplasmanTakimi)+1]) #İlk sırada ise + avaraja değer toplanır.
	d5 = int(Son5d5[len(DeplasmanTakimi)+3])
elif Son5d5[0:len(DeplasmanTakimi)]!=DeplasmanTakimi :
	c5 = int(Son5d5[-((len(DeplasmanTakimi))+15)])
	d5 = int(Son5d5[-((len(DeplasmanTakimi))+17)])

if c5>d5:
	A14=1
elif c5==d5:
	A14=0
elif c5<d5:
	A14=-1

A15 = int(DeplasmanAvarajArti)
A16 = -(int(DeplasmanAvarajEksi))

Tarih = (driver.find_element_by_xpath("""//*[@id="match-details"]/div/div[1]/div/div[1]/div[3]""")).text
	#print(Tarih)
#A23 = float(Tarih[19:])
tahminlistesi = []
tahminlistesi.append(EvSahibiTakim)
tahminlistesi.append(DeplasmanTakimi)
print(len(tahminlistesi))
import time
bugun = time.asctime()
tahminlistesi.append(bugun)
print(bugun)
KayitAdedi = len(pandas.read_csv("Database.csv"))
print(KayitAdedi)
tahminlistesi.append(KayitAdedi)
TB =0 #Tahmini Birden Bire
TS =0 #Tahmini Birden Sıfıra
TI =0 #Tahmini Birden ikiye

for i in range(0, 1000):
	clf = tree.DecisionTreeClassifier()
	df = pandas.read_csv('Database.csv', sep=',', header=0, usecols=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17])
	df2 = pandas.read_csv('Database2.csv', sep=',', header=0, usecols=[18])
	X = df.values #Maçlar
	Y = df2.values #Sonuçlar
	clf = clf.fit(X, Y)
	prediction = clf.predict([[A0,A1,A2,A3,A4,A5,A6,A7,1,A9,A10,A11,A12,A13,A14,A15,A16,-1]])
	# print(EvSahibiTakim, " - ", DeplasmanTakimi, " karşılaşması için ", i+1, ". tahminim=", end="", sep="")
	# print(prediction)
	#Yüzde Hesaplama
	if prediction=="s":
		TS+=1
		pass
	if prediction=="b":
		TB+=1
		pass
	if prediction=="i":
		TI+=1
		pass
	
	# tahminlistesi.append(prediction)
	mactahmini = [EvSahibiTakim, " - ", DeplasmanTakimi,prediction]
if TS!=0:
		print("Maçın berabere bitme ihtimali %"+str(TS)+".")
		tahminlistesi.append("Maçın berabere bitme ihtimali %"+str(TS/10)+".")
		pass
if TB!=0:
		print("Maçı ev sahibinin kazanma ihtimali %"+str(TB)+".")
		tahminlistesi.append("Maçı ev sahibinin kazanma ihtimali %"+str(TB/10)+".")
		pass
if TI!=0:
		print("Maçı ev sahibinin kazanma ihtimali %"+str(TI)+".")
		tahminlistesi.append("Maçı ev sahibinin kazanma ihtimali %"+str(TI/10)+".")
		pass

with open('Results.csv', 'a', newline='', encoding='utf-8') as f:
	w = csv.writer(f, delimiter=',')
	w.writerow(tahminlistesi)

driver.close()