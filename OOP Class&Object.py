#ini adalah class
class Cat:
    '''
    contoh kelas dan object
    '''
    spesies = 'Kucing'

    #ini adalah attribute
    def __init__(self, nama, tipe):
        self.nama = nama
        self.tipe = tipe
    
    #ini adalah object/method
    def run(self, speed):
        print('Kucing', self.nama, 'berlari dengan', speed)

    def play(self):
        print('Kucing', self.nama, 'bermain dengan kucing lainnya')
    
    def eat(self):
        pass

#membuat object
yamaha = Cat(nama='Yamaha', tipe='Anggora')
honda = Cat(nama='Honda', tipe='Persian')

print('Yamaha adalah seekor', yamaha.__class__.spesies)
print(yamaha.nama, 'merupakan jenis kucing', yamaha.tipe)
yamaha.run('sangat cepat')
yamaha.play()
print(yamaha.__doc__)
