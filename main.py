
from tkinter import *
from PIL import Image, ImageTk
import pybase64
from tkinter import messagebox


window = Tk()
window.title("Secret Notes")
window.minsize(width=350,height=520)

resim = ImageTk.PhotoImage(Image.open('logo.webp'))
label = Label(width=100,height=100,image=resim)
label.pack()


def sifreolustur():
        title = Entry_baslik.get()
        sifre = entry_sifre.get()
        notes = text_not.get('1.0',END)
        notes = notes.encode("ascii")
        notes = pybase64.b64encode(notes)
        notes = notes.decode("ascii")
        if title == "" or notes == "" or sifre =="":
           messagebox.showwarning("Uyarı","Tüm bilgileri doldurunuz")
        else:
           dosya = open("deneme.txt","a")
           dosya.write(f'\n{Entry_baslik.get()}\n {notes}')
           text_not.delete('1.0',END)
           Entry_baslik.delete(0,END)
           entry_sifre.delete(0,END)
def sifrecoz():

        notescoz = text_not.get('1.0',END)
        notescoz = notescoz.encode("ascii")
        notescoz = pybase64.b64decode(notescoz)
        notescoz = notescoz.decode("ascii")
        text_not.delete('1.0',END)
        text_not.insert(END,notescoz)
git add

label_title = Label(text="Başlık Giriniz")
label_title.pack()
Entry_baslik = Entry(width=20)
Entry_baslik.pack()
label_bilgi = Label(text="Gizlenecek Bilgiler")
label_bilgi.pack()
text_not = Text(height=15, width=30)
text_not.pack()
label_sifre = Label(text="Şifrenizi Giriniz")
label_sifre.pack()
entry_sifre = Entry(width=20)
entry_sifre.pack()
buton_sifreleme =Button(text="Şifrele&Kaydet",command=sifreolustur)
buton_sifreleme.pack()
buton_sifrecoz = Button(text="Şifre Çöz",command=sifrecoz)
buton_sifrecoz.pack()



window.mainloop()
