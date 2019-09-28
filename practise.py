# -*- coding: UTF-8 -*-

import random
'''
#1
a =["Archie","leon","cynthia","eathson","kevin"]
b =[1,2,3,4,5,6,7]

print(a)
print(b)
#2

a+=["mike"]
print(a)

#3
for i in range(3):
    a.append('xxx')
    print(a)

a.extend(a)
print(a)


#4
c=a+b
print(c)


#5
length=len(a)
print('lenth of tuple a is %d'% length)

#6
index =1
print(a[index])

#7
length =len(a)
for i in range(length):
    print(a[i])

print("------------------------------------------------------------------------------")
for element in a:
    print(element)


print("==================================================================================")
for i in range(5):
    lucky=random.choice(a)
    print(lucky)

#8

a =["Archie","leon","cynthia","eathson","kevin"]

index=3
a[index]="cosmo"
print("_____________________________________________")
print(a)


#9
a =["Archie","leon","cynthia","eathson","kevin"]
index=0
del a[index]
del a[index]
print("||||||||||||||||||||||||||||||||||||||||||||||||||||||||")

print(a)


a.clear()
print(a)





for time in range(10):
    password=random.randint(0,999999)
    s_pwd="%06d" % password
    print(s_pwd)

print("\n ++++++++++++++++++++++++++++++++++++++++++++++")
nums=('0','1','2','3','4','5','6','7','8','9')
password=[]

length=4

pwd=''
for i in range(length):
    s=random.choice(nums)
    pwd=s
    print(pwd)
print('\n\n---cutting line 3---')
# 定义所有可用的字符
char1 = ['0','1','2','3','4','5','6','7','8','9']
char2 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
char3 = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
char4 = ['~','!','@','#','$','%','^','&','*','(',')','_','+','-','=','{','}','[',']',':','"',';','<','>','?',',','.','/']


char_All=char1 +char2+char3+char4
length=8
pwd=''
for i in range(length):
    s=random.choice(char_All)
    pwd+=s
print(pwd)

family_words = ("赵","钱","孙","李","周","吴","郑","王")
indox=0
print("%s"%(family_words[indox]))
for name in family_words:
    print ("%s"% name, end='')
print('\n')

print("###############################################################")
times=5
print('总共有%d个姓供挑选，计划挑选%d 次'%(len(family_words),times))
for i in range(times):
    print("picked family name is :%s"%random.choice(family_words))
'''





print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')

family_words = ("赵","钱","孙","李","周","吴","郑","王")
given_words = ["致浩","明云","浩烨","兆忠","予忻","顺雨","尚扬","俊祥","语禅","予浩"]

given_words1 = [ \
"潮","彻","郴","琛","澈","臣","辰","晨","承","盛","程", \
"池","炽","冲","重","崇","绸","畴","酬","筹","楚","处", \
]
given_words.extend(given_words1)
print(given_words)

full_name=''
class_name=[]

times=30
for i in range(times):
    fname=random.choice(family_words)
    lname=random.choice(given_words)
    full_name=fname+''+lname
    print(full_name)
    class_name.append(full_name)

print('---------------------------------------')
print(class_name)
