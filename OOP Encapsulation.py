'''
ENCAPSULATION : BERFUNGSI UNTUK MEMBATASI AKSES/MODIFIKASI ATRIBUT PADA CLASS
CARA MODIFIKASINYA YAITU DENGAN MEMBUAT SETTER DAN GETTER

'''

class Mobil:
    def __init__(self, plat):

        self.__plat = plat
        self.__tipe = 'Avanza'
        self.__bensin= 40 # liter            

    # getter
    def lihatMaksimumBensin(self):
        print('Maksimum bensin yaitu: ' ,{self.__bensin}, 'liter')

    # setter
    def aturMaksimumBensin(self, bensin): 
        self.__bensin = bensin

avanza = Mobil(plat='B 7185 XC')
avanza.lihatMaksimumBensin()

avanza.__bensin = 100
avanza.lihatMaksimumBensin()

avanza.aturMaksimumBensin(100) # setter
avanza.lihatMaksimumBensin() # getter