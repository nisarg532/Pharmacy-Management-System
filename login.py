from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import datetime
from time import strftime

def main():
    win=Tk()
    app=Login_Window(win)
    win.mainloop()



class Login_Window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")

        self.var_pass=StringVar()
        self.var_email=StringVar()
       
        
        self.bg=ImageTk.PhotoImage(file=r"../Images/bgimage.jpg")
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        frame=Frame(self.root,bg="black")
        frame.place(x=610,y=170,width=340,height=450)   

        img1=Image.open("../Images/LoginIconAppl.png")     
        img1=img1.resize((100,100),Image.LANCZOS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lblimg1=Label(image=self.photoimage1,bg="black",borderwidth=0)
        lblimg1.place(x=730,y=175,width=100,height=100)

        get_str=Label(frame,text="Get Started",font=("times new roman",20,"bold"),fg="white",bg="black")
        get_str.place(x=95,y=100)

        #Labels
        username_lbl=Label(frame,text="Username",font=("times new roman",15,"bold"),fg="white",bg="black")
        username_lbl.place(x=70,y=155)

        self.txtuser=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtuser.place(x=40,y=180,width=270)

        password_lbl=Label(frame,text="Password",font=("times new roman",15,"bold"),fg="white",bg="black")
        password_lbl.place(x=70,y=225)

        self.txtpass=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtpass.place(x=40,y=250,width=270)

        #icons
        img2=Image.open("../Images/LoginIconAppl.png")     
        img2=img2.resize((25,25),Image.LANCZOS)
        self.photoimage2=ImageTk.PhotoImage(img2)
        lblimg1=Label(image=self.photoimage2,bg="black",borderwidth=0)
        lblimg1.place(x=650,y=323,width=25,height=25)

        img3=Image.open("../Images/lock-512.png")     
        img3=img3.resize((25,25),Image.LANCZOS)
        self.photoimage3=ImageTk.PhotoImage(img3)
        lblimg1=Label(image=self.photoimage3,bg="black",borderwidth=0)
        lblimg1.place(x=650,y=393,width=25,height=25)

        #Login Buttton
        loginbtn=Button(frame,text="Login",command=self.login,cursor="hand2",font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="red",activeforeground="white",activebackground="red")
        loginbtn.place(x=110,y=300,width=120,height=35)

        #Register Button
        registerbtn=Button(frame,command=self.register_window,text="New User Register",font=("times new roman",10,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        registerbtn.place(x=15,y=350,width=160)

        #Forget Pass Button
        forgotpassbtn=Button(frame,command=self.forgot_password_window,text="Forgot Password",font=("times new roman",10,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        forgotpassbtn.place(x=10,y=370,width=160)
    
    
    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)


    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror=("Error","All Field Required")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="root",database="my_data")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from register where email=%s and password=%s",(
                self.txtuser.get(),
                self.txtpass.get()
            ))
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid Username & Password")
            else:
                open_main=messagebox.askyesno("Choose option","Access only admin")
                if open_main>0:
                    messagebox.showinfo("Success","Login Successful")
                    self.new_window=Toplevel(self.root)
                    self.app=PharmacyManagementSystem(self.new_window)
                    self.root.withdraw()

                    self.new_window.protocol("WM_DELETE_WINDOW", self.on_pharmacy_close)

                else:
                    if not open_main:
                        return
            conn.commit()
            conn.close()

    def on_pharmacy_close(self):
        self.new_window.destroy()  # Close the pharmacy window
        self.root.deiconify()  # Show the login window again

    def forgot_password_window(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Please Enter Email Address to reset password")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="root",database="my_data")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.txtuser.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            #print(row)
            if row==None:
                messagebox.showerror("Error","Email Not Registered")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forgot Password")
                self.root2.geometry("340x450+610+170")

                l=Label(self.root2,text="Forgot Password",font=("times new roman",15,"bold"),fg="red",bg="white")                
                l.place(x=0,y=10,relwidth=1)

                securityq_lbl=Label(self.root2,text="Security Question",font=("times new roman",15,"bold"),bg="white")
                securityq_lbl.place(x=50,y=80)

                self.combo_security_Q=ttk.Combobox(self.root2,font=("times new roman",15,"bold"),state="readonly")
                self.combo_security_Q["values"]=("Select","Your Birth Place","Your Partner Name","Your Pet Name")
                self.combo_security_Q.place(x=50,y=110,width=250)
                self.combo_security_Q.current(0)

                securitya_lbl=Label(self.root2,text="Security Answer",font=("times new roman",15,"bold"),bg="white")
                securitya_lbl.place(x=50,y=150)
        
                self.securitya_lbl=ttk.Entry(self.root2,font=("times new roman",15,"bold"))
                self.securitya_lbl.place(x=50,y=180,width=250)

        #row4
                new_password=Label(self.root2,text="New Password",font=("times new roman",15,"bold"),bg="white",fg="black")
                new_password.place(x=50,y=220)

                self.txt_newpass=ttk.Entry(self.root2,font=("times new roman",15,"bold"))
                self.txt_newpass.place(x=50,y=250,width=250)

                btn=Button(self.root2,text="Reset",command=self.reset_pass,font=("times new roman",15,"bold"),fg="white",bg="green")
                btn.place(x=100, y=290)

    def reset_pass(self):
        if self.combo_security_Q.get()=="Select":
            messagebox.showerror("Error","Select the Security Question Answer",parent=self.root2)
        elif self.securitya_lbl.get()=="":
            messagebox.showerror("Error","Please enter the answer",parent=self.root2)
        elif self.txt_newpass.get()=="":
            messagebox.showerror("Error","Please enter the new password",parent=self.root2)

        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="root",database="my_data")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s and securityQ=%s and securityA=%s")
            value=(self.txtuser.get(),self.combo_security_Q.get(),self.securitya_lbl.get())
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Please enter correct Answer",parent=self.root2)    
            else:
                query=("update register set password=%s where email=%s")
                value=(self.txt_newpass.get(),self.txtuser.get())
                my_cursor.execute(query,value)
                conn.commit()
                conn.close()
                messagebox.showinfo("Success","Password Change Successfully, Login now",parent=self.root2)
                self.root2.destroy()
    

class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1550x800+0+0")

        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_pass=StringVar()
        self.var_cpass=StringVar()
        self.var_check=IntVar()


        #main bg image
        self.bg=ImageTk.PhotoImage(file=r"../Images/bgimage.jpg")
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        #sub Bg image
        self.bg1=ImageTk.PhotoImage(file=r"../Images/dog_bg.jpeg")
        left_lbl_bg=Label(self.root,image=self.bg1)
        left_lbl_bg.place(x=50,y=100,width=470,height=550)

        #main frame
        frame=Frame(self.root,bg="white")
        frame.place(x=520,y=100,width=800,height=550)   

        register_lbl=Label(frame,text="Register Here",font=("times new roman",20,"bold"),fg="dark green",bg="white")
        register_lbl.place(x=20,y=20)

        #Labels and entry Field
        #row1
        fname_lbl=Label(frame,text="First Name",font=("times new roman",15,"bold"),bg="white")
        fname_lbl.place(x=50,y=100)
        
        fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15,"bold"))
        fname_entry.place(x=50,y=130,width=250)

        lname_lbl=Label(frame,text="Last Name",font=("times new roman",15,"bold"),bg="white")
        lname_lbl.place(x=370,y=100)
        
        lname_entry=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",15,"bold"))
        lname_entry.place(x=370,y=130,width=250)

        #row2
        contact_lbl=Label(frame,text="Contact No",font=("times new roman",15,"bold"),bg="white")
        contact_lbl.place(x=50,y=170)
        
        self.txtcontact=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",15,"bold"))
        self.txtcontact.place(x=50,y=200,width=250)

        email_lbl=Label(frame,text="Email",font=("times new roman",15,"bold"),bg="white")
        email_lbl.place(x=370,y=170)
        
        self.txtemail=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",15,"bold"))
        self.txtemail.place(x=370,y=200,width=250)

        #row3
        securityq_lbl=Label(frame,text="Security Question",font=("times new roman",15,"bold"),bg="white")
        securityq_lbl.place(x=50,y=240)
        
        self.combo_security_Q=ttk.Combobox(frame,textvariable=self.var_securityQ,font=("times new roman",15,"bold"),state="readonly")
        self.combo_security_Q["values"]=("Select","Your Birth Place","Your Partner Name","Your Pet Name")
        self.combo_security_Q.place(x=50,y=270,width=250)
        self.combo_security_Q.current(0)

        securitya_lbl=Label(frame,text="Security Answer",font=("times new roman",15,"bold"),bg="white")
        securitya_lbl.place(x=370,y=240)
        
        self.securitya_lbl=ttk.Entry(frame,textvariable=self.var_securityA,font=("times new roman",15,"bold"))
        self.securitya_lbl.place(x=370,y=270,width=250)

        #row4
        password_lbl=Label(frame,text="Password",font=("times new roman",15,"bold"),bg="white",fg="black")
        password_lbl.place(x=50,y=310)

        self.txtpass=ttk.Entry(frame,textvariable=self.var_pass,font=("times new roman",15,"bold"))
        self.txtpass.place(x=50,y=340,width=250)

        cpassword_lbl=Label(frame,text="Confirm Password",font=("times new roman",15,"bold"),bg="white",fg="black")
        cpassword_lbl.place(x=370,y=310)

        self.txtcpass=ttk.Entry(frame,textvariable=self.var_cpass,font=("times new roman",15,"bold"))
        self.txtcpass.place(x=370,y=340,width=250)

        #checkbox
        checkbtn=Checkbutton(frame,variable=self.var_check,text="I Agree to the Terms & Conditions",font=("times new roman",12,"bold"),onvalue=1,offvalue=0)
        checkbtn.place(x=50,y=380)

        #buttons
        img=Image.open("../Images/register-now-button1.jpg")
        img=img.resize((200,50),Image.LANCZOS)
        self.photoimage=ImageTk.PhotoImage(img)
        b1=Button(frame,image=self.photoimage,command=self.register_data,borderwidth=0,cursor="hand2")
        b1.place(x=10,y=420,width=200)

        img1=Image.open("../Images/loginpng.png")
        img1=img1.resize((200,50),Image.LANCZOS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        b1=Button(frame,image=self.photoimage1,command=self.return_login,borderwidth=0,cursor="hand2")
        b1.place(x=330,y=420,width=200)

    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="Select":
            messagebox.showerror("Error","All fields are required")
        elif self.var_pass.get()!=self.var_cpass.get() or self.var_pass.get()=="":
            messagebox.showerror("Error","Password & Confirm Password does not match")
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please Agree to Terms & Conditions")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="root",database="my_data")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","User already exist,please try another email")
            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                    self.var_fname.get(),
                    self.var_lname.get(),
                    self.var_contact.get(),
                    self.var_email.get(),
                    self.var_securityQ.get(),
                    self.var_securityA.get(),
                    self.var_pass.get()
                ))    
            conn.commit()
            conn.close()
            messagebox.showinfo("Success","Register Successful")
    
    
    def return_login(self):
        self.root.destroy()
    
class PharmacyManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Pharmacy Management System")
        self.root.geometry("1550x800+0+0")

        # ===============================varibles Declaration==========================================================
        self.ref_var=StringVar()
        self.cmpName_var=StringVar()
        self.typeMed_var=StringVar()
        self.medName_var=StringVar()
        self.lot_var=StringVar()
        self.issuedate_var=StringVar()
        self.expdate_var=StringVar()
        self.uses_var=StringVar()
        self.sideEffect_var=StringVar()
        self.warning_var=StringVar()
        self.dosage_var=StringVar()
        self.price_var=StringVar()
        self.product_var=StringVar()

        # ========== Title label======================================================================================
        lbltitle=Label(self.root,text="PHARMACY MANAGEMENT SYSTEM",bg="white",fg="darkgreen",bd=15,relief=RIDGE,font=("times new roman",50,"bold"),padx=2,pady=6)
        lbltitle.pack(side=TOP,fill=X)


        img3 = Image.open("logos.jpg")
        img3 = img3.resize((80,80), Image.LANCZOS)
        self.photoImg3 =  ImageTk.PhotoImage(img3)
        b3 =Button(self.root,image=self.photoImg3,text="CodeWithKiran",borderwidth=0,font=("times new roman",22,"bold"),fg="white",cursor="hand2")
        b3.place(x=70,y=20)


        # ======leftrightDataframe======================================================================================
        DataFrame=Frame(self.root,bd=15,padx=20,relief=RIDGE)
        DataFrame.place(x=0,y=120,width=1530,height=400)
        
        DataFrameLeft=LabelFrame(DataFrame,bd=10,padx=20,relief=RIDGE,fg="darkgreen",
                                                font=("arial",12,"bold"),text="Medicine Information")
        DataFrameLeft.place(x=0,y=5,width=900,height=350)

        lblReg=Label(DataFrameLeft,width=37,font=("arial",15,"bold"),text="Stay Home Stay Safe",fg="red",padx=2,bg="white")
        lblReg.place(x=410,y=140)

        # =======images=======================================================

        img1 = Image.open("lab.jpg")
        img1 = img1.resize((150,135), Image.LANCZOS)
        self.photoImg1 =  ImageTk.PhotoImage(img1)
        b4 =Button(self.root,image=self.photoImg1,text="CodeWithKiran",borderwidth=0,font=("times new roman",22,"bold"),fg="white",cursor="hand2")
        b4.place(x=770,y=330)

        img2 = Image.open("eng.jpg")
        img2 = img2.resize((150,135), Image.LANCZOS)
        self.photoImg2 =  ImageTk.PhotoImage(img2)
        b4 =Button(self.root,image=self.photoImg2,text="CodeWithKiran",borderwidth=0,font=("times new roman",22,"bold"),fg="white",cursor="hand2")
        b4.place(x=620,y=330)

        img4 = Image.open("tab.jpg")
        img4 = img4.resize((150,135), Image.LANCZOS)
        self.photoImg4 =  ImageTk.PhotoImage(img4)
        b5 =Button(self.root,image=self.photoImg4,text="CodeWithKiran",borderwidth=0,font=("times new roman",22,"bold"),fg="white",cursor="hand2")
        b5.place(x=475,y=330)
        # ===========Buttonframe=================================================================================
        ButtonFrame=Frame(self.root,bd=15,padx=20,relief=RIDGE)
        ButtonFrame.place(x=0,y=520,width=1530,height=65)

        # ========MainButtons=======
        btnAddData=Button(ButtonFrame,command=self.add_data,text="ADD MEDICINE",font=("arial",13,"bold"),width=14,bg="darkgreen",fg="white")
        btnAddData.grid(row=0,column=0)

        btnUpdateMed=Button(ButtonFrame,command=self.update_data,text="UPDATE",font=("arial",13,"bold"),width=14,bg="darkgreen",fg="white")
        btnUpdateMed.grid(row=0,column=1)

        btnDeleteMed=Button(ButtonFrame,command=self.mDelete,text="DELETE",font=("arial",13,"bold"),width=14,bg="red",fg="white")
        btnDeleteMed.grid(row=0,column=2)

        btnRestMed=Button(ButtonFrame,command=self.Reset,text="RESET",font=("arial",13,"bold"),width=14,bg="darkgreen",fg="white")
        btnRestMed.grid(row=0,column=3)

        btnExitMed=Button(ButtonFrame,command=self.iExit,text="EXIT",font=("arial",13,"bold"),width=14,bg="darkgreen",fg="white")
        btnExitMed.grid(row=0,column=4)

        # ==========Search By========
        lblSearch=Label(ButtonFrame,font=("arial",17,"bold"),text="Search By",padx=2,bg="red",fg="white")
        lblSearch.grid(row=0,column=5,sticky=W)

        # variable
        self.serch_var=StringVar()
        search_combo=ttk.Combobox(ButtonFrame,textvariable=self.serch_var,width=12,font=("times new roman",17),state="readonly")
        search_combo['values']=("Select Option","Ref","medname","lot")
        search_combo.grid(row=0,column=6,sticky=W)
        search_combo.current(0)

        self.serchTxt_var=StringVar()
        txtSearch=Entry(ButtonFrame,textvariable=self.serchTxt_var,bd=3,relief=RIDGE,width=12,font=("times new roman",17))
        txtSearch.grid(row=0,column=7)


        btnExit=Button(ButtonFrame,command=self.search_data,text="SEARCH",font=("arial",12,"bold"),width=14,bg="darkgreen",fg="white")
        btnExit.grid(row=0,column=8)

        btnExit=Button(ButtonFrame,command=self.fatch_data,text="SHOW ALL",font=("arial",12,"bold"),width=13,bg="darkgreen",fg="white")
        btnExit.grid(row=0,column=9)

        # ===================Details Frame===================================================================================
        # ===================Main Labels And enty=========================================================================
        FrameDetails=Frame(self.root,bd=15,padx=20,relief=RIDGE)
        FrameDetails.place(x=0,y=590,width=1530,height=210)

        conn=mysql.connector.connect(host="localhost",user="root",password="root",database="my_data")
        my_cursor=conn.cursor()
        my_cursor.execute("select ref from medicine")
        r=my_cursor.fetchall()

        lblrefno=Label(DataFrameLeft,font=("arial",12,"bold"),text="Reference No",padx=2,pady=6)
        lblrefno.grid(row=0,column=0,sticky=W)

        comrefno=ttk.Combobox(DataFrameLeft,textvariable=self.ref_var,state="readonly",
                                                        font=("arial",12,"bold"),width=27)
        comrefno['value']=r
        comrefno.current(0)
        comrefno.grid(row=0,column=1)

        lblCmpName=Label(DataFrameLeft,font=("arial",12,"bold"),text="Company Name:",padx=2,pady=6)
        lblCmpName.grid(row=1,column=0,sticky=W)
        txtCmpName=Entry(DataFrameLeft,textvariable=self.cmpName_var,font=("arial",13,"bold"),bg="white",bd=2,relief=RIDGE,width=29)
        txtCmpName.grid(row=1,column=1)

        lblTypeofMedicine=Label(DataFrameLeft,font=("arial",12,"bold"),text="Type Of Medicine",padx=2,pady=6)
        lblTypeofMedicine.grid(row=2,column=0,sticky=W)

        comTypeofMedicine=ttk.Combobox(DataFrameLeft,textvariable=self.typeMed_var,state="readonly",
                                                        font=("arial",12,"bold"),width=27)
        comTypeofMedicine['value']=("Tablet","Liquid","Capsules","Topical Medicines","Drops","Inhales","Injection")
        comTypeofMedicine.current(0)
        comTypeofMedicine.grid(row=2,column=1)

        # ==========AddMedicine============
        conn=mysql.connector.connect(host="localhost",user="root",password="root",database="my_data")
        my_cursor=conn.cursor()
        my_cursor.execute("select MedicineName from medicine")
        ide=my_cursor.fetchall()
        # self.fetch_Medicine_data()
        
        lblMedicineName=Label(DataFrameLeft,font=("arial",12,"bold"),text="Medicine Name",padx=2,pady=6)
        lblMedicineName.grid(row=3,column=0,sticky=W)

        comMedicineName=ttk.Combobox(DataFrameLeft,textvariable=self.medName_var,state="readonly",
                                                        font=("arial",12,"bold"),width=27)
        comMedicineName['value']=ide
        comMedicineName.current(0)
        comMedicineName.grid(row=3,column=1)


        lblLotNo=Label(DataFrameLeft,font=("arial",12,"bold"),text="Lot No:",padx=2,pady=6)
        lblLotNo.grid(row=4,column=0,sticky=W)
        txtLotNo=Entry(DataFrameLeft,textvariable=self.lot_var,font=("arial",13,"bold"),bg="white",bd=2,relief=RIDGE,width=29)
        txtLotNo.grid(row=4,column=1)

        lblIssueDate=Label(DataFrameLeft,font=("arial",12,"bold"),text="Issue Date:",padx=2,pady=6)
        lblIssueDate.grid(row=5,column=0,sticky=W)
        txtIssueDate=Entry(DataFrameLeft,textvariable=self.issuedate_var,font=("arial",13,"bold"),bg="white",bd=2,relief=RIDGE,width=29)
        txtIssueDate.grid(row=5,column=1)

        lblExDate=Label(DataFrameLeft,font=("arial",12,"bold"),text="Exp Date:",padx=2,pady=6)
        lblExDate.grid(row=6,column=0,sticky=W)
        txtExDate=Entry(DataFrameLeft,textvariable=self.expdate_var,font=("arial",13,"bold"),bg="white",bd=2,relief=RIDGE,width=29)
        txtExDate.grid(row=6,column=1)

        lblUses=Label(DataFrameLeft,font=("arial",12,"bold"),text="Uses:",padx=2,pady=4)
        lblUses.grid(row=7,column=0,sticky=W)
        txtUses=Entry(DataFrameLeft,textvariable=self.uses_var,font=("arial",13,"bold"),bg="white",bd=2,relief=RIDGE,width=29)
        txtUses.grid(row=7,column=1)

        lblSideEffect=Label(DataFrameLeft,font=("arial",12,"bold"),text="Side Effect:",padx=2,pady=6)
        lblSideEffect.grid(row=8,column=0,sticky=W)
        txtSideEffect=Entry(DataFrameLeft,textvariable=self.sideEffect_var,font=("arial",13,"bold"),bg="white",bd=2,relief=RIDGE,width=29)
        txtSideEffect.grid(row=8,column=1)

        lblPrecWarning=Label(DataFrameLeft,font=("arial",12,"bold"),text="Prec&Warning:",padx=15)
        lblPrecWarning.grid(row=0,column=2,sticky=W)
        txtPrecWarning=Entry(DataFrameLeft,textvariable=self.warning_var,font=("arial",12,"bold"),bg="white",bd=2,relief=RIDGE,width=29)
        txtPrecWarning.grid(row=0,column=3)

        lblDosage=Label(DataFrameLeft,font=("arial",12,"bold"),text="Dosage:",padx=15,pady=6)
        lblDosage.grid(row=1,column=2,sticky=W)
        txtDosage=Entry(DataFrameLeft,textvariable=self.dosage_var,font=("arial",12,"bold"),bg="white",bd=2,relief=RIDGE,width=29)
        txtDosage.grid(row=1,column=3)

        lblPrice=Label(DataFrameLeft,font=("arial",12,"bold"),text="Tablets Price:",padx=15,pady=6)
        lblPrice.grid(row=2,column=2,sticky=W)
        txtPrice=Entry(DataFrameLeft,textvariable=self.price_var,font=("arial",12,"bold"),bg="white",bd=2,relief=RIDGE,width=29)
        txtPrice.grid(row=2,column=3)

        lblProductQt=Label(DataFrameLeft,font=("arial",12,"bold"),text="Product QT:",padx=15,pady=6)
        lblProductQt.grid(row=3,column=2,sticky=W)
        txtProductQt=Entry(DataFrameLeft,textvariable=self.product_var,font=("arial",12,"bold"),bg="white",bd=2,relief=RIDGE,width=29)
        txtProductQt.grid(row=3,column=3,sticky=W)


# ===============================Right Department Management labelframe =============================================================

        DataFrameRight=LabelFrame(DataFrame,bd=12,padx=20,relief=RIDGE,fg="darkgreen",
                                            font=("arial",12,"bold"),text="New Medicine Add Department")
        DataFrameRight.place(x=910,y=5,width=540,height=350)

        # =====Inside label and entry ================================================
        # ============variables medicine=============

        img5 = Image.open("tablet.jpg")
        img5 = img5.resize((200,75), Image.LANCZOS)
        self.photoImg5 =  ImageTk.PhotoImage(img5)
        b6 =Button(self.root,image=self.photoImg5,text="CodeWithKiran",borderwidth=0,font=("times new roman",22,"bold"),fg="white",cursor="hand2")
        b6.place(x=960,y=160)

        img6 = Image.open("tablet.jpg")
        img6 = img6.resize((200,75), Image.LANCZOS)
        self.photoImg6 =  ImageTk.PhotoImage(img6)
        b6 =Button(self.root,image=self.photoImg6,text="CodeWithKiran",borderwidth=0,font=("times new roman",22,"bold"),fg="white",cursor="hand2")
        b6.place(x=1160,y=160)

        
        img7 = Image.open("tab.jpg")
        img7 = img7.resize((200,145), Image.LANCZOS)
        self.photoImg7 =  ImageTk.PhotoImage(img7)
        b6 =Button(self.root,image=self.photoImg7,text="CodeWithKiran",borderwidth=0,font=("times new roman",22,"bold"),fg="white",cursor="hand2")
        b6.place(x=1270,y=160)

        l_ref=Label(DataFrameRight,text="Reference No",fg="black",bg="white",font=("times new roman",15))
        l_ref.place(x=0,y=80)
        
        self.ref_add_var=StringVar()
        entry_ref=ttk.Entry(DataFrameRight,textvariable=self.ref_add_var,width=15,font=("times new roman",15))
        entry_ref.place(x=135,y=80)
        
        l_Medicine=Label(DataFrameRight,text="Medicine Name",fg="black",bg="white",font=("times new roman",15))
        l_Medicine.place(x=0,y=110)
        
        self.medicine_add_var=StringVar()
        entry_Medicine=ttk.Entry(DataFrameRight,textvariable=self.medicine_add_var,width=15,font=("times new roman",15))
        entry_Medicine.place(x=135,y=110)

        # ================================ right side frame table ==============================================
        side_frame=Frame(DataFrameRight,bd=4,relief=RIDGE,bg="white")
        side_frame.place(x=0,y=150,width=290,height=160)

        # ================================ right side frame ==============================================

        sc_x=ttk.Scrollbar(side_frame,orient=HORIZONTAL)
        sc_x.pack(side=BOTTOM,fill=X)
        sc_y=ttk.Scrollbar(side_frame,orient=VERTICAL)
        sc_y.pack(side=RIGHT,fill=Y)

        self.medicine_table=ttk.Treeview(side_frame,column=("ref","tbname"),xscrollcommand=sc_x.set,yscrollcommand=sc_y.set)

        sc_x.config(command=self.medicine_table.xview)
        sc_y.config(command=self.medicine_table.yview)

        self.medicine_table.heading("ref",text="Ref No")
        self.medicine_table.heading("tbname",text="Tablet Name")
        self.medicine_table["show"]="headings"
        self.medicine_table.column("ref",width=10)
        self.medicine_table.column("tbname",width=50)
        self.medicine_table.pack(fill=BOTH,expand=1)
        self.fetch_Medicine_data()
        self.medicine_table.bind("<ButtonRelease>",self.get_cursor_med)
       
        # ================================== Medicine Add button=============================================================

        down_frame=Frame(DataFrameRight,bd=4,relief=RIDGE,bg="darkgreen")
        down_frame.place(x=330,y=150,width=135,height=160)

        add_btn=Button(down_frame,text="ADD",command=self.add_medicine,font=("arial",12,"bold"),width=12,fg="white",bg="lime") 
        add_btn.grid(row=0,column=0,pady=2)

        update_btn=Button(down_frame,command=self.med_update,text="UPDATE",font=("arial",12,"bold"),width=12,fg="white",bg="purple")
        update_btn.grid(row=1,column=0,pady=2)

        delete_btn=Button(down_frame,command=self.medDelete,text="DELETE",font=("arial",12,"bold"),width=12,fg="white",bg="red")
        delete_btn.grid(row=2,column=0,pady=2)

        clear_btn=Button(down_frame,command=self.clear_med,text="CLEAR",font=("arial",12,"bold"),width=12,fg="white",bg="orange")
        clear_btn.grid(row=3,column=0,pady=2)
     
   
        # =======Scrollbar and Main Table=====================================================================================
        Table_frame=Frame(FrameDetails,bd=6,relief=RIDGE,bg="powder blue")
        Table_frame.place(x=0,y=1,width=1460,height=180)

        scroll_x=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(Table_frame,orient=VERTICAL)
        self.pharmacy_table=ttk.Treeview(Table_frame,column=("reg","companyname","type","tabletname","lotno","issuedate",
                                            "expdate","uses","sideeffect","warning","dosage","price","productqt")
                                            ,xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
       
        scroll_x.config(command=self.pharmacy_table.xview)
        scroll_y.config(command=self.pharmacy_table.yview)

        self.pharmacy_table["show"]="headings"
   
        self.pharmacy_table.heading("reg",text="Reference No")
        self.pharmacy_table.heading("companyname",text="Company Name")
        self.pharmacy_table.heading("type",text="Type Of Medicine")
        self.pharmacy_table.heading("tabletname",text="Tablet Name")
        self.pharmacy_table.heading("lotno",text="Lot No")
        self.pharmacy_table.heading("issuedate",text="Issue Date")
        self.pharmacy_table.heading("expdate",text="Exp Date")
        self.pharmacy_table.heading("uses",text="Uses")
        self.pharmacy_table.heading("sideeffect",text="Side Effect")
        self.pharmacy_table.heading("warning",text="Prec&Warning")
        self.pharmacy_table.heading("dosage",text="Dosage")
        self.pharmacy_table.heading("price",text="Price")
        self.pharmacy_table.heading("productqt",text="Product Qts")
        self.pharmacy_table.pack(fill=BOTH,expand=1)

        self.pharmacy_table.column("reg",width=100)
        self.pharmacy_table.column("companyname",width=100)
        self.pharmacy_table.column("type",width=100)
        self.pharmacy_table.column("tabletname",width=100)
        self.pharmacy_table.column("lotno",width=100)
        self.pharmacy_table.column("issuedate",width=100)
        self.pharmacy_table.column("expdate",width=100)
        self.pharmacy_table.column("uses",width=100)
        self.pharmacy_table.column("sideeffect",width=100)
        self.pharmacy_table.column("warning",width=100)
        self.pharmacy_table.column("dosage",width=100)
        self.pharmacy_table.column("price",width=100)
        self.pharmacy_table.column("productqt",width=100)

        self.pharmacy_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fatch_data()
    

    # ===================== MedicineAdd=================================================================      
    def add_medicine(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="root",database="my_data")
        my_cursor=conn.cursor()
        my_cursor.execute("insert into medicine(ref,MedicineName) values(%s,%s)",(                                                        
                                                                            self.ref_add_var.get(),
                                                                            self.medicine_add_var.get(),
                                                                         
                                                                        ))
        conn.commit()
        self.fetch_Medicine_data()
        self.catchdata()
        self.clear_med()
        
        conn.close()
        messagebox.showinfo("Success","Medicine Added!!")


    
    # ===================fetch data ============================================================

    def fetch_Medicine_data(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="root",database="my_data")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from medicine")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.medicine_table.delete(*self.medicine_table.get_children())
            for i in rows:
                self.medicine_table.insert("",END,values=i)
            conn.commit()
        conn.close()  

     # ====================== clear =============================================================

    def clear_med(self):
        self.ref_add_var.set("")
        self.medicine_add_var.set("")
    # ======================getCursorMedicine======================================================
    def get_cursor_med(self,event=" "):
        cursor_rows=self.medicine_table.focus()
        content=self.medicine_table.item(cursor_rows)
        row=content["values"]
        self.ref_add_var.set(row[0])
        self.medicine_add_var.set(row[1])

    # ====================medicien delete===========================================================
    def medDelete(self):
        mDelete=messagebox.askyesno("Pharmacy Management System","Do you delete this Medicine")
        if mDelete>0:
            conn=mysql.connector.connect(host="localhost",username="root",password="root",database="my_data")
            my_cursor=conn.cursor()
            sql="delete from medicine where ref=%s"
            val=(self.ref_add_var.get(),)
            my_cursor.execute(sql,val)
        else:
            if not mDelete:
                return 
         
        conn.commit()
        self.fetch_Medicine_data()
        self.clear_med()
        conn.close()
    # ============================updateall===================================================================
    def med_update(self):
            if self.ref_add_var.get()=="" or self.medicine_add_var.get()=="":
                messagebox.showwarning("Warning","All fields are required")
            else:
                try:
                    conn=mysql.connector.connect(host="localhost",user="root",password="root",database="my_data")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update medicine set MedicineName=%s where ref=%s",(
                                                                                            self.medicine_add_var.get(),
                                                                                            self.ref_add_var.get()                                                                                                                                
                                                                                                                            
                                                                                         ))
                                                                                                                            
                    conn.commit()
                    self.fetch_Medicine_data()
                    conn.close()
                    messagebox.showinfo("Success","Data Successfully updated") 
                    
        
                                                                                                                                                            
                except Exception as es:
                    messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)
    # ==========================Add Main Data====================================================
    def add_data(self):
        if self.ref_var.get()=="" or self.typeMed_var.get()=="":
            messagebox.showerror("Error","All Fields Are Required")
        
        else:
            try:
                conn=mysql.connector.connect(host="localhost",user="root",password="root",database="my_data")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into pharmacy values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                
                                                                                self.ref_var.get(),
                                                                                self.cmpName_var.get(),
                                                                                self.typeMed_var.get(),
                                                                                self.medName_var.get(),
                                                                                self.lot_var.get(),
                                                                                self.issuedate_var.get(),
                                                                                self.expdate_var.get(),
                                                                                self.uses_var.get(),
                                                                                self.sideEffect_var.get(),
                                                                                self.warning_var.get(),
                                                                                self.dosage_var.get(),
                                                                                self.price_var.get(),
                                                                                self.product_var.get()
                                                      
                
                                                                                ))
                conn.commit()
                self.fatch_data()
                conn.close()
                messagebox.showinfo("Success","Medicine has been Added")
             
            except Exception as es:
                messagebox.showerror("Error",f" Must be enter Integer number:{str(es)}",parent=self.root)
     # ========================Update=============================================================
    def update_data(self):
        if self.ref_var.get()=="":
            messagebox.showerror("Error","All Fields Are Required")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="root",database="my_data")
            my_cursor=conn.cursor()
            my_cursor.execute("update pharmacy set CompanyName=%s,TypeOfMedicine=%s,medname=%s,lot=%s,issuedate=%s,expdate=%s,uses=%s,sideeffect=%s,warning=%s,dosage=%s,price=%s,product=%s where Ref=%s",(
                                                                                
                                                                                                                                                                                                                
                                                                                                                                                                                                                self.cmpName_var.get(),
                                                                                                                                                                                                                self.typeMed_var.get(),
                                                                                                                                                                                                                self.medName_var.get(),
                                                                                                                                                                                                                self.lot_var.get(),
                                                                                                                                                                                                                self.issuedate_var.get(),
                                                                                                                                                                                                                self.expdate_var.get(),
                                                                                                                                                                                                                self.uses_var.get(),
                                                                                                                                                                                                                self.sideEffect_var.get(),
                                                                                                                                                                                                                self.warning_var.get(),
                                                                                                                                                                                                                self.dosage_var.get(),
                                                                                                                                                                                                                self.price_var.get(),
                                                                                                                                                                                                                self.product_var.get(),
                                                                                                                                                                                                                self.ref_var.get()
                                                                                                                                                                                                            
                                                                                                                                                                                                                                                                

                                                                                                                                                                                                                 ))
                                                                                                    
            conn.commit()
            self.fatch_data()
            self.Reset()
            conn.close()
            messagebox.showinfo("UPDATE","Record has been updated successfully")

                                                      

    # ====================fetchdata=================================================
    def fatch_data(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="root",database="my_data")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from pharmacy")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.pharmacy_table.delete(*self.pharmacy_table.get_children())
            for i in rows:
                self.pharmacy_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    # =======================get cursor================================================
    def get_cursor(self,event=""):
        cursor_row=self.pharmacy_table.focus()
        content=self.pharmacy_table.item(cursor_row)
        row=content["values"]

        
        self.ref_var.set(row[0]),
        self.cmpName_var.set(row[1]),
        self.typeMed_var.set(row[2]),
        self.medName_var.set(row[3]),
        self.lot_var.set(row[4]),
        self.issuedate_var.set(row[5]),
        self.expdate_var.set(row[6]),
        self.uses_var.set(row[7]),
        self.sideEffect_var.set(row[8]),
        self.warning_var.set(row[9]),
        self.dosage_var.set(row[10]),
        self.price_var.set(row[11]),
        self.product_var.set(row[12])
    # =====================Delete================================================================
    def mDelete(self): 
        if self.lot_var.get()=="":
            messagebox.showinfo("ERROR","First Select the Details!!")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="root",database="my_data")
            my_cursor=conn.cursor()
            query="delete from pharmacy where Ref=%s"
            value=(self.ref_var.get(),)
            my_cursor.execute(query,value)
            
            conn.commit()
            conn.close()
            self.fatch_data()
            self.Reset()
            messagebox.showinfo("DELETE","Medicine Information has been Deleted successfully")         

    # =====================Exit================================================================
    def iExit(self):
        iExit=tkinter.messagebox.askyesno("Pharmacy Management System","Confirm if you want to exit")
        if iExit>0:
            root.destroy()
            return

    # ==============================reset========================================================
    def Reset(self):    
        # self.ref_var.set(""),
        self.cmpName_var.set(""),
        # self.typeMed_var.set(""),
        # self.medName_var.set(""),
        self.lot_var.set(""),
        self.issuedate_var.set(""),
        self.expdate_var.set(""),
        self.uses_var.set(""),
        self.sideEffect_var.set(""),
        self.warning_var.set(""),
        self.dosage_var.set(r""),
        self.price_var.set(r""),
        self.product_var.set(r"")

   
    def search_data(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="root",database="my_data")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from pharmacy where " +str(self.serch_var.get())+" LIKE '%"+str(self.serchTxt_var.get())+"%'")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.pharmacy_table.delete(*self.pharmacy_table.get_children())
            for i in rows:
                self.pharmacy_table.insert("",END,values=i)
            conn.commit()
        conn.close()
      
     
if __name__ == "__main__":
    main()