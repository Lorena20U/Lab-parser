class Node:
    def __init__(self, val):
        self.valor = val
        self.next = None

    def getValor(self):
        return self.valor
 
    def getNext(self):
        return self.next
 
    def setValor(self, val):
        self.valor = val

    def setNext(self, val):
        self.next = val

class List:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head is None

    #Agregando nodo a la lista
    def add(self, v):
        new_node = Node(v)
        new_node.setNext(self.head)
        self.head = new_node

    #imprimir
    def printList(self):
        current = self.head
        while current is not None:
            print(f"Value: {current.getValor()}")
            current = current.getNext()

#a = List()
#a.add(5)
#a.printList()