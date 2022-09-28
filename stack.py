class Stack:
    def __init__(self, posicion):
        self.stack = []
        self.posicion = posicion

    def __bool__(self):
        return bool(self.stack)

    def __str__(self):
        return str(self.stack)

    def push(self, data):
        #Empuja a la parte sup
        self.stack.append(data)

    def pop(self):
        #Saca un elem de la parte sup
        return self.stack.pop()

    def peek(self):
        #Observa al elemento superior de la pila
        return self.stack[-1]

    def is_empty(self):
        #Comprueba si esta vacia
        return not bool(self.stack)

    def size(self):
        #Tamanio
        return len(self.stack)

    def __contains__(self, item):
        #Comprueba si esta en la pila
        return item in self.stack

#a = Stack(1)
#a.push(1)
#a.push(2)
#print(a)