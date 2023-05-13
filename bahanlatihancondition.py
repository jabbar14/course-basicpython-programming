hargalaptop = 4000000
hargahp = 900000

if hargalaptop < 5000000:
    if hargahp > 3000000:
        print('saya hanya ingin membeli laptop saja')
    elif 1000000 <= hargahp < 3000000:
        print('saya ingin mempertimbangkan')
    else:
        print('saya ingin membeli hp dan laptop')
else:
    print('saya hanya melihat-lihat')