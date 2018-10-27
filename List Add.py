# Maçkolik Bilgi v0.2
# Written by Mahir Yıldızhan
# www.mahiryildizhan.com
from selenium import webdriver
import csv
import numpy as np
print("Please enter Mackolik link=")

file2="Links.csv"
row2 = np.genfromtxt(file2, usecols=[0], delimiter=',', dtype=str)
for j in range(0, len(row2)):
	url=row2[j]

	filename ="Database.csv"
	row = np.genfromtxt(filename, usecols=[23], delimiter=',', dtype=str)
	ArsivBilgisi=False
	for i in range(0, len(row)):
		if(row[i]==url):
			ArsivBilgisi=True

	if ArsivBilgisi==False:
		chrome_path = r"C:\Python36\chromedriver.exe"
		driver = webdriver.Chrome(chrome_path)
		#driver.set_window_position(-2000, 0)#Minimize the screen.
		driver.get(url)
		A22 = url
		#Ev Sahibi Takım
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

		A20 = EvSahibiTakim

		#-------------------------------------------------------#
		#Deplasman Takımı
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


		A21 = DeplasmanTakimi

		#-------------------------------------------------------#
		#Ev Sahibi Takım Değeri
		EvSahibiTakimD1 = (driver.find_element_by_xpath("""//*[@id="dvHomeSquad"]/table/tbody/tr[12]/td""")).text
		#print(EvSahibiTakimD1)
		EvSahibiTakimD2= EvSahibiTakimD1[16:]
		#print(EvSahibiTakimD2)
		#print(len(EvSahibiTakimD2))
		if len(EvSahibiTakimD2)==14:
			EvSahibiTakimD3=EvSahibiTakimD2[0:2]+EvSahibiTakimD2[3:6]
		elif len(EvSahibiTakimD2)==15:
			EvSahibiTakimD3=EvSahibiTakimD2[0:3]+EvSahibiTakimD2[4:7]
		elif len(EvSahibiTakimD2)==13:
			EvSahibiTakimD3=EvSahibiTakimD2[0:1]+EvSahibiTakimD2[2:5]

		A0=int(EvSahibiTakimD3)/100000

		#-------------------------------------------------------#
		#Ev Sahibi Takım Son 5 Maçı
		EvSahibiAvarajArti = 0
		EvSahibiAvarajEksi = 0 

		Son5e1 = driver.find_element_by_xpath("""//*[@id="match-details"]/div/div[1]/div/div[2]/div[1]/div[3]/div[2]""").get_attribute("title")
		#print(Son5e1)
		#print(len(Son5e1))
		if Son5e1[0:len(EvSahibiTakim)]==EvSahibiTakim : #Ev sahibi ilk sırada mı değil mi algılar.
			EvSahibiAvarajArti = EvSahibiAvarajArti + int(Son5e1[len(EvSahibiTakim)+1]) #İlk sırada ise + avaraja değer toplanır.
			EvSahibiAvarajEksi = EvSahibiAvarajEksi + int(Son5e1[len(EvSahibiTakim)+3])
		elif Son5e1[0:len(EvSahibiTakim)]!=EvSahibiTakim :
			EvSahibiAvarajArti = EvSahibiAvarajArti + int(Son5e1[-((len(EvSahibiTakim))+15)])
			EvSahibiAvarajEksi = EvSahibiAvarajEksi + int(Son5e1[-((len(EvSahibiTakim))+17)])
		#print(EvSahibiAvarajArti)
		#print(EvSahibiAvarajEksi)
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
		#print(Son5e2)
		if Son5e2[0:len(EvSahibiTakim)]==EvSahibiTakim : #Ev sahibi ilk sırada mı değil mi algılar.
			EvSahibiAvarajArti = EvSahibiAvarajArti + int(Son5e2[len(EvSahibiTakim)+1]) #İlk sırada ise + avaraja değer toplanır.
			EvSahibiAvarajEksi = EvSahibiAvarajEksi + int(Son5e2[len(EvSahibiTakim)+3])
		elif Son5e2[0:len(EvSahibiTakim)]!=EvSahibiTakim :
			EvSahibiAvarajArti = EvSahibiAvarajArti + int(Son5e2[-((len(EvSahibiTakim))+15)])
			EvSahibiAvarajEksi = EvSahibiAvarajEksi + int(Son5e2[-((len(EvSahibiTakim))+17)])
		#print(EvSahibiAvarajArti)
		#print(EvSahibiAvarajEksi)
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
		#print(Son5e3)
		if Son5e3[0:len(EvSahibiTakim)]==EvSahibiTakim : #Ev sahibi ilk sırada mı değil mi algılar.
			EvSahibiAvarajArti = EvSahibiAvarajArti + int(Son5e3[len(EvSahibiTakim)+1]) #İlk sırada ise + avaraja değer toplanır.
			EvSahibiAvarajEksi = EvSahibiAvarajEksi + int(Son5e3[len(EvSahibiTakim)+3])
		elif Son5e3[0:len(EvSahibiTakim)]!=EvSahibiTakim :
			EvSahibiAvarajArti = EvSahibiAvarajArti + int(Son5e3[-((len(EvSahibiTakim))+15)])
			EvSahibiAvarajEksi = EvSahibiAvarajEksi + int(Son5e3[-((len(EvSahibiTakim))+17)])
		#print(EvSahibiAvarajArti)
		#print(EvSahibiAvarajEksi)
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
		#print(Son5e4)
		if Son5e4[0:len(EvSahibiTakim)]==EvSahibiTakim : #Ev sahibi ilk sırada mı değil mi algılar.
			EvSahibiAvarajArti = EvSahibiAvarajArti + int(Son5e4[len(EvSahibiTakim)+1]) #İlk sırada ise + avaraja değer toplanır.
			EvSahibiAvarajEksi = EvSahibiAvarajEksi + int(Son5e4[len(EvSahibiTakim)+3])
		elif Son5e4[0:len(EvSahibiTakim)]!=EvSahibiTakim :
			EvSahibiAvarajArti = EvSahibiAvarajArti + int(Son5e4[-((len(EvSahibiTakim))+15)])
			EvSahibiAvarajEksi = EvSahibiAvarajEksi + int(Son5e4[-((len(EvSahibiTakim))+17)])
		#print(EvSahibiAvarajArti)
		#print(EvSahibiAvarajEksi)
		if Son5e4[0:len(EvSahibiTakim)]==EvSahibiTakim : #Ev sahibi ilk sırada mı değil mi algılar.
			a4 = int(Son5e4[len(EvSahibiTakim)+1]) #İlk sırada ise + avaraja değer toplanır.
			b4 = int(Son5e4[len(EvSahibiTakim)+3])
		elif Son5e4[0:len(EvSahibiTakim)]!=EvSahibiTakim :
			a4 = int(Son5e4[-((len(EvSahibiTakim))+15)])
			b4 = int(Son5e4[-((len(EvSahibiTakim))+17)])
		#print(a4, b4)
		if a4>b4:
			A4=1
		elif a4==b4:
			A4=0
		elif a4<b4:
			A4=-1

		Son5e5 = driver.find_element_by_xpath("""//*[@id="match-details"]/div/div[1]/div/div[2]/div[1]/div[3]/div[6]""").get_attribute("title")
		#print(Son5e5)
		if Son5e5[0:len(EvSahibiTakim)]==EvSahibiTakim : #Ev sahibi ilk sırada mı değil mi algılar.
			EvSahibiAvarajArti = EvSahibiAvarajArti + int(Son5e5[len(EvSahibiTakim)+1]) #İlk sırada ise + avaraja değer toplanır.
			EvSahibiAvarajEksi = EvSahibiAvarajEksi + int(Son5e5[len(EvSahibiTakim)+3])
		elif Son5e5[0:len(EvSahibiTakim)]!=EvSahibiTakim :
			EvSahibiAvarajArti = EvSahibiAvarajArti + int(Son5e5[-((len(EvSahibiTakim))+15)])
			EvSahibiAvarajEksi = EvSahibiAvarajEksi + int(Son5e5[-((len(EvSahibiTakim))+17)])
		#print(EvSahibiAvarajArti)
		#print(EvSahibiAvarajEksi)
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
		#-------------------------------------------------------#
		#Deplasman Takım Değeri
		DeplasmanTakimD1= (driver.find_element_by_xpath("""//*[@id="dvAwaySquad"]/table/tbody/tr[12]/td""")).text
		#print(DeplasmanTakimD1)
		DeplasmanTakimD2 = DeplasmanTakimD1[16:]
		#print(DeplasmanTakimD2)
		if len(DeplasmanTakimD2)==14:
			DeplasmanTakimD3=DeplasmanTakimD2[0:2]+DeplasmanTakimD2[3:6]
		elif len(EvSahibiTakimD2)==15:
			DeplasmanTakimD3=DeplasmanTakimD2[0:3]+DeplasmanTakimD2[4:7]
		elif len(DeplasmanTakimD2)==13:
			DeplasmanTakimD3=DeplasmanTakimD2[0:1]+DeplasmanTakimD2[2:5]
		#print(DeplasmanTakimD3)

		A9=int(DeplasmanTakimD3)/100000

		#-------------------------------------------------------#
		#Deplasman Takım Son 5 Maçı
		DeplasmanAvarajArti = 0
		DeplasmanAvarajEksi = 0

		Son5d1 = driver.find_element_by_xpath("""//*[@id="match-details"]/div/div[1]/div/div[2]/div[3]/div[3]/div[2]""").get_attribute("title")
		#print(Son5d1)
		if Son5d1[0:len(DeplasmanTakimi)]==DeplasmanTakimi : #Ev sahibi ilk sırada mı değil mi algılar.
			DeplasmanAvarajArti = DeplasmanAvarajArti + int(Son5d1[len(DeplasmanTakimi)+1]) #İlk sırada ise + avaraja değer toplanır.
			DeplasmanAvarajEksi = DeplasmanAvarajEksi + int(Son5d1[len(DeplasmanTakimi)+3])
		elif Son5d1[0:len(DeplasmanTakimi)]!=DeplasmanTakimi :
			DeplasmanAvarajArti = DeplasmanAvarajArti + int(Son5d1[-((len(DeplasmanTakimi))+15)])
			DeplasmanAvarajEksi = DeplasmanAvarajEksi + int(Son5d1[-((len(DeplasmanTakimi))+17)])
		#print(DeplasmanAvarajArti)
		#print(DeplasmanAvarajEksi)
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
		#print(Son5d2)
		if Son5d2[0:len(DeplasmanTakimi)]==DeplasmanTakimi : #Ev sahibi ilk sırada mı değil mi algılar.
			DeplasmanAvarajArti = DeplasmanAvarajArti + int(Son5d2[len(DeplasmanTakimi)+1]) #İlk sırada ise + avaraja değer toplanır.
			DeplasmanAvarajEksi = DeplasmanAvarajEksi + int(Son5d2[len(DeplasmanTakimi)+3])
		elif Son5d2[0:len(DeplasmanTakimi)]!=DeplasmanTakimi :
			DeplasmanAvarajArti = DeplasmanAvarajArti + int(Son5d2[-((len(DeplasmanTakimi))+15)])
			DeplasmanAvarajEksi = DeplasmanAvarajEksi + int(Son5d2[-((len(DeplasmanTakimi))+17)])
		#print(DeplasmanAvarajArti)
		#print(DeplasmanAvarajEksi)
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
		#print(Son5d3)
		if Son5d3[0:len(DeplasmanTakimi)]==DeplasmanTakimi : #Ev sahibi ilk sırada mı değil mi algılar.
			DeplasmanAvarajArti = DeplasmanAvarajArti + int(Son5d3[len(DeplasmanTakimi)+1]) #İlk sırada ise + avaraja değer toplanır.
			DeplasmanAvarajEksi = DeplasmanAvarajEksi + int(Son5d3[len(DeplasmanTakimi)+3])
		elif Son5d3[0:len(DeplasmanTakimi)]!=DeplasmanTakimi :
			DeplasmanAvarajArti = DeplasmanAvarajArti + int(Son5d3[-((len(DeplasmanTakimi))+15)])
			DeplasmanAvarajEksi = DeplasmanAvarajEksi + int(Son5d3[-((len(DeplasmanTakimi))+17)])
		#print(DeplasmanAvarajArti)
		#print(DeplasmanAvarajEksi)
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
		#print(Son5d4)
		if Son5d4[0:len(DeplasmanTakimi)]==DeplasmanTakimi : #Ev sahibi ilk sırada mı değil mi algılar.
			DeplasmanAvarajArti = DeplasmanAvarajArti + int(Son5d4[len(DeplasmanTakimi)+1]) #İlk sırada ise + avaraja değer toplanır.
			DeplasmanAvarajEksi = DeplasmanAvarajEksi + int(Son5d4[len(DeplasmanTakimi)+3])
		elif Son5d4[0:len(DeplasmanTakimi)]!=DeplasmanTakimi :
			DeplasmanAvarajArti = DeplasmanAvarajArti + int(Son5d4[-((len(DeplasmanTakimi))+15)])
			DeplasmanAvarajEksi = DeplasmanAvarajEksi + int(Son5d4[-((len(DeplasmanTakimi))+17)])
		#print(DeplasmanAvarajArti)
		#print(DeplasmanAvarajEksi)
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
		#print(Son5d5)
		if Son5d5[0:len(DeplasmanTakimi)]==DeplasmanTakimi : #Ev sahibi ilk sırada mı değil mi algılar.
			DeplasmanAvarajArti = DeplasmanAvarajArti + int(Son5d5[len(DeplasmanTakimi)+1]) #İlk sırada ise + avaraja değer toplanır.
			DeplasmanAvarajEksi = DeplasmanAvarajEksi + int(Son5d5[len(DeplasmanTakimi)+3])
		elif Son5d5[0:len(DeplasmanTakimi)]!=DeplasmanTakimi :
			DeplasmanAvarajArti = DeplasmanAvarajArti + int(Son5d5[-((len(DeplasmanTakimi))+15)])
			DeplasmanAvarajEksi = DeplasmanAvarajEksi + int(Son5d5[-((len(DeplasmanTakimi))+17)])
		#print(DeplasmanAvarajArti)
		#print(DeplasmanAvarajEksi)
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

		#-------------------------------------------------------#
		#İlk Yarı Sonucu
		ilkYariSonucu = (driver.find_element_by_xpath("""//*[@id="dvHTScoreText"]""")).text
		#print(ilkYariSonucu)
		#print(len(ilkYariSonucu))#
		ilkYariSonucu2=ilkYariSonucu[5:]
		#print(ilkYariSonucu2)
		ilkYariEvSahibiSkoru=ilkYariSonucu2[0] #NOT!:Eğer maç skoru çift haneli rakamlara geldiyse program patlar.
		ilkYariDeplasmanSkoru=ilkYariSonucu2[4] #NOT!:Eğer maç skoru çift haneli rakamlara geldiyse program patlar.
		if ilkYariEvSahibiSkoru>ilkYariDeplasmanSkoru:
			IY=1
		elif ilkYariEvSahibiSkoru==ilkYariDeplasmanSkoru:
			IY=0
		elif ilkYariEvSahibiSkoru<ilkYariDeplasmanSkoru:
			IY=2
		#print(IY)

		#-------------------------------------------------------#
		#Maç Sonucu
		MacSonucu = (driver.find_element_by_xpath("""//*[@id="dvScoreText"]""")).text
		#print(MacSonucu)
		#print(len(MacSonucu)) #Skor sayılarının doğruluğunu teyit et.
		MacSonuEvSahibiSkoru=MacSonucu[0] #NOT!:Eğer maç skoru çift haneli rakamlara geldiyse program patlar.
		MacSonuDeplasmanSkoru=MacSonucu[4] #NOT!:Eğer maç skoru çift haneli rakamlara geldiyse program patlar.
		if MacSonuEvSahibiSkoru>MacSonuDeplasmanSkoru:
			MS=1
		elif MacSonuEvSahibiSkoru==MacSonuDeplasmanSkoru:
			MS=0
		elif MacSonuEvSahibiSkoru<MacSonuDeplasmanSkoru:
			MS=2
		#print(MS)
		A18_1=str(IY)+str(MS)

		if A18_1=='00':
			A18='ss'
		if A18_1=='01':
			A18='sb'
		if A18_1=='02':
			A18='si'
		if A18_1=='10':
			A18='bs'
		if A18_1=='11':
			A18='bb'
		if A18_1=='12':
			A18='bi'
		if A18_1=='20':
			A18='is'
		if A18_1=='21':
			A18='ib'
		if A18_1=='22':
			A18='ii'



		#-------------------------------------------------------#
		#Maç Tarihi
		Tarih = (driver.find_element_by_xpath("""//*[@id="match-details"]/div/div[1]/div/div[1]/div[3]""")).text
		#print(Tarih)
		Saat = Tarih
		Tarih=Tarih[8:]
		Tarih=Tarih[:10]
		A19=Tarih
		A23= Saat[19:]

		#-------------------------------------------------------#
		A8=1
		A17=-1

		#Sonuçların Yazdırılması
		basliklar=[A0,A1,A2,A3,A4,A5,A6,A7,A8,A9,A10,A11,
				   A12,A13,A14,A15,A16,A17,A18,A19,A20,A21,A22,A23]


		with open('Database.csv', 'a', newline='', encoding='utf-8') as f:
			w = csv.writer(f, delimiter=',')
			w.writerow(basliklar)
			#w.writerow(basliklar2)

		driver.close()
		print(EvSahibiTakim, "vs", DeplasmanTakimi, "Done.")
	else:
		print("This match is in our database.")
		print("Done without adding match.")