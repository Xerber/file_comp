f1_in=[]
f2_in=[]
#Open our files and remove \n
with open('1.txt', encoding='utf-8') as file:
    for i in file:
        f1_in.append(i.strip('\n'))
with open('2.txt', encoding='utf-8') as file:
    for i in file:
        f2_in.append(i.strip('\n'))
#---
def comparison(f1_in,f2_in):
    for i in f1_in:
        if i not in f2_in:
            print(i)
        else:
            pass
    print('*'*20+'\n')
#Start data comparison and print info
print('Start comparison File1 to File2\n')
comparison(f1_in,f2_in)
print('Start comparison File2 to File1\n')
comparison(f2_in,f1_in)
input('')