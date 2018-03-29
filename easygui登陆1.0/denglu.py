from easygui import*
import pickle
import os
os.chdir('C:\\Users\\Xinyu\\Desktop\\python\\easygui登陆1.0')
a=[0,1]
b=[0,1]
count=0
def login():                           
    c=multpasswordbox(msg='',title='',fields=('账户','密码'))
    for i in range(0,2): 
        a[i]=c[i]   
def signup():                        
    d=multenterbox(msg='>>>请正确填写以下信息注册<<<',title='注册YY',fields=('帐户名','密码','邮箱'))
    for i in range(0,2):
        b[i]=d[i]
def main():                           
    global count
    file=open('data.pkl','rb')
    database=pickle.load(file)
    file.close()
    login()
    if a[0] not in database:             
        z=ccbox('用户不存在，是否注册新账户','',choices=('Yes','No'))
        if z==1:
            signup()
            database.update({b[0]:b[1]})
            file=open('data.pkl','wb')
            pickle.dump(database,file)
            file.close()
            if database.get(b[0])==b[1]:
                msgbox('注册成功！')
            else:
                msgbox('注册失败')
        main()
    else:     
        if database.get(a[0])!=a[1]:
            count+=1
            msgbox('！密码错误！','错误')
            if count==3:
                count=0
                x=ccbox('是否要修改密码？','提示',choices=('Yes','No'))
                if x==1:
                    def mima():
                        xx=multenterbox('','',fields=('输入新密码：','再次输入新密码：'))
                        if xx[0]!=xx[1]:
                            msgbox('两次输入密码不一致')
                            xx.pop(0)
                            xx.pop(0)
                            mima()
                        database[a[0]]=xx[0]
                    mima()
                    file=open('data.pkl','wb')
                    pickle.dump(database,file)
                    file.close()
                    msgbox('修改成功！','')
            main()
        else:
            count=0
            t=ccbox('写下你想要说的话：','欢迎进入YY',choices=('开始写','B'),image='C:\\Users\\Xinyu\\Desktop\\python\\easygui登陆1.0\\1.gif')
            if t==1:
                text=textbox()
                os.chdir('C:\\Users\\Xinyu\\Desktop')
                f=open(a[0]+'.txt','w')
                f.write(text)
                f.seek(2,0)
                f.close()
                
main()




