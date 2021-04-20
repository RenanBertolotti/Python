import os
import shutil

caminho_original = r"C:\Users\Reinan\Documents"
caminho_novo = r"C:\Users\Reinan\Documents\CriadoPeloPython"


try:
    os.mkdir(caminho_novo)     #Cria a pasta nova
except FileExistsError as e:
    print(f'Pasta {caminho_novo} já existe.')


for root, dirs, files in os.walk(caminho_original):
    for file in files:
        old_file_path = os.path.join(root, file)
        new_file_path = os.path.join(caminho_novo, file)

        #Para copiar ou mover arquivos por extensoes, pode-se utilizar:
        if ".str" in file: #nesse casso copia arquivos de extensão .str
            shutil.move(old_file_path, new_file_path)  #Move a os arquivos do "caminho antigo" para o "caminho novo"
            shutil.copy(old_file_path, new_file_path)  #Copia a os arquivos do "caminho antigo" para o "caminho novo"
            os.remove(new_file_path)  #Remove a os arquivos do "caminho novo"
            print(f"Arquivos {file} movido com sucesso")
