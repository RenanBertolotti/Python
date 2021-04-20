"""
Exercicio de perguntas e respostas
"""

perguntas = {
    "Pergunta 1" : {
        "pergunta"   : "Quanto é 2+2? ",
        "respostas" : {
            "a" : '1',
            "b" : '4',
            "c" : '5',
        },
        "resposta_certa" : "b",
    },
    "Pergunta 2": {
        "pergunta": "Quanto é 3*2? ",
        "respostas": {
            "a": '62',
            "b": '10',
            "c": '6',
        },
        "resposta_certa": "c",
    }
}

print()

for pk, pv in perguntas.items():
    print(f"{pk}: {pv['pergunta']}")

    print("Escolha uma opção abaixo:")
    for rk, rv in pv["respostas"].items():
        print(f"[{rk}]: {rv}")

    resposta_usuario = input("Sua resposta: ")

    if resposta_usuario == (pv["resposta_certa"]):
        print("Voce acertou")
    else:
        print("Voce errou")

    print()
