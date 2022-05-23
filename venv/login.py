from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
from tkinter import filedialog
from PIL import ImageTk, Image, ImageOps, ImageDraw
from tinydb import TinyDB, Query
import cv2
import imutils
import numpy as np
import threading

def login():
    # Create Window
    window = Tk()
    window.title("Criminal Detection | Login")
    w = 1280
    h = 720
    ws = window.winfo_screenwidth()
    hs = window.winfo_screenheight()
    x = (ws / 2) - (w / 2)
    y = 0
    window.geometry("%dx%d+%d+%d" % (w, h, x, y))
    window.resizable(0,0)
    window.iconbitmap("imagesIcons/CDLogo.ico")
    window.config(bg = "#939393")

    def submit():
        if entUsername.get() == "" or entPassword.get() == "":
            messagebox.showwarning(title = "Warning", message = "Please enter Username or Password")
        else:
            if entUsername.get() == "Aman" and entPassword.get() == "Aman123":
                messagebox.showinfo(title = "Login ", message = "Login Sucessfull")
                window.destroy()
                cameraSetup()
            else:
                messagebox.showerror(title = "Error", message = "Invalid Username or Password")

    def forgotPwd():
        window.destroy()
        forgotPassword()

    # Create Frame for Photo
    frmPhoto = Frame(master = window, height = 250, bg = "#939393")
    frmPhoto.pack(fill = X, expand = 1)

    frame = Frame(master = frmPhoto, bg = "#939393", width = 400)
    frame.grid(row = 0, column = 0)

    frame = Frame(master = frmPhoto, bg = "#939393")
    frame.grid(row = 0, column = 1)
    img = ImageTk.PhotoImage(Image.open("imagesIcons/CDLogo.png"))
    lblPhoto = Label(master = frame, image = img, bg = "#939393")
    lblPhoto.pack()

    # Create Frame for Login Details
    frmMain = Frame(master = window, height = 400,width = 800, bg = "#939393")
    frmMain.pack(fill = BOTH, expand = 1)

    frame = Frame(master=frmMain, bg = "#939393", width = 300)
    frame.grid(row = 0, column = 0, rowspan = 5)

    frame = Frame(master=frmMain, bg = "#C4C4C4")
    frame.grid(row = 1, column = 1, pady=5)
    lUsername = Label(master = frame, text = 'Username:', font = ('roboto',24),bg = '#C4C4C4')
    lUsername.pack(padx = 5, pady = 5)

    frame = Frame(master=frmMain, bg = "#C4C4C4")
    frame.grid(row = 1, column = 2, pady=5)
    entUsername = Entry(master = frame, font = ('roboto',25), width = 30, bg = '#81D6E1')
    entUsername.pack(padx = 5, pady = 5)

    frame = Frame(master=frmMain, bg = "#C4C4C4")
    frame.grid(row = 2, column = 1, pady=5)
    lPassword = Label(master = frame, text = 'Password:', font = ('roboto',24),bg = '#C4C4C4')
    lPassword.pack(padx = 9, pady = 5)

    frame = Frame(master=frmMain, bg = "#C4C4C4")
    frame.grid(row = 2, column = 2, pady=5)
    entPassword = Entry(master = frame, font = ('roboto',25), width = 30, bg = '#81D6E1', show = "*")
    entPassword.pack(padx = 5, pady = 5)

    frame = Frame(master=frmMain, bg = "#C4C4C4")
    frame.grid(row = 3, column = 1, columnspan = 2, pady = 5)
    btnLogin = Button(master = frame ,text = 'Login', font = ('roboto',32),width=28,bd=5,bg = '#81D6E1', command = submit)
    btnLogin.pack(padx = 5, pady = 5)

    frame = Frame(master=frmMain, bg = "#939393")
    frame.grid(row = 4, column = 1, sticky = "w", pady  = 5)
    btnForgotPwd = Button(master = frame ,text = 'Forgot Password?', command = forgotPwd, bg = '#939393', borderwidth = 0,font = ('arial',10,'underline','bold'))
    btnForgotPwd.pack()

    window.mainloop()

def forgotPassword():
    # Create Window
    window = Tk()
    window.title("Criminal Detection | Forgot Password")
    w = 1280
    h = 720
    ws = window.winfo_screenwidth()
    hs = window.winfo_screenheight()
    x = (ws / 2) - (w / 2)
    y = 0
    window.geometry("%dx%d+%d+%d" % (w, h, x, y))
    window.resizable(0, 0)
    window.iconbitmap("imagesIcons/CDLogo.ico")
    window.config(bg="#939393")

    def confirm():
        if entRecovery.get() == "123456" and entPassword.get() != "":
            userAns = messagebox.askquestion("Change Password", "Are you sure?")
            if userAns == "yes":
                window.destroy()
                login()
        elif entRecovery.get() == "" or entPassword.get() == "":
            messagebox.showwarning(title = "Warning", message = "Please enter Recovery code or New password")
        elif entRecovery != "123456":
            messagebox.showerror(title="Error", message="Invalid Recovery code")


    # Create Window
    frame = Frame(master=window, bg="#939393", width=250)
    frame.grid(row=0, column=0, rowspan=3)

    frame = Frame(master=window, bg="#939393")
    frame.grid(row=0, column=1, pady=100, columnspan = 2)
    lblText = Label(master=frame, text='Forgot Password', font=('roboto', 32), bg='#939393').pack(padx=5, pady=5)

    frame = Frame(master=window, bg="#C4C4C4")
    frame.grid(row=1, column=1, pady=5)
    lblRecovery = Label(master=frame, text='Recovery Code:', font=('roboto', 24), bg='#C4C4C4')
    lblRecovery.pack(padx=9, pady=5)

    frame = Frame(master=window, bg="#C4C4C4")
    frame.grid(row=1, column=2, pady=5)
    entRecovery = Entry(master=frame, font=('roboto', 25), width=30, bg='#81D6E1')
    entRecovery.pack(padx=5, pady=5)

    frame = Frame(master=window, bg="#C4C4C4")
    frame.grid(row=2, column=1, pady=5)
    lPassword = Label(master=frame, text='New Password:', font=('roboto', 24), bg='#C4C4C4')
    lPassword.pack(padx=11, pady=5)

    frame = Frame(master=window, bg="#C4C4C4")
    frame.grid(row=2, column=2, pady=5)
    entPassword = Entry(master=frame, font=('roboto', 25), width=30, bg='#81D6E1', show="*")
    entPassword.pack(padx=5, pady=5)

    frame = Frame(master=window, bg="#C4C4C4")
    frame.grid(row=3, column=1, columnspan=2, pady=30)
    btnLogin = Button(master=frame, text='Confirm', font=('roboto', 32), width=25, bd=5, bg='#81D6E1', command=confirm)
    btnLogin.pack(padx=5, pady=5)

    window.mainloop()

# TinyDB setup for Presets
presetDB = TinyDB("localDB/presetDB.json")
query = Query()
# presetDB.truncate()
# presetDB.insert({"name": "Preset 1", "value": 1})
selectedPresetNumber = 0
def cameraSetup():
    # Create Window
    window = Tk()
    window.title("Criminal Detection | Camera Setup")
    w = 1280
    h = 720
    ws = window.winfo_screenwidth()
    hs = window.winfo_screenheight()
    x = (ws / 2) - (w / 2)
    y = 0
    window.geometry("%dx%d+%d+%d" % (w, h, x, y))
    window.resizable(0, 0)
    window.iconbitmap("imagesIcons/CDLogo.ico")
    window.config(bg="#939393")

    def getPresetNumber():
        no = 0
        results = presetDB.all()
        no = len(results)
        return no

    presetNo = getPresetNumber()

    def addPreset():
        window.destroy()
        cameraPresetSetup()

    def selectPreset(presetNumber):
        global selectedPresetNumber
        if presetNo > 1:
            if presetNumber == 1:
                btnpreset1.config(relief=SOLID, bd = 5)
                btnpreset2.config(relief=SOLID,bd = 0)
            elif presetNumber == 2:
                btnpreset1.config(relief=SOLID, bd = 0)
                btnpreset2.config(relief=SOLID,bd = 5)
        else:
            btnpreset1.config(relief=SOLID, bd=5)
        selectedPresetNumber = presetNumber

    def editPreset():
        window.destroy()
        cameraPresetSetup()

    def next():
        if selectedPresetNumber == 0:
            messagebox.showerror(title="Error", message="Please select a preset to continue.")
        else:
            window.destroy()
            cameraView(selectedPresetNumber)


    frame = Frame(master=window, bg="#939393", width=225)
    frame.grid(row=0, column=0, rowspan=3)

    frame = Frame(master=window, bg="#939393")
    frame.grid(row=0, column=1, pady=80, columnspan=3)
    lblText = Label(master=frame, text='Camera Setup', font=('roboto', 32), bg='#939393').pack(padx=5, pady=5)

    # Dynamically adding Preset Buttons

    if presetNo == 1:
        frame = Frame(master=window, bg="#C4C4C4", relief=SOLID, bd=0)
        frame.grid(row=1, column=1, padx=30)
        btnpreset1 = Button(master=frame, text='Preset 1', font=('roboto', 24), width=11, height=5, bd=0, bg='#81D6E1', command=lambda: selectPreset(1))
        btnpreset1.pack(padx=5, pady=5)

    elif presetNo == 2:
        frame = Frame(master=window, bg="#C4C4C4", relief=SOLID, bd=0)
        frame.grid(row=1, column=1, padx=30)
        btnpreset1 = Button(master=frame, text='Preset 1', font=('roboto', 24), width=11, height=5, bd=0, bg='#81D6E1', command=lambda: selectPreset(1))
        btnpreset1.pack(padx=5, pady=5)

        frame = Frame(master=window, bg="#C4C4C4", relief=SOLID, bd=0)
        frame.grid(row=1, column=2, padx=30)
        btnpreset2 = Button(master=frame, text='Preset 2', font=('roboto', 24), width=11, height=5, bd=0, bg='#81D6E1', command=lambda: selectPreset(2))
        btnpreset2.pack(padx=5, pady=5)

    frame = Frame(master=window, bg="#C4C4C4")
    frame.grid(row=1, column=presetNo+1, padx = 30)
    btnAddPreset = Button(master=frame, text='\u2795', font=('roboto', 24), width=11, height=5, bd=0, bg='#81D6E1', command=addPreset)
    btnAddPreset.pack(padx=5, pady=5)

    if presetNo == 2:
        btnAddPreset.config(state = "disabled")

    frame = Frame(master=window, bg="#C4C4C4")
    frame.grid(row=2, column=1, pady=30)
    btnEdit = Button(master=frame, text='Edit', font=('roboto', 32), width=10, bd=5, bg='#81D6E1', command=editPreset)
    btnEdit.pack(padx=5, pady=5)

    if presetNo == 0:
        btnEdit.config(state = "disabled")

    frame = Frame(master=window, bg="#C4C4C4")
    frame.grid(row=2, column=2, pady=30)
    btnLogin = Button(master=frame, text='Next', font=('roboto', 32), width=10, bd=5, bg='#81D6E1', command=next)
    btnLogin.pack(padx=5, pady=5)

    window.mainloop()

def cameraPresetSetup():
    # Create Window
    window = Tk()
    window.title("Criminal Detection | Preset Setup")
    w = 1280
    h = 720
    ws = window.winfo_screenwidth()
    hs = window.winfo_screenheight()
    x = (ws / 2) - (w / 2)
    y = 0
    window.geometry("%dx%d+%d+%d" % (w, h, x, y))
    window.resizable(0, 0)
    window.iconbitmap("imagesIcons/CDLogo.ico")
    window.config(bg="#939393")

    def getCameraList():
        try:
            index = 0
            arr = []
            while True:
                cap = cv2.VideoCapture(index)
                if not cap.read()[0]:
                    break
                else:
                    arr.append(index)
                cap.release()
                cv2.destroyAllWindows()
                index += 1
            return arr
        except:
            pass

    def deletePreset():
        if v.get() == "1":
            isThere = presetDB.search(query.value == 1)
            if len(isThere) != 0:
                sure = messagebox.askyesno("Delete Preset","Are you sure?")
                if sure:
                    presetDB.remove(query.value == 1)

            elif len(isThere) == 0:
                messagebox.showwarning("Warning","No preset are there yet to be deleted.")
        else:
            isThere = presetDB.search(query.value == 2)
            if len(isThere) != 0:
                sure = messagebox.askyesno("Delete Preset", "Are you sure?")
                if sure:
                    presetDB.remove(query.value == 2)
            elif len(isThere) == 0:
                messagebox.showwarning("Warning","No preset are there yet to be deleted.")

    def savePreset():
        if v.get() == "1":
            isThere = presetDB.search(query.value == 1)
            if len(isThere) != 0:
                sure = messagebox.askyesno("Save Preset", "Are you sure?")
                if sure:
                    presetDB.update({"camera_number": cmbxCameraNo.get(), "mode": cmbxMode.get(), "ip1": entIP1.get(),
                                     "ip2": entIP2.get(), "ip3": entIP3.get(), "ip4": entIP4.get()}, query.value == 1)
            elif len(isThere) == 0:
                presetDB.insert({"name": "Preset 1", "value": 1, "camera_number": cmbxCameraNo.get(), "mode": cmbxMode.get(),
                                 "ip1": entIP1.get(), "ip2": entIP2.get(), "ip3": entIP3.get(), "ip4": entIP4.get()})
                messagebox.showinfo("Info","Preset Created.")
        else:
            isThere = presetDB.search(query.value == 2)
            if len(isThere) != 0:
                sure = messagebox.askyesno("Save Preset", "Are you sure?")
                if sure:
                    presetDB.update({"camera_number": cmbxCameraNo.get(), "mode": cmbxMode.get(), "ip1": entIP1.get(),
                                     "ip2": entIP2.get(), "ip3": entIP3.get(), "ip4": entIP4.get()}, query.value == 2)
            elif len(isThere) == 0:
                presetDB.insert(
                    {"name": "Preset 2", "value": 2, "camera_number": cmbxCameraNo.get(), "mode": cmbxMode.get(),
                     "ip1": entIP1.get(), "ip2": entIP2.get(), "ip3": entIP3.get(), "ip4": entIP4.get()})
                messagebox.showinfo("Info","Preset Created.")

    def cancel():
        sure = messagebox.askyesno("Exit", "Are you sure you want to leave preset editing?")
        if sure:
            window.destroy()
            cameraSetup()

    def loadOne():
        data = presetDB.search(query.value == 1)
        if len(data) != 0:
            cmbxCameraNo.current(int(data[0]["camera_number"]) - 1)
            if data[0]["mode"] == "Webcam":
                cmbxMode.current(0)
                entIP1.delete(0, END)
                entIP2.delete(0, END)
                entIP3.delete(0, END)
                entIP4.delete(0, END)
                entIP1.config(state="disabled")
                entIP2.config(state="disabled")
                entIP3.config(state="disabled")
                entIP4.config(state="disabled")
            else:
                entIP1.config(state="normal")
                entIP2.config(state="normal")
                entIP3.config(state="normal")
                entIP4.config(state="normal")
                cmbxMode.current(1)
                entIP1.delete(0, END)
                entIP2.delete(0, END)
                entIP3.delete(0, END)
                entIP4.delete(0, END)
                entIP1.insert(0, data[0]["ip1"])
                entIP2.insert(0, data[0]["ip2"])
                entIP3.insert(0, data[0]["ip3"])
                entIP4.insert(0, data[0]["ip4"])
        elif len(data) == 0:
            cmbxCameraNo.current(0)
            cmbxMode.current(0)
            entIP1.delete(0, END)
            entIP2.delete(0, END)
            entIP3.delete(0, END)
            entIP4.delete(0, END)
            entIP1.config(state="disabled")
            entIP2.config(state="disabled")
            entIP3.config(state="disabled")
            entIP4.config(state="disabled")

    def loadTwo():
        data = presetDB.search(query.value == 2)
        if len(data) != 0:
            cmbxCameraNo.current(int(data[0]["camera_number"]) - 1)
            if data[0]["mode"] == "Webcam":
                cmbxMode.current(0)
                entIP1.delete(0, END)
                entIP2.delete(0, END)
                entIP3.delete(0, END)
                entIP4.delete(0, END)
                entIP1.config(state="disabled")
                entIP2.config(state="disabled")
                entIP3.config(state="disabled")
                entIP4.config(state="disabled")
            else:
                entIP1.config(state="normal")
                entIP2.config(state="normal")
                entIP3.config(state="normal")
                entIP4.config(state="normal")
                cmbxMode.current(1)
                entIP1.delete(0, END)
                entIP2.delete(0, END)
                entIP3.delete(0, END)
                entIP4.delete(0, END)
                entIP1.insert(0, data[0]["ip1"])
                entIP2.insert(0, data[0]["ip2"])
                entIP3.insert(0, data[0]["ip3"])
                entIP4.insert(0, data[0]["ip4"])
        elif len(data) == 0:
            cmbxCameraNo.current(0)
            cmbxMode.current(0)
            entIP1.delete(0, END)
            entIP2.delete(0, END)
            entIP3.delete(0, END)
            entIP4.delete(0, END)
            entIP1.config(state="disabled")
            entIP2.config(state="disabled")
            entIP3.config(state="disabled")
            entIP4.config(state="disabled")

    messagebox.showinfo("Wait", "Getting Camera info so click ok and wait.")
    cameraList = getCameraList()
    availCameraNo = len(cameraList)
    if availCameraNo > 3:
        for i in range(4, availCameraNo):
            cameraList.pop(4)
        availCameraNo = 4
    for i in range(availCameraNo):
        cameraList[i] += 1

    frmCombo = Frame(master=window, bg="#939393")
    frmCombo.pack(fill=X)

    frame = Frame(master=frmCombo, bg="#939393", height = 50)
    frame.grid(row=0, column=0, columnspan = 8, pady=5)

    frame = Frame(master=frmCombo, bg="#939393", width=175)
    frame.grid(row=1, column=0, pady=5)

    frame = Frame(master=frmCombo, bg="#C4C4C4")
    frame.grid(row=1, column=1, pady=5)

    v = StringVar(frame, "1")

    rdbtn1 = Radiobutton(frame, text="Preset 1", variable=v, value=1, bg="#939393", font=('roboto', 16), command = loadOne)
    rdbtn1.pack(padx = 5, pady = 5)

    frame = Frame(master=frmCombo, bg="#C4C4C4")
    frame.grid(row=1, column=2, pady=5)
    rdbtn2 = Radiobutton(frame, text="Preset 2", variable=v, value=2, bg="#939393", font=('roboto', 16), command = loadTwo)
    rdbtn2.pack(padx=5, pady=5)

    frame = Frame(master=frmCombo, bg="#939393", width = 50)
    frame.grid(row=1, column=3, pady=5)

    frame = Frame(master=frmCombo, bg="#C4C4C4")
    frame.grid(row=1, column=4, pady=5)
    lblCameraNo = Label(master=frame, text='Camera Number:', font=('roboto', 16), bg='#939393')
    lblCameraNo.pack(padx=5, pady=5)

    m = StringVar()

    frame = Frame(master=frmCombo, bg="#C4C4C4")
    frame.grid(row=1, column=5, pady=5)
    cmbxCameraNo = Combobox(frame, width = 10, state="readonly", textvariable=m, font=('roboto', 16))
    cmbxCameraNo['values'] = cameraList
    cmbxCameraNo.pack(padx=5, pady=5)
    cmbxCameraNo.current(0)

    frame = Frame(master=frmCombo, bg="#939393", width=50)
    frame.grid(row=1, column=6, pady=5)

    frame = Frame(master=frmCombo, bg="#C4C4C4")
    frame.grid(row=1, column=7, pady=5)
    lblMode = Label(master=frame, text='Mode:', font=('roboto', 16), bg='#939393')
    lblMode.pack(padx=5, pady=5)

    n = StringVar()

    frame = Frame(master=frmCombo, bg="#C4C4C4")
    frame.grid(row=1, column=8, pady=5)
    cmbxMode = Combobox(frame, width=10, state="readonly", textvariable=n, font=('roboto', 16))
    cmbxMode['values'] = ["Webcam","IP"]
    cmbxMode.pack(padx=5, pady=5)
    cmbxMode.current(0)

    frame = Frame(master=frmCombo, bg="#939393", height=50)
    frame.grid(row=2, column=0, columnspan=8, pady=5)

    frmIP = Frame(master=window, height=400, width=800, bg="#939393")
    frmIP.pack(fill=BOTH, expand=1)

    frame = Frame(master=frmIP, bg="#939393", width=325)
    frame.grid(row=0, column=0, pady=5, rowspan = 5)

    frame = Frame(master=frmIP, bg="#C4C4C4")
    frame.grid(row=0, column=1, pady=5)
    lblIP1 = Label(master=frame, text='IP 1:', font=('roboto', 24), bg='#C4C4C4')
    lblIP1.pack(padx=5, pady=5)

    frame = Frame(master=frmIP, bg="#C4C4C4")
    frame.grid(row=0, column=2, pady=5)
    entIP1 = Entry(master=frame, font=('roboto', 25), width=30, bg='#81D6E1')
    entIP1.pack(padx=5, pady=5)

    frame = Frame(master=frmIP, bg="#C4C4C4")
    frame.grid(row=1, column=1, pady=5)
    lblIP2 = Label(master=frame, text='IP 2:', font=('roboto', 24), bg='#C4C4C4')
    lblIP2.pack(padx=5, pady=5)

    frame = Frame(master=frmIP, bg="#C4C4C4")
    frame.grid(row=1, column=2, pady=5)
    entIP2 = Entry(master=frame, font=('roboto', 25), width=30, bg='#81D6E1')
    entIP2.pack(padx=5, pady=5)

    frame = Frame(master=frmIP, bg="#C4C4C4")
    frame.grid(row=2, column=1, pady=5)
    lblIP3 = Label(master=frame, text='IP 3:', font=('roboto', 24), bg='#C4C4C4')
    lblIP3.pack(padx=5, pady=5)

    frame = Frame(master=frmIP, bg="#C4C4C4")
    frame.grid(row=2, column=2, pady=5)
    entIP3 = Entry(master=frame, font=('roboto', 25), width=30, bg='#81D6E1')
    entIP3.pack(padx=5, pady=5)

    frame = Frame(master=frmIP, bg="#C4C4C4")
    frame.grid(row=3, column=1, pady=5)
    lblIP4 = Label(master=frame, text='IP 4:', font=('roboto', 24), bg='#C4C4C4')
    lblIP4.pack(padx=5, pady=5)

    frame = Frame(master=frmIP, bg="#C4C4C4")
    frame.grid(row=3, column=2, pady=5)
    entIP4 = Entry(master=frame, font=('roboto', 25), width=30, bg='#81D6E1')
    entIP4.pack(padx=5, pady=5)

    frame = Frame(master=frmIP, bg="#C4C4C4")
    frame.grid(row=4, column=1, columnspan=2, pady=5)
    btnSave = Button(master=frame, text='Delete Preset', font=('roboto', 20), width=35, bd=5, bg='#81D6E1', command=deletePreset)
    btnSave.pack(padx=5, pady=5)

    frame = Frame(master=frmIP, bg="#C4C4C4")
    frame.grid(row=5, column=1, columnspan=2, pady=5)
    btnSave = Button(master=frame, text='Save Preset', font=('roboto', 20), width=35, bd=5, bg='#81D6E1', command=savePreset)
    btnSave.pack(padx=5, pady=5)

    frame = Frame(master=frmIP, bg="#C4C4C4")
    frame.grid(row=6, column=1, columnspan=2, pady=5)
    btnSave = Button(master=frame, text='Cancel / Exit', font=('roboto', 20), width=35, bd=5, bg='#81D6E1', command=cancel)
    btnSave.pack(padx=5, pady=5)

    def cmbxChanged(event):
        data = presetDB.search(query.value == 1)
        if cmbxMode.get() == "Webcam":
            entIP1.delete(0, END)
            entIP2.delete(0, END)
            entIP3.delete(0, END)
            entIP4.delete(0, END)
            entIP1.config(state = "disabled")
            entIP2.config(state="disabled")
            entIP3.config(state="disabled")
            entIP4.config(state="disabled")
            cmbxCameraNo["values"] = cameraList
            cmbxCameraNo.current(0)
        elif cmbxMode.get() == "IP":
            entIP1.config(state="normal")
            entIP2.config(state="normal")
            entIP3.config(state="normal")
            entIP4.config(state="normal")
            ipCameraList = [1,2,3,4]
            cmbxCameraNo["values"] = ipCameraList

    cmbxMode.bind("<<ComboboxSelected>>", cmbxChanged)
    rdbtn1.bind("<<>>")

    loadOne()
    if cmbxMode.get() == "Webcam":
        entIP1.delete(0, END)
        entIP2.delete(0, END)
        entIP3.delete(0, END)
        entIP4.delete(0, END)
        entIP1.config(state = "disabled")
        entIP2.config(state="disabled")
        entIP3.config(state="disabled")
        entIP4.config(state="disabled")
    elif cmbxMode.get() == "IP":
        entIP1.config(state="normal")
        entIP2.config(state="normal")
        entIP3.config(state="normal")
        entIP4.config(state="normal")
    window.mainloop()

def cameraView(selectedPreset):
    # Create Window
    window = Tk()
    window.title("Criminal Detection | Camera View")
    w = 1280
    h = 720
    ws = window.winfo_screenwidth()
    hs = window.winfo_screenheight()
    x = (ws / 2) - (w / 2)
    y = 0
    window.geometry("%dx%d+%d+%d" % (w, h, x, y))
    window.resizable(0, 0)
    window.iconbitmap("imagesIcons/CDLogo.ico")
    window.config(bg="#939393")

    presetData = presetDB.search(query.value == selectedPreset)
    cameraNo = presetData[0]["camera_number"]
    mode = presetData[0]["mode"]

    messagebox.showinfo("Wait", "Loading all the selected cameras click ok and wait.")

    if cameraNo == "1":
        if mode == "Webcam":
            cap0 = cv2.VideoCapture(0)
        elif mode == "IP":
            cap0 = cv2.VideoCapture(presetData[0]["ip1"])
    elif cameraNo == "2":
        if mode == "Webcam":
            cap0 = cv2.VideoCapture(0)
            cap1 = cv2.VideoCapture(1)
        elif mode == "IP":
            cap0 = cv2.VideoCapture(presetData[0]["ip1"])
            cap1 = cv2.VideoCapture(presetData[0]["ip2"])
    elif cameraNo == "3":
        if mode == "Webcam":
            cap0 = cv2.VideoCapture(0)
            cap1 = cv2.VideoCapture(1)
            cap2 = cv2.VideoCapture(2)
        elif mode == "IP":
            cap0 = cv2.VideoCapture(presetData[0]["ip1"])
            cap1 = cv2.VideoCapture(presetData[0]["ip2"])
            cap2 = cv2.VideoCapture(presetData[0]["ip3"])
    elif cameraNo == "4":
        if mode == "Webcam":
            cap0 = cv2.VideoCapture(0)
            cap1 = cv2.VideoCapture(1)
            cap2 = cv2.VideoCapture(2)
            cap3 = cv2.VideoCapture(3)
        elif mode == "IP":
            cap0 = cv2.VideoCapture(presetData[0]["ip1"])
            cap1 = cv2.VideoCapture(presetData[0]["ip2"])
            cap2 = cv2.VideoCapture(presetData[0]["ip3"])
            cap3 = cv2.VideoCapture(presetData[0]["ip4"])

    def showFrame():
        if cameraNo == "1":
            _, frame1 = cap0.read()
            frame1 = imutils.resize(frame1, height=300, width=400)
            frame1 = cv2.flip(frame1, 1)
            cv2image1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2RGBA)
            img1 = Image.fromarray(cv2image1)
            imgtk1 = ImageTk.PhotoImage(image=img1)
            lblVideo1.imgtk1 = imgtk1
            lblVideo1.configure(image=imgtk1)
            lblVideo1.after(50, showFrame)
        elif cameraNo == "2":
            _, frame0 = cap0.read()
            frame0 = imutils.resize(frame0, height=300, width=400)
            frame0 = cv2.flip(frame0, 1)
            cv2image0 = cv2.cvtColor(frame0, cv2.COLOR_BGR2RGBA)
            img0 = Image.fromarray(cv2image0)
            imgtk0 = ImageTk.PhotoImage(image=img0)
            lblVideo1.imgtk0 = imgtk0
            lblVideo1.configure(image=imgtk0)

            _, frame1 = cap1.read()
            frame1 = imutils.resize(frame1, height=300, width=400)
            frame1 = cv2.flip(frame1, 1)
            cv2image1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2RGBA)
            img1 = Image.fromarray(cv2image1)
            imgtk1 = ImageTk.PhotoImage(image=img1)
            lblVideo2.imgtk1 = imgtk1
            lblVideo2.configure(image=imgtk1)
            lblVideo2.after(50, showFrame)

        elif cameraNo == "3":
            _, frame0 = cap0.read()
            frame0 = imutils.resize(frame0, height=300, width=400)
            frame0 = cv2.flip(frame0, 1)
            cv2image0 = cv2.cvtColor(frame0, cv2.COLOR_BGR2RGBA)
            img0 = Image.fromarray(cv2image0)
            imgtk0 = ImageTk.PhotoImage(image=img0)
            lblVideo1.imgtk0 = imgtk0
            lblVideo1.configure(image=imgtk0)

            _, frame1 = cap1.read()
            frame1 = imutils.resize(frame1, height=300, width=400)
            frame1 = cv2.flip(frame1, 1)
            cv2image1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2RGBA)
            img1 = Image.fromarray(cv2image1)
            imgtk1 = ImageTk.PhotoImage(image=img1)
            lblVideo2.imgtk1 = imgtk1
            lblVideo2.configure(image=imgtk1)

            _, frame2 = cap2.read()
            frame2 = imutils.resize(frame2, height=300, width=400)
            frame2 = cv2.flip(frame2, 1)
            cv2image2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2RGBA)
            img2 = Image.fromarray(cv2image2)
            imgtk2 = ImageTk.PhotoImage(image=img2)
            lblVideo3.imgtk2 = imgtk2
            lblVideo3.configure(image=imgtk2)
            lblVideo3.after(50, showFrame)

        elif cameraNo == "4":
            _, frame0 = cap0.read()
            frame0 = imutils.resize(frame0, height=300, width=400)
            frame0 = cv2.flip(frame0, 1)
            cv2image0 = cv2.cvtColor(frame0, cv2.COLOR_BGR2RGBA)
            img0 = Image.fromarray(cv2image0)
            imgtk0 = ImageTk.PhotoImage(image=img0)
            lblVideo1.imgtk0 = imgtk0
            lblVideo1.configure(image=imgtk0)

            _, frame1 = cap1.read()
            frame1 = imutils.resize(frame1, height=300, width=400)
            frame1 = cv2.flip(frame1, 1)
            cv2image1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2RGBA)
            img1 = Image.fromarray(cv2image1)
            imgtk1 = ImageTk.PhotoImage(image=img1)
            lblVideo2.imgtk1 = imgtk1
            lblVideo2.configure(image=imgtk1)

            _, frame2 = cap2.read()
            frame2 = imutils.resize(frame2, height=300, width=400)
            frame2 = cv2.flip(frame2, 1)
            cv2image2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2RGBA)
            img2 = Image.fromarray(cv2image2)
            imgtk2 = ImageTk.PhotoImage(image=img2)
            lblVideo3.imgtk2 = imgtk2
            lblVideo3.configure(image=imgtk2)

            _, frame3 = cap3.read()
            frame3 = imutils.resize(frame3, height=300, width=400)
            frame3 = cv2.flip(frame3, 1)
            cv2image3 = cv2.cvtColor(frame3, cv2.COLOR_BGR2RGBA)
            img3 = Image.fromarray(cv2image3)
            imgtk3 = ImageTk.PhotoImage(image=img3)
            lblVideo4.imgtk3 = imgtk3
            lblVideo4.configure(image=imgtk3)
            lblVideo4.after(50, showFrame)

    def next():
        window.destroy()
        if cameraNo == "1":
            cap0.release()
        elif cameraNo == "2":
            cap0.release()
            cap1.release()
        elif cameraNo == "3":
            cap0.release()
            cap1.release()
            cap2.release()
        elif cameraNo == "4":
            cap0.release()
            cap1.release()
            cap2.release()
            cap3.release()
        cv2.destroyAllWindows()
        screeningMode()


    frmTop = Frame(master=window, bg="#939393")
    frmTop.pack(fill=X)

    frame = Frame(master=frmTop, bg="#939393", width=525)
    frame.grid(row=0, column=0, pady=5)

    frame = Frame(master=frmTop, bg="#939393")
    frame.grid(row=0, column=1, pady=5)
    lblCameraView = Label(master=frame, text='Camera View', font=('roboto', 24), bg='#939393')
    lblCameraView.pack(padx=5, pady=5)

    frame = Frame(master=frmTop, bg="#C4C4C4")
    frame.grid(row=0, column=2, pady=2, padx=100)
    btnNext = Button(master=frame, text='⇒', font=('roboto', 15), bd=0, width = 10, bg='#81D6E1', command=next)
    btnNext.pack(padx=5, pady=5)

    frmBottom = Frame(master=window, bg="#939393")
    frmBottom.pack(fill=X)

    frame = Frame(master=frmBottom, bg="#939393", width = 225)
    frame.grid(row=0, column=0, rowspan=2, pady=5)

    frame = Frame(master=frmBottom, bg="#C4C4C4", height=300, width=400)
    frame.grid(row=0, column=1, pady=5, padx=5)
    myimage = ImageTk.PhotoImage(Image.open("white.png"))
    lblVideo1 = Label(master=frame, image = myimage)
    lblVideo1.pack(padx=1, pady=1)

    frame = Frame(master=frmBottom, bg="#C4C4C4", height=300, width=400)
    frame.grid(row=0, column=2, pady=5, padx=5)
    lblVideo2 = Label(master=frame, image = myimage)
    lblVideo2.pack(padx=1, pady=1)

    frame = Frame(master=frmBottom, bg="#C4C4C4", height=300, width=400)
    frame.grid(row=1, column=1, pady=5, padx=5)
    lblVideo3 = Label(master=frame, image = myimage)
    lblVideo3.pack(padx=1, pady=1)

    frame = Frame(master=frmBottom, bg="#C4C4C4", height=300, width=400)
    frame.grid(row=1, column=2, pady=5, padx=5)
    lblVideo4 = Label(master=frame, image = myimage)
    lblVideo4.pack(padx=1, pady=1)

    showFrame()

    window.mainloop()

isDetectionByPhoto = -1

def screeningMode():
    window = Tk()
    window.title("Criminal Detection | Screening mode")
    w = 1280
    h = 720
    ws = window.winfo_screenwidth()
    hs = window.winfo_screenheight()
    x = (ws / 2) - (w / 2)
    y = 0
    window.geometry("%dx%d+%d+%d" % (w, h, x, y))
    window.resizable(0, 0)
    window.iconbitmap("imagesIcons/CDLogo.ico")
    window.config(bg="#939393")

    def clickedPhoto():
        global isDetectionByPhoto
        isDetectionByPhoto = 1
        window.destroy()
        photoBrowser()

    def clickedLive():
        global isDetectionByPhoto
        isDetectionByPhoto = 0
        window.destroy()
        liveFeed()

    frame = Frame(master=window, bg="#939393", width=320)
    frame.grid(row=0, column=0)

    frame = Frame(master=window, bg="#939393")
    frame.grid(row=0, column=1, pady=50, columnspan=2)
    lblText = Label(master=frame, text='Screening mode', font=('roboto', 32), bg='#939393').pack(padx=5, pady=5)

    frame = Frame(master=window, bg="#C4C4C4")
    frame.grid(row=1, column=1, columnspan=2, pady=30)
    btnLogin = Button(master=frame, text='Detection by Photo', font=('roboto', 32), width=25, bd=5, bg='#81D6E1', command=clickedPhoto)
    btnLogin.pack(padx=5, pady=5)

    frame = Frame(master=window, bg="#C4C4C4")
    frame.grid(row=2, column=1, columnspan=2, pady=30)
    btnLogin = Button(master=frame, text='Live Detection', font=('roboto', 32), width=25, bd=5, bg='#81D6E1', command=clickedLive)
    btnLogin.pack(padx=5, pady=5)

    window.mainloop()

img = []

def photoBrowser():
    window = Tk()
    window.title("Criminal Detection | Photo Browser")
    w = 1280
    h = 720
    ws = window.winfo_screenwidth()
    hs = window.winfo_screenheight()
    x = (ws / 2) - (w / 2)
    y = 0
    window.geometry("%dx%d+%d+%d" % (w, h, x, y))
    window.resizable(0, 0)
    window.iconbitmap("imagesIcons/CDLogo.ico")
    window.config(bg="#939393")

    def create_mask():
        mask = Image.new('L', (300, 300), 0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((0, 0) + mask.size, fill=255)
        return mask

    def browseImg():
        global img

        imgPath = filedialog.askopenfilename()
        img  = Image.open(imgPath)

        width, height = img.size
        if width > height:
            result = Image.new(img.mode, (width, width), (0,0,0))
            result.paste(img, (0, (width - height) // 2))
            img = result
        else:
            result = Image.new(img.mode, (height, height), (0,0,0))
            result.paste(img, ((height - width) // 2, 0))
            img = result

        img = img.resize((300,300))
        img = np.array(img)

        mask = create_mask()
        mask = np.array(mask)

        maskedImgOne = cv2.bitwise_or(img, img, mask=mask)

        mask = cv2.bitwise_not(mask)
        modifiedDarkGrey = cv2.bitwise_or(imgDarkGrey, imgDarkGrey, mask=mask)

        finalImg = cv2.bitwise_or(maskedImgOne, modifiedDarkGrey)

        finalImgPIL = Image.fromarray(finalImg)
        finalImgPIL = ImageTk.PhotoImage(finalImgPIL)

        lblPhoto.finalImgPIL = finalImgPIL
        lblPhoto.configure(image = finalImgPIL)

    def next():
        global img

        try:
            if img.any():
                window.destroy()
                liveFeed()
            else:
                messagebox.showwarning("Alert","Please select a photo.")
        except:
            messagebox.showwarning("Alert","Please select a photo.")




    imgLightGrey = cv2.imread("lightGrey.png")

    imgDarkGrey = cv2.imread("darkGrey.png")

    mask = create_mask()
    mask = np.array(mask)

    maskedImgOne = cv2.bitwise_or(imgLightGrey, imgLightGrey, mask = mask)

    mask = cv2.bitwise_not(mask)
    modifiedDarkGrey = cv2.bitwise_or(imgDarkGrey, imgDarkGrey, mask=mask)

    finalImg = cv2.bitwise_or(maskedImgOne, modifiedDarkGrey)

    finalImgPIL = Image.fromarray(finalImg)
    finalImgPIL = ImageTk.PhotoImage(finalImgPIL)


    frmSpace = Frame(master=window, bg="#939393", height=150, width=140)
    frmSpace.grid(row=0, column=0)

    frmLeft = Frame(master=window, bg="#939393")
    frmLeft.grid(row=1, column=1)

    lblPhoto = Label(master=frmLeft, image = finalImgPIL, bd =0)
    lblPhoto.pack(padx=70, pady=1)

    frmRight = Frame(master=window, bg="#939393", height = 400, width = 500)
    frmRight.grid(row=1, column=2)

    frame = Frame(master=frmRight, bg="#939393")
    frame.grid(row=0, column=0, sticky = "W")
    lblName = Label(master=frame, text='Name:', font=('roboto', 25), bg='#939393').pack(padx=5, pady=5)

    frame = Frame(master=frmRight, bg="#C4C4C4")
    frame.grid(row=1, column=0, pady=5)
    entName = Entry(master=frame, font=('roboto', 25), width=30,bd = 0, bg='#939393', disabledbackground='#939393', state = "disabled")
    entName.pack()

    frame = Frame(master=frmRight, bg="#939393")
    frame.grid(row=2, column=0, sticky = "W")
    lblRecord = Label(master=frame, text='Record:', font=('roboto', 25), bg='#939393').pack(padx=5, pady=5)

    frame = Frame(master=frmRight, bg="#C4C4C4")
    frame.grid(row=3, column=0, pady=5)
    entRecord = Entry(master=frame, font=('roboto', 25), width=30,bd = 0, bg='#939393', disabledbackground='#939393', state = "disabled")
    entRecord.pack()

    frame = Frame(master=frmRight, bg="#C4C4C4")
    frame.grid(row=4, column=0, pady=5)
    btnBrowse = Button(master=frame, text='Browse', font=('roboto', 25), width=28, bd=5, bg='#81D6E1', command=browseImg)
    btnBrowse.pack(padx=5, pady=5)

    frame = Frame(master=frmRight, bg="#C4C4C4")
    frame.grid(row=5, column=0, pady=5)
    btnBrowse = Button(master=frame, text='Next', font=('roboto', 25), width=28, bd=5, bg='#81D6E1', command=next)
    btnBrowse.pack(padx=5, pady=5)

    window.mainloop()


def liveFeed():
    window = Tk()
    window.title("Criminal Detection | Live Feed")
    w = 1280
    h = 720
    ws = window.winfo_screenwidth()
    hs = window.winfo_screenheight()
    x = (ws / 2) - (w / 2)
    y = 0
    window.geometry("%dx%d+%d+%d" % (w, h, x, y))
    window.resizable(0, 0)
    window.iconbitmap("imagesIcons/CDLogo.ico")
    window.config(bg="#939393")

    global selectedPresetNumber

    if selectedPresetNumber == 0:
        selectedPresetNumber = 1

    presetData = presetDB.search(query.value == selectedPresetNumber)

    cameraNo = presetData[0]["camera_number"]
    mode = presetData[0]["mode"]

    frmTop = Frame(master=window, bg="#939393", height = 20)
    frmTop.grid(row=0, column=0)

    frmBottom = Frame(master=window, bg="#939393")
    frmBottom.grid(row = 1, column = 0)

    frame = Frame(master=frmBottom, bg="#939393", width=225)
    frame.grid(row=0, column=0, rowspan=2)

    frame = Frame(master=frmBottom, bg="#C4C4C4", height=350, width=500)
    frame.grid(row=0, column=1, padx=5, pady=5)
    myimage = ImageTk.PhotoImage(Image.open("white.png"))
    lblVideo1 = Label(master=frame, image=myimage, bd = 1)
    lblVideo1.pack(padx=1, pady=1)

    frame = Frame(master=frmBottom, bg="#C4C4C4", height=350, width=500)
    frame.grid(row=0, column=2, padx=5, pady=5)
    lblVideo2 = Label(master=frame, image=myimage, bd = 1)
    lblVideo2.pack(padx=1, pady=1)

    frame = Frame(master=frmBottom, bg="#C4C4C4", height=350, width=500)
    frame.grid(row=1, column=1, padx=5, pady=5)
    lblVideo3 = Label(master=frame, image=myimage, bd = 1)
    lblVideo3.pack(padx=1, pady=1)

    frame = Frame(master=frmBottom, bg="#C4C4C4", height=350, width=500)
    frame.grid(row=1, column=2, padx=5, pady=5)
    lblVideo4 = Label(master=frame, image=myimage, bd = 1)
    lblVideo4.pack(padx=1, pady=1)

    def detected():
        window.destroy()
        alert()

    if isDetectionByPhoto == 1:
        pass

    elif isDetectionByPhoto == 0:
        pass

    elif isDetectionByPhoto == -1:
        print("Something is wrong how did you reach here...!")

    if cameraNo == "1":
        if mode == "Webcam":
            cap0 = cv2.VideoCapture(0)
        elif mode == "IP":
            cap0 = cv2.VideoCapture(presetData[0]["ip1"])
    elif cameraNo == "2":
        if mode == "Webcam":
            cap0 = cv2.VideoCapture(0)
            cap1 = cv2.VideoCapture(1)
        elif mode == "IP":
            cap0 = cv2.VideoCapture(presetData[0]["ip1"])
            cap1 = cv2.VideoCapture(presetData[0]["ip2"])
    elif cameraNo == "3":
        if mode == "Webcam":
            cap0 = cv2.VideoCapture(0)
            cap1 = cv2.VideoCapture(1)
            cap2 = cv2.VideoCapture(2)
        elif mode == "IP":
            cap0 = cv2.VideoCapture(presetData[0]["ip1"])
            cap1 = cv2.VideoCapture(presetData[0]["ip2"])
            cap2 = cv2.VideoCapture(presetData[0]["ip3"])
    elif cameraNo == "4":
        if mode == "Webcam":
            cap0 = cv2.VideoCapture(0)
            cap1 = cv2.VideoCapture(1)
            cap2 = cv2.VideoCapture(2)
            cap3 = cv2.VideoCapture(3)
        elif mode == "IP":
            cap0 = cv2.VideoCapture(presetData[0]["ip1"])
            cap1 = cv2.VideoCapture(presetData[0]["ip2"])
            cap2 = cv2.VideoCapture(presetData[0]["ip3"])
            cap3 = cv2.VideoCapture(presetData[0]["ip4"])

    def showFrame():
        if cameraNo == "1":
            _, frame1 = cap0.read()
            frame1 = imutils.resize(frame1, height=300, width=400)
            frame1 = cv2.flip(frame1, 1)
            cv2image1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2RGBA)
            img1 = Image.fromarray(cv2image1)
            imgtk1 = ImageTk.PhotoImage(image=img1)
            lblVideo1.imgtk1 = imgtk1
            lblVideo1.configure(image=imgtk1)
            lblVideo1.after(50, showFrame)
        elif cameraNo == "2":
            _, frame0 = cap0.read()
            frame0 = imutils.resize(frame0, height=300, width=400)
            frame0 = cv2.flip(frame0, 1)
            cv2image0 = cv2.cvtColor(frame0, cv2.COLOR_BGR2RGBA)
            img0 = Image.fromarray(cv2image0)
            imgtk0 = ImageTk.PhotoImage(image=img0)
            lblVideo1.imgtk0 = imgtk0
            lblVideo1.configure(image=imgtk0)

            _, frame1 = cap1.read()
            frame1 = imutils.resize(frame1, height=300, width=400)
            frame1 = cv2.flip(frame1, 1)
            cv2image1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2RGBA)
            img1 = Image.fromarray(cv2image1)
            imgtk1 = ImageTk.PhotoImage(image=img1)
            lblVideo2.imgtk1 = imgtk1
            lblVideo2.configure(image=imgtk1)
            lblVideo2.after(50, showFrame)

        elif cameraNo == "3":
            _, frame0 = cap0.read()
            frame0 = imutils.resize(frame0, height=300, width=400)
            frame0 = cv2.flip(frame0, 1)
            cv2image0 = cv2.cvtColor(frame0, cv2.COLOR_BGR2RGBA)
            img0 = Image.fromarray(cv2image0)
            imgtk0 = ImageTk.PhotoImage(image=img0)
            lblVideo1.imgtk0 = imgtk0
            lblVideo1.configure(image=imgtk0)

            _, frame1 = cap1.read()
            frame1 = imutils.resize(frame1, height=300, width=400)
            frame1 = cv2.flip(frame1, 1)
            cv2image1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2RGBA)
            img1 = Image.fromarray(cv2image1)
            imgtk1 = ImageTk.PhotoImage(image=img1)
            lblVideo2.imgtk1 = imgtk1
            lblVideo2.configure(image=imgtk1)

            _, frame2 = cap2.read()
            frame2 = imutils.resize(frame2, height=300, width=400)
            frame2 = cv2.flip(frame2, 1)
            cv2image2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2RGBA)
            img2 = Image.fromarray(cv2image2)
            imgtk2 = ImageTk.PhotoImage(image=img2)
            lblVideo3.imgtk2 = imgtk2
            lblVideo3.configure(image=imgtk2)
            lblVideo3.after(50, showFrame)

        elif cameraNo == "4":
            _, frame0 = cap0.read()
            frame0 = imutils.resize(frame0, height=300, width=400)
            frame0 = cv2.flip(frame0, 1)
            cv2image0 = cv2.cvtColor(frame0, cv2.COLOR_BGR2RGBA)
            img0 = Image.fromarray(cv2image0)
            imgtk0 = ImageTk.PhotoImage(image=img0)
            lblVideo1.imgtk0 = imgtk0
            lblVideo1.configure(image=imgtk0)

            _, frame1 = cap1.read()
            frame1 = imutils.resize(frame1, height=300, width=400)
            frame1 = cv2.flip(frame1, 1)
            cv2image1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2RGBA)
            img1 = Image.fromarray(cv2image1)
            imgtk1 = ImageTk.PhotoImage(image=img1)
            lblVideo2.imgtk1 = imgtk1
            lblVideo2.configure(image=imgtk1)

            _, frame2 = cap2.read()
            frame2 = imutils.resize(frame2, height=300, width=400)
            frame2 = cv2.flip(frame2, 1)
            cv2image2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2RGBA)
            img2 = Image.fromarray(cv2image2)
            imgtk2 = ImageTk.PhotoImage(image=img2)
            lblVideo3.imgtk2 = imgtk2
            lblVideo3.configure(image=imgtk2)

            _, frame3 = cap3.read()
            frame3 = imutils.resize(frame3, height=300, width=400)
            frame3 = cv2.flip(frame3, 1)
            cv2image3 = cv2.cvtColor(frame3, cv2.COLOR_BGR2RGBA)
            img3 = Image.fromarray(cv2image3)
            imgtk3 = ImageTk.PhotoImage(image=img3)
            lblVideo4.imgtk3 = imgtk3
            lblVideo4.configure(image=imgtk3)
            lblVideo4.after(50, showFrame)

    showFrame()

    window.mainloop()

def alert():
    window = Tk()
    window.title("Criminal Detection | Alert")
    w = 1280
    h = 720
    ws = window.winfo_screenwidth()
    hs = window.winfo_screenheight()
    x = (ws / 2) - (w / 2)
    y = 0
    window.geometry("%dx%d+%d+%d" % (w, h, x, y))
    window.resizable(0, 0)
    window.iconbitmap("imagesIcons/CDLogo.ico")
    window.config(bg="#939393")

    tmpImage = ImageTk.PhotoImage(Image.open("White500x350.png"))

    frmSpace = Frame(master=window, bg="#939393")
    frmSpace.grid(row=0, column=0, columnspan = 3, pady=5)
    lblText = Label(master=frmSpace, text='Alert', font=('roboto', 24), bg='#939393').pack(padx=500, pady=10)

    frmLeft = Frame(master=window, bg="#939393")
    frmLeft.grid(row=1, column=1)

    lblPhoto = Label(master=frmLeft, image=tmpImage, bd=0)
    lblPhoto.pack(padx=70, pady=1)

    frmRight = Frame(master=window, bg="#939393", height=400, width=500)
    frmRight.grid(row=1, column=2)

    frame = Frame(master=frmRight, bg="#939393")
    frame.grid(row=0, column=0, sticky="W")
    lblName = Label(master=frame, text='Name:', font=('roboto', 25), bg='#939393').pack(padx=5, pady=5)

    frame = Frame(master=frmRight, bg="#C4C4C4")
    frame.grid(row=1, column=0, pady=5)
    entName = Entry(master=frame, font=('roboto', 25), width=30, bd=0, disabledbackground='#939393', state="disabled")
    entName.pack()

    frame = Frame(master=frmRight, bg="#939393")
    frame.grid(row=2, column=0, sticky="W")
    lblRecord = Label(master=frame, text='Record:', font=('roboto', 25), bg='#939393').pack(padx=5, pady=5)

    frame = Frame(master=frmRight, bg="#C4C4C4")
    frame.grid(row=3, column=0, pady=5)
    entRecord = Entry(master=frame, font=('roboto', 25), width=30, bd=0, disabledbackground='#939393', state="disabled")
    entRecord.pack()

    frame = Frame(master=frmRight, bg="#939393")
    frame.grid(row=4, column=0, sticky="W")
    lblLocation = Label(master=frame, text='Location:', font=('roboto', 25), bg='#939393').pack(padx=5, pady=5)

    frame = Frame(master=frmRight, bg="#C4C4C4")
    frame.grid(row=5, column=0, pady=5)
    entLocation = Entry(master=frame, font=('roboto', 25), width=30, bd=0, disabledbackground='#939393', state="disabled")
    entLocation.pack()

    frmBottom = Frame(master=window, bg="#939393", height = 100, width=100)
    frmBottom.grid(row=2, column=0, columnspan=3, pady=10)

    frame = Frame(master=frmBottom, bg="#C4C4C4")
    frame.grid(row=4, column=0, pady=5)
    btnContinue = Button(master=frame, text='Continue', font=('roboto', 25), width=30, bd=5, bg='#81D6E1', command=None)
    btnContinue.pack(padx=5, pady=5)

    window.mainloop()


login()