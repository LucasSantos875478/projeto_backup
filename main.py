import funcoes
from tkinter import messagebox

diretorios = funcoes.pastas_backup()
caminho_backup = funcoes.local_backup()
dirs, arqs = funcoes.separando_arqdir(diretorios)
funcoes.copiando_diretorios(dirs, caminho_backup)
funcoes.copiando_arquivos(arqs, caminho_backup)
funcoes.zip_folder(caminho_backup)
messagebox.showinfo('Backup Finalizado', 'Backup Realizado com sucesso!!')
