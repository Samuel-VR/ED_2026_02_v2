class Heap:

    def __init__(self):
        self.arreglo = [float('-inf')]

    def insert(self, valor):
        self.arreglo.append(valor)
        indice_hijo=len(self.arreglo)-1
        hijo=self.arreglo[indice_hijo]
        indice_padre=indice_hijo//2
        padre=self.arreglo[indice_padre]
        while hijo<padre:
            self.arreglo[indice_hijo], self.arreglo[indice_padre] = self.arreglo[indice_padre], self.arreglo[indice_hijo]

            indice_hijo=indice_padre
            indice_padre=indice_hijo//2
            hijo=self.arreglo[indice_hijo]
            padre=self.arreglo[indice_padre]

    def remove_smallest(self):

        menor = self.arreglo[1]
        ultimo = self.arreglo.pop()

        if len(self.arreglo) > 1:
            self.arreglo[1] = ultimo
            indice = 1

            while 2 * indice < len(self.arreglo):
                hijo = 2 * indice
                hijo_derecho = hijo + 1

                if (hijo_derecho < len(self.arreglo)
                        and self.arreglo[hijo_derecho] < self.arreglo[hijo]):
                    hijo = hijo_derecho

                if self.arreglo[indice] <= self.arreglo[hijo]:
                    break

                self.arreglo[indice], self.arreglo[hijo] = (self.arreglo[hijo], self.arreglo[indice])
                indice = hijo

        return menor

    def build_heap(self, lista):
        pass
