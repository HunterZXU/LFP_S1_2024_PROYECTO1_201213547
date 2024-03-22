from tkinter import *
from tkinter import ttk
import manejo_archivos

class menu_principal:
    def menu():
        # Propiedad de la ventana
        root = Tk()
        root.title("Traductor de HTML")
        root.geometry("1300x800")
        root.resizable(width=False, height=False)
        
        # Crear un marco que se expanda y ocupe todo el espacio disponible
        mainframe = ttk.Frame(root)
        mainframe.place(relx=0, rely=0, relwidth=1, relheight=1)

        # textbox izquierdo
        text_box1 = Text(mainframe, wrap="none")
        text_box1.place(x=5, y=50, width=500, height=600)  # Definir tamaño y posición
        
        # barra de desplazamiento vertical izquierdo
        scroll_y1 = Scrollbar(mainframe, orient="vertical", command=text_box1.yview)
        scroll_y1.place(x=500, y=50, height=600)
        text_box1.config(yscrollcommand=scroll_y1.set)
        
        # barra de desplazamiento horizontal izquierdo
        scroll_x1 = Scrollbar(mainframe, orient="horizontal", command=text_box1.xview)
        scroll_x1.place(x=5, y=650, width=500)
        text_box1.config(xscrollcommand=scroll_x1.set)

        # textbox derecho
        text_box2 = Text(mainframe, wrap="none")
        text_box2.place(x=780, y=50, width=500, height=600)  # Definir tamaño y posición

        # barra de desplazamiento vertical derecho
        scroll_y2 = Scrollbar(mainframe, orient="vertical", command=text_box2.yview)
        scroll_y2.place(x=1280, y=50, height=600)
        text_box2.config(yscrollcommand=scroll_y2.set)
        
        # barra de desplazamiento horizontal derecho
        scroll_x2 = Scrollbar(mainframe, orient="horizontal", command=text_box2.xview)
        scroll_x2.place(x=780, y=650, width=500)
        text_box2.config(xscrollcommand=scroll_x2.set)

        # boton para cargar archivo
        button1 = Button(root, text= "Cargar Archivo",font=("Helvetica", 10, "bold"),command=manejo_archivos.imprimir)
        button1.place(x=560, y=100, width= 175, height= 60)

        # boton para traducir archivo
        button2 = Button(root, text= "Traducir",font=("Helvetica", 10, "bold"),command=manejo_archivos.imprimir)
        button2.place(x=560, y=500, width= 175, height= 60)
        
        # prueba de textbox
        #text_box1.insert("1.0", "Este es un texto de ejemplo que puede ser largo y necesitar desplazamiento horizontal y vertical.")

        #label izquierdo
        label1 = Label(mainframe, text="Texto de entrada:", font=("Helvetica", 14, "bold"))
        label1.place(x=140,y=10, width= 175, height= 40)

        #label derecho
        label2 = Label(mainframe, text="Traduccion:", font=("Helvetica", 14, "bold"))
        label2.place(x=960,y=10, width= 175, height= 40)

        root.mainloop()

if __name__ == "__main__":
    menu_principal.menu()