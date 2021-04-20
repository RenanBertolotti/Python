"""
Documentação:
https://pythonhosted.org/PyPDF2/
Mais exemplos de uso:
http://www.blog.pythonlibrary.org/2018/06/07/an-intro-to-pypdf2/

pip install pypdf2 # virtualenv
pipenv install pypdf2 # pipenv
"""
import PyPDF2
import os

###### Unindo PDF
caminhoPDF = "pdf"

novo_pdf = PyPDF2.PdfFileMerger()


for root, dirs, files in os.walk(caminhoPDF):
    for file in files:
        if file.endswith(".pdf"): #Checa se é pdf
            caminhoCompleto = os.path.join(root, file)

            arquivo_pdf = open(caminhoCompleto, "rb")
            novo_pdf.append(arquivo_pdf)

with open(f"{caminhoPDF}/novo_arquivo.pdf", 'wb') as meu_novo_pdf:
    novo_pdf.write(meu_novo_pdf)


###### Dividindo PDF
with open('pdf/novo_arquivo.pdf', "rb") as arquivoPdf:
    leitor = PyPDF2.PdfFileReader(arquivoPdf)
    num_paginas = leitor.getNumPages()

    for pagina in range(num_paginas):
        escritor = PyPDF2.PdfFileWriter()
        pagina_atual = leitor.getPage(pagina)
        escritor.addPage(pagina_atual)

        with open(f"NovosPdfs/{pagina}.pdf", "wb") as novo_pdf:
            escritor.write(novo_pdf)