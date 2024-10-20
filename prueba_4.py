import tkinter as tk
from tkinter import messagebox
import requests
from bs4 import BeautifulSoup

# Función para realizar el web scraping
def scrape():
    url = url_entry.get()  # Obtener la URL de la caja de texto
    if not url:
        messagebox.showerror("Error", "Por favor, ingresa una URL válida.")
        return

    try:
        # Realizar la solicitud HTTP
        response = requests.get(url)
        response.raise_for_status()  # Verificar si la solicitud fue exitosa
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Buscar los precios en la página
        # Cambia 'price' por la clase o el identificador correcto de la página que estés scrapeando
        price = soup.find_all("div", class_="ui-search-result__wrapper")
        
        if price:
            # Extraer y mostrar todos los precios encontrados
            result_text = "Precios encontrados:\n"
            for price in price:
                result_text += price.get_text() + "\n"  # Obtener el texto de cada precio
            result_label.config(text=result_text)
        else:
            result_label.config(text="No se encontraron precios en la página.")

    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"No se pudo obtener la página: {e}")

# Configurar la interfaz gráfica
root = tk.Tk()
root.title("Web Scraper de Precios con Python")

# Etiqueta y caja de texto para ingresar la URL
url_label = tk.Label(root, text="Ingresa la URL:")
url_label.pack(pady=10)
url_entry = tk.Entry(root, width=50)
url_entry.pack(pady=5)

# Botón para iniciar el proceso de scraping
scrape_button = tk.Button(root, text="Iniciar Scraping", command=scrape)
scrape_button.pack(pady=20)

# Etiqueta para mostrar los resultados
result_label = tk.Label(root, text="")
result_label.pack(pady=10)

# Iniciar la aplicación
root.mainloop()