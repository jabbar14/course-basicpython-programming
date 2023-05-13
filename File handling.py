'''
#read
data = open('./data.txt', mode='r', encoding='utf-8')

string = data.read()
string1 = string.replace('adalah', 'merupakan')
print(string1)

#append
data =open('./data.txt', mode='a', encoding='utf-8')
data.write('\npython adalah jalan ninjaku')
data.write('\n ess teross')
data.close()

'''

#Best practice
with open('./data.txt', mode='r', encoding='utf=8') as f:
    print(f.read())