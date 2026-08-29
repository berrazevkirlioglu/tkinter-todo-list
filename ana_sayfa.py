from tkinter import *
from tkinter import messagebox
import subprocess
import sys
import sqlite3


def tablo_olustur():
    try:
        conn = sqlite3.connect("yapilicaklar.db")
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS todos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                gorev_metni TEXT,
                tamamlandi_mi INTEGER DEFAULT 0
            )
        """)
        conn.commit()
        conn.close()
    except sqlite3.Error as e:
        print("Tablo hatası:", e)

tablo_olustur()


aktif_user_id = int(sys.argv[1]) if len(sys.argv) > 1 else 1
aktif_kullanici_ad = sys.argv[2] if len(sys.argv) > 2 else "Kullanıcı"

gorev_kayitlari = []


pencere = Tk()
pencere.configure(bg="#f8fafc")
pencere.geometry("450x580")
pencere.title("Yapılacaklar Listesi")


yazi = Label(
    pencere, 
    text=f"{aktif_kullanici_ad}'in Görevleri", 
    bg="#f8fafc", 
    fg="#0f172a", 
    font=("Segoe UI", 15, "bold")
)
yazi.place(x=35, y=20, width=380)


text = Entry(
    pencere, 
    bg="#ffffff", 
    fg="#0f172a", 
    insertbackground="#2563eb", 
    relief="solid", 
    bd=1, 
    font=("Segoe UI", 10)
)
text.place(x=35, y=65, width=280, height=38)


liste= Listbox(
    pencere, 
    bg="#ffffff", 
    fg="#1e293b", 
    selectbackground="#dbeafe", 
    selectforeground="#1e40af", 
    font=("Segoe UI", 11), 
    relief="solid", 
    bd=1, 
    highlightthickness=0,
    activestyle="none"
)
liste.place(x=35, y=120, width=380, height=310)


def gorevleri_yukle():
    liste.delete(0, END)
    gorev_kayitlari.clear()
    
    try:
        conn = sqlite3.connect("yapilicaklar.db")
        cursor = conn.cursor()
        cursor.execute(
            "SELECT id, gorev_metni, tamamlandi_mi FROM todos WHERE user_id = ?",
            (aktif_user_id,)
        )
        veriler = cursor.fetchall()
        conn.close()

        for satir in veriler:
            todo_id, metin, tamamlandi = satir
            gorev_kayitlari.append((todo_id, tamamlandi))
            
            durum_isareti = "✓" if tamamlandi == 1 else "○"
            liste.insert(END, f"  {durum_isareti}  {metin}")

    except sqlite3.Error as hata:
        messagebox.showerror("Veritabanı Hatası", f"Görevler yüklenirken hata oluştu:\n{hata}")

def gorev_ekle():
    yeni_gorev = text.get().strip()
    if not yeni_gorev:
        messagebox.showerror("Eksik Bilgi", "Lütfen eklenecek görevi yazın!")
        return

    try:
        conn = sqlite3.connect("yapilicaklar.db")
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO todos (user_id, gorev_metni, tamamlandi_mi) VALUES (?, ?, 0)",
            (aktif_user_id, yeni_gorev)
        )
        conn.commit()
        conn.close()

        text.delete(0, END)
        gorevleri_yukle()

    except sqlite3.Error as hata:
        messagebox.showerror("Veritabanı Hatası", f"Görev eklenirken hata oluştu:\n{hata}")

def durum_degistir():
    secili_indeks = liste.curselection()
    if not secili_indeks:
        messagebox.showwarning("Uyarı", "Lütfen durumunu değiştirmek istediğiniz görevi seçin!")
        return

    indeks = secili_indeks[0]
    todo_id, mevcut_durum = gorev_kayitlari[indeks]
    yeni_durum = 0 if mevcut_durum == 1 else 1

    try:
        conn = sqlite3.connect("yapilicaklar.db", timeout=10)
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE todos SET tamamlandi_mi = ? WHERE id = ?",
            (yeni_durum, todo_id)
        )
        conn.commit()
        conn.close()

        gorevleri_yukle()

    except sqlite3.Error as hata:
        messagebox.showerror("Veritabanı Hatası", f"Durum güncellenemedi:\n{hata}")

def gorev_sil():
    secili_indeks = liste.curselection()
    if not secili_indeks:
        messagebox.showwarning("Uyarı", "Lütfen silmek istediğiniz görevi seçin!")
        return

    indeks = secili_indeks[0]
    todo_id, _ = gorev_kayitlari[indeks]

    try:
        conn = sqlite3.connect("yapilicaklar.db", timeout=10)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM todos WHERE id = ?", (todo_id,))
        conn.commit()
        conn.close()

        gorevleri_yukle()

    except sqlite3.Error as hata:
        messagebox.showerror("Veritabanı Hatası", f"Görev silinemedi:\n{hata}")

def oturumu_kapat():
    pencere.destroy()
    subprocess.Popen([sys.executable, "giris_ekranı.py"])


btn = Button(
    pencere, 
    text="Ekle", 
    command=gorev_ekle, 
    bg="#2563eb", 
    fg="#ffffff", 
    activebackground="#1d4ed8", 
    activeforeground="#ffffff", 
    font=("Segoe UI", 10, "bold"), 
    relief="flat", 
    bd=0, 
    cursor="hand2"
)
btn.place(x=325, y=65, width=90, height=38)

btn1= Button(
    pencere, 
    text="Tamamla / Geri Al", 
    command=durum_degistir, 
    bg="#e0e7ff", 
    fg="#3730a3", 
    activebackground="#c7d2fe", 
    activeforeground="#312e81", 
    font=("Segoe UI", 9, "bold"), 
    relief="flat", 
    bd=0, 
    cursor="hand2"
)
btn1.place(x=35, y=445, width=185, height=38)

btn2 = Button(
    pencere, 
    text="Görevi Sil", 
    command=gorev_sil, 
    bg="#fee2e2", 
    fg="#991b1b", 
    activebackground="#fecaca", 
    activeforeground="#7f1d1d", 
    font=("Segoe UI", 9, "bold"), 
    relief="flat", 
    bd=0, 
    cursor="hand2"
)
btn2.place(x=230, y=445, width=185, height=38)

btn3 = Button(
    pencere, 
    text="Oturumu Kapat", 
    command=oturumu_kapat, 
    bg="#f1f5f9", 
    fg="#475569", 
    activebackground="#e2e8f0", 
    activeforeground="#1e293b", 
    font=("Segoe UI", 9, "bold"), 
    relief="flat", 
    bd=0, 
    cursor="hand2"
)
btn3.place(x=35, y=495, width=380, height=36)


gorevleri_yukle()

pencere.mainloop()