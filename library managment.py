from tkinter import *
import tkinter as tk
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
import datetime
import tkinter


class LibraryManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Library Management System")
        self.root.geometry("1920x1080")



# ================================================= variable ==================================================================


        self.member_var=StringVar()
        self.prn_var=StringVar()
        self.id_var=StringVar()
        self.firstname_var=StringVar()
        self.lastname_var=StringVar()
        self.address1_var=StringVar()
        self.address2_var=StringVar()
        self.postcode_var=StringVar()
        self.mobile_var=StringVar()
        self.bookid_var=StringVar()
        self.booktitle_var=StringVar()
        self.auther_var=StringVar()
        self.dateborrowed_var=StringVar()
        self.datedue_var=StringVar()
        self.daysonbook_var=StringVar()
        self.lateratefine_var=StringVar()
        self.dateoverdue_var=StringVar()
        self.finallprice_var=StringVar()




        lbltitle=Label(self.root,text="LIBRARY MANAGEMENT SYSTEM",bg="sky blue",fg="green",bd=20,relief=RIDGE,font=("times new roman",50,"bold"),padx=2,pady=6)
        lbltitle.pack(side=TOP,fill=X)


        frame=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="sky blue")
        frame.place(x=0,y=130,width=1920,height=400)
        
# =========================DATAFRAMELEFT==============================================================================================
        DataFrameLeft=LabelFrame(frame,text="Library Membership Information",bg="sky blue",fg="blue",bd=12,relief=RIDGE,font=("times new roman",12,"bold"))
        DataFrameLeft.place(x=0,y=5,width=1400,height=350)

        lblMember=Label(DataFrameLeft,textvariable=self.member_var,font=("times new roman",12,"bold"),text="Member Type:",bg="sky blue",padx=2,pady=6)
        lblMember.grid(row=0,column=0,sticky=W)

        comMember=ttk.Combobox(DataFrameLeft,textvariable=self.member_var,font=("times new roman",12,"bold"),width=27,state="readonly")
        comMember["value"]=("Admin Staff","Student","Lecture")
        comMember.current(0)
        comMember.grid(row=0,column=1)

        lblPRN_NO=Label(DataFrameLeft,bg="sky blue",text="PRN No:",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblPRN_NO.grid(row=1,column=0,sticky=W)
        txtPRN_NO=Entry(DataFrameLeft,font=("times new roman",12,"bold"),width=29,textvariable=self.prn_var)
        txtPRN_NO.grid(row=1,column=1)

        lblTitle=Label(DataFrameLeft,bg="sky blue",text="ID No:",font=("times new roman",12,"bold"),padx=2,pady=4)
        lblTitle.grid(row=2,column=0,sticky=W)
        txtTitle=Entry(DataFrameLeft,font=("times new roman",12,"bold"),width=29,textvariable=self.id_var)
        txtTitle.grid(row=2,column=1)

        lblFirstName=Label(DataFrameLeft,bg="sky blue",text="First Name:",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblFirstName.grid(row=3,column=0,sticky=W)
        txtFirstName=Entry(DataFrameLeft,font=("times new roman",12,"bold"),width=29,textvariable=self.firstname_var)
        txtFirstName.grid(row=3,column=1)

        lblLastName=Label(DataFrameLeft,bg="sky blue",text="Last Name:",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblLastName.grid(row=4,column=0,sticky=W)
        txtLastName=Entry(DataFrameLeft,font=("times new roman",12,"bold"),width=29,textvariable=self.lastname_var)
        txtLastName.grid(row=4,column=1)

        lblAddress1=Label(DataFrameLeft,bg="sky blue",text="Address 1:",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblAddress1.grid(row=5,column=0,sticky=W)
        txtAddress1=Entry(DataFrameLeft,font=("times new roman",12,"bold"),width=29,textvariable=self.address1_var)
        txtAddress1.grid(row=5,column=1)

        lblAddress2=Label(DataFrameLeft,bg="sky blue",text="Address 2:",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblAddress2.grid(row=6,column=0,sticky=W)
        txtAddress2=Entry(DataFrameLeft,font=("times new roman",12,"bold"),width=29,textvariable=self.address2_var)
        txtAddress2.grid(row=6,column=1)

        lblPostCode=Label(DataFrameLeft,bg="sky blue",text="Post Code:",font=("times new roman",12,"bold"),padx=2,pady=4)
        lblPostCode.grid(row=7,column=0,sticky=W)
        txtPostCode=Entry(DataFrameLeft,font=("times new roman",12,"bold"),width=29,textvariable=self.postcode_var)
        txtPostCode.grid(row=7,column=1)

        lblMobile=Label(DataFrameLeft,bg="sky blue",text="Mobile:",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblMobile.grid(row=8,column=0,sticky=W)
        txtMobile=Entry(DataFrameLeft,font=("times new roman",12,"bold"),width=29,textvariable=self.mobile_var)
        txtMobile.grid(row=8,column=1)

        lblBookId=Label(DataFrameLeft,bg="sky blue",text="Book Id:",font=("times new roman",12,"bold"),padx=2,pady=4)
        lblBookId.grid(row=0,column=2,sticky=W)
        txtBookId=Entry(DataFrameLeft,font=("times new roman",12,"bold"),width=29,textvariable=self.bookid_var)
        txtBookId.grid(row=0,column=3)

        lblBookTitle=Label(DataFrameLeft,bg="sky blue",text="Book Title:",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblBookTitle.grid(row=1,column=2,sticky=W)
        txtBookTitle=Entry(DataFrameLeft,font=("times new roman",12,"bold"),width=29,textvariable=self.booktitle_var)
        txtBookTitle.grid(row=1,column=3)

        lblAuthor=Label(DataFrameLeft,bg="sky blue",text="Author:",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblAuthor.grid(row=2,column=2,sticky=W)
        txtAuthor=Entry(DataFrameLeft,font=("times new roman",12,"bold"),width=29,textvariable=self.auther_var)
        txtAuthor.grid(row=2,column=3)

        lblDateBorrowed=Label(DataFrameLeft,bg="sky blue",text="Date Borrowed:",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblDateBorrowed.grid(row=3,column=2,sticky=W)
        txtDateBorrowed=Entry(DataFrameLeft,font=("times new roman",12,"bold"),width=29,textvariable=self.dateborrowed_var)
        txtDateBorrowed.grid(row=3,column=3)

        lblDateDue=Label(DataFrameLeft,bg="sky blue",text="Date Due:",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblDateDue.grid(row=4,column=2,sticky=W)
        txtDateDue=Entry(DataFrameLeft,font=("times new roman",12,"bold"),width=29,textvariable=self.datedue_var)
        txtDateDue.grid(row=4,column=3)

        lblDaysOnBook=Label(DataFrameLeft,bg="sky blue",text="Days On Book:",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblDaysOnBook.grid(row=5,column=2,sticky=W)
        txtDaysOnBook=Entry(DataFrameLeft,font=("times new roman",12,"bold"),width=29,textvariable=self.daysonbook_var)
        txtDaysOnBook.grid(row=5,column=3)

        lblLateReturnFine=Label(DataFrameLeft,bg="sky blue",text="Late Return Fine:",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblLateReturnFine.grid(row=6,column=2,sticky=W)
        txtLateReturnFine=Entry(DataFrameLeft,font=("times new roman",12,"bold"),width=29,textvariable=self.lateratefine_var)
        txtLateReturnFine.grid(row=6,column=3)


        lblDateOverDate=Label(DataFrameLeft,bg="sky blue",text="Date Over Date:",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblDateOverDate.grid(row=7,column=2,sticky=W)
        txtDateOverDate=Entry(DataFrameLeft,font=("t6mes new roman",12,"bold"),width=26,textvariable=self.dateoverdue_var)
        txtDateOverDate.grid(row=7,column=3)

        lblActualPrice=Label(DataFrameLeft,bg="sky blue",text="Actual Price:",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblActualPrice.grid(row=8,column=2,sticky=W)
        txtActualPrice=Entry(DataFrameLeft,font=("times new roman",12,"bold"),width=29,textvariable=self.finallprice_var    )
        txtActualPrice.grid(row=8,column=3)
        
       #=====================================DataFrameRight========================================================================

        DataFrameRight=LabelFrame(frame,text="Books Details",bg="sky blue",fg="blue",bd=12,relief=RIDGE,font=("times new roman",12,"bold"))
        DataFrameRight.place(x=900,y=5,width=960,height=350)

        self.txtBox=Text(DataFrameRight,font=("times new roman",12,"bold"),width=32,height=16,padx=2,pady=6)
        self.txtBox.grid(row=0,column=2)

        listScrollbar=Scrollbar(DataFrameRight)
        listScrollbar.grid(row=0,column=1,sticky="ns")
        

        listBoooks=['Core Python','Java','Advanced Java','Machine Learning','Data Science','Django','C++','HTML','CSS','Javascript','PHP',
                   'Big Data','Java','Advance Python','Advanced ML','Advanced Big Data','Advanced Data Science','Advanced HTML']


        def SelectBook(event=""):
            value=str(listBox.get(listBox.curselection()))
            x=value
            if (x=="Core Python"):
                self.bookid_var.set("BKID5454")
                self.booktitle_var.set("Core Python")
                self.auther_var.set("monty joe")
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.lateratefine_var.set("RS.50")
                self.dateoverdue_var.set("NO")
                self.finallprice_var.set("RS.788")
            
            if (x=="Java"):
                self.bookid_var.set("BKID5455")
                self.booktitle_var.set("Java")
                self.auther_var.set("ranche")
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.lateratefine_var.set("RS.50")
                self.dateoverdue_var.set("NO")
                self.finallprice_var.set("RS.455")

            if (x=="Advanced Java"):
                self.bookid_var.set("BKID5456")
                self.booktitle_var.set("Advanced Java")
                self.auther_var.set("Emily Dickinson")
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.lateratefine_var.set("RS.50")
                self.dateoverdue_var.set("NO")
                self.finallprice_var.set("RS.600")

            if (x=="Machine Learning"):
                self.bookid_var.set("BKID5457")
                self.booktitle_var.set("Machine Learning")
                self.auther_var.set("H. P. Lovecraft")
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.lateratefine_var.set("RS.50")
                self.dateoverdue_var.set("NO")
                self.finallprice_var.set("RS.188")

            if (x=="Data Science"):
                self.bookid_var.set("BKID5458")
                self.booktitle_var.set("Data Science")
                self.auther_var.set("Leo Tolstoy")
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.lateratefine_var.set("RS.50")
                self.dateoverdue_var.set("NO")
                self.finallprice_var.set("RS.300")

            if (x=="Django"):
                self.bookid_var.set("BKID5459")
                self.booktitle_var.set("Django")
                self.auther_var.set("Seneca")
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.lateratefine_var.set("RS.50")
                self.dateoverdue_var.set("NO")
                self.finallprice_var.set("RS.900")
            
            if (x=="C++"):
                self.bookid_var.set("BKID5460")
                self.booktitle_var.set("C++")
                self.auther_var.set("John Donne")
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.lateratefine_var.set("RS.50")
                self.dateoverdue_var.set("NO")
                self.finallprice_var.set("RS.588")

            if (x=="HTML"):
                self.bookid_var.set("BKID5461")
                self.booktitle_var.set("HTML")
                self.auther_var.set("Sarah Williams")
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.lateratefine_var.set("RS.50")
                self.dateoverdue_var.set("NO")
                self.finallprice_var.set("RS.855")

            if (x=="CSS"):
                self.bookid_var.set("BKID5462")
                self.booktitle_var.set("CSS")
                self.auther_var.set("John Keats")
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.lateratefine_var.set("RS.50")
                self.dateoverdue_var.set("NO")
                self.finallprice_var.set("RS.456")

            if (x=="Javascript"):
                self.bookid_var.set("BKID5463")
                self.booktitle_var.set("java script")
                self.auther_var.set("Theodor Herzl")
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.lateratefine_var.set("RS.50")
                self.dateoverdue_var.set("NO")
                self.finallprice_var.set("RS.1000")

            if (x=="PHP"):
                self.bookid_var.set("BKID5464")
                self.booktitle_var.set("PHP")
                self.auther_var.set("Ernest Hemingway")
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.lateratefine_var.set("RS.50")
                self.dateoverdue_var.set("NO")
                self.finallprice_var.set("RS.500")
            
            if (x=="Big Data"):
                self.bookid_var.set("BKID5465")
                self.booktitle_var.set("Big Data")
                self.auther_var.set("Anton Chekhov")
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.lateratefine_var.set("RS.50")
                self.dateoverdue_var.set("NO")
                self.finallprice_var.set("RS.456")

            if (x=="Java"):
                self.bookid_var.set("BKID5466")
                self.booktitle_var.set("Java")
                self.auther_var.set("Jacob De Haas")
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.lateratefine_var.set("RS.50")
                self.dateoverdue_var.set("NO")
                self.finallprice_var.set("RS.800")

            if (x=="Advance Python"):
                self.bookid_var.set("BKID5467")
                self.booktitle_var.set("Advanced python")
                self.auther_var.set("Anton Chekhov")
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.lateratefine_var.set("RS.50")
                self.dateoverdue_var.set("NO")
                self.finallprice_var.set("RS.980")

            if (x=="Advanced ML"):
                self.bookid_var.set("BKID5468")
                self.booktitle_var.set("Advance ML")
                self.auther_var.set("Jack London")
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.lateratefine_var.set("RS.50")
                self.dateoverdue_var.set("NO")
                self.finallprice_var.set("RS.450")

            if (x=="Advanced Big Data"):
                self.bookid_var.set("BKID5469")
                self.booktitle_var.set("Advanced Big Data")
                self.auther_var.set("Abraham Lincoln")
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.lateratefine_var.set("RS.50")
                self.dateoverdue_var.set("NO")
                self.finallprice_var.set("RS.680")
            
            if (x=="Advanced Data Science"):
                self.bookid_var.set("BKID5470")
                self.booktitle_var.set("Advanced Data Science")
                self.auther_var.set("O. Henry")
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.lateratefine_var.set("RS.50")
                self.dateoverdue_var.set("NO")
                self.finallprice_var.set("RS.600")

            if (x=="Advanced HTML"):
                self.bookid_var.set("BKID5471")
                self.booktitle_var.set("Advanced HTML")
                self.auther_var.set("Franz Kafka")
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.lateratefine_var.set("RS.50")
                self.dateoverdue_var.set("NO")
                self.finallprice_var.set("RS.700")




        listBox=Listbox(DataFrameRight,font=("times new roman",12,"bold"),width=40,height=15)
        listBox.bind("<<ListboxSelect>>",SelectBook)
        listBox.grid(row=0,column=0,padx=4)
        listScrollbar.config(command=listBox.yview)

        for item in listBoooks:
            listBox.insert(END,item)
        

       # =============================================BUTTON FRAME=================================================================
        Framebutton=Frame(self.root,bd=12,relief=RIDGE,padx=300,pady=10,bg="sky blue")
        Framebutton.place(x=0,y=530,width=1920,height=100)

        btnAddData=Button(Framebutton,command=self.adda_data,text="ADD DATA",font=("times new roman",12,"bold"),width=23,bg="red",fg="white")
        btnAddData.grid(row=0,column=0)

        btnAddData=Button(Framebutton,command=self.showData,text="SHOW DATA",font=("times new roman",12,"bold"),width=23,bg="yellow",fg="black")
        btnAddData.grid(row=0,column=1)

        btnAddData=Button(Framebutton,command=self.update,text="UPDATE",font=("times new roman",12,"bold"),width=23,bg="purple",fg="white")
        btnAddData.grid(row=0,column=2)

        btnAddData=Button(Framebutton,command=self.delete,text="DELETE",font=("times new roman",12,"bold"),width=23,bg="orange",fg="white")
        btnAddData.grid(row=0,column=3)

        btnAddData=Button(Framebutton,command=self.reset,text="RESET",font=("times new roman",12,"bold"),width=23,bg="pink",fg="black")
        btnAddData.grid(row=0,column=4)

        btnAddData=Button(Framebutton,command=self.iExit,text="EXIT",font=("times new roman",12,"bold"),width=23,bg="blue",fg="white")
        btnAddData.grid(row=0,column=5)

        # =============================================INFORMATION FRAME===========================================================
        FrameDetails=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="sky blue")
        FrameDetails.place(x=0,y=600,width=1920,height=420)

        Table_frame=Frame(FrameDetails,bd=6,relief=RIDGE,bg="sky blue")
        Table_frame.place(x=45,y=8,width=1760,height=380)

        xscroll=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        yscroll=ttk.Scrollbar(Table_frame,orient=VERTICAL)

        self.library_table=ttk.Treeview(Table_frame,column=("membertype","prnno","title","firstname","lastname","address1","address2","postid",
                                                            "mobile","bookid","booktitle","author","dateborrowed","datedue",
                                                            "days","latereturnfine","dateoverdue","finalprice"),
                                                            xscrollcommand=xscroll.set,yscrollcommand=yscroll.set)

        xscroll.pack(side=BOTTOM,fill=X)
        yscroll.pack(side=RIGHT,fill=Y)

        xscroll.config(command=self.library_table.xview)
        yscroll.config(command=self.library_table.yview)

        self.library_table.heading("membertype",text="Member Type")
        self.library_table.heading("prnno",text="PRN No.")
        self.library_table.heading("title",text="Title")
        self.library_table.heading("firstname",text="First Name")
        self.library_table.heading("lastname",text="Last Name")
        self.library_table.heading("address1",text="Address1")
        self.library_table.heading("address2",text="Address2")
        self.library_table.heading("postid",text="Post ID")
        self.library_table.heading("mobile",text="Mobile Number")
        self.library_table.heading("bookid",text="Book ID")
        self.library_table.heading("booktitle",text="Book Title")
        self.library_table.heading("author",text="Author")
        self.library_table.heading("dateborrowed",text="Date of Borrowed")
        self.library_table.heading("datedue",text="Date Due")
        self.library_table.heading("days",text="Days on Book")
        self.library_table.heading("latereturnfine",text="Late return Fine")
        self.library_table.heading("dateoverdue",text="Date over Due")
        self.library_table.heading("finalprice",text="Final Price")

        
        self.library_table["show"]="headings"
        self.library_table.pack(fill=BOTH,expand=1)

        self.library_table.column("membertype",width=100)
        self.library_table.column("prnno",width=100)
        self.library_table.column("title",width=100)
        self.library_table.column("firstname",width=100)
        self.library_table.column("lastname",width=100)
        self.library_table.column("address1",width=100)
        self.library_table.column("address2",width=100)
        self.library_table.column("postid",width=100)
        self.library_table.column("mobile",width=100)
        self.library_table.column("bookid",width=100)
        self.library_table.column("booktitle",width=100)
        self.library_table.column("author",width=100)
        self.library_table.column("dateborrowed",width=100)
        self.library_table.column("datedue",width=100)
        self.library_table.column("days",width=100)
        self.library_table.column("latereturnfine",width=100)
        self.library_table.column("dateoverdue",width=100)
        self.library_table.column("finalprice",width=100)
         
        self.fatch_data()
        self.library_table.bind("<ButtonRelease-1>",self.get_cursor)

    def adda_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="password",database="mydata")
        my_cursor=conn.cursor()
        my_cursor.execute("insert into library values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                                self.member_var.get(),
                                                                                                                self.prn_var.get(),
                                                                                                                self.id_var.get(),
                                                                                                                self.firstname_var.get(),
                                                                                                                self.lastname_var.get(),
                                                                                                                self.address1_var.get(),
                                                                                                                self.address2_var.get(),
                                                                                                                self.postcode_var.get(),
                                                                                                                self.mobile_var.get(),
                                                                                                                self.bookid_var.get(),
                                                                                                                self.booktitle_var.get(),
                                                                                                                self.auther_var.get(),
                                                                                                                self.dateborrowed_var.get(),
                                                                                                                self.datedue_var.get(),
                                                                                                                self.daysonbook_var.get(),
                                                                                                                self.lateratefine_var.get(),
                                                                                                                self.dateoverdue_var.get(),
                                                                                                                self.finallprice_var.get()
                                                                                                                ))
        conn.commit()
        self.fatch_data()
        conn.close()

        messagebox.showinfo("Success","Member has been inserted successfully")


    def update(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="password",database="mydata")
        my_cursor=conn.cursor()
        my_cursor.execute("update library set Member=%s,ID=%s,FisrtName=%s,LastName=%s,Address1=%s,Address2=%s,PosdId=%s,Mobile=%s,Bookid=%s,BookTitle=%s,Auther=%s,Databorrowed=%s,datedue=%s,dayasofbook=%s,latereturnfine=%s,dateoverdue=%s,finalprice=%s where PRN_NO=%s",(
                                                        self.member_var.get(),
                                                        self.id_var.get(),
                                                        self.firstname_var.get(),
                                                        self.lastname_var.get(),
                                                        self.address1_var.get(),
                                                        self.address2_var.get(),
                                                        self.postcode_var.get(),
                                                        self.mobile_var.get(),
                                                        self.bookid_var.get(),
                                                        self.booktitle_var.get(),
                                                        self.auther_var.get(),
                                                        self.dateborrowed_var.get(),
                                                        self.datedue_var.get(),
                                                        self.daysonbook_var.get(),
                                                        self.lateratefine_var.get(),
                                                        self.dateoverdue_var.get(),
                                                        self.finallprice_var.get(),
                                                        self.prn_var.get(),
                                                        ))
        conn.commit()
        self.fatch_data()
        self.reset()
        conn.close()

        messagebox.showinfo("Success","member has been updated")

    
    def fatch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="password",database="mydata")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from library")
        rows=my_cursor.fetchall()

        if len(rows)!=0:
            self.library_table.delete(*self.library_table.get_children())
            for i in rows:
                self.library_table.insert("",END,values=i)
            conn.commit()
        conn.close()


    def get_cursor(self,event=""):
        cursor_row=self.library_table.focus()
        content=self.library_table.item(cursor_row)
        row=content['values']

        self.member_var.set(row[0])
        self.prn_var.set(row[1]),
        self.id_var.set(row[2]),
        self.firstname_var.set(row[3]),
        self.lastname_var.set(row[4]),
        self.address1_var.set(row[5]),
        self.address2_var.set(row[6]),
        self.postcode_var.set(row[7]),
        self.mobile_var.set(row[8]),
        self.bookid_var.set(row[9]),
        self.booktitle_var.set(row[10]),
        self.auther_var.set(row[11]),
        self.dateborrowed_var.set(row[12]),
        self.datedue_var.set(row[13]),
        self.daysonbook_var.set(row[14]),
        self.lateratefine_var.set(row[15]),
        self.dateoverdue_var.set(row[16]),
        self.finallprice_var.set(row[17])

    def showData(self):
        self.txtBox.insert(END,"Member Type:\t\t"+ self.member_var.get() + "\n")
        self.txtBox.insert(END,"PRN NO:\t\t"+ self.prn_var.get() + "\n")
        self.txtBox.insert(END,"ID No\t\t"+ self.id_var.get() + "\n")
        self.txtBox.insert(END,"FirstName:\t\t"+ self.firstname_var.get() + "\n")
        self.txtBox.insert(END,"LastName:\t\t"+ self.lastname_var.get() + "\n")
        self.txtBox.insert(END,"Address1:\t\t"+ self.address1_var.get() + "\n")
        self.txtBox.insert(END,"Address2:\t\t"+ self.address2_var.get() + "\n")
        self.txtBox.insert(END,"Post Code:\t\t"+ self.postcode_var.get() + "\n")
        self.txtBox.insert(END,"Mobile No:\t\t"+ self.mobile_var.get() + "\n")
        self.txtBox.insert(END,"Book ID:\t\t"+ self.bookid_var.get() + "\n")
        self.txtBox.insert(END,"Book Title:\t\t"+ self.booktitle_var.get() + "\n")
        self.txtBox.insert(END,"Auther:\t\t"+ self.auther_var.get() + "\n")
        self.txtBox.insert(END,"DateBorrowed\t\t"+ self.dateborrowed_var.get() + "\n")
        self.txtBox.insert(END,"DateDue:\t\t"+ self.datedue_var.get() + "\n")
        self.txtBox.insert(END,"DaysOnBook:\t\t"+ self.daysonbook_var.get() + "\n")
        self.txtBox.insert(END,"LateRateFine:\t\t"+ self.lateratefine_var.get() + "\n")
        self.txtBox.insert(END,"DateOverDue:\t\t"+ self.dateoverdue_var.get() + "\n")
        self.txtBox.insert(END,"FinallPrice:\t\t"+ self.finallprice_var.get() + "\n")
        self.txtBox.insert(END,"============================\t\t"+ "\n")
        

    def reset(self):
        self.member_var.set(""),
        self.prn_var.set(""),
        self.id_var.set(""),
        self.firstname_var.set(""),
        self.lastname_var.set(""),
        self.address1_var.set(""),
        self.address2_var.set(""),
        self.postcode_var.set(""),
        self.mobile_var.set(""),
        self.bookid_var.set(""),
        self.booktitle_var.set(""),
        self.auther_var.set(""),
        self.dateborrowed_var.set(""),
        self.datedue_var.set(""),
        self.daysonbook_var.set(""),
        self.lateratefine_var.set(""),
        self.dateoverdue_var.set(""),
        self.finallprice_var.set("")
        self.txtBox.delete("1.0",END)

    def iExit(self):
        iExit=tkinter.messagebox.askyesno("Library managment sysytem","do you want to exit")
        if iExit>0:
            self.root.destroy()
            return()

    
    def delete(self):
        if self.prn_var.get()=="" or self.id_var.get()=="":
            messagebox.showerror("Error","First select the member")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="password",database="mydata")
            my_cursor=conn.cursor()
            query="delete from library where PRN_NO=%s"
            value=(self.prn_var.get(),)
            my_cursor.execute(query,value)

            conn.commit()
            self.fatch_data()
            self.reset()
            conn.close()

            messagebox.showinfo("Success","Member has been deleted")




if __name__ == "__main__":
    root=Tk()
    obj=LibraryManagementSystem(root)
    root.mainloop()
    
    