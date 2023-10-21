#Hecho por Angelo Lemes

import secrets
import string
import tkinter as tk
import tkinter.messagebox

def generar_contrasena(longitud, incluir_mayusculas, incluir_numeros, incluir_simbolos):
    caracteres = string.ascii_lowercase
    if incluir_mayusculas:
        caracteres += string.ascii_uppercase
    if incluir_numeros:
        caracteres += string.digits
    if incluir_simbolos:
        caracteres += string.punctuation
    contrasena = ''.join(secrets.choice(caracteres) for i in range(longitud))
    return contrasena

def generar_contrasena_gui():
    longitud = int(longitud_entry.get())
    incluir_mayusculas = mayusculas_var.get()
    incluir_numeros = numeros_var.get()
    incluir_simbolos = simbolos_var.get()
    contrasena = generar_contrasena(longitud, incluir_mayusculas, incluir_numeros, incluir_simbolos)
    contrasena_entry.delete(0, tk.END)  # Limpiar el campo de entrada de contraseñas
    contrasena_entry.insert(0, contrasena)  # Mostrar la contraseña generada

def copiar_contrasena():
    contrasena = contrasena_entry.get()
    if contrasena:
        ventana.clipboard_clear()  # Borrar el portapapeles
        ventana.clipboard_append(contrasena)  # Agregar la contraseña al portapapeles
        ventana.update()  # Actualizar el portapapeles
        tkinter.messagebox.showinfo("Copiado", "Contraseña copiada al portapapeles")

# Crear la ventana de la interfaz gráfica
ventana = tk.Tk()
ventana.title("Generador de contraseñas")

# Crear la entrada para la longitud de la contraseña
longitud_label = tk.Label(ventana, text="Longitud:")
longitud_label.grid(row=0, column=0)
longitud_entry = tk.Entry(ventana)
longitud_entry.grid(row=0, column=1)

# Crear las opciones para la contraseña
opciones_label = tk.Label(ventana, text="Opciones:")
opciones_label.grid(row=1, column=0)
mayusculas_var = tk.BooleanVar()
mayusculas_checkbox = tk.Checkbutton(ventana, text="Incluir mayúsculas", variable=mayusculas_var)
mayusculas_checkbox.grid(row=2, column=0)
numeros_var = tk.BooleanVar()
numeros_checkbox = tk.Checkbutton(ventana, text="Incluir números", variable=numeros_var)
numeros_checkbox.grid(row=3, column=0)
simbolos_var = tk.BooleanVar()
simbolos_checkbox = tk.Checkbutton(ventana, text="Incluir símbolos", variable=simbolos_var)
simbolos_checkbox.grid(row=4, column=0)

# Crear el botón para generar la contraseña 
generar_button = tk.Button(ventana, text="Generar", command=generar_contrasena_gui)
generar_button.grid(row=5, column=0)

# Crear la etiqueta para mostrar la contraseña generada
contrasena_entry = tk.Entry(ventana, show="*")  # Mostrar la contraseña con asteriscos
contrasena_entry.grid(row=6, column=0)

# Crear el botón para copiar la contraseña al portapapeles
copiar_button = tk.Button(ventana, text="Copiar", command=copiar_contrasena)
copiar_button.grid(row=7, column=0)

# Iniciar la ventana de la interfaz gráfica
ventana.mainloop()
