import tkinter as tk
from tkinter import scrolledtext as st
from gaussian_kernel import gaussian_blur
from convolution import convolution
from line_detection import line_detection
import cv2

class Procesar_imagen:

    # Constructor
    def _init_(self):
        # 1. Definicion y creacion del objeto frame (Tk) (JFrame)
        self.frame = tk.Tk()
        self.frame.title(":)")
        self.frame.geometry("600x400")

        # 2. Definicion y creacion de los atributos del frame
        self.ib_imagen = tk.Label(self.frame, text="Imagen a buscar:")
        self.tf_image = tk.Entry(self.frame, width=20)
        self.bCapturar = tk.Button(self.frame, text="Capturar Datos",
                                command=self.ca_image)

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


class Output:

    # Constructor
    def _init_(self, text):
        # 1. Definicion y creacion del objeto frame (Tk)
        self.frame = tk.Tk()
        self.frame.title("Output")
        self.frame.geometry("600x400")
        self.text = text
        # 2. Colocar la salida de texto
        self.scrolledtext1 = st.ScrolledText(self.frame, width=80, height=20)
        self.scrolledtext1.grid(column=0, row=0, padx=10, pady=10)

        tex_me = self.output(self.text)
        # Hacer visible al frame
        self.frame.mainloop()

    # Metodos para imprimir los tatos
    def output(self, text):
        self.scrolledtext1.insert("1.0", text)
        print (text)
        return 0


#text = "sdadsadsdasddasdda"
# image = Output(text)ddd
# image_name = Procesar_imagen()
image_name = 'turquia.jpg'
img = cv2.imread(image_name)

# Hacer kernel gausiano
kernel_gauss = gaussian_blur(9)

# Hacer convolusion
img = convolution(img, kernel_gauss, True)

# Aplicar Line Detection
img = line_detection(img, verbose=True)