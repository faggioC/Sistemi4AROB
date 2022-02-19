class Pila():
    def __init__(self):
        self.pila = []

    def push(self,elemento):
        self.pila.append(elemento)
    
    def pop(self):
        if len(self.pila) == 0:
            return None
        else: return self.pila.pop()

    def print(self):
        print(self.pila)

class Coda():
    def __init__(self):
        self.coda = []

    def enqueue(self,elemento):
        self.coda.append(elemento)
    
    def dequeue(self):
        if len(self.coda) == 0:
            return None
        else: return self.coda.pop(0)

    def print(self):
        print(self.coda)
