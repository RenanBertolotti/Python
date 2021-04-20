class TaErradoError(Exception):
    pass


def testar():
    raise TaErradoError("Ta Errado")

try:
    testar()
except TaErradoError as e:
    print(e)