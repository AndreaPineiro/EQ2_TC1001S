# EQ2_TC1001S
Repositorio en Equipo - Herramientas Computacionales: El Arte de la Programación

En este proyecto hicimos una interfaz gráfica donde el usuario puede seleccionar una imagen. Esta imagen pasará por 3 filtros que hicimos: gaussian blur, __Joaquin__ y line detection. Finalmente, debemos tener una imagen convolusionada donde tenga los bordes detectados. 

Para correr este proyecto es necesario correr el archivo de main.py, el cual no recibe ningun argumento. El programa desplegara la interfaz para elegir la imagen.

- - - -

Información de Interfaz: 
La interfaz grafica hace uso de la libreria tkinter y sus modulo "filedialog", y el codigo puede correr en versiones de Python 3.8.5 en adelante. 
https://docs.python.org/3/library/dialog.html
https://docs.python.org/es/3.8/library/tk.html
 

## Información de Gaussian_blur: 
- R, Fisher. (2033). *Gaussian Smoothing*. Recuperado de https://homepages.inf.ed.ac.uk/rbf/HIPR2/gsmooth.htm el 6 de mayo de 2021.
- Abhisek Jana. Recuperado de https://github.com/benjaminva/semena-tec-tools-vision/blob/master/Scripts/Proyecto%20Vision/gaussian_blur.py el 6 de mayo de 2021.


## Información de Laplassian


## Información de Line Detection:
Para este filtro, se realizaron 4 detecciones: la de líneas horizontales, líneas verticales, líneas a 45° y a 135°.
Después de mostrar cada una de estas detecciones, se crea una imagen con todas las líneas. 
- AiShack(S,F). *Convolution*. Ai Shack. Recuperado de https://aishack.in/tutorials/image-convolution-examples/ el 6 de mayo de 2021.
- S,A (2012). *Line Detection*. CSE. Recuperado de https://www.cse.unr.edu/~bebis/CS791E/Notes/LineDetection.pdf el 6 de mayo de 2021.



