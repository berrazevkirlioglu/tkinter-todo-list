from tkinter import *
from tkinter import messagebox
import subprocess
import sys
import sqlite3

def giris_yap():
    mail = text2.get().strip()
    sifre = text3.get()

    if not mail or not sifre:
        messagebox.showerror("Eksik Bilgi", "Lütfen tüm alanları doldurun!")
        return

    try:
        conn = sqlite3.connect("yapilicaklar.db")
        cursor = conn.cursor()

        cursor.execute(
            'SELECT * FROM "users" WHERE mail = ? AND sifre = ?',
            (mail, sifre)
        )
        kullanici = cursor.fetchone()
        conn.close()

        if kullanici:
            user_id = kullanici[0]
            ad = kullanici[1] if len(kullanici) > 1 else "Kullanıcı"

            messagebox.showinfo("Hoş Geldiniz", f"Giriş başarılı! Hoş geldin {ad}.")
            pencere.destroy()

            
            subprocess.Popen([sys.executable, "ana_sayfa.py", str(user_id), str(ad)])
        else:
            messagebox.showerror("Hata", "E-posta veya şifre hatalı!")

    except sqlite3.Error as hata:
        messagebox.showerror("Veritabanı Hatası", f"Bir hata oluştu:\n{hata}")

def ilk_ekrana_don():
    pencere.destroy()
    subprocess.Popen([sys.executable, "ilk_ekran.py"])

def kayit_ekranina_don():
    pencere.destroy()
    subprocess.Popen([sys.executable, "kayıt_ekranı.py"])

pencere = Tk()
pencere.configure(bg="#f8fafc")
pencere.geometry("420x500")
pencere.title("Giriş Sayfası")


yazi = Label(pencere, text="Hesabınıza giriş yapın", bg="#f8fafc", fg="#0f172a", font=("Segoe UI", 15, "bold"))
yazi.place(x=40, y=25, width=340)

yazi1 = Label(pencere, text="Görevlerinizi görüntülemek için bilgilerinizi girin", bg="#f8fafc", fg="#64748b", font=("Segoe UI", 9))
yazi1.place(x=40, y=55, width=340)


yazi2 = Label(pencere, text="E-posta Adresi", bg="#f8fafc", fg="#334155", font=("Segoe UI", 9, "bold"))
yazi2.place(x=40, y=100)

text2 = Entry(
    pencere,
    bg="#ffffff",
    fg="#0f172a", 
    insertbackground="#2563eb", 
    relief="solid", 
    bd=1, 
    font=("Segoe UI", 10)
)
text2.place(x=40, y=125, width=340, height=36)


yazi3 = Label(pencere, text="Şifre", bg="#f8fafc", fg="#334155", font=("Segoe UI", 9, "bold"))
yazi3.place(x=40, y=180)

text3 = Entry(
    pencere, 
    bg="#ffffff", 
    fg="#0f172a", 
    insertbackground="#2563eb", 
    relief="solid", 
    bd=1, 
    font=("Segoe UI", 10), 
    show="*"
)
text3.place(x=40, y=205, width=340, height=36)


btn = Button(
    pencere, 
    text="Giriş Yap", 
    command=giris_yap, 
    bg="#2563eb", 
    fg="#ffffff", 
    activebackground="#1d4ed8", 
    activeforeground="#ffffff", 
    font=("Segoe UI", 10, "bold"), 
    relief="flat", 
    bd=0, 
    cursor="hand2"
)
btn.place(x=40, y=275, width=340, height=42)


btn2= Button(
    pencere, 
    text="Hesabın yok mu? Kayıt Ol", 
    command=kayit_ekranina_don, 
    bg="#e0e7ff", 
    fg="#3730a3", 
    activebackground="#c7d2fe", 
    activeforeground="#312e81", 
    font=("Segoe UI", 9, "bold"), 
    relief="flat", 
    bd=0, 
    cursor="hand2"
)
btn2.place(x=40, y=330, width=340, height=38)


btn1 = Button(
    pencere, 
    text="Ana Menüye Dön", 
    command=ilk_ekrana_don, 
    bg="#f1f5f9", 
    fg="#475569", 
    activebackground="#e2e8f0", 
    activeforeground="#1e293b", 
    font=("Segoe UI", 9), 
    relief="flat", 
    bd=0, 
    cursor="hand2"
)
btn1.place(x=40, y=380, width=340, height=34)

pencere.mainloop()