import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

class Hospital:
    def __init__(self, root):
        self.root = root
        self.root.title("Hospital Management System")
        self.root.geometry("1540x800+0+0")

        self.connect_db()
        
        self.lbltitle = tk.Label(self.root, bd=20, relief=tk.RIDGE, text="HOSPITAL MANAGEMENT SYSTEM", fg="red", bg="white", font=("times new roman", 50, "bold"))
        self.lbltitle.pack(side=tk.TOP, fill=tk.X)
        
        # ===================================== Dataframe ==================================
        Dataframe = tk.Frame(self.root, bd=20, relief=tk.RIDGE)
        Dataframe.place(x=0, y=130, width=1530, height=400)
        
        DataframeLeft = tk.LabelFrame(Dataframe, bd=10, relief=tk.RIDGE, padx=10,
                                   font=("times new roman", 12, "bold"), text="Patient Information")
        DataframeLeft.place(x=0, y=5, width=980, height=350)
        
        DataframeRight = tk.LabelFrame(Dataframe, bd=10, relief=tk.RIDGE, padx=10,
                                    font=("times new roman", 12, "bold"), text="Prescription")
        DataframeRight.place(x=990, y=5, width=460, height=350)
        
        # ===================================== Buttons frame ==================================
        Buttonframe = tk.Frame(self.root, bd=20, relief=tk.RIDGE)
        Buttonframe.place(x=0, y=530, width=1530, height=70)
             
        # ===================================== Details frame ==================================
        Detailsframe = tk.Frame(self.root, bd=20, relief=tk.RIDGE)
        Detailsframe.place(x=0, y=600, width=1530, height=190)
        
        # ===================================== DataframeLeft ==================================
        lblNameTablet = tk.Label(DataframeLeft, text="Names Of Tablet", font=("calibri", 14, "bold"), padx=2, pady=6)
        lblNameTablet.grid(row=0, column=0)
        
        self.comNametablet = ttk.Combobox(DataframeLeft, state="readonly", font=("calibri", 14, "bold"), width=33)
        self.comNametablet["values"] = ("Nice", "Corona Vaccine", "Acetaminophen", "Adderall", "Amlodipine", "Ativan")
        self.comNametablet.current(0)
        self.comNametablet.grid(row=0, column=1)

        lblref = tk.Label(DataframeLeft, font=("calibri", 14, "bold"), text="Reference No:", padx=2)
        lblref.grid(row=1, column=0, sticky=tk.W)
        self.txtref = tk.Entry(DataframeLeft, font=("calibri", 14, "bold"), width=35)
        self.txtref.grid(row=1, column=1)

        lblDose = tk.Label(DataframeLeft, font=("calibri", 14, "bold"), text="Dose:", padx=2, pady=4)
        lblDose.grid(row=2, column=0, sticky=tk.W)
        self.txtDose = tk.Entry(DataframeLeft, font=("calibri", 14, "bold"), width=35)
        self.txtDose.grid(row=2, column=1)

        lblNoOftablets = tk.Label(DataframeLeft, font=("calibri", 14, "bold"), text="No Of Tablets:", padx=2, pady=6)
        lblNoOftablets.grid(row=3, column=0, sticky=tk.W)
        self.txtNoOftablets = tk.Entry(DataframeLeft, font=("calibri", 14, "bold"), width=35)
        self.txtNoOftablets.grid(row=3, column=1)

        lblLot = tk.Label(DataframeLeft, font=("calibri", 14, "bold"), text="Lot:", padx=2, pady=6)
        lblLot.grid(row=4, column=0, sticky=tk.W)
        self.txtLot = tk.Entry(DataframeLeft, font=("calibri", 14, "bold"), width=35)
        self.txtLot.grid(row=4, column=1)

        lblissueDate = tk.Label(DataframeLeft, font=("calibri", 14, "bold"), text="Issue Date:", padx=2, pady=6)
        lblissueDate.grid(row=5, column=0, sticky=tk.W)
        self.txtissueDate = tk.Entry(DataframeLeft, font=("calibri", 14, "bold"), width=35)
        self.txtissueDate.grid(row=5, column=1)

        lblExpDate = tk.Label(DataframeLeft, font=("calibri", 14, "bold"), text="Exp Date:", padx=2, pady=6)
        lblExpDate.grid(row=6, column=0, sticky=tk.W)
        self.txtExpDate = tk.Entry(DataframeLeft, font=("calibri", 14, "bold"), width=35)
        self.txtExpDate.grid(row=6, column=1)

        lblDailyDose = tk.Label(DataframeLeft, font=("calibri", 14, "bold"), text="Daily Dose:", padx=2, pady=4)
        lblDailyDose.grid(row=7, column=0, sticky=tk.W)
        self.txtDailyDose = tk.Entry(DataframeLeft, font=("calibri", 14, "bold"), width=35)
        self.txtDailyDose.grid(row=7, column=1)

        lblSideEffect = tk.Label(DataframeLeft, font=("calibri", 14, "bold"), text="Side Effect:", padx=2, pady=6)
        lblSideEffect.grid(row=8, column=0, sticky=tk.W)
        self.txtSideEffect = tk.Entry(DataframeLeft, font=("calibri", 14, "bold"), width=35)
        self.txtSideEffect.grid(row=8, column=1)

        lblFurtherinfo = tk.Label(DataframeLeft, font=("calibri", 14, "bold"), text="Further Information", padx=2)
        lblFurtherinfo.grid(row=0, column=2, sticky=tk.W)
        self.txtFurtherinfo = tk.Entry(DataframeLeft, font=("calibri", 14, "bold"), width=35)
        self.txtFurtherinfo.grid(row=0, column=3)

        lblBloodPressure = tk.Label(DataframeLeft, font=("calibri", 14, "bold"), text="Blood Pressure", padx=2, pady=6)
        lblBloodPressure.grid(row=1, column=2, sticky=tk.W)
        self.txtBloodPressure = tk.Entry(DataframeLeft, font=("calibri", 14, "bold"), width=35)
        self.txtBloodPressure.grid(row=1, column=3)

        lblStorage = tk.Label(DataframeLeft, font=("calibri", 14, "bold"), text="Storage Advice:", padx=2, pady=6)
        lblStorage.grid(row=2, column=2, sticky=tk.W)
        self.txtStorage = tk.Entry(DataframeLeft, font=("calibri", 14, "bold"), width=35)
        self.txtStorage.grid(row=2, column=3)

        lblMedicine = tk.Label(DataframeLeft, font=("calibri", 14, "bold"), text="Medication", padx=2, pady=6)
        lblMedicine.grid(row=3, column=2, sticky=tk.W)
        self.txtMedicine = tk.Entry(DataframeLeft, font=("calibri", 14, "bold"), width=35)
        self.txtMedicine.grid(row=3, column=3)

        lblPatientId = tk.Label(DataframeLeft, font=("calibri", 14, "bold"), text="Patient Id", padx=2, pady=6)
        lblPatientId.grid(row=4, column=2, sticky=tk.W)
        self.txtPatientId = tk.Entry(DataframeLeft, font=("calibri", 14, "bold"), width=35)
        self.txtPatientId.grid(row=4, column=3)

        lblNhsNumber = tk.Label(DataframeLeft, font=("calibri", 14, "bold"), text="NHS Number", padx=2, pady=6)
        lblNhsNumber.grid(row=5, column=2, sticky=tk.W)
        self.txtNhsNumber = tk.Entry(DataframeLeft, font=("calibri", 14, "bold"), width=35)
        self.txtNhsNumber.grid(row=5, column=3)

        lblPatientName = tk.Label(DataframeLeft, font=("calibri", 14, "bold"), text="Patient Name", padx=2, pady=6)
        lblPatientName.grid(row=6, column=2, sticky=tk.W)
        self.txtPatientName = tk.Entry(DataframeLeft, font=("calibri", 14, "bold"), width=35)
        self.txtPatientName.grid(row=6, column=3)

        lblDateOfBirth = tk.Label(DataframeLeft, font=("calibri", 14, "bold"), text="Date Of Birth", padx=2, pady=6)
        lblDateOfBirth.grid(row=7, column=2, sticky=tk.W)
        self.txtDateOfBirth = tk.Entry(DataframeLeft, font=("calibri", 14, "bold"), width=35)
        self.txtDateOfBirth.grid(row=7, column=3)

        lblPatientAddress = tk.Label(DataframeLeft, font=("calibri", 14, "bold"), text="Patient Address", padx=2, pady=6)
        lblPatientAddress.grid(row=8, column=2, sticky=tk.W)
        self.txtPatientAddress = tk.Entry(DataframeLeft, font=("calibri", 14, "bold"), width=35)
        self.txtPatientAddress.grid(row=8, column=3)

        # ===================================== DataframeRight =====================================
        self.txtPrescription = tk.Text(DataframeRight, font=("calibri", 14, "bold"), width=45, height=16, padx=2, pady=6)
        self.txtPrescription.grid(row=0, column=0)

        # ===================================== Buttons ============================================
        btnPrescription = tk.Button(Buttonframe, text="Prescription", bg="blue", fg="white", font=("calibri", 14, "bold"), width=23, padx=2, pady=6, command=self.prescription)
        btnPrescription.grid(row=0, column=0)

        btnPrescriptionData = tk.Button(Buttonframe, text="Prescription Data", bg="blue", fg="white", font=("calibri", 14, "bold"), width=23, padx=2, pady=6, command=self.prescription_data)
        btnPrescriptionData.grid(row=0, column=1)

        btnUpdate = tk.Button(Buttonframe, text="Update", bg="blue", fg="white", font=("calibri", 14, "bold"), width=23, padx=2, pady=6, command=self.update_data)
        btnUpdate.grid(row=0, column=2)

        btnDelete = tk.Button(Buttonframe, text="Delete", bg="blue", fg="white", font=("calibri", 14, "bold"), width=23, padx=2, pady=6, command=self.delete_data)
        btnDelete.grid(row=0, column=3)

        btnClear = tk.Button(Buttonframe, text="Clear", bg="blue", fg="white", font=("calibri", 14, "bold"), width=23, padx=2, pady=6, command=self.clear_fields)
        btnClear.grid(row=0, column=4)

        btnExit = tk.Button(Buttonframe, text="Exit", bg="blue", fg="white", font=("calibri", 14, "bold"), width=23, padx=2, pady=6, command=self.exit_app)
        btnExit.grid(row=0, column=5)

        # ===================================== Table ==============================================
        # ===================================== Scrollbar ==========================================
        scroll_x = ttk.Scrollbar(Detailsframe, orient=tk.HORIZONTAL)
        scroll_y = ttk.Scrollbar(Detailsframe, orient=tk.VERTICAL)
        self.hospital_table = ttk.Treeview(Detailsframe, columns=("nameoftablets", "ref", "dose", "nooftablets", "lot", "issuedate",
                                                                  "expdate", "dailydose", "storage", "nhsnumber", "pname", "dob", "address"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=tk.BOTTOM, fill=tk.X)
        scroll_y.pack(side=tk.RIGHT, fill=tk.Y)

        scroll_x.config(command=self.hospital_table.xview)
        scroll_y.config(command=self.hospital_table.yview)
        self.hospital_table.heading("nameoftablets", text="Name Of Tablet")
        self.hospital_table.heading("ref", text="Reference No.")
        self.hospital_table.heading("dose", text="Dose")
        self.hospital_table.heading("nooftablets", text="No Of Tablets")
        self.hospital_table.heading("lot", text="Lot")
        self.hospital_table.heading("issuedate", text="Issue Date")
        self.hospital_table.heading("expdate", text="Exp Date")
        self.hospital_table.heading("dailydose", text="Daily Dose")
        self.hospital_table.heading("storage", text="Storage")
        self.hospital_table.heading("nhsnumber", text="NHS Number")
        self.hospital_table.heading("pname", text="Patient Name")
        self.hospital_table.heading("dob", text="DOB")
        self.hospital_table.heading("address", text="Address")

        self.hospital_table["show"] = "headings"

        self.hospital_table.pack(fill=tk.BOTH, expand=1)
    
    def connect_db(self):
        self.conn = sqlite3.connect('hospital.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS patients (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nameoftablets TEXT,
            ref TEXT,
            dose TEXT,
            nooftablets TEXT,
            lot TEXT,
            issuedate TEXT,
            expdate TEXT,
            dailydose TEXT,
            sideeffect TEXT,
            furtherinfo TEXT,
            bloodpressure TEXT,
            storage TEXT,
            medication TEXT,
            patientid TEXT,
            nhsnumber TEXT,
            pname TEXT,
            dob TEXT,
            address TEXT
        )''')
        self.conn.commit()


    def prescription(self):
        self.txtPrescription.delete("1.0", tk.END)
        self.txtPrescription.insert(tk.END, f"Name of Tablets: {self.comNametablet.get()}\n")
        self.txtPrescription.insert(tk.END, f"Reference No: {self.txtref.get()}\n")
        self.txtPrescription.insert(tk.END, f"Dose: {self.txtDose.get()}\n")
        self.txtPrescription.insert(tk.END, f"No of Tablets: {self.txtNoOftablets.get()}\n")
        self.txtPrescription.insert(tk.END, f"Lot: {self.txtLot.get()}\n")
        self.txtPrescription.insert(tk.END, f"Issue Date: {self.txtissueDate.get()}\n")
        self.txtPrescription.insert(tk.END, f"Exp Date: {self.txtExpDate.get()}\n")
        self.txtPrescription.insert(tk.END, f"Daily Dose: {self.txtDailyDose.get()}\n")
        self.txtPrescription.insert(tk.END, f"Side Effect: {self.txtSideEffect.get()}\n")
        self.txtPrescription.insert(tk.END, f"Further Information: {self.txtFurtherinfo.get()}\n")
        self.txtPrescription.insert(tk.END, f"Blood Pressure: {self.txtBloodPressure.get()}\n")
        self.txtPrescription.insert(tk.END, f"Storage Advice: {self.txtStorage.get()}\n")
        self.txtPrescription.insert(tk.END, f"Medication: {self.txtMedicine.get()}\n")
        self.txtPrescription.insert(tk.END, f"Patient ID: {self.txtPatientId.get()}\n")
        self.txtPrescription.insert(tk.END, f"NHS Number: {self.txtNhsNumber.get()}\n")
        self.txtPrescription.insert(tk.END, f"Patient Name: {self.txtPatientName.get()}\n")
        self.txtPrescription.insert(tk.END, f"Date of Birth: {self.txtDateOfBirth.get()}\n")
        self.txtPrescription.insert(tk.END, f"Patient Address: {self.txtPatientAddress.get()}\n")

    def prescription_data(self):
        # Get data from the entry fields
        data = (
            self.comNametablet.get(),
            self.txtref.get(),
            self.txtDose.get(),
            self.txtNoOftablets.get(),
            self.txtLot.get(),
            self.txtissueDate.get(),
            self.txtExpDate.get(),
            self.txtDailyDose.get(),
            self.txtSideEffect.get(),
            self.txtFurtherinfo.get(),
            self.txtBloodPressure.get(),
            self.txtStorage.get(),
            self.txtMedicine.get(),
            self.txtPatientId.get(),
            self.txtNhsNumber.get(),
            self.txtPatientName.get(),
            self.txtDateOfBirth.get(),
            self.txtPatientAddress.get()
        )

        # Insert data into the database
        self.cursor.execute('''INSERT INTO patients (nameoftablets, ref, dose, nooftablets, lot, issuedate, expdate,
                          dailydose, sideeffect, furtherinfo, bloodpressure, storage, medication, patientid, nhsnumber, pname, dob, address)
                          VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', data)
        self.conn.commit()

        # Display data in the Treeview
        self.hospital_table.insert("", "end", values=data)

    def update_data(self):
        selected_item = self.hospital_table.selection()
        if selected_item:
            values = self.hospital_table.item(selected_item)['values']

            # Update the entry fields with selected item values
            self.comNametablet.set(values[0])
            self.txtref.delete(0, tk.END)
            self.txtref.insert(0, values[1])
            self.txtDose.delete(0, tk.END)
            self.txtDose.insert(0, values[2])
            self.txtNoOftablets.delete(0, tk.END)
            self.txtNoOftablets.insert(0, values[3])
            self.txtLot.delete(0, tk.END)
            self.txtLot.insert(0, values[4])
            self.txtissueDate.delete(0, tk.END)
            self.txtissueDate.insert(0, values[5])
            self.txtExpDate.delete(0, tk.END)
            self.txtExpDate.insert(0, values[6])
            self.txtDailyDose.delete(0, tk.END)
            self.txtDailyDose.insert(0, values[7])
            self.txtSideEffect.delete(0, tk.END)
            self.txtSideEffect.insert(0, values[8])
            self.txtFurtherinfo.delete(0, tk.END)
            self.txtFurtherinfo.insert(0, values[9])
            self.txtBloodPressure.delete(0, tk.END)
            self.txtBloodPressure.insert(0, values[10])
            self.txtStorage.delete(0, tk.END)
            self.txtStorage.insert(0, values[11])
            self.txtMedicine.delete(0, tk.END)
            self.txtMedicine.insert(0, values[12])
            self.txtPatientId.delete(0, tk.END)
            self.txtPatientId.insert(0, values[13])
            self.txtNhsNumber.delete(0, tk.END)
            self.txtNhsNumber.insert(0, values[14])
            self.txtPatientName.delete(0, tk.END)
            self.txtPatientName.insert(0, values[15])
            self.txtDateOfBirth.delete(0, tk.END)
            self.txtDateOfBirth.insert(0, values[16])
            self.txtPatientAddress.delete(0, tk.END)
            self.txtPatientAddress.insert(0, values[17])

            # Update data in the database
            self.cursor.execute('''UPDATE patients SET nameoftablets=?, dose=?, nooftablets=?, lot=?, issuedate=?, expdate=?,
                                  dailydose=?, sideeffect=?, furtherinfo=?, bloodpressure=?, storage=?, medication=?, patientid=?,
                                  nhsnumber=?, pname=?, dob=?, address=? WHERE ref=?''',
                                (values[0], values[2], values[3], values[4], values[5], values[6], values[7], values[8],
                                 values[9], values[10], values[11], values[12], values[13], values[14], values[15],
                                 values[16], values[17], values[1]))
            self.conn.commit()
        else:
            messagebox.showerror("Error", "Please select a record to update.")

    def delete_data(self):
        selected_item = self.hospital_table.selection()
        if selected_item:
            if messagebox.askyesno("Delete", "Are you sure you want to delete this record?"):
                values = self.hospital_table.item(selected_item)['values']
                self.cursor.execute("DELETE FROM patients WHERE ref=?", (values[1],))
                self.conn.commit()

                self.hospital_table.delete(selected_item)
                messagebox.showinfo("Success", "Record deleted successfully.")
        else:
            messagebox.showerror("Error", "Please select a record to delete.")

    def clear_fields(self):
        # Clear entry fields
        self.comNametablet.set("")
        self.txtref.delete(0, tk.END)
        self.txtDose.delete(0, tk.END)
        self.txtNoOftablets.delete(0, tk.END)
        self.txtLot.delete(0, tk.END)
        self.txtissueDate.delete(0, tk.END)
        self.txtExpDate.delete(0, tk.END)
        self.txtDailyDose.delete(0, tk.END)
        self.txtSideEffect.delete(0, tk.END)
        self.txtFurtherinfo.delete(0, tk.END)
        self.txtBloodPressure.delete(0, tk.END)
        self.txtStorage.delete(0, tk.END)
        self.txtMedicine.delete(0, tk.END)
        self.txtPatientId.delete(0, tk.END)
        self.txtNhsNumber.delete(0, tk.END)
        self.txtPatientName.delete(0, tk.END)
        self.txtDateOfBirth.delete(0, tk.END)
        self.txtPatientAddress.delete(0, tk.END)

    def exit_app(self):
        self.conn.close()
        self.root.destroy()

root = tk.Tk()
ob = Hospital(root)
root.mainloop()
