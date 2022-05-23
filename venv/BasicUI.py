from tkinter import *

def login():
    print('Login')

def forgotPwd():
    print('Forgot Password')

window = Tk()
window.geometry('1280x720')
window.title('Criminal Detection')
window.resizable(0,0)
window.config(bg = '#939393')

cnvCircle =  Canvas(window, bg = '#939393', width=150 ,height =150, highlightthickness=0)
cnvCircle.create_oval(0,0,148,148,outline = 'black',width = 1)
cnvCircle.place(x=580,y=50)

lUsername = Label(window, text = 'Username:', font = ('roboto',24),bg = '#939393').place(x=292,y=268)

txtUsername = Entry(window)
txtUsername.config(font = ('roboto',24), width = '30', bg = '#81D6E1')
txtUsername.place(x=464,y=268)

lPassword = Label(window, text = 'Password:', font = ('roboto',24),bg = '#939393').place(x=292,y=338)

txtPassword = Text(window,font = ('roboto',24), height = '1', width = '30')
txtPassword = Entry(window,show = '*')
txtPassword.config(font = ('roboto',24), width = '30', bg = '#81D6E1')
txtPassword.place(x=464,y=338)

btnLogin = Button(window ,text = 'Login', font = ('roboto',32),width=28,bd=5,bg = '#81D6E1', command = login).place(x=294,y=408)

btnForgotPwd = Button(window ,text = 'Forgot Password?', command = forgotPwd,bg = '#939393', borderwidth = 0,font = ('arial',20,'underline','bold')).place(x=292,y=508)


window.mainloop()