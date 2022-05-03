from tkinter import*

def calcfactoriel():
    N = int(Entree1.get())
    factoriel=1
    for i in range(1,N+1):
        factoriel = factoriel*i
    N2 = factoriel
    Entree2.delete(0,END)
    Entree2.insert(0,N2)

fen = Tk()
fen.geometry("350x200")

label1 = Label(fen, text = "Entrez la valeur de N")
label1.grid(row=2, column=1, padx=10)

Entree1 = Entry(fen)
Entree1.grid(row=2, column=2, padx=10)

label2 = Label(fen, text="Le factoriel de N est:")
label2.grid(row=4, column=1)

Entree2 = Entry(fen)
Entree2.grid(row=4, column=2)

fen.mainloop()