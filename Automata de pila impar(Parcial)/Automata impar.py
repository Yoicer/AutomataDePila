import pila
import tkinter
from tkinter import Label
from tkinter import *
from tkinter import ttk



class Autopi:
    def __init__(self, p):
        self.pila = p
        self.estado_1 = True
        self.estado_2 = False
        self.estado_final = False

#control del estado en el que se esta
    def getEstado_1(self):
        return self.estado_1
    def getEstado_2(self):
        return self.estado_2
    def getEstado_final(self):
        return self.estado_final

#cambia de estado activando el estado al que se rueda
    def activaEstado_1(self):
        self.estado_1=True
        self.estado_2=False
        self.estado_final=False

    def activaEstado_2(self):
        self.estado_2=True
        self.estado_1=False
        self.estado_final=False

    def activaEstado_final(self):
        self.estado_final=True
        self.estado_1=False
        self.estado_2=False

#transiciones estando en estado 1 :)
    #transiciones con b
    def b_b_bb(self):
        print('saca de la pila: ',self.pila.quitar())
        self.pila.apilar('b')
        
        self.pila.apilar('b')
        self.activaEstado_1()

    def b_a_ab(self):
        print('saca de la pila: ',self.pila.quitar())
        self.pila.apilar('a')
        self.pila.apilar('b')
        self.activaEstado_1()
    def b_n_nb(self):
        print('saca de la pila: ',self.pila.quitar())
        self.pila.apilar('#')
        print(self.pila.cima())
        self.pila.apilar('b')
        self.activaEstado_1()
#transiciones con a
    def a_b_ba(self):
        print('saca de la pila: ',self.pila.quitar())
        self.pila.apilar('b')
        self.pila.apilar('a')
        self.activaEstado_1()
    def a_n_na(self):
        print('saca de la pila: ',self.pila.quitar())
        self.pila.apilar('#')
        self.pila.apilar('a')
        self.activaEstado_1()
    def a_a_aa(self):
        print('saca de la pila: ',self.pila.quitar())
        self.pila.apilar('a')
        self.pila.apilar('a')
        self.activaEstado_1()
#transiciones con c
    def c_n_n(self):
        print('saca de la pila: ',self.pila.quitar())
        self.pila.apilar('#')
        print('apila:  #')
        self.activaEstado_2()
    def c_b_b(self):
        print('saca de la pila: ',self.pila.quitar())
        self.pila.apilar('b')
        print('apila: b')
        self.activaEstado_2()
    def c_a_a(self):
        print('saca de la pila: ',self.pila.quitar())
        self.pila.apilar('a')
        print('apila: a')
        self.activaEstado_2()

#tansiciones estando en el estado 2 :)
    def b_b_y(self):
        print('saca de la pila: ',self.pila.quitar())
        self.activaEstado_2()

    def a_a_y(self):
        print('saca de la pila: ',self.pila.quitar())
        self.activaEstado_2()

    def y_n_n(self):
        print('saca de la pila: ',self.pila.quitar())
        self.pila.apilar('#')
        self.activaEstado_final()

    
        

    def prueba(self, palabra):
        palabra=palabra+' '
        print('Estado 1  -  Estado 2  -  Estado Final  -  Cima Pila  -  Caracter')
        for caracter in palabra:
            print(self.getEstado_1(),'           ', self.getEstado_2(),'         ',self.getEstado_final(),'               ', self.pila.cima(),'              ', caracter)
            if (caracter != 'a' and caracter != 'b' and caracter != 'c' and caracter != '#' and caracter != ' '):
                print('El caracter es invalido en el lenguaje !!!')
                break
            elif (self.getEstado_1()):
                if (caracter=='b'):
                    if (self.pila.cima()== 'b'):
                        self.b_b_bb()
                    elif (self.pila.cima()== 'a'):
                        self.b_a_ab()
                    elif (self.pila.cima() == '#'):
                        self.b_n_nb()
                elif (caracter ==  'a'):
                    if (self.pila.cima()== 'b'):
                        self.a_b_ba()
                    elif (self.pila.cima()== 'a'):
                        self.a_a_aa()
                    elif (self.pila.cima() == '#'):
                        self.a_n_na()
                elif (caracter == 'c'):
                    if (self.pila.cima()== 'b'):
                        self.c_b_b()
                    elif (self.pila.cima()== 'a'):
                        self.c_a_a()
                    elif (self.pila.cima() == '#'):
                        self.c_n_n()
            elif (self.getEstado_2()):
                if (caracter == 'b'):
                    if (self.pila.cima() == 'b'):
                        self.b_b_y()
                    else:
                        break
                elif (caracter == 'a'):
                    if (self.pila.cima() == 'a'):
                        self.a_a_y()
                    else:
                        break
                elif(caracter == ' '):
                    print('palabra terminada')
                    if (self.pila.cima() == '#' and self.getEstado_2()):
                        self.y_n_n()
         

        if (self.getEstado_final()):
            print('*La palabra es palindrome*')
        elif(self.getEstado_1()):
            print('*Las Palabras del lenguaje deben llevar por lomenos una C *')
            print('* La palabra no es palondrime*')
        else:
            print('* La palabra no es palondrime*')
            


pila=pila.Pila()
auto= Autopi(pila)
auto.prueba('abcba')

def cargarlistbox(lista,listbox):
    ind,largo=0,len(lista)
    while ind < largo:
        listbox.insert(END,lista[ind])
        ind+=1
def funcion():
    otra_ventana = tkinter.Toplevel(root)
    otra_ventana.minsize(width=600,height=500)

    scrollbar = Scrollbar(otra_ventana)
    scrollbar.pack(side=RIGHT, fill=Y)
    
    listbox = Listbox(otra_ventana)
    listbox.insert(0, 'Hola :v')
    cargarlistbox('holamundooooooooooooooooooooo',listbox)
    
    listbox.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=listbox.yview)
    listbox['bg'] = 'black'
    listbox['fg'] = 'blue'

    listbox.pack(side=LEFT, fill=BOTH, expand=1)
    root.iconify()

root = tkinter.Tk()

img = PhotoImage(file="prueba.gif")
widget = Label(root, image=img).pack()

boton = tkinter.Button(root, text="Abrir otra ventana", command=funcion)
boton['bg'] = 'black' 
boton['fg'] = 'blue'
boton.pack()

listbox = Listbox(root)
listbox.place(relwidth=1 ,relheight=-0.50)
listbox['bg'] = 'black'
listbox['fg'] = 'blue'
listbox.pack(side=LEFT, fill=BOTH, expand=1)
listbox.insert(END, 'Descripcion')

scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

root.minsize(width=600,height=500)
root.mainloop()



    				


		





