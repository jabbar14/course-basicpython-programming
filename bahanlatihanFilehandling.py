with open('./data.txt', mode='r', encoding='utf-8') as f:
    print(f.read())
    

with open('./data.txt', mode='a', encoding='utf-8') as f:
    f.write('\nBahasa pemrigraman python memiliki masa depan yang cerah')
    f.write('\nhalo gaes')

