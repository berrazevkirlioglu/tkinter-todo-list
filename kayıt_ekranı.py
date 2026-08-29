from tkinter import *
from tkinter import messagebox
import subprocess
import sys
import sqlite3

def uyari():
    ad = text2.get().strip()
    soyad = text3.get().strip()
    mail = text4.get().strip()
    sifre = text5.get()

    if not ad or not soyad or not mail or not sifre:
        messagebox.showerror("Eksik Bilgi", "Lütfen tüm alanları eksiksiz doldurun!")
        return

    try:
        conn = sqlite3.connect("yapilicaklar.db")
        cursor = conn.cursor()

        cursor.execute('SELECT * FROM "users" WHERE mail=?', (mail,))
        mevcut_kullanici = cursor.fetchone()

        if mevcut_kullanici:
            messagebox.showerror("Hata", "Bu e-posta adresi zaten kayıtlı!")
            conn.close()
            return

        cursor.execute("""
            INSERT INTO "users" (ad, soyad, mail, sifre) 
            VALUES (?, ?, ?, ?)
        """, (ad, soyad, mail, sifre))
        
        conn.commit()
        conn.close()

        messagebox.showinfo("Başarılı", "Hesabınız başarıyla oluşturuldu!")

        text2.delete(0, END)
        text3.delete(0, END)
        text4.delete(0, END)
        text5.delete(0, END)
  
        giris_sayfasina_git()

    except sqlite3.Error as hata:
        messagebox.showerror("Veritabanı Hatası", f"Bir hata oluştu:\n{hata}")

def giris_sayfasina_git():
    pencere.destroy()
    subprocess.Popen([sys.executable, "giris_ekranı.py"])

pencere = Tk()
pencere.configure(bg="#f8fafc")
pencere.geometry("420x620")
pencere.title("Kayıt Ekranı")

yazi = Label(pencere, text="Yeni Hesap Oluştur", bg="#f8fafc", fg="#0f172a", font=("Segoe UI", 15, "bold"))
yazi.place(x=40, y=20, width=340)

yazi1 = Label(pencere, text="Görevlerinizi yönetmek için bilgilerinizi girin", bg="#f8fafc", fg="#64748b", font=("Segoe UI", 9))
yazi1.place(x=40, y=50, width=340)


yazi2 = Label(pencere, text="Ad", bg="#f8fafc", fg="#334155", font=("Segoe UI", 9, "bold"))
yazi2.place(x=40, y=90)

text2 = Entry(pencere, bg="#ffffff", fg="#0f172a", insertbackground="#2563eb", relief="solid", bd=1, font=("Segoe UI", 10))
text2.place(x=40, y=115, width=340, height=36)


yazi3 = Label(pencere, text="Soyad", bg="#f8fafc", fg="#334155", font=("Segoe UI", 9, "bold"))
yazi3.place(x=40, y=165)

text3 = Entry(pencere, bg="#ffffff", fg="#0f172a", insertbackground="#2563eb", relief="solid", bd=1, font=("Segoe UI", 10))
text3.place(x=40, y=190, width=340, height=36)


yazi4 = Label(pencere, text="E-Posta Adresi", bg="#f8fafc", fg="#334155", font=("Segoe UI", 9, "bold"))
yazi4.place(x=40, y=240)

text4 = Entry(pencere, bg="#ffffff", fg="#0f172a", insertbackground="#2563eb", relief="solid", bd=1, font=("Segoe UI", 10))
text4.place(x=40, y=265, width=340, height=36)


yazi5 = Label(pencere, text="Şifre", bg="#f8fafc", fg="#334155", font=("Segoe UI", 9, "bold"))
yazi5.place(x=40, y=315)

text5 = Entry(pencere, bg="#ffffff", fg="#0f172a", insertbackground="#2563eb", relief="solid", bd=1, font=("Segoe UI", 10), show="*")
text5.place(x=40, y=340, width=340, height=36)


btn = Button(pencere, text="Kayıt Ol", command=uyari, bg="#2563eb", fg="#ffffff", activebackground="#1d4ed8", activeforeground="#ffffff", font=("Segoe UI", 10, "bold"), relief="flat", bd=0, cursor="hand2")
btn.place(x=40, y=410, width=340, height=42)

btn1 = Button(pencere, text="Zaten hesabın var mı? Giriş Yap", command=giris_sayfasina_git, bg="#e0e7ff", fg="#3730a3", activebackground="#c7d2fe", activeforeground="#312e81", font=("Segoe UI", 9, "bold"), relief="flat", bd=0, cursor="hand2")
btn1.place(x=40, y=465, width=340, height=38)

pencere.mainloop()