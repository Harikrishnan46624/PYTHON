from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector


class Hospital:
    def __init__(self, root) -> None:
        self.root = root
        self.root.title("Hospitsal Mangement System")
        self.root.geometry("1540x800+0+0")

        self.Nameoftablets=StringVar()
        self.ref = StringVar()
        self.Dose = StringVar()
        self.NumberofTablets = StringVar()
        self.Lot = StringVar()
        self.IssueDate = StringVar()
        self.EXPDate = StringVar()
        self.DailyDose = StringVar()
        self.sideeffect = StringVar()
        self.FurtherInformation = StringVar()
        self.storageAdvice = StringVar()
        self.DrivingUsingMachine = StringVar()
        self.HowToUseMedicene = StringVar()
        self.PatientId = StringVar()
        self.nhsNumber = StringVar()
        self.PatientName = StringVar()
        self.DateOfBirth = StringVar()
        self.PatientAdress = StringVar()
        self.bloodpressure = StringVar()

        lbltitle = Label(self.root,bd=20,relief=RIDGE,text="HOSPITAL MANAGMENT SYSTEM",fg='RED',bg='white',font=("times new roma",50,'bold'))
        lbltitle.pack(side=TOP,fill=X)

        # ============================Data Frame================================
        Dataframe = Frame(self.root,bd = 20,relief=RIDGE)
        Dataframe.place(x=0, y=130, width=1530, height=400)

        DataframeLeft = LabelFrame(Dataframe, bd=10, relief=RIDGE, padx=20, font=("arial", 12, 'bold'), text="Patient Information")
        DataframeLeft.place(x=0, y=5, width=980, height=350)

        DataframeRight = LabelFrame(Dataframe, bd=10, relief=RIDGE, padx=20, font=("arial",12,'bold'),text="Prescription")
        DataframeRight.place(x=990, y=5, width=460, height=350)

        # ============================Buttons Frame================================

        Buttonframe = Frame(self.root,bd = 20,relief=RIDGE)
        Buttonframe.place(x=0,y=530,width=1530,height=70)
        
        # ============================Details Frame================================

        Detailsframe = Frame(self.root,bd = 20,relief=RIDGE)
        Detailsframe.place(x=0, y=600, width=1530, height=190)

        # ============================Data Frame Left================================

        iblNameTablet = Label(DataframeLeft, text="Names of Tablet", font=("arial", 12, 'bold'), padx=2, pady=6)
        iblNameTablet.grid(row=0, column=0)

        comNametablet = ttk.Combobox(DataframeLeft,textvariable=self.Nameoftablets, state="readonly", font=("arial", 12, 'bold'),width=33)
        comNametablet["values"] = ("Nice", "corona Vacacine", "Acetaminophen", "Adderall", "Amlodphine", "Ativan")
        comNametablet.grid(row=0, column=1)

        lblref = Label(DataframeLeft, font=("arial", 12, 'bold'), text="Refence No:",padx=2)
        lblref.grid(row=1,column=0,sticky=W)
        txtref = Entry(DataframeLeft, font=("arial", 13, 'bold'),textvariable=self.ref, width=35)
        txtref.grid(row=1, column=1)

        lblDose = Label(DataframeLeft,font=("arial", 12, 'bold'), text="Dose:",padx=2, pady=4)
        lblDose.grid(row=2,column=0,sticky=W)
        txtDose = Entry(DataframeLeft, font=("arial", 13, 'bold'),textvariable=self.Dose, width=35)
        txtDose.grid(row=2, column=1)

        lblNoftablets = Label(DataframeLeft, font=("arial", 12, 'bold'), text="No of Tablets:",padx=2, pady=6)
        lblNoftablets.grid(row=3,column=0,sticky=W)
        txtNoftablets = Entry(DataframeLeft, font=("arial", 13, 'bold'),textvariable=self.NumberofTablets, width=35)
        txtNoftablets.grid(row=3, column=1)

        lblLot = Label(DataframeLeft, font=("arial", 12, 'bold'), text="Lot:",padx=2, pady=6)
        lblLot.grid(row=4,column=0,sticky=W)
        txtLot = Entry(DataframeLeft, font=("arial", 13, 'bold'),textvariable=self.Lot, width=35)
        txtLot.grid(row=4, column=1)

        lblissueDate = Label(DataframeLeft, font=("arial", 12, 'bold'), text="Issue Date:",padx=2, pady=4)
        lblissueDate.grid(row=5,column=0,sticky=W)
        txtissueDate = Entry(DataframeLeft, font=("arial", 13, 'bold'),textvariable=self.IssueDate, width=35)
        txtissueDate.grid(row=5, column=1)

        lblExpDate = Label(DataframeLeft, font=("arial", 12, 'bold'), text="Exp Date:",padx=2, pady=4)
        lblExpDate.grid(row=6,column=0,sticky=W)
        txtExpDate = Entry(DataframeLeft, font=("arial", 13, 'bold'),textvariable=self.EXPDate, width=35)
        txtExpDate.grid(row=6, column=1)

        lblDailyDose = Label(DataframeLeft, font=("arial", 12, 'bold'), text="Daily Dose:",padx=2, pady=4)
        lblDailyDose.grid(row=7,column=0,sticky=W)
        txtDailyDose = Entry(DataframeLeft, font=("arial", 13, 'bold'),textvariable=self.DailyDose, width=35)
        txtDailyDose.grid(row=7, column=1)

        lblSideEffect = Label(DataframeLeft, font=("arial", 12, 'bold'), text="Side Effect:",padx=2, pady=6)
        lblSideEffect.grid(row=8,column=0,sticky=W)
        txtSideEffect = Entry(DataframeLeft, font=("arial", 13, 'bold'),textvariable=self.sideeffect, width=35)
        txtSideEffect.grid(row=8, column=1)

        lblFurther = Label(DataframeLeft, font=("arial", 12, 'bold'), text="Further Information:",padx=2)
        lblFurther.grid(row=0,column=2,sticky=W)
        txtFurther = Entry(DataframeLeft, font=("arial", 13, 'bold'),textvariable=self.FurtherInformation, width=35)
        txtFurther.grid(row=0, column=3)

        lblBloodepres = Label(DataframeLeft, font=("arial", 12, 'bold'), text="Blood Pressure:",padx=2, pady=6)
        lblBloodepres.grid(row=1,column=2,sticky=W)
        txtBloodepres = Entry(DataframeLeft, font=("arial", 13, 'bold'),textvariable=self.bloodpressure, width=35)
        txtBloodepres.grid(row=1, column=3)

        lblStorage = Label(DataframeLeft, font=("arial", 12, 'bold'), text="Storage Advice:",padx=2, pady=6)
        lblStorage.grid(row=2,column=2,sticky=W)
        txtStorage = Entry(DataframeLeft, font=("arial", 13, 'bold'),textvariable=self.storageAdvice, width=35)
        txtStorage.grid(row=2, column=3)

        lblMedicene = Label(DataframeLeft, font=("arial", 12, 'bold'), text="Medicination:",padx=2, pady=6)
        lblMedicene.grid(row=3,column=2,sticky=W)
        txtMedicene = Entry(DataframeLeft, font=("arial", 13, 'bold'),textvariable=self.HowToUseMedicene, width=35)
        txtMedicene.grid(row=3, column=3,sticky=W)

        lblPateintid = Label(DataframeLeft, font=("arial", 12, 'bold'), text="Patiend Id:",padx=2, pady=6)
        lblPateintid.grid(row=4,column=2,sticky=W)
        txtPateintid = Entry(DataframeLeft, font=("arial", 13, 'bold'),textvariable=self.PatientId, width=35)
        txtPateintid.grid(row=4, column=3)

        lblNhsNumber = Label(DataframeLeft, font=("arial", 12, 'bold'), text="NHS Nunmber:",padx=2, pady=6)
        lblNhsNumber.grid(row=5,column=2,sticky=W)
        txtNhsNumber = Entry(DataframeLeft, font=("arial", 13, 'bold'),textvariable=self.nhsNumber, width=35)
        txtNhsNumber.grid(row=5, column=3)

        lblPanientName = Label(DataframeLeft, font=("arial", 12, 'bold'), text="Patient Name:",padx=2, pady=6)
        lblPanientName.grid(row=6,column=2,sticky=W)
        txtPanientName = Entry(DataframeLeft, font=("arial", 13, 'bold'),textvariable=self.PatientName, width=35)
        txtPanientName.grid(row=6, column=3)

        lblDOB = Label(DataframeLeft, font=("arial", 12, 'bold'), text="Date of Birth:",padx=2, pady=6)
        lblDOB.grid(row=7,column=2,sticky=W)
        txtDOB = Entry(DataframeLeft, font=("arial", 13, 'bold'),textvariable=self.DateOfBirth, width=35)
        txtDOB.grid(row=7, column=3)

        lblPatientAdress = Label(DataframeLeft, font=("arial", 12, 'bold'), text="Patient Adress:",padx=2, pady=4)
        lblPatientAdress.grid(row=8,column=2,sticky=W)
        txtPatientAdress = Entry(DataframeLeft, font=("arial", 13, 'bold'),textvariable=self.PatientAdress, width=35)
        txtPatientAdress.grid(row=8, column=3)

        # ============================Data Frame Right================================

        self.txtprescription = Text(DataframeRight, font=("arial", 12, 'bold'), width=45, height=16,padx=2, pady=6)
        self.txtprescription.grid(row=0, column=0)

        # ============================Data Frame Buttons================================

        btnprescription = Button(Buttonframe,command=self.iprectioption, text="Prescription", bg="green", fg="white", font=("arial", 12, 'bold'), width=23, padx=2, pady=6)
        btnprescription.grid(row=0, column=0)  

        btnprescriptionData = Button(Buttonframe,command=self.iprescriptionData, text="Prescription Data", bg="green", fg="white", font=("arial", 12, 'bold'), width=23, padx=2, pady=6)
        btnprescriptionData.grid(row=0, column=1)

        btnUpdate = Button(Buttonframe,command=self.update_data, text="Update", bg="green", fg="white", font=("arial", 12, 'bold'), width=23, padx=2, pady=6)
        btnUpdate.grid(row=0, column=2)

        btnDelte = Button(Buttonframe,command=self.idelete, text="Delete", bg="green", fg="white", font=("arial", 12, 'bold'), width=23, padx=2, pady=6)
        btnDelte.grid(row=0, column=3)

        btnClear = Button(Buttonframe,command=self.clear, text="Clear", bg="green", fg="white", font=("arial", 12, 'bold'), width=23, padx=2, pady=6)
        btnClear.grid(row=0, column=4)

        btnExit = Button(Buttonframe,command=self.iExit, text="Exit", bg="green", fg="white", font=("arial", 12, 'bold'), width=23, padx=2, pady=6)
        btnExit.grid(row=0, column=5)

        # ============================Table================================
        # ============================Scroll Bar================================

        scroll_x = ttk.Scrollbar(Detailsframe, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(Detailsframe, orient=VERTICAL)
        self.hospital_table = ttk.Treeview(Detailsframe, column=("nameoftablets", "ref", "dose", "nooftablets", 'lot', 'issuedate', 'expdate', 'dailydose', 'storage', 'nhsnumber', 'pname', 'dob', 'address'),xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x = ttk.Scrollbar(command=self.hospital_table.xview)
        scroll_y = ttk.Scrollbar(command=self.hospital_table.yview)

        self.hospital_table.heading("nameoftablets", text="Name Of Tablets")
        self.hospital_table.heading("ref", text="Reference No")
        self.hospital_table.heading("dose", text="Dose")
        self.hospital_table.heading("nooftablets", text="No of Tablets")
        self.hospital_table.heading("lot", text="Lot")
        self.hospital_table.heading("issuedate", text="Issue Date")
        self.hospital_table.heading("expdate", text="EXP Date")
        self.hospital_table.heading("dailydose", text="Daily Dose")
        self.hospital_table.heading("storage", text="Storage")
        self.hospital_table.heading("nhsnumber", text="NHS Number")
        self.hospital_table.heading("pname", text="Patient Name")
        self.hospital_table.heading("dob", text="DOB")
        self.hospital_table.heading("address", text="Address")


        self.hospital_table["show"] = "headings"
        
        self.hospital_table.column("nameoftablets", width=100)
        self.hospital_table.column("ref", width=100)
        self.hospital_table.column("dose", width=100)
        self.hospital_table.column("nooftablets", width=100)
        self.hospital_table.column("lot", width=100)
        self.hospital_table.column("issuedate", width=100)
        self.hospital_table.column("expdate", width=100)
        self.hospital_table.column("dailydose", width=100)
        self.hospital_table.column("storage", width=100)
        self.hospital_table.column("nhsnumber", width=100)
        self.hospital_table.column("pname", width=100)
        self.hospital_table.column("dob", width=100)
        self.hospital_table.column("address", width=100)

        self.hospital_table.pack(fill=BOTH, expand=1)
        self.hospital_table.bind("<ButtonRelease-1>", self.get_cursor)


        self.fetch_data()

    # ============================Functionality Declration================================

    def iprescriptionData(self):
        if self.Nameoftablets.get() == "" or self.ref.get() == "":
            messagebox.showerror("Error", "All fields are required")
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password='asdf.,098765', database="mydata")
            my_cursor = conn.cursor()
            my_cursor.execute("insert into hospital values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
                self.Nameoftablets.get(), self.ref.get(), self.Dose.get(), self.NumberofTablets.get(), self.Lot.get(),
                self.IssueDate.get(), self.EXPDate.get(), self.DailyDose.get(),self.sideeffect.get(),self.FurtherInformation.get(),
                self.bloodpressure.get(), self.storageAdvice.get(),self.PatientId.get(),self.HowToUseMedicene.get(),
                self.nhsNumber.get(), self.PatientName.get(), self.DateOfBirth.get(), self.PatientAdress.get()))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Success", "Record has been inserted")

    def update_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password='asdf.,098765',port = "3306", database="mydata")
        my_cursor = conn.cursor()
        update_query = "UPDATE hospital SET `Refernce No`=%s, `Name of Tablet`=%s, `Dose`=%s, `No of Tablets`=%s, `Lot`=%s, `Issue date`=%s, `EXP Date`=%s, `Daily Dose`=%s, `Side effect`=%s, `Further information`=%s, `Blood pressure`=%s, `Storage Advice`=%s, `Patiend Id`=%s, `HowToUseMedicene`=%s, `nhsNumber`=%s, `PatientName`=%s, `DateOfBirth`=%s, `Patient Adres`=%s WHERE `Refernce No`=%s"

        data = (self.Nameoftablets.get(), self.ref.get(), self.Dose.get(), self.NumberofTablets.get(), self.Lot.get(), self.IssueDate.get(), self.EXPDate.get(), self.DailyDose.get(), self.sideeffect.get(), self.FurtherInformation.get(), self.bloodpressure.get(), self.storageAdvice.get(), self.PatientId.get(), self.HowToUseMedicene.get(), self.nhsNumber.get(), self.PatientName.get(), self.DateOfBirth.get(), self.PatientAdress.get(), self.ref.get())

        my_cursor.execute(update_query, data)


    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password='asdf.,098765', database='mydata')
        my_cursor = conn.cursor()
        my_cursor.execute("select * from hospital")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.hospital_table.delete(*self.hospital_table.get_children())
            for i in rows:
                self.hospital_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    def get_cursor(self, event = ""):
        cursor_rows = self.hospital_table.focus()
        content = self.hospital_table.item(cursor_rows)
        row = content["values"]

        self.Nameoftablets.set(row[0]), self.ref.set(row[1]), self.Dose.set(row[2]), self.NumberofTablets.set(row[3]), self.Lot.set(row[4]),
        self.IssueDate.set(row[5]), self.EXPDate.set(row[6]), self.DailyDose.set(row[7]),self.sideeffect.set(row[8]),self.FurtherInformation.set(row[9]),
        self.bloodpressure.set(row[10]), self.storageAdvice.set(row[11]),self.PatientId.set(row[12]),self.HowToUseMedicene.set(row[13]),
        self.nhsNumber.set(row[14]), self.PatientName.set(row[15]), self.DateOfBirth.set(row[16]), self.PatientAdress.set(row[17])

    def iprectioption(self):
        self.txtprescription.insert(END,"Names of Tablet:\t\t\t"+self.Nameoftablets.get()+"\n")
        self.txtprescription.insert(END,"Reference No:\t\t\t"+self.ref.get()+"\n")
        self.txtprescription.insert(END,"Dose:\t\t\t"+self.Dose.get()+"\n")
        self.txtprescription.insert(END,"No of Tablets:\t\t\t"+self.NumberofTablets.get()+"\n")
        self.txtprescription.insert(END,"Lot:\t\t\t"+self.Lot.get()+"\n")
        self.txtprescription.insert(END,"Issue Date:\t\t\t"+self.IssueDate.get()+"\n")
        self.txtprescription.insert(END,"Exp Date:\t\t\t"+self.EXPDate.get()+"\n")
        self.txtprescription.insert(END,"Daily Dose:\t\t\t"+self.DailyDose.get()+"\n")
        self.txtprescription.insert(END,"Side Effect:\t\t\t"+self.sideeffect.get()+"\n")
        self.txtprescription.insert(END,"Further Information:\t\t\t"+self.FurtherInformation.get()+"\n")
        self.txtprescription.insert(END,"Blood Pressure:\t\t\t"+self.bloodpressure.get()+"\n")
        self.txtprescription.insert(END,"Storage Advice:\t\t\t"+self.storageAdvice.get()+"\n")
        self.txtprescription.insert(END,"Patiend Id:\t\t\t"+self.PatientId.get()+"\n")
        self.txtprescription.insert(END,"Medicination:\t\t\t"+self.HowToUseMedicene.get()+"\n")
        self.txtprescription.insert(END,"NHS Nunmber:\t\t\t"+self.nhsNumber.get()+"\n")
        self.txtprescription.insert(END,"Patient Name:\t\t\t"+self.PatientName.get()+"\n")
        self.txtprescription.insert(END,"Date of Birth:\t\t\t"+self.DateOfBirth.get()+"\n")
        self.txtprescription.insert(END,"Patient Adress:\t\t\t"+self.PatientAdress.get()+"\n")

        
    def idelete(self):
        conn = mysql.connector.connect(host="localhost", username="root", password='asdf.,098765', database='mydata')
        my_cursor = conn.cursor()
        query = ("delete from hospital where Refernce No=%s")
        value = (self.ref.get())
        my_cursor.execute(query, value)

        conn.commit()
        conn.close()
        self.fetch_data()
        messagebox.showinfo("Delete","patient has been deleted succesfully")

    def clear(self):
        self.Nameoftablets.set(""), self.ref.set(""), self.Dose.set(''), self.NumberofTablets.set(''), self.Lot.set(''),
        self.IssueDate.set(""), self.EXPDate.set(''), self.DailyDose.set(''),self.sideeffect.set(''),self.FurtherInformation.set(''),
        self.bloodpressure.set(''), self.storageAdvice.set(''),self.PatientId.set(''),self.HowToUseMedicene.set(''),
        self.nhsNumber.set(''), self.PatientName.set(''), self.DateOfBirth.set(''), self.PatientAdress.set('')
        self.txtprescription.delete("1.0",END)

    def iExit(self):
        iExit = messagebox.askyesno("Hospital managment system","confirm you want to exit")
        if iExit > 0:
            root.destroy()
            return








root = Tk()
ob = Hospital(root)
root.mainloop()