import tkinter as tk

class BlocoMemoria:
    def __init__(self, inicio, tamanho, processo=None):
        self.inicio = inicio
        self.tamanho = tamanho
        self.processo = processo

# Exemplo de memória final
memoria = [
    BlocoMemoria(0, 150, "P2"),
    BlocoMemoria(150, 250, "P4"),
    BlocoMemoria(400, 250, "P4"),
    BlocoMemoria(650, 120, "P5"),
    BlocoMemoria(770, 230, None),
]

class MemoriaGUI(tk.Tk):
    def __init__(self, memoria):
        super().__init__()
        self.title("Simulador de Gerenciamento de Memória")
        self.geometry("850x300")
        self.memoria = memoria
        self._criar_widgets()

    def _criar_widgets(self):
        self.canvas = tk.Canvas(self, width=800, height=100, bg='white')
        self.canvas.pack(pady=20)

        legenda_frame = tk.Frame(self)
        legenda_frame.pack()

        tk.Label(legenda_frame, text="Legenda:", font=("Arial", 10, "bold")).pack(side="left", padx=5)
        tk.Label(legenda_frame, text="Livre", bg="lightgray", width=10).pack(side="left", padx=5)
        tk.Label(legenda_frame, text="Ocupado", bg="skyblue", width=10).pack(side="left", padx=5)

        self._desenhar_memoria()

    def _desenhar_memoria(self):
        largura_total = 800
        altura_bloco = 60
        memoria_total = sum(bloco.tamanho for bloco in self.memoria)
        pos_x = 0

        for bloco in self.memoria:
            largura = (bloco.tamanho / memoria_total) * largura_total
            cor = 'lightgray' if bloco.processo is None else 'skyblue'
            self.canvas.create_rectangle(pos_x, 20, pos_x + largura, 20 + altura_bloco, fill=cor, outline='black')
            texto = f"{bloco.processo or 'Livre'}\n{bloco.tamanho} KB"
            self.canvas.create_text(pos_x + largura / 2, 20 + altura_bloco / 2, text=texto, font=("Arial", 9))
            pos_x += largura

if __name__ == "__main__":
    gui = MemoriaGUI(memoria)
    gui.mainloop()
