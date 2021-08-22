from tkinter import*
from tkinter.ttk import*

root = Tk()
root.title("Usuario")
root.geometry("600x600")
root.resizable(width=False, height=False)
root.config(bg="powderblue")


usuario= Label(root, text="Ingrese el Nombre del Usuario:")
usuario.pack()


Usuario1 = StringVar()
adm=Entry(root, width=30 , textvariable=Usuario1)
adm.pack()

contraseña = Label(root, text="contraseña:")
contraseña.pack()


contra = StringVar()
contra1 = Entry(root, width=30, textvariable=contra, show="*")
contra1.pack()

def ingresar():
    if Usuario1.get()=="programador" and contra.get()=="12345":
        root.title("Correcto")
    else:
        root.title("Es incorrecto")

bt= Button(root, text="Entrar", command=ingresar)
bt.pack(side=BOTTOM)


root.mainloop()
