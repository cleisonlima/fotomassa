import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image

# Função para abrir e carregar a imagem
def abrir_imagem():
    global img, caminho_arquivo
    caminho_arquivo = filedialog.askopenfilename(
        filetypes=[("Arquivos de Imagem", "*.png;*.jpg;*.jpeg;*.bmp;*.gif;*.ico")]
    )
    if caminho_arquivo:
        img = Image.open(caminho_arquivo)
        messagebox.showinfo("Imagem Carregada", f"Imagem {caminho_arquivo} carregada com sucesso!")

# Função para salvar/converter a imagem
def salvar_imagem():
    if img:
        formato = formato_var.get()
        if not formato:
            messagebox.showwarning("Aviso", "Selecione um formato para salvar!")
            return
        caminho_salvar = filedialog.asksaveasfilename(
            defaultextension=f".{formato.lower()}",
            filetypes=[(f"{formato} files", f"*.{formato.lower()}")]
        )
        if caminho_salvar:
            img.save(caminho_salvar, formato.upper())
            messagebox.showinfo("Sucesso", f"Imagem salva como {caminho_salvar}!")
    else:
        messagebox.showwarning("Aviso", "Nenhuma imagem carregada!")

# Janela principal
root = tk.Tk()
root.title("Foto Massa - Conversor de Imagens")
root.geometry("450x320")
root.configure(bg="#FFFAF0")  # cor de fundo clara e acolhedora

# Título
titulo = tk.Label(root, text="📸 Foto Massa", font=("Arial", 20, "bold"), bg="#FFFAF0", fg="#FF4500")
titulo.pack(pady=10)

subtitulo = tk.Label(root, text="Converta suas imagens rapidinho!", font=("Arial", 12), bg="#FFFAF0")
subtitulo.pack(pady=5)

# Botão para abrir imagem
btn_abrir = tk.Button(root, text="Abrir Imagem", font=("Arial", 12, "bold"), bg="#FFA500", fg="white", command=abrir_imagem)
btn_abrir.pack(pady=15, ipadx=10, ipady=5)

# Seleção de formato
formato_var = tk.StringVar()
tk.Label(root, text="Escolha o formato:", font=("Arial", 12), bg="#FFFAF0").pack(pady=5)

frame_formatos = tk.Frame(root, bg="#FFFAF0")
frame_formatos.pack(pady=5)
formatos = ["PNG", "JPEG", "BMP", "GIF", "ICO"]
for f in formatos:
    tk.Radiobutton(frame_formatos, text=f, variable=formato_var, value=f, font=("Arial", 11), bg="#FFFAF0").pack(side="left", padx=10)

# Botão para salvar/converter
btn_salvar = tk.Button(root, text="Salvar Imagem", font=("Arial", 12, "bold"), bg="#32CD32", fg="white", command=salvar_imagem)
btn_salvar.pack(pady=20, ipadx=10, ipady=5)

# Inicializa variável global
img = None
caminho_arquivo = None

# Executa a aplicação
root.mainloop()
