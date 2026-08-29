from tkinter import *
import subprocess
import sys

def giris():
    pencere.destroy()
    subprocess.Popen([sys.executable,"giris_ekranı.py"])

def kayit():
    pencere.destroy()
    subprocess.Popen([sys.executable,"kayıt_ekranı.py"])

pencere=Tk()
pencere.configure(bg="#f8fafc")
pencere.geometry("400x300")
pencere.title("ilksayfa")

yazı=Label(pencere,text="HOŞGELDİNİZ",bg="#f8fafc",fg="#0f172a",font=("Segoe UI", 16, "bold"))
yazı.place(x=50,y=30,width=300)

yazı=Label(pencere,text="To-Do List Uygulaması",bg="#f8fafc",fg="#64748b",font=("Segoe UI", 10, "italic"))
yazı.place(x=50,y=60,width=300)

btn=Button(pencere,text="Kayıt Ol",command=kayit,bg="#e0e7ff", fg="#3730a3", activebackground="#c7d2fe", activeforeground="#312e81", font=("Segoe UI", 10, "bold"), relief="flat", bd=0,cursor="hand2")
btn.place(x=60, y=120, width=280, height=42)

btn1=Button(pencere,text="Giriş Sayfası",command=giris,bg="#2563eb", fg="#ffffff", activebackground="#1d4ed8", activeforeground="#ffffff", font=("Segoe UI", 10, "bold"), relief="flat", bd=0,cursor="hand2")
btn1.place(x=60, y=175, width=280, height=42)

pencere.mainloop()