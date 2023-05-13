def cek_modulus(angka1,angka2):
    hasil = angka1*angka2
    if hasil%2 == 1:
        print('Modulus adalah 1')
    elif hasil%2 == 0:
        print('Modulus adalah 0')

    return hasil

mod = cek_modulus(12, 8)
print(mod)

