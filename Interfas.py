import tkinter as tk


class Procesar_imagen:

    # Constructor
    def __init__(self):
        # 1. Definicion y creacion del objeto frame (Tk) (JFrame)
        self.frame = tk.Tk()
        self.frame.title(":)")
        self.frame.geometry("600x400")

        # 2. Definicion y creacion de los atributos del frame
        self.ib_imagen = tk.Label(self.frame, text="Imagen a buscar:")
        self.tf_image = tk.Entry(self.frame, width=20)
        self.bCapturar = tk.Button(self.frame, text="Capturar Datos",
                                command=self.ca_image)

        self.taDatos = tk.Text(self.frame, width=40, height=10)

        # 3. Colocar los objetos de los atributos en un Layout
        self.ib_imagen.grid(row=0, column=0)
        self.tf_image.grid(row=0, column=1)
        self.bCapturar.grid(row=6, column=0)

        # Hacer visible al frame
        self.frame.mainloop()

    # Metodos para obtener el nombre de la imagen
    def get_image(self):
        cve = self.tf_image.get()
        return cve

    def ca_image(self):
        datos = self.get_image()
        print(datos)


image = Procesar_imagen()
