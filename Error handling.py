#Logical error
'''
try:
    var1 = 10
    var2 = 0
    hasil = var1/var2
except:
    print('Opps! terjadi error')

print('kode setelah error')
'''

try:
    var1 = 10
    var2 = 0
    hasil = var1/var2
except Exception as e:
    print('Opps! terjadi error jenis', e.__class__)

print('kode setelah error')
