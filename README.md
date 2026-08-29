
# 📝 Python Tkinter & SQLite To-Do List Application

Python Tkinter kütüphanesi kullanılarak geliştirilmiş, çok kullanıcılı ve SQLite veritabanı destekli bir masaüstü yapılacaklar listesi (To-Do List) uygulaması.

---

## 🚀 Özellikler

* **Çoklu Kullanıcı Desteği:** Kullanıcı kayıt ve giriş (authentication) sistemi.
* **Kişiselleştirilmiş Görev Yönetimi:** Her kullanıcının yalnızca kendi eklediği görevleri görüntüleyebilmesi (`user_id` bazlı ilişkilendirme).
* **CRUD İşlemleri:** Görev ekleme, tamamlama/geri alma (durum güncelleme) ve silme.
* **Modern Arayüz:** Indigo/Slate renk paletiyle oluşturulmuş kullanıcı dostu Tkinter GUI.
* **Kalıcı Veri Depolama:** SQLite3 ile ilişkisel veritabanı yönetimi.

---

## 🛠️ Kullanılan Teknolojiler

* **Programlama Dili:** Python 3.x
* **Grafiksel Kullanıcı Arayüzü (GUI):** Tkinter
* **Veritabanı:** SQLite3
* **Süreç Yönetimi:** `subprocess`, `sys`

---

## 📂 Proje Yapısı

```text
├── yapilicaklar.db      # SQLite veritabanı dosyası
├── ilk_ekran.py         # Karşılama ve yönlendirme ekranı
├── kayit_ekrani.py      # Yeni kullanıcı kayıt sayfası
├── giris_ekrani.py      # Kullanıcı giriş sayfası
├── ana_sayfa.py         # To-Do listesi ve görev yönetim paneli
└── README.md            # Proje dokümantasyonu
