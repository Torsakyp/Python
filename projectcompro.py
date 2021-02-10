import csv
from tkinter import *
from tkinter import messagebox
income=0
manu=0
money=0
day = 0
i=1
x=0
total=0
totalincome = 0
totalmoney = 0
paylist=0
inputmo=0
payall=0
M=0
def calculate(*args):
        try:
                global inputmo
                global i , M
                inputin = income.get()
                inputma = manu.get()        
                inputmo = money.get()        
                incomelist = []
                incomelist.append(inputin)        
                manulist = []
                manulist.append(inputma)
                paylist = []
                totalall=[]
                global x        
                global total
                global payall
                if i==1 or x==1:
                        total=sum(incomelist)+total - inputmo
                        for O in range(len(paylist)):
                                M=inputmo+0
                                payall=M+M
                        print("เงินคงเหลือ -->" , total ,"บาท")
                        totalall.append(total)
                        i+=1
                        x+=1
                        print("x=",i,"อิอิ")
                elif i>=2 or x>=1:
                        total=total - inputmo
                        for O in range(len(paylist)):
                                M=inputmo+0
                                payall=M+M
                        print("เงินคงเหลือ -->",total,"บาท")
                        totalall.append(total)
                        i+=1
                        print("x--->",i)
                lst = [[day , inputma , inputmo , total]]       
                print("รายการ -->" , inputma)
                print("ค่าใช้จ่าย -->" , inputmo ,"บาท")
                print("--------------------")
                print(lst)
                
                lb5=Label(mywin,text=total)
                lb5.grid(row=5,column=1,padx=0,pady=0)
                try:
                        filepath="./project.csv"
                        with open(filepath,"a") as outfile:
                                writer = csv.writer(outfile,lineterminator="\n")
                                writer.writerows(lst)
                        with open(filepath,"r") as infile:
                                rd = csv.reader(infile)
                        
                except Exception:
                        messagebox.showwarning(title="Close Program",message="โปรดปิดโปรแกรม .csv")  
                clear()
        except TclError:
                messagebox.showwarning(title="Type Error",message="โปรดใส่รายได้เป็นตัวเลข \n โปรดใส่รายการเป็นตัวอักษร \n โปรดใส่ค่าใช้จ่ายเป็นตัวเลข")


                
def clear(*args):
        ent2.delete(0,END)
        ent3.delete(0,END)
def nextday(*args):
        try:
                global x        
                x=1
                i=1
                ent1.delete(0,END)
                incomelist=0
                incomein=0
                inputmo=0
                total=0
                global day
                day+=1
                if day==1 :
                        day1=Label(mywin,text="    วันจันทร์    ")
                        day1.grid(row=7,column=1,padx=0,pady=0)
                elif day==2:
                        day2=Label(mywin,text="    วันอังคาร   ")
                        day2.grid(row=7,column=1,padx=0,pady=0)
                elif day==3:
                        day3=Label(mywin,text="     วันพุธ   ")
                        day3.grid(row=7,column=1,padx=0,pady=0)
                elif day==4:
                        day4=Label(mywin,text="   วันพฤหัสบดี   ")
                        day4.grid(row=7,column=1,padx=0,pady=0)                        
                elif day==5:
                        day5=Label(mywin,text="   วันศุกร์    ")
                        day5.grid(row=7,column=1,padx=0,pady=0)
                elif day==6:
                        day6=Label(mywin,text="   วันเสาร์   ")
                        day6.grid(row=7,column=1,padx=0,pady=0)
                elif day==7:
                        day7=Label(mywin,text="    วันอาทิตย์    ")
                        day7.grid(row=7,column=1,padx=0,pady=0)
                        NWEEK=Button(mywin,text="End",width=10,command=endgui)
                        NWEEK.grid(row=7,column=2,padx=0,pady=0)
    
        except TclError:
                messagebox.showwarning(title="Type Error",message="โปรดใส่รายได้เป็นตัวเลข \n โปรดใส่รายการเป็นตัวอักษร \n โปรดใส่ค่าใช้จ่ายเป็นตัวเลข")
def endgui():
        if inputmo <= 0 :
                mywin.distory()
        else:
                gui2()                        
                print("date/;",day)    
def gui2():
        global totalincome , totalmoney , paylist
        amount= Tk()
        amount.minsize(300,200)
        amount.title("คำนวณรายรับ-รายจ่าย")
        NW=Label(amount,text="โปรแกรมคำนวณรายรับ-รายจ่าย / สัปดาห์")
        NW.grid(row=0,column=1)


        '''NW1=Label(amount,text="รายรับรวม =")
        NW1.grid(row=1,column=0,padx=0,pady=0)
        NW5=Label(amount,text=totalincome)
        NW5.grid(row=1,column=1,padx=0,pady=0)
        

        NW2=Label(amount,text="รายจ่ายรวม =")
        NW2.grid(row=2,column=0,padx=0,pady=0)
        NW6=Label(amount,text=imputmo)
        NW6.grid(row=2,column=1,padx=0,pady=0)'''     
        


        NW3=Label(amount,text="เงินคงเหลือรวม =")
        NW3.grid(row=3,column=0,padx=0,pady=0)     
        NW4=Label(amount,text=total)
        NW4.grid(row=3,column=1,padx=0,pady=0)             
        calculate()

global mywin
mywin = Tk()
income=IntVar()
manu=StringVar()
money=IntVar()
moneyleft=IntVar()
paylist=IntVar()


mywin.minsize(300,200)
mywin.title("คำนวณรายรับ-รายจ่าย")
lb=Label(mywin,text="โปรแกรมคำนวณรายรับ-รายจ่าย / สัปดาห์")
lb.grid(row=0,column=1)

lb1=Label(mywin,text="รายได้")
lb1.grid(row=1,column=0,padx=0,pady=0)
ent1=Entry(mywin,textvariable=income,width=7)
ent1.grid(row=1,column=1,padx=0,pady=5)

lb2=Label(mywin,text="รายการ")
lb2.grid(row=2,column=0,padx=0,pady=0)
ent2=Entry(mywin,textvariable= manu)
ent2.grid(row=2,column=1)

lb3=Label(mywin,text="ค่าใช้จ่าย")
lb3.grid(row=3,column=0,padx=0,pady=0)
ent3=Entry(mywin,textvariable= money)
ent3.grid(row=3,column=1)

lb4 = Label(mywin, text="เงินคงเหลือ =")
lb4.grid(row=5,column=0,padx=0,pady=0)

btOK=Button(mywin,text="Enter",width=10,command=calculate)
btOK.grid(row=4,column=0)
bt=Button(mywin,text="close",width=10,command=mywin.destroy)
bt.grid(row=4,column=1)
ND=Button(mywin,text="next day",width=10,command=nextday)
ND.grid(row=6,column=1)

mywin.bind("<Return>" , calculate)
nextday()


