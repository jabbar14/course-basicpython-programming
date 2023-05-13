dictmurid = {
    'namamurid' : ['agus', 'andi', 'ajeng', 'ari', 'budi', 'baso', 'cica', 'dian', 'emil', 'farhan']
}

dictkaryawan = {
    'namakaryawan' : ['jabbar', 'ian', 'azis', 'fikri', 'fikar', 'arik', 'arul', 'arzam', 'naila', 'akhyar']
}

print(dictmurid['namamurid'][2])
print(dictmurid['namamurid'][9])
print(dictkaryawan['namakaryawan'][2])
print(dictkaryawan['namakaryawan'][9])
print('='*50)

for key, value in dictmurid.items():
    print(key, value)
for key, value in dictkaryawan.items():
    print(key, value)