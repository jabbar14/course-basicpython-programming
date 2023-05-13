import re

teks1 = 'saya sedang berdomisili di tokyo bisa dihubungi di nomor berikut 021 7581 6521'
x = re.sub('\d{3} \d{4} \d{4}', '',teks1)
print(x)

teks2 = 'tokyo'
x = re.match('^t...o$', teks2)
print(x)

teks3 = 'saya sedang berdomisili di Tokyo bisa dihubungi di nomor berikut 021 7581 6521'
x = re.findall('\d{3} \d{4} \d{4}', teks3)
print(x)

x = re.findall('Tokyo', teks3)
print(x)
