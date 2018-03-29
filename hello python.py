# -*- coding: utf-8 -*-
print ('郭')
#  LIST
a=['join',10,
   'jack',20,
   'jan',30]
a.append(1)
a.insert(2,3)
a.pop(2)
a.pop(6)
print (a)
# TUPLE
b=(1,2,3)
print (b[1])
#DICT
c={
   'jack':10,
   'join':20,
   'jan':30
   }
if 'jack' in c:
   print (c['jack'])
print (c.values())
for v in c.values():
    print (v)
#print (c.itemvalues())
#for v in c.itemvalues():
#    print (v)
for key,values in c.items():
    print (key,':',values)
print (c.get('sam'))
c['guo']=11
c['jack']=33
print (c)
for key in c:
   print (key+':',c[key])
   print (key,':',c[key])
#SET
d=set([1,2,4])
print (d)
print (1 in d)
s = set([('Adam', 95), ('Lisa', 85), ('Bart', 59)])
for f in s:
    print (f[0]+':',f[1])
e=[1,2,3]
print(sum(e))
#FUNCTION
def greet (name='world'):
    print ('Hello,'+name+'.')
greet()
greet('join')
def mulit(ss,sk=2):
    while sk>0:
        sk=sk-1;
        ss=ss*ss;
    print (ss)
    return ss
mulit(2)
def sss(*leg):
    sum=0.0
    if len(leg)==0:
        return sum
    for x in leg:
        sum=sum+x
    return sum
print (sss())
print (sss(1,2,3))
print (sss(1,2,3,4))
lll=[1,2,3,4,5,6,7,8]
kkk=[]
for ii in range(3):
    kkk.append(lll[ii])
print (kkk)
#CUT
print (lll[1:3])
print (lll[0:6:2])
L=range(1,101)  ###
print (L)
print (L[2::3])   # 3*n
print  (L[4:51:5])  #5*n &&<=50
print (L[4::5])
print (L[4::5][-10:])
#
A=['sam','join','jack']
for index,x in enumerate(A):
    print (index,'-',x)
AA=[]
for x in range(1,101):
    AA.append(x*x)
print (AA)
BB=[x*(x+1) for x in range(1,11,2)]  # 1*2  3*4+....
print (BB)
Q=[x*x for x in range(1,10) if x%2==0]
print (Q)
W=[m+n for m in 'ABC' for n in '123']
print (W)
print (abs(-10))
fff=abs
print (fff(-12))
#abs=len
#print abs([1,2])
def addd(x,y,f):
    return f(x)+f(y)
print (addd(1,-2,abs))
print ('{0} love {1}.{2}'.format('I','fish','com'))
def odd(x):
    return x%2==0
print (filter(odd,[1,2,3,4,5,6]))
# import math
import math
def is_sqr(x):
    r=int(math.sqrt(x))
    return x==r*r
print (filter(is_sqr,range(1,100)))  # double = =
#SORTED
ax=[1,23,4,5,6,7,8]
bx=sorted(ax)
print (bx)

#实现忽略大小写的字符比较（ASCLL比较）
def strings_com(xx,yy):
    x=xx.upper()
    y=yy.upper()
    if x>y:
        return 1
    if x<y:
        return -1
    return 0
print (sorted(['bob', 'about', 'Zoo', 'Credit'],reverse=True))
#lambda(类似C的宏定义)
g=lambda x:x*2+1
print (g(2))
gg=lambda xx,yy:xx-yy
print (gg(1,2))
#汉诺塔问题求解
def han(n,x,y,z):
    if n==1:
        print (x,'-->',z)
    else:
        han(n-1,x,z,y)#把n-1个移动到中间
        print (x,'-->',z)#再把移走n-1个后的最底下的移动到最右面
        han(n-1,y,x,z)#最后把位于中间的n-1个移动到最右面
print('---------------------------------Tower of Hanoi-----------------------------------------')
n=int(input('Please input the number of plantes:'))
han(n,'X','Y','Z')
#函数的嵌套
def fun1():
    print("fun1 is using")
    def fun2():
        print ("fun2 is using")
    fun2()
fun1()
#函数闭包
def funx(x):
    def funy(y):
        return x*y
    return funy
b=funx(8)(5)
ass=funx(8)
print (b,'\n',ass(5))
#nonlocal(避免局部变量报错)  注释 三个单引号
"""def fun11():   
    x=5;
    def fun22():
        nonlocal x
        x*=x
        return x
    return fun22
print fun11()"""
#DICT
dict1=dict((('a',10),('b',20),('c',30)))  #dict()里面只有一个元素
print (dict1)
dict2={}#fromkeys
print (dict2.fromkeys((1,2,3),'guo')) #将 guo作为1，2，3的值
print (dict2.fromkeys((1,2,3),(4,5,6)))  #不会分别分配4，5，6而是将（4，5，6）分配给1，2和3
dict3={}
print (dict3.fromkeys(range(0,101),'赞'))#fromkeys并没有改变dict3
dict3=dict3.fromkeys(range(0,101),'GUO')
for key in dict3.keys():
    print (key)
dict3.clear()
print (dict3)
a={'A':1,'B':2,'C':3}
b=a.copy()           #浅拷贝   拷贝到不同的位置
c=a                  #a,c都指向 a
print (a,b,c,id(a),id(b),id(c),'\n',a.popitem()) # .popitem() 随机弹出一个数
#SET
a=[1,2,3,4,5,5,6,6,7]    #SET 中的数据唯一
b=[]
for s in a:
    if s not in b:
        b.append(s)
print (b)
c=list(set(a))   #去掉重复数据
print (c)
#Document
f=open('G:\\g.txt','a')  #只写
#f.write('20183132132112d31h32d1tr2h1232r3t1h23drhtdrthd\ngsgt45rg4t5r4g55rtrt5g4rtg\ntr5g456r4g65t46r5g456rtg\n')
f=open('G:\\g.txt','r') #只读
f.read()
f.readline()  #一行一行的读
f.seek(0,0)   #先指到首行
txt=list(f)  #将内容转换为一个列表
for eachline in txt:  #将每一行打出
    print(eachline)
f.seek(0,0)
for eachline in f:
    print(eachline)
f.close()#必须  关闭文件 占用内存
#分别保存文件
ff=open('G://guo.txt')
boy=[]
girl=[]
count=1
for line in ff:  # 如果不是分割线，则分割
    if line[:6]!='======':
        (roal,spokeline)=line.split('：',1)
        if roal=='悟空':
            boy.append(spokeline)
        if roal=='紫霞':
            girl.append(spokeline)
    else:
        file_nameboy='boy_'+str(count)+'.txt'
        file_namegirl='girl_'+str(count)+'.txt'

        boy_file=open(file_nameboy,'w')
        girl_file=open(file_namegirl,'w')

        boy_file.writelines(boy)
        girl_file.writelines(girl)

        boy_file.close()
        girl_file.close()

        boy=[]
        girl=[]

        count+=1
ff.close()





