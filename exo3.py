from tkinter import*

def calcfactoriel():
    N = int(Entree1.get())
    factoriel=1
    for i in range(1,N+1):
        factoriel = factoriel*i
    N2 = factoriel
    Entree2.delete(0,END)
    Entree2.insert(0,N2)

def delete():
    Entree1.delete(0,END)
    Entree2.delete(0,END)

fen = Tk()
fen.geometry("350x200")

label1 = Label(fen, text = "Entrez la valeur de N")
label1.place(x=50, y=50)

Entree1 = Entry(fen)
Entree1.place(x=200, y=50)

label2 = Label(fen, text="Le factorielle de N est:")
label2.place(x=50, y=100)

Entree2 = Entry(fen)
Entree2.place(x=200, y=100)

Calculer = Button(fen, text="Calculer le factorielle", command=calcfactoriel)
Calculer.place(x=210, y=150)

Effacer = Button(fen, text="Effacer le contenu", command=delete)
Effacer.place(x=80, y=150)
fen.mainloop()