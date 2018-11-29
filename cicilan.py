class bankXYZ():
	"""docstring for bankXYZ"""
	def bunga(self,pinjaman):
		self.pinjaman = pinjaman
		if (pinjaman<1000000000):
			bunga=0.15
		elif (1000000000<=pinjaman<=10000000000):
			bunga=0.148
		elif (10000000001<=pinjaman<=100000000000):
			bunga=0.147
		else:
			bunga=0.145
		return bunga
	def totalBunga(self,pinjaman,bunga):
		self.bunga = bunga
		self.pinjaman = pinjaman
		totalBunga = pinjaman * bunga
		return totalBunga
	def cicilan(self,pinjaman,tBunga,lCicil):
		self.tBunga = tBunga
		self.pinjaman = pinjaman
		self.lCicil = lCicil
		cicilan = (pinjaman+tBunga)/lCicil
		return cicilan
class bankABC(bankXYZ):
	"""docstring for bankXYZ"""
	def bunga(self,pinjaman):
		self.pinjaman = pinjaman
		if (pinjaman<1000000000):
			bunga=0.15
		elif (1000000000<=pinjaman<=10000000000):
			bunga=0.148		
		else:
			bunga=0.145
		return bunga	
	def cicilan(self,pinjaman,tBunga, lCicil):
		self.tBunga = tBunga
		self.pinjaman = pinjaman
		self.lCicil = lCicil		
		provisi = input('Masukkan provisi: ')
		cicilan = (pinjaman+tBunga)/lCicil+provisi
		return cicilan
masuk = True
while masuk:	
	milih = input('Masuk program? (1) YA (2) TIDAK: ')
	if milih == 1:
		pinjaman = input('Masukkan pinjaman: ')
		if pinjaman>0:
			pilih = input('Masukkan (1) Bank XYZ atau (2) Bank ABC: ')
			lCicil = input('Masukkan lama cicilan: ')
			if pilih == 1:
				bankXYZ = bankXYZ()
				a = bankXYZ.bunga(pinjaman)
				b = bankXYZ.totalBunga(pinjaman,a)
				c = bankXYZ.cicilan(pinjaman,b,lCicil)
				print 'Jumlah cicilan: ',c,'rupiah per',lCicil,'bulan'
			elif pilih == 2:
				bankABC = bankABC()
				a = bankABC.bunga(pinjaman)
				b = bankABC.totalBunga(pinjaman,a)
				c = bankABC.cicilan(pinjaman,b,lCicil)
				print 'Jumlah cicilan: ',c,'rupiah per',lCicil,'bulan'
			else:
				print 'SALAH INPUT'
		else:
			print 'SALAH INPUT'
	else:
		masuk = False	