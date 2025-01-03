from tkinter import *
from PIL import ImageTk,Image
import datetime,random

tick=[]
price=0
logged=False
Signup=['','','','','']




root=Tk()
root.config(bg='white')
root.geometry('888x500+300+100')
root.title('MOVIE TICKET BOOKING')
bill= BURGER= CD= CHIPS= FRIES= HOTDOG= PASTRIES= PIZZA= POP=0
'''root.iconbitmap('ico.ico')'''
#__________________________________________________________________________________________________________________
#__________________________________________________________________________________________________________________
e=StringVar()
film=StringVar()
dt=StringVar()
D=StringVar()

def Main():
    global root, e
    for widget in root.winfo_children():
        widget.destroy()

    pvr_image=ImageTk.PhotoImage(Image.open('pvr2.png'))
    plabel=Label(image=pvr_image)
    plabel.place(x=0,y=0)

    x=LabelFrame(root, borderwidth=3, padx=20, pady=20, bg='light blue')
    x.place(x=30,y=150)

    a=Entry(root,textvariable=e, borderwidth=3, width=40, state='disabled', font=("bold", 10))
    a.place(x=48,y=100)

    def write(x):
        a.config(state='normal')
        a.delete(0, END)
        a.insert(0,x)
        a.config(state='disabled')

    Button(x, text='DELHI', font=("bold", 10), borderwidth=0, pady=0.8, bg='light blue', command=lambda:write('DELHI')).grid(row=0,column=0)
    Button(x, text='CHENNAI', font=("bold", 10), borderwidth=0, pady=0.8, bg='light blue', command=lambda:write('CHENNAI')).grid(row=0,column=1)
    Button(x, text='HYDERABAD', font=("bold", 10), borderwidth=0, pady=0.8, bg='light blue', command=lambda:write('HYDERABAD')).grid(row=0,column=2)
    Button(x, text='MOHALI', font=("bold", 10), borderwidth=0, pady=0.8, bg='light blue', command=lambda:write('MOHALI')).grid(row=1,column=0)
    Button(x, text='JAIPUR', font=("bold", 10), borderwidth=0, pady=0.8, bg='light blue', command=lambda:write('JAIPUR')).grid(row=1,column=1)
    Button(x, text='AHMADABAD', font=("bold", 10), borderwidth=0, pady=0.8, bg='light blue', command=lambda:write('AHMADABAD')).grid(row=1,column=2)
    Button(x, text='KOLKATA', font=("bold", 10), borderwidth=0, pady=0.8, bg='light blue', command=lambda:write('KOLKATA')).grid(row=2,column=0)
    Button(x, text='BENGALURU', font=("bold", 10), borderwidth=0, pady=0.8, bg='light blue', command=lambda:write('BENGALURU')).grid(row=2,column=1)
    Button(x, text='INDORE', font=("bold", 10), borderwidth=0, pady=0.8, bg='light blue', command=lambda:write('INDORE')).grid(row=2,column=2)
    Button(x, text='PATNA', font=("bold", 10), borderwidth=0, pady=0.8, bg='light blue', command=lambda:write('PATNA')).grid(row=3,column=0)
    Button(x, text='BHUVANESHWAR', font=("bold", 10), borderwidth=0, pady=0.8, bg='light blue', command=lambda:write('BHUVANESHWAR')).grid(row=3,column=1)
    Button(x, text='SRINAGAR', font=("bold", 10), borderwidth=0, pady=0.8, bg='light blue', command=lambda:write('SRINAGAR')).grid(row=3,column=2)


    Button(root, text='Next', font=("bold", 10), padx=15, pady=0.8, bg='light green', command=Ticket).place(x=400,y=250)

    food=Button(root, text='Food', font=("bold", 10), padx=50, pady=2, bg='light blue', command=Food).place(x=600,y=150)

    if not logged:
        Sign_up=Button(root, text='Sign_up', font=("bold", 10), padx=25, pady=0.8, bg='light blue', command=sign_up)
        Sign_up.place(x=480,y=450)
       
        Login=Button(root, text='Login', font=("bold", 10), padx=25, pady=0.8, bg='light blue', command=login)
        Login.place(x=590,y=450)
    else:
        def out():
            global logged
            logged=False
            Main()
        log=LabelFrame(root, relief=RAISED, borderwidth=3, padx=20, pady=10, bg='white')
        log.place(x=600,y=100)
        Label(log, text='Name : {}/nEmail : {}/nAge : {}/nGender : {}'.format(Signup[0],Signup[1],Signup[2],Signup[3]), font=("bold", 12), bg='white').pack()
        sign_out=Button(root, text='Sign Out', font=("bold", 10), padx=25, pady=0.8, bg='light blue', command=out)
        sign_out.place(x=630,y=450)
   
    
    root.mainloop()

#__________________________________________________________________________________________________________________
#__________________________________________________________________________________________________________________


def Ticket():
    
    global root, e, price, film, dt, D
    root.config(bg='SystemButtonFace')
    if e.get()=='':
        Main()
    for widget in root.winfo_children():
        widget.destroy()
    pvr_image=ImageTk.PhotoImage(Image.open('pvr4.png'))
    plabel=Label(image=pvr_image)
    plabel.place(x=0,y=0)

    x=LabelFrame(root, borderwidth=3, padx=20, pady=20, bg='light blue')
    x.place(x=80,y=150)
    a=Entry(root,textvariable=film, borderwidth=3, width=40, state='disabled', bg='light blue', font=("bold", 10))
    a.place(x=48,y=100)
    def write(x):
        a.config(state='normal')
        a.delete(0, END)
        a.insert(0,x)
        a.config(state='disabled')
    Button(x, text='BAHUBALI (2h,22min)', font=("bold", 10), borderwidth=0, pady=0.8, bg='light blue', command=lambda:write('BAHUBALI')).grid(row=0,column=0)
    Button(x, text='TANAJI (2h,20min)', font=("bold", 10), borderwidth=0, pady=0.8, bg='light blue', command=lambda:write('TANAJI')).grid(row=1,column=0)
    Button(x, text='BALA  (2h,10min)', font=("bold", 10), borderwidth=0, pady=0.8, bg='light blue', command=lambda:write('BALA')).grid(row=2,column=0)
    Button(x, text='ROCKY MENTAL  (2h,19min)', font=("bold", 10), borderwidth=0, pady=0.8, bg='light blue', command=lambda:write('ROCKEY MENTAL')).grid(row=3,column=0)
    Button(x, text='AVENGERS  (2h,17min)', font=("bold", 10), borderwidth=0, pady=0.8, bg='light blue', command=lambda:write('AVENGERS')).grid(row=4,column=0)
    Button(x, text='UJDA CHAMAN  (2h,11min)', font=("bold", 10), borderwidth=0, pady=0.8, bg='light blue', command=lambda:write('UJADA CHAMAN')).grid(row=5,column=0)
    Button(x, text='GODZZILA  (1h,50min)', font=("bold", 10), borderwidth=0, pady=0.8, bg='light blue', command=lambda:write('GODZZILA')).grid(row=6,column=0)
    Button(x, text='GOOD NEWZ  (2h,30min)', font=("bold", 10), borderwidth=0, pady=0.8, bg='light blue', command=lambda:write('GOOD NEWZ')).grid(row=7,column=0)
    Button(x, text='SHOLAY  (2h,54min)', font=("bold", 10), borderwidth=0, pady=0.8, bg='light blue', command=lambda:write('SHOLAY')).grid(row=8,column=0)
    Button(x, text='DHOOM 3  (2h,31min)', font=("bold", 10), borderwidth=0, pady=0.8, bg='light blue', command=lambda:write('DHOOM 3')).grid(row=9,column=0)
    Button(x, text='DANGAL  (2h,20min)', font=("bold", 10), borderwidth=0, pady=0.8, bg='light blue', command=lambda:write('DANGAL')).grid(row=10,column=0)
    Button(x, text='HOUSEFULL  (2h,20min)', font=("bold", 10), borderwidth=0, pady=0.8, bg='light blue', command=lambda:write('HOUSEFULL')).grid(row=11,column=0)

    date=Entry(root,textvariable=dt, borderwidth=3, font=("bold", 10))
    date.place(x=380,y=100)
    date.delete(0,END)
    date.insert(0,'{}'.format(datetime.date.today()))

    D2=OptionMenu(root, D, '2D', '3D')
    D2.place(x=380,y=150)
    def col(x):
        global price
        price1=0
        if x!=0 and film.get()!='':
            if x not in tick:
                tick.append(x)
            else:
                for i in range(len(tick)):
                    if tick[i]==x:
                        tick.pop(i)
                        break
        Label(root, text='    '*100).place(x=550,y=300)
        Label(root, text='    '*100).place(x=550,y=330)
        Label(root, text='Selected Seats: {}'.format(tick)).place(x=550,y=300)
        if film.get()=='BAHUBALI':
            price1=500
        elif film.get=='':
            pass
        else:
            price1=150
        price=len(tick)*price1
        Label(root, text='Price: {}'.format(price)).place(x=550,y=330)
    col(0)
       
    Button(root, text='1', padx=8,bg='light blue', command=lambda:col('1')).place(x=570,y=100)
    Button(root, text='2', padx=8,bg='light blue', command=lambda:col('2')).place(x=610,y=100)
    Button(root, text='3', padx=8,bg='light blue', command=lambda:col('3')).place(x=650,y=100)
    Button(root, text='4', padx=8,bg='light blue', command=lambda:col('4')).place(x=690,y=100)
    Button(root, text='5', padx=8,bg='light blue', command=lambda:col('5')).place(x=730,y=100)  
    Button(root, text='6', padx=8,bg='light blue', command=lambda:col('6')).place(x=570,y=130)
    Button(root, text='7', padx=8,bg='light blue', command=lambda:col('7')).place(x=610,y=130)
    Button(root, text='8', padx=8,bg='light blue', command=lambda:col('8')).place(x=650,y=130)
    Button(root, text='9', padx=8,bg='light blue', command=lambda:col('9')).place(x=690,y=130)
    Button(root, text='10', padx=5,bg='light blue', command=lambda:col('10')).place(x=730,y=130)
    Button(root, text='11', padx=5,bg='light blue', command=lambda:col('11')).place(x=570,y=160)
    Button(root, text='12', padx=5,bg='light blue', command=lambda:col('12')).place(x=610,y=160)
    Button(root, text='13', padx=5,bg='light blue', command=lambda:col('13')).place(x=650,y=160)
    Button(root, text='14', padx=5,bg='light blue', command=lambda:col('14')).place(x=690,y=160)
    Button(root, text='15', padx=5,bg='light blue', command=lambda:col('15')).place(x=730,y=160)  
    Button(root, text='16', padx=5,bg='light blue', command=lambda:col('16')).place(x=570,y=190)
    Button(root, text='17', padx=5,bg='light blue', command=lambda:col('17')).place(x=610,y=190)
    Button(root, text='18', padx=5,bg='light blue', command=lambda:col('18')).place(x=650,y=190)
    Button(root, text='19', padx=5,bg='light blue', command=lambda:col('19')).place(x=690,y=190)
    Button(root, text='20', padx=5,bg='light blue', command=lambda:col('20')).place(x=730,y=190)
    Button(root, text='21', padx=5,bg='light blue', command=lambda:col('21')).place(x=570,y=220)
    Button(root, text='22', padx=5,bg='light blue', command=lambda:col('22')).place(x=610,y=220)
    Button(root, text='23', padx=5,bg='light blue', command=lambda:col('23')).place(x=650,y=220)
    Button(root, text='24', padx=5,bg='light blue', command=lambda:col('24')).place(x=690,y=220)
    Button(root, text='25', padx=5,bg='light blue', command=lambda:col('25')).place(x=730,y=220)  
    Button(root, text='26', padx=5,bg='light blue', command=lambda:col('26')).place(x=570,y=250)
    Button(root, text='27', padx=5,bg='light blue', command=lambda:col('27')).place(x=610,y=250)
    Button(root, text='28', padx=5,bg='light blue', command=lambda:col('28')).place(x=650,y=250)
    Button(root, text='29', padx=5,bg='light blue', command=lambda:col('29')).place(x=690,y=250)
    Button(root, text='30', padx=5,bg='light blue', command=lambda:col('30')).place(x=730,y=250)


       
    #Button(root, text='t', padx=padx, command=col(1,10,10)).place(x=580,y=400)
    Main1=Button(root, text='◄', font=("bold", 10), padx=15, pady=5, bg='light blue', command=Main)
    Main1.place(x=0,y=0)

    Button(root, text='Confirm', font=("bold", 10), padx=15, pady=0.8, bg='white', command=Confirm).place(x=640,y=400)

    root.mainloop()   
#__________________________________________________________________________________________________________________
#__________________________________________________________________________________________________________________


def Confirm():
    global tick, e
    sno=random.randint(1,99999)
    cinema=['v3s','ANSAL PLAZA','RAJNI COMPLEX','MAHAGUN MALL','BESTECH SQUARE','PACIFIC MALL','GOKULAM CINEMA']
    global root, price, film, dt, D
    for widget in root.winfo_children():
        widget.destroy()
    if tick==[] or dt.get()=='' or D.get()=='':
        Ticket()
        price=0
    else:
        Main1=Button(root, text='◄', font=("bold", 10), padx=15, pady=5, bg='light blue', command=Ticket)
        Main1.place(x=0,y=0)
        Label(root, text='TICKET NO IS :  {}'.format(random.randint(1,99999)), font=('bold', 14)).place(x=100,y=50)
        Label(root, text='Total Price: {}'.format(price), font=('bold', 14)).place(x=100,y=100)
        Label(root, text='Movie Name: {}'.format(film.get()), font=('bold', 14)).place(x=100,y=150)
        Label(root, text='Date: {}'.format(dt.get()), font=('bold', 14)).place(x=100,y=200)
        Label(root, text='2D / 3D: {}'.format(D.get()), font=('bold', 14)).place(x=100,y=250)
        Label(root, text='Cinema: {}'.format(random.choice(cinema)), font=('bold', 14)).place(x=100,y=300)
        Label(root, text='your seats are/is: {}'.format(tick), font=('bold', 14)).place(x=100,y=300)
        Label(root, text='YOUR TICKET IS CONFIRMED!', font=("bold", 14)).place(x=278,y=400)
       


       
        print("TICKET DETAIL ARE :")
        print("    =>TOTAL AMOUNT:$",price)
        print("    =>SELECTED MOVIE IS:", film.get())
        print("    =>DATE OF MOVIE IS :",dt.get())
        print("    =>MOVIE DIMMENSION IS:",D.get())
        print("    =>CHOOSED CINEMA HOUSE :",random.choice(cinema))
        print("    =>SEATS IS/ARE:",(tick))

        print("         YOUR TICKET IS CONFIRMED!")
      
        

def Food():
    global root, bill
    for widget in root.winfo_children():
        widget.destroy()

    def zero():
        global bill, tea, coff, L, mL, VegBk, NBk, Vmeal, Nmeal
        bill=0
        tea=0
        coff=0
        L=0
        mL=0
        VegBk=0
        NBk=0
        Vmeal=0
        Nmeal=0
        Food()
    zero() 
    def Total(x):
        global bill, tea, coff, L, mL, VegBk, NBk, Vmeal, Nmeal

        if x==7 or x==-7:
            if x>0:
                tea+=1
            elif bill*tea!=0:
                tea-=1
                
        elif x==8 or x==-8:
            if x>0:
                coff+=1
            elif bill*coff!=0:
                coff-=1
                
        elif x==15 or x==-15:
            if x>0:
                L+=1
            elif bill*L!=0:
                L-=1

        elif x==10 or x==-10:
            if x>0:
                mL+=1
            elif bill*mL!=0:
                mL-=1

        elif x==25 or x==-25:
            if x>0:
                VegBk+=1
            elif bill*VegBk!=0:
                VegBk-=1
                
        elif x==35 or x==-35:
            if x>0:
                NBk+=1
            elif bill*NBk!=0:
                NBk-=1

        elif x==50 or x==-50:
            if x>0:
                Vmeal+=1
            elif bill*Vmeal!=0:
                Vmeal-=1

        elif x==55 or x==-55:
            if x>0:
                Nmeal+=1
            elif bill*Nmeal!=0:
                Nmeal-=1

        if bill+x>=0:
            bill+=x
        
        l1=Label(root, text="Total :          Total Cost:", font=("bold", 10)).place(x=560,y=50)
        e1 = Entry(root, textvariable=tea, borderwidth=5, font=("bold", 10), width=3)
        e1.place(x=600,y=48)
        e1.delete(0, END)
        e1.insert(0, "{}".format(tea))
        e1 = Entry(root, borderwidth=5, font=("bold", 10), width=3)
        e1.place(x=708,y=48)
        e1.delete(0, END)
        e1.insert(0, "{}₹".format(tea*7))

        l2=Label(root, text="Total :          Total Cost:", font=("bold", 10)).place(x=560,y=81)
        e2 = Entry(root, textvariable=coff, borderwidth=5, font=("bold", 10), width=3)
        e2.place(x=600,y=79)
        e2.delete(0, END)
        e2.insert(0, "{}".format(coff))
        e2 = Entry(root, borderwidth=5, font=("bold", 10), width=3)
        e2.place(x=708,y=79)
        e2.delete(0, END)
        e2.insert(0, "{}₹".format(coff*8))

        l3=Label(root, text="Total :          Total Cost:", font=("bold", 10)).place(x=560,y=153)
        e3 = Entry(root, textvariable=L, borderwidth=5, font=("bold", 10), width=3)
        e3.place(x=600,y=151)
        e3.delete(0, END)
        e3.insert(0, "{}".format(L))
        e3 = Entry(root, borderwidth=5, font=("bold", 10), width=3)
        e3.place(x=708,y=151)
        e3.delete(0, END)
        e3.insert(0, "{}₹".format(L*15))
        
        l4=Label(root, text="Total :          Total Cost:", font=("bold", 10)).place(x=560,y=178)
        e4 = Entry(root, textvariable=mL, borderwidth=5, font=("bold", 10), width=3)
        e4.place(x=600,y=176)
        e4.delete(0, END)
        e4.insert(0, "{}".format(mL))
        e4 = Entry(root, borderwidth=5, font=("bold", 10), width=3)
        e4.place(x=708,y=176)
        e4.delete(0, END)
        e4.insert(0, "{}₹".format(mL*10))
        
        l5=Label(root, text="Total :          Total Cost:", font=("bold", 10)).place(x=560,y=243)
        e5 = Entry(root, textvariable=VegBk, borderwidth=5, font=("bold", 10), width=3)
        e5.place(x=600,y=241)
        e5.delete(0, END)
        e5.insert(0, "{}".format(VegBk))
        e5 = Entry(root, borderwidth=5, font=("bold", 10), width=3)
        e5.place(x=708,y=241)
        e5.delete(0, END)
        e5.insert(0, "{}₹".format(VegBk*25))
        
        l6=Label(root, text="Total :          Total Cost:", font=("bold", 10)).place(x=560,y=278)
        e6 = Entry(root, textvariable=NBk, borderwidth=5, font=("bold", 10), width=3)
        e6.place(x=600,y=276)
        e6.delete(0, END)
        e6.insert(0, "{}".format(NBk))
        e6 = Entry(root, borderwidth=5, font=("bold", 10), width=3)
        e6.place(x=708,y=276)
        e6.delete(0, END)
        e6.insert(0, "{}₹".format(NBk*35))
        
        l7=Label(root, text="Total :          Total Cost:", font=("bold", 10)).place(x=560,y=368)
        e7 = Entry(root, textvariable=Vmeal, borderwidth=5, font=("bold", 10), width=3)
        e7.place(x=600,y=366)
        e7.delete(0, END)
        e7.insert(0, "{}".format(Vmeal))
        e7 = Entry(root, borderwidth=5, font=("bold", 10), width=3)
        e7.place(x=708,y=366)
        e7.delete(0, END)
        e7.insert(0, "{}₹".format(Vmeal*50))
        
        l8=Label(root, text="Total :          Total Cost:", font=("bold", 10)).place(x=560,y=398)
        e8 = Entry(root, textvariable=Nmeal, borderwidth=5, font=("bold", 10), width=3)
        e8.place(x=600,y=396)
        e8.delete(0, END)
        e8.insert(0, "{}".format(Nmeal))
        e8 = Entry(root, borderwidth=5, font=("bold", 10), width=3)
        e8.place(x=708,y=396)
        e8.delete(0, END)
        e8.insert(0, "{}₹".format(Nmeal*55))
        
        e9 = Entry(root, textvariable=bill, borderwidth=5, font=("bold", 10), width=10)
        e9.place(x=660,y=460)
        e9.delete(0, END)
        e9.config(state='normal')
        e9.insert(0, "{}₹".format(bill))
        e9.config(state='disabled')
    
    # Confirm Order______________


    def confirm():
        global root
        if bill>0:
            for widget in root.winfo_children():
                widget.destroy()
            tn=IntVar()
            sn=IntVar()

            def done():
                try:
                    if tn.get()!= 0:
                        Label(root, text='       '*10).place(x=650,y=165)
                    else:
                        Label(root, text='Enter Train No.', font=("bold", 14), fg='red').place(x=650,y=158)
                except:
                    Label(root, text='       '*10).place(x=650,y=165)
                    Label(root, text='Only Digits', font=("bold", 14), fg='red').place(x=650,y=158)
                #====================================================================
                try:
                    if sn.get()!= 0:
                        Label(root, text='       '*10).place(x=650,y=245)
                    else:
                        Label(root, text='Enter Seat No.', font=("bold", 14), fg='red').place(x=650,y=238)
                except:
                    Label(root, text='       '*10).place(x=650,y=245)
                    Label(root, text='Only Digits', font=("bold", 14), fg='red').place(x=650,y=238)
                #====================================================================
                try:
                    if tn.get()!=0 and sn.get()!=0:
                        e1.config(state='disabled')
                        e2.config(state='disabled')
                        Label(root, text='CONFIRMED!', font=("bold", 16)).place(x=380,y=350)
                except:
                    pass
            
            Label(root, text="Enter Train Number", font=("bold", 15)).place(x=360,y=120)

            Label(root, text="Enter Seat Number", font=("bold", 15)).place(x=360,y=200)

            e1=Entry(root, textvariable=tn, borderwidth=5, font=("bold", 10))
            e1.place(x=375,y=160)
            e2=Entry(root, textvariable=sn, borderwidth=5, font=("bold", 10))
            e2.place(x=375,y=240)
            
            Button(root, text='Confirm', font=("bold", 10), padx=15, pady=2, bg='light blue', command=done).place(x=390,y=350)

            Main1=Button(root, text='◄', font=("bold", 10), padx=15, pady=2, bg='light blue', command=Food)
            Main1.place(x=0,y=0)
        else:
            Food()

    Label(root, text='Total :', font=('bold',14)).place(x=600,y=460)
    
    FOOD=ImageTk.PhotoImage(Image.open('food menu.png'))
    label1=Label(image=FOOD)
    label1.place(x=0,y=0)

    add1=Button(root, text='⬆', font=("bold", 8), command=lambda:Total(7))
    add1.place(x=520,y=53)
    Button(root, text='⬇', font=("bold", 8), command=lambda:Total(-7)).place(x=755,y=53)

    add2=Button(root, text='⬆', font=("bold", 8), command=lambda:Total(8))
    add2.place(x=520,y=78)
    Button(root, text='⬇', font=("bold", 8), command=lambda:Total(-8)).place(x=755,y=78)

    add3=Button(root, text='⬆', font=("bold", 8), command=lambda:Total(15))
    add3.place(x=520,y=157)
    Button(root, text='⬇', font=("bold", 8), command=lambda:Total(-15)).place(x=755,y=157)

    add4=Button(root, text='⬆', font=("bold", 8), command=lambda:Total(10))
    add4.place(x=520,y=182)
    Button(root, text='⬇', font=("bold", 8), command=lambda:Total(-10)).place(x=755,y=182)

    add5=Button(root, text='⬆', font=("bold", 8), command=lambda:Total(25))
    add5.place(x=520,y=247)
    Button(root, text='⬇', font=("bold", 8), command=lambda:Total(-25)).place(x=755,y=247)

    add6=Button(root, text='⬆', font=("bold", 8), command=lambda:Total(35))
    add6.place(x=520,y=282)
    Button(root, text='⬇', font=("bold", 8), command=lambda:Total(-35)).place(x=755,y=282)

    add7=Button(root, text='⬆', font=("bold", 8), command=lambda:Total(50))
    add7.place(x=520,y=372)
    Button(root, text='⬇', font=("bold", 8), command=lambda:Total(-50)).place(x=755,y=372)

    add8=Button(root, text='⬆', font=("bold", 8), command=lambda:Total(55))
    add8.place(x=520,y=397)
    Button(root, text='⬇', font=("bold", 8), command=lambda:Total(-55)).place(x=755,y=397)
    
    show=Button(root, text='Next', font=("bold", 12), padx=20, bg='light blue', command=confirm).place(x=400,y=460)
    
    Main1=Button(root, text='◄', font=("bold", 10), padx=15, pady=5, bg='light blue', command=Main)
    Main1.place(x=0,y=460)

    # Refresh
    refresh=Button(root, text='⟲', font=("bold", 10), bg='light blue', padx=10, pady=5, command=zero)
    refresh.place(x=847,y=0)

    Total(0)
    root.mainloop()
    

   
   

#____________________________________________________________________________________________________________________

def sign_up():
    global root
    for widget in root.winfo_children():
        widget.destroy()

    def Add_account():
        global logged
        if Gender.get()==1:
            Signup[3]='Male'
        elif Gender.get()==2:
            Signup[3]='Female'
        else:
            pass
        if name.get()=='':
            Label(root, text='Enter Name!!', font=("bold", 10), fg='red').place(x=560, y=130)
        else:
            Signup[0]=name.get()
            Label(root, text='     '*18, font=("bold", 10), fg='red').place(x=560, y=130)
        if mail.get()=='':
            Label(root, text='Enter Email!!', font=("bold", 10), fg='red').place(x=560, y=180)
        else:
            Signup[1]=mail.get()
            Label(root, text='     '*18, font=("bold", 10), fg='red').place(x=560, y=180)
        if age.get()=='':
            Label(root, text='Enter Age!!', font=("bold", 10), fg='red').place(x=560, y=270)
        else:
            Signup[2]=age.get()
            Label(root, text='     '*18, font=("bold", 10), fg='red').place(x=560, y=270)

        if name.get()=='' or mail.get()=='' or age.get()=='':
            pass
        else:
            logged=True
        if logged:
            Main()
       

   
    label_0 = Label(root, text="Fill Details",width=20,font=("bold", 20))
    label_0.place(x=180,y=53)


    NAME = Label(root, text="FullName",width=20,font=("bold", 10))
    NAME.place(x=160,y=130)


    name=StringVar()


    Name = Entry(root,textvariable=name)
    Name.place(x=330,y=130)

    MAIL = Label(root, text="Email",width=20,font=("bold", 10))
    MAIL.place(x=158,y=180)


    mail=StringVar()


    Mail = Entry(root,textvariable=mail)
    Mail.place(x=330,y=180)

    GENDER = Label(root, text="Gender",width=20,font=("bold", 10))
    GENDER.place(x=160,y=230)

    Gender = IntVar()

    Radiobutton(root, text="Male",padx = 5, variable=Gender, value=1).place(x=330,y=230)
    Radiobutton(root, text="Female",padx = 20, variable=Gender, value=2).place(x=385,y=230)

    AGE = Label(root, text="Age:",width=20,font=("bold", 10))
    AGE.place(x=160,y=280)


    age=StringVar()

   
    Age = Entry(root,textvariable=age)
    Age.place(x=330,y=280)

    Button(root, text='◄', font=("bold", 10), padx=15, pady=5, bg='light blue', command=Main).place(x=0,y=0)
    Button(root, text='Submit', width=20, pady=2.2, bg='light blue', command=Add_account).place(x=270,y=380)


    root.mainloop()


def login():
    global root
    for widget in root.winfo_children():
        widget.destroy()

    label_0 = Label(root, text="Login",width=20,font=("bold", 20))
    label_0.place(x=180,y=53)

    MAIL = Label(root, text="Email",width=20,font=("bold", 14))
    MAIL.place(x=100,y=178)


    mail=StringVar()
    Mail = Entry(root,textvariable=mail, width=24, borderwidth=5, font=("bold", 10))
    Mail.place(x=350,y=180)

    Button(root, text='◄', font=("bold", 10), padx=15, pady=5, bg='light blue', command=Main).place(x=0,y=0)
    Button(root, text='→', bg='light blue', font=("bold", 10)).place(x=506,y=180)


    root.mainloop()



















if __name__=='__main__':
    Main()
