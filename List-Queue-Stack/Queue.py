import time

class Queue:

    def __init__(self):
        self.queue = []
        self.len_queue = 0

    def push(self, e):
        self.queue.append(e)
        self.len_queue += 1

    def pop(self):
        if not self.empty():
            self.queue.pop(0)
            self.len_queue -= 1

    def empty(self):
        if self.len_queue == 0:
            return True
        return False

    def length(self):
        return self.len_queue

    def front(self):
        if not self.empty():
            return self.queue
        return None

    def menu(self, contador = 0):
        while contador == 0:

            print('Insira a opção desejada: \n')
            opcao = (input('0 - PARA SAIR\n'
                                '1 - PARA ADICIONAR A FILA\n'
                                '2 - PARA MOSTRAR A FILA\n'
                                '3 - PARA EXIBIR O TAMANHO DA FILA\n'
                                '4 - PARA REMOVER O PRIMEIRO ELEMENTO DA FILA\n'
                                '--->'))

            if opcao == '0':
                contador = 1

            elif opcao == '1':
                element = input('Coloque aqui o elemento para ser adicionado a fila:')
                q.push(element)
                print('Elemento adicionado a fila')
                time.sleep(2)

            elif opcao == '2':
                if q.empty():
                    print('FILA VAZIA')
                else:
                    print(q.front())
                    time.sleep(2)

            elif opcao == '3':
                print('Tamanho da fila:', q.length())
                time.sleep(2)
                

            elif opcao == '4':
                print('FILA ATUAL:', q.front())
                print('Apagando......')
                time.sleep(2)
                q.pop()
                print('FILA ATUALIZADA:',q.front())
                time.sleep(1)
                    


q = Queue()
q.menu()
