import time

class Stack:

    def __init__(self):
        self.stack = []
        self.len_stack = 0

    def push(self, e):
        self.stack.append(e)
        self.len_stack += 1

    def pop(self):
        if not self.empty():
            self.stack.pop(self.len_stack - 1)
            self.len_stack -= 1

    def top(self):
        if not self.empty():
            return self.stack[-1]
        return None

    def empty(self):
        if self.len_stack == 0:
            return True
        return False

    def length(self):
        return self.len_stack

    def menu(self, contador = 0):
        while contador == 0:

            print('Insira a opção desejada: \n')
            opcao = (input('0 - PARA SAIR\n'
                                '1 - PARA ADICIONAR A PILHA\n'
                                '2 - PARA MOSTRAR O ELEMENTO NO TOPO DA PILHA\n'
                                '3 - PARA EXIBIR O TAMANHO DA PILHA\n'
                                '4 - PARA REMOVER O ELEMENTO DO TOPO DA PILHA\n'
                                '--->'))

            if opcao == '0':
                contador = 1

            elif opcao == '1':
                element = input('Coloque aqui o elemento para ser adicionado a pilha:')
                s.push(element)
                print('Elemento adicionado a pilha')
                time.sleep(2)

            elif opcao == '2':
                if s.empty():
                    print('PILHA VAZIA')
                else:
                    print(s.top())
                    time.sleep(2)

            elif opcao == '3':
                print('Tamanho da pilha:', s.length())
                time.sleep(2)
                

            elif opcao == '4':
                print('TOPO DA PILHA :', s.top())
                print('Apagando......')
                time.sleep(2)
                s.pop()
                print('TOPO DA PILHA ATUALIZADA:',s.top())
                time.sleep(1)


s = Stack()
s.menu()