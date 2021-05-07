import tkinter as tk
from tkinter import scrolledtext as st
import cv2
from tkinter import filedialog as fd
from tkinter import messagebox as mb
from gaussian_kernel import gaussian_blur
from convolution import convolution
from line_detection import line_detection


class Procesar_imagen:
    # Constructor
    def __init__(self, image_name=""):
        # 1. Definicion y creacion del objeto frame (Tk)
        self.frame = tk.Tk()
        self.frame.title(":)")
        self.frame.geometry("600x400")
        self.image_name = image_name

        # 2. Definicion y creacion de los atributos del frame
        self.ib_imagen = tk.Label(self.frame, text="Bienvenido, presione en buscar una imagen.")

        self.bCapturar = tk.Button(self.frame, text=" Buscar ", command=self.ca_image)

        # 3. Colocar los objetos de los atributos en un Layout
        self.ib_imagen.grid(row=0, column=0)
        self.bCapturar.grid(row=0, column=200)

        # Hacer visible al frame
        self.frame.mainloop()

    # Metodos para obtener el nombre de la imagen
    def ca_image(self):
        self.image_name = fd.askopenfilename(title="Seleccione la imagen")
        if self.image_name != "":
            print (self.image_name)
            self.frame.destroy()
        return self.image_name


class Output:

    # Constructor
    def __init__(self, text):
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


if __name__ == "__main__":
    #Se manda a llamar la interfaz para buscar la imagen
    image = Procesar_imagen()
    #Se guarda el atributo "image_name" de la clase "Principal" en la variable "image_name"
    image_name = image.image_name
    # se saca la matriz de la imagen
    img = cv2.imread(image_name)

    # Hacer kernel gausiano
    kernel_gauss = gaussian_blur(9)

    # Hacer convolusion
    img = convolution(img, kernel_gauss, True)
    output = Output("Gaussian Blur\n" + "Shape:" + str(img.shape[0]) + " X " + str(img.shape[1]))
    # Aplicar Line Detection
    img = line_detection(img, verbose=True)
    output = Output("Line Detection\n" + "Shape:" + str(img.shape[0]) + " X " + str(img.shape[1]))
