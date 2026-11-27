import math
import statistics
import tkinter as tk
from tkinter import messagebox

class Notas:
    def __init__(self, lista_notas: list):
        self.lista_notas = lista_notas

    def calcular_promedio(self) -> float:
        return statistics.mean(self.lista_notas)

    def calcular_desviacion_estandar(self) -> float:
        # Desviación estándar muestral
        return statistics.stdev(self.lista_notas) if len(self.lista_notas) > 1 else 0.0

    def calcular_mayor(self) -> float:
        return max(self.lista_notas)

    def calcular_menor(self) -> float:
        return min(self.lista_notas)


class VentanaNotas(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculadora de Notas")
        self.geometry("320x380")
        self.resizable(False, False)

        self.entradas_notas = []
        self.crear_interfaz()

    def crear_interfaz(self):
        
        for i in range(1, 6):
            tk.Label(self, text=f"Nota {i}:", font=("Arial", 10)).grid(
                row=i - 1, column=0, padx=15, pady=6, sticky="w"
            )
            entry = tk.Entry(self, width=15, font=("Arial", 10))
            entry.grid(row=i - 1, column=1, padx=15, pady=6)
            self.entradas_notas.append(entry)

        
        btn_calcular = tk.Button(
            self,
            text="Calcular",
            command=self.calcular_estadisticas,
            bg="#4CAF50",
            fg="white",
            font=("Arial", 10, "bold"),
            width=10,
        )
        btn_calcular.grid(row=5, column=0, pady=12, padx=10)

        btn_limpiar = tk.Button(
            self,
            text="Limpiar",
            command=self.limpiar_campos,
            bg="#f44336",
            fg="white",
            font=("Arial", 10, "bold"),
            width=10,
        )
        btn_limpiar.grid(row=5, column=1, pady=12, padx=10)

        
        self.lbl_promedio = tk.Label(self, text="Promedio: ", font=("Arial", 10, "bold"))
        self.lbl_promedio.grid(row=6, column=0, columnspan=2, sticky="w", padx=15, pady=3)

        self.lbl_desviacion = tk.Label(self, text="Desviación estándar: ", font=("Arial", 10, "bold"))
        self.lbl_desviacion.grid(row=7, column=0, columnspan=2, sticky="w", padx=15, pady=3)

        self.lbl_mayor = tk.Label(self, text="Mayor nota: ", font=("Arial", 10, "bold"))
        self.lbl_mayor.grid(row=8, column=0, columnspan=2, sticky="w", padx=15, pady=3)

        self.lbl_menor = tk.Label(self, text="Menor nota: ", font=("Arial", 10, "bold"))
        self.lbl_menor.grid(row=9, column=0, columnspan=2, sticky="w", padx=15, pady=3)

    def calcular_estadisticas(self):
        try:
            valores = []
            for entry in self.entradas_notas:
                val = float(entry.get())
                if not (0 <= val <= 5):
                    messagebox.showerror("Error", "Las notas deben estar entre 0 y 5.")
                    return
                valores.append(val)

            objeto_notas = Notas(valores)

            self.lbl_promedio.config(text=f"Promedio: {objeto_notas.calcular_promedio():.2f}")
            self.lbl_desviacion.config(
                text=f"Desviación estándar: {objeto_notas.calcular_desviacion_estandar():.2f}"
            )
            self.lbl_mayor.config(text=f"Mayor nota: {objeto_notas.calcular_mayor():.2f}")
            self.lbl_menor.config(text=f"Menor nota: {objeto_notas.calcular_menor():.2f}")

        except ValueError:
            messagebox.showerror("Error de Entrada", "Por favor ingrese valores numéricos válidos.")

    def limpiar_campos(self):
        for entry in self.entradas_notas:
            entry.delete(0, tk.END)
        self.lbl_promedio.config(text="Promedio: ")
        self.lbl_desviacion.config(text="Desviación estándar: ")
        self.lbl_mayor.config(text="Mayor nota: ")
        self.lbl_menor.config(text="Menor nota: ")


if __name__ == "__main__":
    app = VentanaNotas()
    app.mainloop()


    