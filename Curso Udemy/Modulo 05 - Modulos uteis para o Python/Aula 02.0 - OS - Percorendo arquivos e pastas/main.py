import os

def formata_tamanho(tamanho):
    base = 1024
    kilo = base
    mega = base ** 2
    giga = base ** 3
    tera = base ** 4
    peta = base ** 5

    if tamanho < kilo:
        texto = "B"
    elif tamanho < mega:
        tamanho /= kilo
        texto = 'K'
    elif tamanho < giga:
        tamanho /= mega
        texto = 'M'
    elif tamanho < tera:
        tamanho /= giga
        texto = 'G'
    elif tamanho < peta:
        tamanho /= tera
        texto = 'T'
    else:
        tamanho /= peta
        texto = 'P'

    tamanho = round(tamanho, 2)
    return f'{tamanho}-{texto}'

#tambem pode usar com barra invertida: caminho_procura = r'\Users\Reinan\Documents'
caminho_procura = '/Users/Reinan/Documents'
#ou caminho_procura = input("Digite um caminho: ")
termo_procura = "Tabela"
#ou termo_procura = input("Digite um termo: ")

contador = 0

for raiz, diretorios, arquivos in os.walk(caminho_procura):
    for arquivo in arquivos:
        if termo_procura in arquivo:
            try:
                contador += 1
                caminho_completo = os.path.join(raiz, arquivo) #pega o caminho completo dos arquivos
                nome_arquivo, ext_arquivo = os.path.splitext(caminho_completo)  #separa a lista em caminhoEnome e extensao do arquivo
                tamanho = os.path.getsize(caminho_completo) #mostra o tamanho dos arquivos

                print()
                print("Encontrei o arquivo:",arquivo)
                print("Caminho:",caminho_completo)
                print("Nome:", nome_arquivo)
                print("Extensão:", ext_arquivo)
                print("Tamanho:", tamanho)
                print("Tamanho formatado: ", formata_tamanho(tamanho))
            except PermissionError as e:
                print("Sem permissões.")
            except FileNotFoundError as e:
                print("Arquivo nao encontrado")
            except Exception as e:
                print("Erro desconhecido")

print()
print(f"{contador} arquivo(s) encontrado(s).")