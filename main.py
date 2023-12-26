import tkinter as tk
from tkinter import messagebox, colorchooser, filedialog

def salvar_configuracoes():
    try:
        with open("config.txt", "w") as config_file:
            config_file.write(f"{text_editor.cget('bg')}\n")
            config_file.write(f"{text_editor.cget('fg')}\n")
    except Exception as e:
        messagebox.showerror("Erro ao Salvar Configurações", f"Ocorreu um erro ao salvar as configurações: {e}")

def carregar_configuracoes():
    try:
        with open("config.txt", "r") as config_file:
            cor_bg = config_file.readline().strip()
            cor_fg = config_file.readline().strip()
            text_editor.config(bg=cor_bg, fg=cor_fg)
    except FileNotFoundError:
        pass
    except Exception as e:
        messagebox.showerror("Erro ao Carregar Configurações", f"Ocorreu um erro ao carregar as configurações: {e}")

def mudar_tema():
    global modo_escuro
    if modo_escuro:
        text_editor.config(bg='white', fg='black')
        modo_escuro = False
    else:
        text_editor.config(bg='black', fg='white')
        modo_escuro = True
    salvar_configuracoes()

def sobre():
    messagebox.showinfo("Sobre", "Feito por Alisso")

def mudar_cor_selecionada():
    cor = colorchooser.askcolor(title="Escolha uma cor")[1]
    if text_editor.tag_ranges(tk.SEL):
        inicio, fim = text_editor.tag_ranges(tk.SEL)
        text_editor.tag_add(f"cor_{inicio}_{fim}", inicio, fim)
        text_editor.tag_config(f"cor_{inicio}_{fim}", foreground=cor)
    else:
        messagebox.showwarning("Aviso", "Nenhuma área de texto está selecionada.")
    salvar_configuracoes()

def contar_palavras():
    conteudo = text_editor.get("1.0", tk.END)
    palavras = conteudo.split()
    contagem = len(palavras)
    messagebox.showinfo("Contagem de Palavras", f"Total de palavras: {contagem}")

def salvar_arquivo():
    caminho_arquivo = filedialog.asksaveasfilename(defaultextension=".txt",
                                                   filetypes=[("Arquivos de Texto", "*.txt"),
                                                              ("Todos os Arquivos", "*.*")])
    if caminho_arquivo:
        conteudo = text_editor.get("1.0", tk.END)
        try:
            with open(caminho_arquivo, "w") as arquivo:
                arquivo.write(conteudo)
            messagebox.showinfo("Salvo", "Arquivo salvo com sucesso!")
        except Exception as e:
            messagebox.showerror("Erro ao Salvar", f"Ocorreu um erro ao salvar o arquivo: {e}")

raiz = tk.Tk()
raiz.title("Bloco de Notas")

modo_escuro = False

barra_menu = tk.Menu(raiz)

menu_arquivo = tk.Menu(barra_menu, tearoff=0)
menu_arquivo.add_command(label="Sair", command=raiz.destroy)

menu_editar = tk.Menu(barra_menu, tearoff=0)
menu_editar.add_command(label="Mudar Tema", command=mudar_tema)
menu_editar.add_command(label="Mudar Cor Selecionada", command=mudar_cor_selecionada)
menu_editar.add_command(label="Contar Palavras", command=contar_palavras)

menu_ajuda = tk.Menu(barra_menu, tearoff=0)
menu_ajuda.add_command(label="Sobre", command=sobre)

barra_menu.add_cascade(label="Arquivo", menu=menu_arquivo)
barra_menu.add_cascade(label="Editar", menu=menu_editar)
barra_menu.add_cascade(label="Ajuda", menu=menu_ajuda)

raiz.config(menu=barra_menu)

text_editor = tk.Text(raiz)
text_editor.pack(expand=True, fill='both')

text_editor.config(bg='white', fg='black')

menu_arquivo.add_command(label="Salvar", command=salvar_arquivo)
carregar_configuracoes()
raiz.mainloop()
