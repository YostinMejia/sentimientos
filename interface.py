import tkinter as tk
from tkinter import messagebox
from analyzer import Analyzer  # Importar la clase Analyzer

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Analizador de Comentarios de Publicaciones")

        self.analyzer = Analyzer()

        # Componentes de la interfaz de usuario
        self.label = tk.Label(root, text="Introduce tu comentario:")
        self.label.pack()

        self.comment_entry = tk.Entry(root, width=50)
        self.comment_entry.pack()

        self.language_label = tk.Label(root, text="Selecciona el idioma:")
        self.language_label.pack()

        # Selección de idioma
        self.language_var = tk.StringVar(value="en")
        self.language_menu = tk.OptionMenu(root, self.language_var, "en", "es", "fr", "de", "it")
        self.language_menu.pack()

        self.analyze_button = tk.Button(root, text="Analizar Comentario", command=self.analyze_comment)
        self.analyze_button.pack()

    def analyze_comment(self):
        comment = self.comment_entry.get()
        language = self.language_var.get()

        if not comment:
            messagebox.showwarning("Error de Entrada", "Por favor, introduce un comentario.")
            return

        result = self.analyzer.analyze(comment, language)

        if result['pos'] > result['neg']:
            message = "¡Te gustó la publicación!"
        elif result['pos'] < result['neg']:
            message = "No te gustó la publicación."
        else:
            message = "Tu comentario es neutral."

        messagebox.showinfo("Resultado del Análisis de Sentimientos", message)

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
