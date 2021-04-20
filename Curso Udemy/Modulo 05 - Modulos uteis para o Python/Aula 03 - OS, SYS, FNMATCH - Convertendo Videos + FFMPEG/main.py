#https://ffmpeg.zeranoe.com/builds/
"""precisa baixar o ffmpeg e colocar o arquivo ffmpeg.exe e criar uma pasta ffmpeg dentro da raiz deste .main"""

#https://ffmpeg.org/ffmpeg.html -- Documentação

"""  Esse comando abaixo converte o video inteiro
ffmpeg -i "ENTRADA" -i "LEGENDA" -c:v libx264 -crf 23 -preset ultrafast -c:a aac -b:a 320k
-c:s srt -map v:0 -map a 1:0 "SAIDA"
"""

"""  Esse comando abaixo converte o video no tempo setado, que nesse caso foi 10 segundos!
ffmpeg -i "ENTRADA" -i "LEGENDA" -c:v libx264 -crf 23 -preset ultrafast -c:a aac -b:a 320k
-c:s srt -map v:0 -map a 1:0 -ss 00:00:00 -to 00:00:10 "SAIDA"
"""

import os
import fnmatch
import sys

#ver se esta em um sistema operacional linux ou outro.
if sys.platform == 'linux':
    comando_ffmpeg = 'ffmpeg'
else:
    comando_ffmpeg = r"ffmpeg\ffmpeg.exe" #comando para acessar a o app dentro da pasta ffmpeg

codec_video = '-c:v libx264'
crf = '-crf 23'
preset = '-preset ultrafast'
codec_audio = '-c:a aac'
bitrate_audio = '-b:a 320k'
debug ='-ss 00:00:00 -to 00:00:10'

caminho_origem = r"C:\Users\Reinan\Videos\Filmes\Aberracoes [720p] [DUBLADO]"
caminho_destino = r"C:\Users\Reinan\Videos\Filmes\Aberracoes [720p] [DUBLADO]"

for raiz, pastas, arquivos in os.walk(caminho_origem):
    for arquivo in arquivos:
        if fnmatch.fnmatch(arquivo, '*.mp4'): #ve se o arquivo tem a determinada extensao
            caminho_completo = os.path.join(raiz, arquivo) #ve o caminho completo do arquivo junto com o nome.
            nome_arquivo, extensao_arquivo = os.path.splitext(caminho_completo) #divide o nome do arquivo e sua extensao
            caminho_legenda = nome_arquivo + '.srt'

            #Caso tiver legenda, devese utilizar isso abaixo:
            if os.path.isfile(caminho_legenda): #funcao que ve se um determinado arquivo existe na pasta!
                input_legenda = f'-i "{caminho_legenda}"'
                map_legenda = "-c:s srt -map v:0 -map a -map 1:0"
            else:
                input_legenda = ""
                map_legenda = ""
            ################################################################

            nome_arquivo, extensao_arquivo = os.path.splitext(arquivo)
            arquivo_saida = f'{caminho_destino}/{nome_arquivo}_NOVOARQUIVO{extensao_arquivo}' #da o nome do novo arquivo,caso queira mudar a extensao,fazer:
            #arquivo_saida = f'{caminho_destino}/{nome_arquivo}_NOVOARQUIVO.mkv'

            #comando para setar o tempo de video, foi utilizado o "{debug}"
            comando = f'{comando_ffmpeg} -i "{caminho_completo}" {input_legenda} {codec_video} {crf} {preset} {codec_audio} {bitrate_audio} {debug} {map_legenda} "{arquivo_saida}"'
            #caso nao queira tempo de video, utilizar: foi o mesmo comando, porem sem o "{debug}"
            #comando = f'{comando_ffmpeg} -i "{caminho_completo}" {input_legenda} {codec_video} {crf} {preset} {codec_audio} {bitrate_audio} {map_legenda} "{arquivo_saida}"'

            os.system(comando)
