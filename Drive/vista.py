from tkinter import *
from tkinter import ttk
import quickstart

# La clase 'Aplicacion' ha crecido. En el ejemplo se incluyen
# nuevos widgets en el método constructor __init__(): Uno de
# ellos es el botón 'Info'  que cuando sea presionado llamará 
# al método 'verinfo' para mostrar información en el otro 
# widget, una caja de texto: un evento ejecuta una acción: 

class Aplicacion():
    def __init__(self):
        
        # En el ejemplo se utiliza el prefijo 'self' para
        # declarar algunas variables asociadas al objeto 
        # ('mi_app')  de la clase 'Aplicacion'. Su uso es 
        # imprescindible para que se pueda acceder a sus
        # valores desde otros métodos:
        
        self.raiz = Tk()
        self.raiz.geometry('1000x760')
        self.raiz.configure(bg='lightBlue')
        self.raiz.title('Aplicación')
        self.raiz.style=ttk.Style()
        # Impide que los bordes puedan desplazarse para
        # ampliar o reducir el tamaño de la ventana 'self.raiz':
        
        self.raiz.resizable()
        self.raiz.title('Ver info')
        
        # Define el widget Text 'self.tinfo ' en el que se
        # pueden introducir varias líneas de texto:
        
        self.tinfo = Text(self.raiz, width=100, height=40)
        
        # Sitúa la caja de texto 'self.tinfo' en la parte
        # superior de la ventana 'self.raiz':
        
        self.tinfo.pack(side=TOP)
        
        # Define el widget Button 'self.binfo' que llamará 
        # al metodo 'self.verinfo' cuando sea presionado
        
        self.binfo = ttk.Button(self.raiz, text='Info',
                                command=self.verinfo)
        
        # Coloca el botón 'self.binfo' debajo y a la izquierda
        # del widget anterior
                                
        #self.binfo.pack(side=LEFT)
        
        # Define el botón 'self.bsalir'. En este caso
        # cuando sea presionado, el método destruirá o
        # terminará la aplicación-ventana 'self.raíz' con 
        # 'self.raiz.destroy'
        ttk.Style().configure("TButton", padding=3, relief="flat",
      background="#125", font=("algerian",10))
        self.bsalir = ttk.Button(self.raiz, text='Salir', 
                                 command=self.raiz.destroy)
        self.bapi = ttk.Button(self.raiz, text='Excel', command = self.apiEx)
        self.bword = ttk.Button(self.raiz, text='Word', command = self.apiWo)
        self.bpres = ttk.Button(self.raiz, text='Slides', command = self.apiPre)
        self.bpdf = ttk.Button(self.raiz, text='PDF', command = self.apiPDF)
        self.bfolder = ttk.Button(self.raiz, text='Carpetas', command = self.apifol)
        self.bdescarga = ttk.Button(self.raiz, text='Descargar', command = self.apidesc)
        self.bcrear = ttk.Button(self.raiz, text='crear', command = self.apicrea)
        self.bcreardoc = ttk.Button(self.raiz, text='Crear Doc', command = self.creaDoc)
        self.bapi.place(x=270, y=655)
        self.bword.place(x=270, y=688)
        self.bpres.place(x=270, y=721)
        self.bpdf.place(x=420, y=708)
        self.bfolder.place(x= 420, y=671)
        self.bsalir.place(x=800, y=685)
        self.bdescarga.place(x=610, y=685)
        self.bcrear.place(x=100, y=671)
        self.bcreardoc.place(x=100, y=708 )

        # El foco de la aplicación se sitúa en el botón
        # 'self.binfo' resaltando su borde. Si se presiona
        # la barra espaciadora el botón que tiene el foco
        # será pulsado. El foco puede cambiar de un widget
        # a otro con la tecla tabulador [tab]
        
        #self.binfo.focus_set()
        self.raiz.mainloop()
        
    def apiEx(self):
        quickstart.api('excel')
        self.tinfo.delete("1.0", END)
        i=len(quickstart.aux)-1
        while i >= 0:
            self.tinfo.insert('1.0', str(i+1)+str(quickstart.aux[i])+'\n')
            i=i-1

    def apiWo(self):
        quickstart.api('word')
        self.tinfo.delete("1.0", END)
        i=len(quickstart.aux)-1
        while i >= 0:
            self.tinfo.insert('1.0', str(i+1)+str(quickstart.aux[i])+'\n')
            i=i-1

    def apiPre(self):
        quickstart.api('pres')
        self.tinfo.delete("1.0", END)
        i=len(quickstart.aux)-1
        while i >= 0:
            self.tinfo.insert('1.0', str(i+1)+str(quickstart.aux[i])+'\n')
            i=i-1

    def apiPDF(self):
        quickstart.api('PDF')
        self.tinfo.delete("1.0", END)
        i=len(quickstart.aux)-1
        while i >= 0:
            self.tinfo.insert('1.0', str(i+1)+str(quickstart.aux[i])+'\n')
            i=i-1

    def apifol(self):
        quickstart.api('carpeta')
        self.tinfo.delete("1.0", END)
        i=len(quickstart.aux)-1
        while i >= 0:
            self.tinfo.insert('1.0', str(i+1)+str(quickstart.aux[i])+'\n')
            i=i-1

    def apidesc(self):
        quickstart.api('descarga')

    def apicrea(self):
        quickstart.api('crear')
        print('creado')

    def creaDoc(self):
        quickstart.api('crearDoc')
        print ('creado')


    def verinfo(self):
        
        # Borra el contenido que tenga en un momento dado
        # la caja de texto
        
        self.tinfo.delete("1.0", END)
        
        # Obtiene información de la ventana 'self.raiz':
        
        info1 = self.raiz.winfo_class()
        info2 = self.raiz.winfo_geometry()
        info3 = str(self.raiz.winfo_width())
        info4 = str(self.raiz.winfo_height())
        info5 = str(self.raiz.winfo_rootx())
        info6 = str(self.raiz.winfo_rooty())
        info7 = str(self.raiz.winfo_id())
        info8 = self.raiz.winfo_name()
        info9 = self.raiz.winfo_manager()
        
        # Construye una cadena de texto con toda la
        # información obtenida:
        
        texto_info = "Clase de 'raiz': " + info1 + "\n"
        texto_info += "Resolución y posición: " + info2 + "\n"
        texto_info += "Anchura ventana: " + info3 + "\n"
        texto_info += "Altura ventana: " + info4 + "\n"
        texto_info += "Pos. Ventana X: " + info5 + "\n"
        texto_info += "Pos. Ventana Y: " + info6 + "\n"
        texto_info += "Id. de 'raiz': " + info7 + "\n"
        texto_info += "Nombre objeto: " + info8 + "\n" 
        texto_info += "Gestor ventanas: " + info9 + "\n"
        
        # Inserta la información en la caja de texto:
        
        self.tinfo.insert("1.0", texto_info)

def main():
    mi_app = Aplicacion()
    return 0

if __name__ == '__main__':
    main()