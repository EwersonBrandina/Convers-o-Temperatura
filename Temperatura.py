from Tkinter import*
#front-end
root = Tk()
#widgets
lb0 = Label(root, text='Insira Cº', font='Arial 25')
in0 = Entry(root, font='Arial 25')
bt0 = Botton(root, 'Obtenha F', font='Arial 25')
lb1 = Label(root, text='Resultado', font='Arial 25')

lb0.grid(row=0, column=0, sticky=NSEW)
in0.grid(row=0, column=1, sticky=NSEW)
bt0.grid(row=1, column=0, sticky=NSEW)
lb1.grid(row=1, column=1, sticky=NSEW)

