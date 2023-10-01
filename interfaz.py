from openpyxl import *
from tkinter import *
from subprocess import call

from customtkinter import *
from customtkinter import CTk, CTkFrame, CTkButton, CTkEntry, CTkImage, CTkLabel, CTkImage

from PIL import ImageTk, Image
from functools import partial


class Interfaz (object):
    def __init__(self) -> None:
        self.ventana=CTk()
        self.ventana.geometry("1240x720")
        
        altura = self.ventana.winfo_reqheight()
        anchura = self.ventana.winfo_reqwidth()
        altura_pantalla = self.ventana.winfo_screenheight()
        anchura_pantalla = self.ventana.winfo_screenwidth()
        print(f"Altura: {altura}\nAnchura: {anchura}\nAltura de pantalla: {altura_pantalla}\nAnchura de pantalla: {anchura_pantalla}")
        x = (anchura_pantalla // 5) - (anchura//4)
        y = (altura_pantalla//5) - (altura//4)
        self.ventana.geometry(f"+{x}+{y}")
        self.ventana.title("Food OK!")
        self.ventana.config(bg="white") 
        #self.ventana.iconbitmap("C:\\Users\\nicol\\Downloads\\captura_iG1_icon.ico")
        self.ventana.iconbitmap("C:\\FO_OK\\captura.ico")
        
        
        self.btns = {}
        self.opciones()
        self.CrearFrame()
        self.ventana.mainloop()
 
    def opciones(self):
        #self.btnEliminar = CTkButton(self.ventana, text='Eliminar').grid(sticky=S, pady=0)
        #self.btnBajar = CTkButton(self.ventana, text='bajar').grid(sticky=S, pady=0)
        self.img2 = ImageTk.PhotoImage(Image.open("C:\\FO_OK\\FOODOK.png").resize((110,110)))
        self.labelfoto = CTkLabel(self.ventana, text='', image = self.img2).place(x=980, y=100)

        self.btnSanwiches = CTkButton(self.ventana,text='SANWICHES',width=120,height=30,border_width=0,corner_radius=20,command=lambda:self.SeleccionSanwich()).place(x=850, y=200)

        self.btnCompletos = CTkButton(self.ventana,text='COMPLETOS',width=120,height=30,border_width=0,corner_radius=20,command=self.borrador).place(x=980, y=200)
        self.btnBebidas = CTkButton(self.ventana,text='BEBIDAS',width=120,height=30,border_width=0,corner_radius=20,).place(x=1110, y=200)
        self.btnPapasfritas = CTkButton(self.ventana,text='PAPASFRITAS',width=120,height=30,border_width=0,corner_radius=20,).place(x=850, y=240)
        self.btnPollo = CTkButton(self.ventana,text='POLLO',width=120,height=30,border_width=0,corner_radius=20,).place(x=980, y=240)
        self.btnPizza = CTkButton(self.ventana,text='PIZZA',width=120,height=30,border_width=0,corner_radius=20,).place(x=1110, y=240)
        self.btnAgregados = CTkButton(self.ventana,text='AGREGADOS',width=120,height=30,border_width=0,corner_radius=20,).place(x=850, y=280)
        self.btnPichangas = CTkButton(self.ventana,text='PICHANGA',width=120,height=30,border_width=0,corner_radius=20,).place(x=980, y=280)
        self.btnColaciones = CTkButton(self.ventana,text='COLACIONES',width=120,height=30,border_width=0,corner_radius=20,).place(x=1110, y=280)
    def CrearFrame(self):
        frame_botones = CTkFrame(self.ventana, width=420, height=680, border_color="green", border_width=10)  # Crea un Frame con fondo negro
        frame_botones.place(x=380, y=20) # Utiliza pack() para el frame

    def SeleccionSanwich(self):
        
        
         # Utiliza pack() para el frame
        self.btns['btnm'] = CTkButton(self.ventana,text='MECHADA',width=180,height=30,border_width=0,corner_radius=20,).place(x=400, y=40)
        self.btnAve = CTkButton(self.ventana,text='AVE',width=180,height=30,border_width=0,corner_radius=20).place(x=400, y=80)
        self.btnLomo = CTkButton(self.ventana,text='LOMO',width=180,height=30,border_width=0,corner_radius=20,).place(x=400, y=120)
        self.btnChurras = CTkButton(self.ventana,text='CHURRASCO',width=180,height=30,border_width=0,corner_radius=20,).place(x=400, y=160)
     
        self.btnMechOK = CTkButton(self.ventana,text='MECHADA OK',width=180,height=30,border_width=0,corner_radius=20,).place(x=400, y=200)
        self.btnMechTRA = CTkButton(self.ventana,text='MECHADA TRADICION',width=180,height=30,border_width=0,corner_radius=20,).place(x=400, y=240)
        
        self.btnAveOK = CTkButton(self.ventana,text='AVE OK',width=180,height=30,border_width=0,corner_radius=20,).place(x=400, y=280)
        self.btnAveTRA = CTkButton(self.ventana,text='AVE TRADICION',width=180,height=30,border_width=0,corner_radius=20,).place(x=400, y=320)
        
        self.btnLomoOK = CTkButton(self.ventana,text='LOMO OK',width=180,height=30,border_width=0,corner_radius=20,).place(x=400, y=360)
        self.btnLomoTRA = CTkButton(self.ventana,text='LOMO TRADICION',width=180,height=30,border_width=0,corner_radius=20,).place(x=400, y=400)
        
        self.btnChuOK = CTkButton(self.ventana,text='CHURRASCO OK',width=180,height=30,border_width=0,corner_radius=20,).place(x=400, y=440)
        self.btnChuTRA = CTkButton(self.ventana,text='CHURRASCO TRADICION',width=180,height=30,border_width=0,corner_radius=20,).place(x=400, y=480)


        self.btn2XLOMO = CTkButton(self.ventana,text='X2LOMO',width=140,height=30,border_width=0,corner_radius=20,).place(x=620, y=40)
        self.btn2XAVE = CTkButton(self.ventana,text='X2AVE',width=140,height=30,border_width=0,corner_radius=20,).place(x=620, y=80)
        self.btnPRECIO100 = CTkButton(self.ventana,text='PRECIO100',width=140,height=30,border_width=0,corner_radius=20,).place(x=620, y=120)

    def borrador(self):
        
        for key in self.btns:
            self.btns[key].destroy()
        self.btns.clear()
       
 

       
    
f =Interfaz()





















