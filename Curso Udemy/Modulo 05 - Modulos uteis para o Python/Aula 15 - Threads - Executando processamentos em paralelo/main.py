from time import sleep
from threading import Thread  # Precisa importar a Classe Thread
from threading import Lock

""" Existe 2 maneiras de se fazer uma Thread, a 1º é criar uma classe:
class MeuThread(Thread):
    def __init__(self, texto, tempo):
        self.texto = texto
        self.tempo = tempo

        super().__init__()

    def run(self):
        sleep(self.tempo)
        print(self.texto)
        

t1 = MeuThread("Thread 1", 5)
t1.start()

t2 = MeuThread("Thread 2", 2)
t2.start()

t3 = MeuThread("Thread 3", 3)
t3.start()

for i in range(20):
    print(i)
    sleep(1)
"""
#####--------------------------------------------------------------------#####

"""
#A 2º maneira é usar a propria classe Thread, segue exemplo a baixo:
def vai_demorar(texto, tempo):
    sleep(tempo)
    print(texto)


t1 = Thread(target=vai_demorar, args=('ola mundo 1!', 5))
t1.start()

t2 = Thread(target=vai_demorar, args=('ola mundo 2!', 1))
t2.start()

t3 = Thread(target=vai_demorar, args=('ola mundo 3!', 3))
t3.start()

for i in range(20):
    print(i)
    sleep(.5)
"""


###############----------OUTRO EXEMPLO---------------------####################
"""
def vai_demorar(texto, tempo):
    sleep(tempo)
    print(texto)


t1 = Thread(target=vai_demorar, args=('ola mundo 1!', 5))
t1.start()

## Tambem é possivel fazer a Thread só executar ela, para isso utiliza o ".join()"
## exemplo:
## t1.join()  ---- Fazendo isso a Thread sera executado primeiro e so depois o codigo continuara.

while t1.is_alive():  #Checa se a Thread está rodando no sistema
    print("Esperando a Thread")
    sleep(2)
"""

###############----------OUTRO EXEMPLO---------------------####################
#Nesse exemplo foi utilizado a Classe Lock, ela trava um metodo para que ele seja executado um de cada vez, independente
#de quantas Threads sejam executada.
# Para usar é necessario utilizar na Classe o "self.lock = Lock()" e no metodo utilizada o self.lock.acquire e o self.lock.release()
# que servem para marcar o inicio e o final do metodo;

class Ingressos:
    def __init__(self, estoque):
        self.estoque = estoque
        self.lock = Lock()

    def comprar(self, quantidade):
        self.lock.acquire()
        if self.estoque < quantidade:
            print("Não temos ingresso suficientes! ")
            self.lock.release()
            return

        sleep(1)

        self.estoque -= quantidade

        print(f"Voce comprou {quantidade} ingresso(s). Ainda temos {self.estoque} ingressos em estoque")
        self.lock.release()


if __name__ == "__main__":
    ingressos = Ingressos(10)

    for i in range(1, 20):
        t = Thread(target= ingressos.comprar, args=(i,))
        t.start()

    print(ingressos.estoque)
