'''
INHERITANCE YAITU MEMBUAT PARENT CLASS DAN CHILD CLASS 
INHERITANCE BERTUJUAN UNTUK MEWARISKAN SELURUH FUNGSIONALITAS DARI PARENT CLASS KE KELAS BARU YAITU CHILD CLASS
AGAR FUNGSIONALITAS YANG SUDAH ADA DAPAT DIKEMBANGKAN ATAU DIKENAL DENGAN ISTILAH OVERIDING  
'''
#Parent Class
class Animal:

    def __init__(self):
        self.jenis = 'Mamalia'
        self.kecepatan = 'Lambat'
    
    def grow(self):
        print('Mamalia ini bertumbuh')
    
    def walk(self):
        print('Kucing', self.jenis, 'sedang berjalan')

#Child Class
class Cat(Animal):

    def __init__(self, nama, jenis):
        
        super().__init__()

        self.nama = nama
        self.jenis = jenis
    
    def run(self):
        print('Kucing', self.jenis, 'berlari...')

yamaha = Cat(nama='Yamaha', jenis='Anggora')
honda = Cat(nama='honda', jenis='Persia')

print(yamaha.kecepatan)
print(yamaha.jenis)
yamaha.run()
yamaha.walk()