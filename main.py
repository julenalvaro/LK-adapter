import pandas as pd
import tkinter as tk
from tkinter import filedialog, messagebox
from os.path import dirname
import os

def procesar_csv(csv_file):
    # Leer el archivo CSV
    df = pd.read_csv(csv_file, sep=';', decimal=',')
    # Procesar los datos
    # Aquí puedes realizar cualquier manipulación o transformación adicional que necesites
    # Por ejemplo, puedes aplicar cálculos, filtrar filas o columnas, etc.

    # borrar la primera columna
    df = df.drop(df.columns[0], axis=1)

    # Obtener el nombre del archivo sin la extensión
    file_name = os.path.splitext(csv_file)[0]
    # Generar el nombre del archivo de salida con la extensión .xlsx
    excel_file = file_name + ".xlsx"
    # Guardar los datos en un archivo Excel
    df.to_excel(excel_file, index=False)
    return excel_file

def browseFiles():
    filename = filedialog.askopenfilename(initialdir="C:/Users/julen/Downloads", title="Select a File",
                                            filetypes=(("CSV files", "*.csv*"), ("all files", "*.*")))
    # Calling function to process CSV and generate Excel file
    excel_file = procesar_csv(filename)
    message = f"Archivo Excel generado correctamente:\n{excel_file}"
    messagebox.showinfo("Éxito", message)

# Create the root window
window = tk.Tk()
window.iconbitmap('./img/2023-05-18_135916.ico')
window.title('LK .csv to .xlsx adapter')

# Get the screen width and height
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# Calculate the center position
x = (screen_width - 500) // 2
y = (screen_height - 200) // 2

# Set the window position
window.geometry(f'500x200+{x}+{y}')

# Create a File Explorer label
button_explore = tk.Button(window, text="Explorar archivos CSV", command=browseFiles)
button_explore.pack(expand=True)

# Run the GUI
window.mainloop()
