class Mobil:
    def __init__(self, nama, tipe, warna):
        self.nama = nama
        self.tipe = tipe
        self.warna = warna

    def kecepatan(self, speed):
        print('Mobil', self.nama, 'memiliki kecepatan', speed)
    
    def kursi(self, seat):
        print('Jenis mobil',self.tipe, 'rata-rata memiliki kursi sebanyak',seat, 'dan berwarna', self.warna)

lamborgini = Mobil(nama='Lamborgini', tipe='Sport', warna='Merah')
avanza = Mobil(nama='Avanza', tipe='Reguler', warna='Putih')

lamborgini.kecepatan('50km/h')
lamborgini.kursi(2)
avanza.kecepatan('11km/h')
avanza.kursi(4)

