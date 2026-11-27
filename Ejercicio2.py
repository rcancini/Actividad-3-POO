import math
import tkinter as tk
from tkinter import messagebox


class FiguraGeometrica:
    def __init__(self):
        self.volumen = 0.0
        self.superficie = 0.0

    def calcular_volumen(self) -> float:
        return 0.0

    def calcular_superficie(self) -> float:
        return 0.0


class Cilindro(FiguraGeometrica):
    def __init__(self, radio: float, altura: float):
        super().__init__()
        self.radio = radio
        self.altura = altura
        self.volumen = self.calcular_volumen()
        self.superficie = self.calcular_superficie()

    def calcular_volumen(self) -> float:
        return math.pi * math.pow(self.radio, 2) * self.altura

    def calcular_superficie(self) -> float:
        area_base = math.pi * math.pow(self.radio, 2)
        area_lateral = 2 * math.pi * self.radio * self.altura
        return (2 * area_base) + area_lateral


class Esfera(FiguraGeometrica):
    def __init__(self, radio: float):
        super().__init__()
        self.radio = radio
        self.volumen = self.calcular_volumen()
        self.superficie = self.calcular_superficie()

    def calcular_volumen(self) -> float:
        return (4 / 3) * math.pi * math.pow(self.radio, 3)

    def calcular_superficie(self) -> float:
        return 4 * math.pi * math.pow(self.radio, 2)


class Piramide(FiguraGeometrica):
    def __init__(self, base: float, altura: float, apotema: float):
        super().__init__()
        self.base = base
        self.altura = altura
        self.apotema = apotema
        self.volumen = self.calcular_volumen()
        self.superficie = self.calcular_superficie()

    def calcular_volumen(self) -> float:
        return (math.pow(self.base, 2) * self.altura) / 3

    def calcular_superficie(self) -> float:
        area_base = math.pow(self.base, 2)
        area_lateral = 2 * self.base * self.apotema
        return area_base + area_lateral



class VentanaPrincipal(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Figuras Geométricas 3D")
        self.geometry("350x250")
        self.resizable(False, False)

        tk.Label(self, text="Seleccione la Figura Geométrica", font=("Arial", 12, "bold")).pack(pady=20)

        btn_cilindro = tk.Button(self, text="Cilindro", command=self.abrir_cilindro, width=20, bg="#2196F3", fg="white", font=("Arial", 10, "bold"))
        btn_cilindro.pack(pady=5)

        btn_esfera = tk.Button(self, text="Esfera", command=self.abrir_esfera, width=20, bg="#2196F3", fg="white", font=("Arial", 10, "bold"))
        btn_esfera.pack(pady=5)

        btn_piramide = tk.Button(self, text="Pirámide", command=self.abrir_piramide, width=20, bg="#2196F3", fg="white", font=("Arial", 10, "bold"))
        btn_piramide.pack(pady=5)

    def abrir_cilindro(self):
        VentanaCilindro(self)

    def abrir_esfera(self):
        VentanaEsfera(self)

    def abrir_piramide(self):
        VentanaPiramide(self)



class VentanaCilindro(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Cilindro")
        self.geometry("280x240")

        tk.Label(self, text="Radio (cm):").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.txt_radio = tk.Entry(self, width=12)
        self.txt_radio.grid(row=0, column=1, padx=10, pady=10)

        tk.Label(self, text="Altura (cm):").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.txt_altura = tk.Entry(self, width=12)
        self.txt_altura.grid(row=1, column=1, padx=10, pady=10)

        btn_calc = tk.Button(self, text="Calcular", command=self.calcular, bg="#4CAF50", fg="white", font=("Arial", 9, "bold"))
        btn_calc.grid(row=2, column=0, columnspan=2, pady=10)

        self.lbl_vol = tk.Label(self, text="Volumen (cm³): ", font=("Arial", 9, "bold"))
        self.lbl_vol.grid(row=3, column=0, columnspan=2, sticky="w", padx=10, pady=2)

        self.lbl_sup = tk.Label(self, text="Superficie (cm²): ", font=("Arial", 9, "bold"))
        self.lbl_sup.grid(row=4, column=0, columnspan=2, sticky="w", padx=10, pady=2)

    def calcular(self):
        try:
            r = float(self.txt_radio.get())
            h = float(self.txt_altura.get())
            c = Cilindro(r, h)
            self.lbl_vol.config(text=f"Volumen (cm³): {c.volumen:.2f}")
            self.lbl_sup.config(text=f"Superficie (cm²): {c.superficie:.2f}")
        except ValueError:
            messagebox.showerror("Error", "Ingrese valores numéricos válidos.")


class VentanaEsfera(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Esfera")
        self.geometry("280x200")

        tk.Label(self, text="Radio (cm):").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.txt_radio = tk.Entry(self, width=12)
        self.txt_radio.grid(row=0, column=1, padx=10, pady=10)

        btn_calc = tk.Button(self, text="Calcular", command=self.calcular, bg="#4CAF50", fg="white", font=("Arial", 9, "bold"))
        btn_calc.grid(row=1, column=0, columnspan=2, pady=10)

        self.lbl_vol = tk.Label(self, text="Volumen (cm³): ", font=("Arial", 9, "bold"))
        self.lbl_vol.grid(row=2, column=0, columnspan=2, sticky="w", padx=10, pady=2)

        self.lbl_sup = tk.Label(self, text="Superficie (cm²): ", font=("Arial", 9, "bold"))
        self.lbl_sup.grid(row=3, column=0, columnspan=2, sticky="w", padx=10, pady=2)

    def calcular(self):
        try:
            r = float(self.txt_radio.get())
            e = Esfera(r)
            self.lbl_vol.config(text=f"Volumen (cm³): {e.volumen:.2f}")
            self.lbl_sup.config(text=f"Superficie (cm²): {e.superficie:.2f}")
        except ValueError:
            messagebox.showerror("Error", "Ingrese valores numéricos válidos.")


class VentanaPiramide(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Pirámide")
        self.geometry("280x280")

        tk.Label(self, text="Base (cm):").grid(row=0, column=0, padx=10, pady=8, sticky="w")
        self.txt_base = tk.Entry(self, width=12)
        self.txt_base.grid(row=0, column=1, padx=10, pady=8)

        tk.Label(self, text="Altura (cm):").grid(row=1, column=0, padx=10, pady=8, sticky="w")
        self.txt_altura = tk.Entry(self, width=12)
        self.txt_altura.grid(row=1, column=1, padx=10, pady=8)

        tk.Label(self, text="Apotema (cm):").grid(row=2, column=0, padx=10, pady=8, sticky="w")
        self.txt_apotema = tk.Entry(self, width=12)
        self.txt_apotema.grid(row=2, column=1, padx=10, pady=8)

        btn_calc = tk.Button(self, text="Calcular", command=self.calcular, bg="#4CAF50", fg="white", font=("Arial", 9, "bold"))
        btn_calc.grid(row=3, column=0, columnspan=2, pady=10)

        self.lbl_vol = tk.Label(self, text="Volumen (cm³): ", font=("Arial", 9, "bold"))
        self.lbl_vol.grid(row=4, column=0, columnspan=2, sticky="w", padx=10, pady=2)

        self.lbl_sup = tk.Label(self, text="Superficie (cm²): ", font=("Arial", 9, "bold"))
        self.lbl_sup.grid(row=5, column=0, columnspan=2, sticky="w", padx=10, pady=2)

    def calcular(self):
        try:
            b = float(self.txt_base.get())
            h = float(self.txt_altura.get())
            a = float(self.txt_apotema.get())
            p = Piramide(b, h, a)
            self.lbl_vol.config(text=f"Volumen (cm³): {p.volumen:.2f}")
            self.lbl_sup.config(text=f"Superficie (cm²): {p.superficie:.2f}")
        except ValueError:
            messagebox.showerror("Error", "Ingrese valores numéricos válidos.")


if __name__ == "__main__":
    app = VentanaPrincipal()
    app.mainloop()


    