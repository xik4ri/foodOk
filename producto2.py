from customtkinter import CTk, CTkButton, CTkFrame

class Interfaz:
    def __init__(self):
        self.ventana = CTk()
        self.ventana.geometry("1240x720")
        
        altura = self.ventana.winfo_reqheight()
        anchura = self.ventana.winfo_reqwidth()
        altura_pantalla = self.ventana.winfo_screenheight()
        anchura_pantalla = self.ventana.winfo_screenwidth()
        print(f"Altura: {altura}\nAnchura: {anchura}\nAltura de pantalla: {altura_pantalla}\nAnchura de pantalla: {anchura_pantalla}")
        x = (anchura_pantalla // 5) - (anchura // 4)
        y = (altura_pantalla // 5) - (altura // 4)
        self.ventana.geometry(f"+{x}+{y}")
        self.ventana.title("Food OK!")
        self.ventana.config(bg="white")
        self.ventana.iconbitmap("C:\\FO_OK\\captura.ico")
        
        self.opciones()
        self.crear_botones()
        
        self.ventana.mainloop()
    
    def opciones(self):
        # Aquí puedes configurar otras opciones de tu interfaz
        pass
    
    def crear_botones(self):
        frame_botones = CTkFrame(self.ventana)  # Crea un Frame con fondo negro
        frame_botones.pack(padx=10, pady=10)
        
        for i in range(1, 6):
            nuevo_boton = CTkButton(frame_botones, text=f'Botón {i}')
            nuevo_boton.pack()

if __name__ == "__main__":
    app = Interfaz()

