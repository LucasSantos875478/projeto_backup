# importando as bibliotecas
import os
from tkinter import messagebox, filedialog
from pathlib import Path
import shutil
import zipfile


def pastas_backup():
    lista_diretorios = []
    while True:
        diretorio = filedialog.askdirectory(title='Selecione os diretórios para backup')
        if diretorio not in lista_diretorios:
            lista_diretorios.append(diretorio)
        parar = messagebox.askyesno('Gerando os caminhos', 'Precisa fazer backup em mais um diretório?')
        if not parar:
            break
    return lista_diretorios


def local_backup():
    while True:
        caminho = filedialog.askdirectory(title='Selecione o local para o backup')
        parar = messagebox.askyesno('Selecionando o caminho', 'O caminho para salvar o backup está correto?')
        if parar:
            break
    return caminho


def separando_arqdir(diretorios):
    lista_arquivos = []
    lista_diretorios = []
    for diretorio in diretorios:
        diretorio = Path(diretorio)
        arquivos = diretorio.iterdir()
        for arquivo in arquivos:
            if arquivo.is_dir():
                lista_diretorios.append(arquivo)
            else:
                lista_arquivos.append(arquivo)
    return lista_diretorios, lista_arquivos


def copiando_arquivos(arquivos, caminho_backup):
    if Path(caminho_backup / Path('Backup')).exists():
        for arquivo in arquivos:
            shutil.copy2(arquivo, Path(caminho_backup / Path('Backup')))
    else:
        Path(caminho_backup / Path('Backup')).mkdir()
        for arquivo in arquivos:
            shutil.copy2(arquivo, Path(caminho_backup / Path('Backup')))


def copiando_diretorios(diretorios, caminho_backup):
    for diretorio in diretorios:
        nome_diretorio = Path(diretorio).name
        novo_caminho = Path(caminho_backup / Path('Backup') / Path(nome_diretorio))
        shutil.copytree(diretorio, novo_caminho)


def zip_folder(caminho_backup):
    nome_zip = filedialog.askdirectory(title='Selecione o diretório para backup ser salvo')
    nome_zip = nome_zip + '/Backup'
    caminho_backup = caminho_backup + '/Backup'
    shutil.make_archive(nome_zip, 'zip', caminho_backup)
    shutil.rmtree(caminho_backup)
