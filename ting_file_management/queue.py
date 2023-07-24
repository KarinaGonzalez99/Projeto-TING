from collections import deque
from ting_file_management.abstract_queue import AbstractQueue


class Queue(AbstractQueue):
    def __init__(self):
        """Inicialize sua estrutura aqui"""
        self.items = deque()

    def __len__(self):
        """Retorna o número de elementos na fila"""
        return len(self.items)

    def enqueue(self, value):
        """Adiciona um item ao final da fila"""
        self.items.append(value)

    def dequeue(self):
        """Remove um item do início da fila"""
        if not self.is_empty():
            return self.items.popleft()
        else:
            return None

    def search(self, index):
        """Retorna um item da fila baseado em um índice"""
        if index < 0 or index >= len(self.items):
            raise IndexError("Índice Inválido ou Inexistente")
        else:
            return self.items[index]

    def is_empty(self):
        """Retorna True se a fila estiver vazia"""
        return not bool(self.items)
