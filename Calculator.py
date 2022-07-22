import tkinter as tk


def topla():
    s1=float(sayi1.get())
    s2=float(sayi2.get())
    sonuc['text'] = str(s1+s2)
def cikar():
    s1=float(sayi1.get())
    s2=float(sayi2.get())
    sonuc['text']=str(s1-s2)

def carp():
    s1=float(sayi1.get())
    s2=float(sayi2.get())
    sonuc['text']=str(s1*s2)

def bol():
    s1=float(sayi1.get())
    s2=float(sayi2.get())
    sonuc['text']=str(s1/s2)




pencere = tk.Tk()
pencere.title("CALCULATOR")
pencere.geometry("300x300")
pencere.configure(bg="blue")

etiket=tk.Label(text="Calculator", bg="light blue", width=10, font="Verdana 18 bold").place(x=70, y=20)

sayi1=tk.Entry(width=10)
sayi1.place(x=20,y=70)

sayi2=tk.Entry(width=10)
sayi2.place(x=100,y=70)

sonuc=tk.Label(text="Sonuc",bg="light blue")
sonuc['font'] = "Verdana 12 bold"
sonuc['fg'] = '#000000'   #hex code renk tanımlamasını kabul eder
sonuc.place(x=185,y=70)


btopla=tk.Button(text="+",font="Verdana 22 bold",command=topla).place(x=20,y=100)
bcikar=tk.Button(text="-",font="Verdana 22 bold",command=cikar).place(x=80,y=100)
bcarp=tk.Button(text="x",font="Verdana 22 bold",command=carp).place(x=140,y=100)
bbol=tk.Button(text="/",font="Verdana 22 bold",command=bol).place(x=200,y=100)

pencere.mainloop()






