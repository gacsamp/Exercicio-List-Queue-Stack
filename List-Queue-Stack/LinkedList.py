import time
import os

class Node:

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.next = None

    def nomeGet(self):
        return self.nome

    def nomeSet(self, nome):
        self._nome = nome

    def idadeGet(self):
        return self.idade

    def idadeSet(self, idade):
        self._idade = idade

    def getNext(self):
        return self.next

    def setNext(self, next):
        self.next = next


class LinkedList:

    def __init__(self):
        self.first = None
        self.last = None
        self.len_list = 0

    def push(self, nome, idade, index):

        if index >= 0:

            # cria o novo nó
            node = Node(nome, idade)

            # verifica se a lista está vazia
            if self.empty():
                self.first = node
                self.last = node
            else:

                if index == 0:
                    # inserção no início
                    node.setNext(self.first)
                    self.first = node
                elif index >= self.len_list:
                    # inserção ao final
                    self.last.setNext(node)
                    self.last = node
                else:
                    # inserção no meio
                    prev_node = self.first
                    curr_node = self.first.getNext()
                    curr_index = 1

                    while curr_node != None:

                        if curr_index == index:
                            # seta o curr_node como o próximo do nó
                            node.setNext(curr_node)
                            # seta o node como o próximo do prev_nodes
                            prev_node.setNext(node)

                        prev_node = curr_node
                        curr_node = curr_node.getNext()
                        curr_index += 1

            # atualiza o tamanho da lista
            self.len_list += 1

    def pop(self, index):

        if not self.empty() and index >= 0 and index < self.len_list:

            flag_remove = False

            if self.first.getNext() == None:
                # possui apenas 1 elemento
                self.first = None
                self.last = None
                flag_remove = True
            elif index == 0:
                # remove do início, mas possui mais de 1 elemento
                self.first = self.first.getNext()
                flag_remove = True
            else:
                '''
                    Se chegou aqui é porque a lista possui mais
                    de 1 elemento e a remoção não é no início
                '''

                prev_node = self.first
                curr_node = self.first.getNext()
                curr_index = 1

                while curr_node != None:

                    if index == curr_index:
                        # o próximo do anterior aponta para o próximo do nó corrente
                        prev_node.setNext(curr_node.getNext())
                        curr_node.setNext(None)
                        flag_remove = True
                        break

                    prev_node = curr_node
                    curr_node = curr_node.getNext()
                    curr_index += 1

            if flag_remove:
                # atualiza o tamanho da lista
                self.len_list -= 1

    def empty(self):
        if self.first == None:
            return True
        return False

    def length(self):
        return self.len_list

    def show(self):
        contador = 0
        curr_node = self.first

        while curr_node != None:
            print(contador,'-','Nome:',curr_node.nomeGet(),'|Idade:',curr_node.idadeGet(),'anos',end='\n')
            curr_node = curr_node.getNext()
            contador +=1
        print('')
    
    def menu(self, contador = 0):
        while contador == 0:

            print('Insira a opção desejada: \n')
            opcao = (input('0 - PARA SAIR\n'
                                '1 - PARA ADCIONAR\n'
                                '2 - PARA MOSTRAR SUAS INFORMAÇÕES EM TELA\n'
                                '3 - PARA EXIBIR O TAMANHO DA LISTA\n'
                                '4 - PARA REMOVER QUALQUER NÓ\n'
                                '--->'))
    

            if opcao == '0':
                contador = 1

            elif opcao == '1':
                os.system('cls' if os.name == 'nt' else 'clear')
                print(35*'-')
                name = input('insira seu nome: ')
                age = int(input('insira sua idade: '))
                posicao  = int(input('insira a posição:'))
                print(35* '-')
                lista.push(name, age, posicao)
                print('Criando nó na aplicação......')
                time.sleep(1)
                print('Nó criado com sucesso ')
                time.sleep(1)
                print(35*'-')
                os.system('cls' if os.name == 'nt' else 'clear')
            
            elif opcao == '2':
                if lista.empty():
                    print('Lista Vazia')
                    time.sleep(1)
                else:
                    lista.show()
                    print(35 * '-')
                    
                    
            
            elif opcao == '3':
                print(35* '-')
                print('Tamanho da lista: {}\n' .format(lista.length()))
                time.sleep(1)

            elif opcao == '4':
                os.system('cls' if os.name == 'nt' else 'clear')
                print(35 * '-')
                lista.show()
                nó = int(input('Coloque o número do nó que quer remover: '))
                lista.pop(nó)
                print('Removendo.......')
                time.sleep(2)
                print('Nó removido')
                print(35 * '-')
                lista.show()
                time.sleep(2)


lista = LinkedList()
lista.menu()