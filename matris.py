#_*_ charset:utf-8 _*_
import os
print("""
		Matris işlemleri
			1 - Matrislerde 4 İşlem
			2 - Matris Determinant/Transpoz İşlemleri
	""")
secim = int(input("İşlem Seçiniz : "))
if secim == 1:
	os.system("clear")
	satir1 = int(input("1. Matris Satır Sayısı : "))
	sutun1 = int(input("1. Matris Sütun Sayısı : "))
	matris1 = [["0"]*sutun1 for i in range(satir1)]
	a = 0
	for i in range(satir1):
		a +=1
		c = 0
		for j in range(sutun1):
			c +=1
			eleman = input("Matrisin {}. Satır {}. Sütun Elemanını Giriniz : ".format(a,c))
			matris1[i][j] = eleman
	os.system("clear")
	print("1. Matrisin Son Hali \n")
	for jkl1 in range(satir1):
		print(matris1[jkl1])
	print("=====================================================================================")
	satir2 = int(input("2. Matrisin Satır Sayısı : "))
	sutun2 = int(input("2. Matrisin Sütun Sayısı : "))
	matris2 = [["0"]*sutun2 for i in range(satir2)]
	d = 0
	for k in range(satir2):
		d +=1
		f = 0
		for l in range(sutun2):
			f +=1
			eleman2 = input("Matrisin {}. Satır {}. Sütun Elemanını Giriniz : ".format(d,f))
			matris2[k][l] = eleman2
	
	for jkl2 in range(satir2):
		print(matris2[jkl2])
		
	print("""
			Bu İki Matrisle Yapmak İstediğiniz İşlemi Seçiniz : 
				1 - Toplama
				2 - Çıkarma
				3 - Çarpma	
				4 - Bölme (AKTİF DEĞİL)
		""")

	secim2 = int(input("Yapmak İstediğiniz İşlemi Giriniz : "))
	
	toplamsonucmatris = [["0"]*sutun1 for i in range(satir1)]	
	if secim2 == 1 : 
		if satir1 != satir2 or sutun1 != sutun2:
			print("Matrislerin Satır/Sütun Sayıları Eşit Değil Toplama İşlemi Yapılamaz...")
		else:
			a = 0
			i = 0
			j = 0
			for i in range(satir1):
				for j in range(sutun1):
					toplamsonucmatris[i][j] = int(matris1[i][j]) + int(matris2[i][j])
			print("\n Toplama İşleminin Sonucu : ")
			for jkl3 in range(satir2):
				print(toplamsonucmatris[jkl3])
	
	cikarmasonucmatris =[["0"]*sutun2 for i in range(satir2)]
	if secim2 == 2:
		if satir1 != satir2 or sutun1 != sutun2:
			print("Matrislerin Satır/Sütun Sayıları Eşit Değil Çıkarma İşlemi Yapılamaz...")
		else:
			a = 0
			i = 0
			j = 0
			for i in range(satir1):
				for j in range(sutun1):
					toplamsonucmatris[i][j] = int(matris1[i][j]) - int(matris2[i][j])
			print("\n Çıkarma İşleminin Sonucu : ")
			for jkl3 in range(satir2):
				print(cikarmasonucmatris[jkl3])
	if secim2 == 3:
		if sutun1 != satir2:
			print("1. Matrisin Sütun Sayısı İle 2. Matrisin Satır Sayısı Eşit Değil Çarpma İşlemi Yapılamaz...")
		else:
			carpimsonucmatris = [["0"]*sutun2 for i in range(satir1)]
			print("ilk matris : ",carpimsonucmatris)
			for i in range(satir1):
				print("i : ",i)
				for j in range(sutun2):
					print("j : ",j)
					for k in range(satir1):
						print("k : ",k)
						carpimsonucmatris[i][j] = int(carpimsonucmatris[i][j])
						carpimsonucmatris[i][j] += int(matris1[i][k]) * int(matris2[k][j])
			print("\nCarpım Sonuc : ",carpimsonucmatris)
if secim == 2:
	os.system("clear")
	satir3 = int(input("Matrisin Satır Sayısı : "))
	sutun3 = int(input	("Matrisin Sütun Sayısı : "))
	matris3 = [[0]*sutun3 for i in range(satir3)]
	i = 0
	j = 0
	d = 0 
	for k in range(satir3):
		d +=1
		f = 0
		for l in range(sutun3):
			f +=1
			eleman3 = input("Matrisin {}. Satır {}. Sütun Elemanını Giriniz : ".format(d,f))
			matris3[k][l] = eleman3
	for jkl4 in range(satir3):
				print(matris3[jkl4])
	print("""
			Matris İşlemleri

				1- Transpoz İşlemi
				2- Determinant İşlemi

		""")
	secim3 = int(input("Yapmak İstediğiniz İşlemi Giriniz : "))
	if secim3 == 1:
		transpoz = [[0]*sutun3 for i in range(satir3)]
		i = 0
		j = 0
		for i in range(satir3):
			for j in range(sutun3):
				a = 0
				a = matris3[i][j]
				transpoz[j][i] = a
		print("\nMatrisin Transpozu : \n")
		for jkl5 in range(satir3):
			print(transpoz[jkl5])
	if secim3 == 2 :
		pass