from tkinter import *
from tkinter.filedialog import askdirectory
import os
w=Tk()
w.iconbitmap(bitmap='b.ico')
w.geometry('600x200+405+310')
w.title('Renamer')
w.resizable(0,0)
var1=StringVar()
var2=StringVar()
var3=StringVar()

def rens(path,subpath):
   try:
      m=os.listdir(path)
      os.mkdir(subpath+'\\'+'main')
      #print(m)
      for s1 in m:
         os.mkdir(subpath+'\\'+'main'+'\\'+s1)
         r=os.listdir(path+'\\'+s1)
         for k in r:
            f=open(path+'\\'+s1+'\\'+k,'r')
            print(k,r,s1)
            x=f.read()
            dx=x.split('\n')
            y=[]
            y2=[]
            for i in dx:
               if i[0:7]=='- 90° R':
                  print(i)
                  z=dx.index(i)
                  y.append(z)
               if i[0:5]=='90° R':
                  y2.append(dx.index(i))
            
      ##      print(x)
            f2=open(subpath+'\\'+'main'+'\\'+s1+'\\'+str(r.index(k)+1)+'-b.st-'+str(s1)+'mm-Q1.dxf','a')
            m1=''

            for k1 in dx:   
               if y:
                  for l in y:
                     if dx.index(k1)==l:
                        m1='-90° R='+k1[8:17]
               if y2:
                  for q in y2:
                     if dx.index(k1)==q:
                        m1='90° R='+k1[6:17]
               if m1=='':
                  m1=k1
                  
               f2.write(m1)
               m1=''
               f2.write('\n')
         f2.close()
         f.close()
      return m
   except:
      var1.set('Error')
      var2.set('Error')
   ##f3=open('1.bst.1.5mm.Q1.dxf','r')
   ##qw=f3.read()
   ##print(qw)

def f1():
   global p
   p=askdirectory()
   var1.set(p)
def f2():
   global yx
   yx=askdirectory()
   var2.set(yx)
def f3():
   rens(p,yx)
   var1.set('')
   var2.set('')

en1=Entry(w,bg='cyan',fg='blue',bd=1,width=50,font=('arial',13,'bold'),textvariable=var1)
en1.place(x=110,y=23)
en2=Entry(w,bg='cyan',fg='blue',bd=1,width=50,font=('arial',13,'bold'),textvariable=var2)
en2.place(x=110,y=60)

bt1=Button(w,text='scr '+chr(57380),bg='#d9d9d9',activebackground='red',bd=1,fg='blue',command=f1,font=('arial',13,'bold'))
bt1.place(x=24,y=22)
bt2=Button(w,text='Dist '+chr(57380),bg='#d9d9d9',activebackground='red',bd=1,fg='blue',font=('arial',13,'bold'),command=f2)
bt2.place(x=20,y=60)
bt3=Button(w,text='GO?',bg='#d9d9d9',activebackground='red',bd=1,fg='blue',font=('arial',10,'bold'),command=f3)
bt3.place(x=20,y=130)
lb4=Label(w,text=' هذا البرنامج تمت صناعته بواسطة عبدالمنعم سامى',bd=1,fg='green',font=('arial',18,'bold'))
lb4.place(x=110,y=130)

w.mainloop()





