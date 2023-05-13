'''
POLYMORPHISM BERTUJUAN UNTUK MEMBUAT FUNGSI UMUM
'''

class Cat:

    def __init__(self):
        self.nama = 'Meong'
        self.tipe ='Kucing'
    
    def forward(self):
        print('Kucing berlari...')

class Bird:

    def __init__(self):
        self.nama = 'Jack Sparrow'
        self.tipe = 'Burung'
    
    def forward(self):
        print('Burung terbang...')

#fungsi umum
def melaju(objek):
    objek.forward()

meong = Cat()
sparrow = Bird()

melaju(meong)
melaju(sparrow)

