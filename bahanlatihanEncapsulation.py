class Mobil:
    def __init__(self, plat):
        
        self.__plat = plat
        self.__tipe = 'Avanza'
        self.__bensin = 40 #liter
    
    #getter
    def lihat_tipemobil(self):
        print('Tipe mobil merupakan : ', self.__tipe)

    #setter
    def atur_tipemobil(self, tipe):
        self.__tipe = tipe

avanza = Mobil(plat='abcd')

avanza.lihat_tipemobil()
avanza.atur_tipemobil('Mercedez')
avanza.lihat_tipemobil()

avanza.lihat_tipemobil()
