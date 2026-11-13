class Heap:
    """Min-heap implementado con un arreglo y posiciones desde 1."""

    def __init__(self):
        # La posición 0 es un centinela y no pertenece al heap.
        self.arreglo = [float("-inf")]

    def insert(self, valor, imagen=False):
        """Inserta un valor y lo desplaza hacia arriba si es necesario."""
        self.arreglo.append(valor)
        posicion = len(self.arreglo) - 1

        # Percolación hacia arriba.
        while posicion > 1:
            padre = posicion // 2
            if self.arreglo[posicion] < self.arreglo[padre]:
                self.arreglo[posicion], self.arreglo[padre] = (
                    self.arreglo[padre], self.arreglo[posicion]
                )
                posicion = padre
            else:
                break

        if imagen:
            self._dibujar()

    def remove_smallest(self, imagen=False):
        """Elimina y devuelve la raíz, que contiene el menor valor."""
        cantidad = len(self.arreglo) - 1

        if cantidad == 0:
            return None

        menor = self.arreglo[1]

        # Si solo hay un elemento, basta con quitarlo.
        if cantidad == 1:
            self.arreglo.pop()
        else:
            # El último elemento ocupa temporalmente el lugar de la raíz.
            self.arreglo[1] = self.arreglo.pop()
            self._bajar(1)

        if imagen:
            self._dibujar()

        return menor

    def build_heap(self, lista, imagen=False):
        """Construye un min-heap mediante el método de abajo hacia arriba."""
        self.arreglo = [float("-inf")] + list(lista)

        # Las hojas ya son heaps. Se reorganizan los nodos internos
        # empezando por el último padre y terminando en la raíz.
        for posicion in range((len(self.arreglo) - 1) // 2, 0, -1):
            self._bajar(posicion)

        if imagen:
            self._dibujar()

    def _bajar(self, posicion):
        """Restablece la propiedad de min-heap desde una posición hacia abajo."""
        cantidad = len(self.arreglo) - 1

        while 2 * posicion <= cantidad:
            hijo_izquierdo = 2 * posicion
            hijo_derecho = hijo_izquierdo + 1
            hijo_menor = hijo_izquierdo

            # Se escoge el hijo de menor valor. En caso de empate,
            # se conserva el hijo izquierdo.
            if (hijo_derecho <= cantidad and
                    self.arreglo[hijo_derecho] < self.arreglo[hijo_izquierdo]):
                hijo_menor = hijo_derecho

            if self.arreglo[hijo_menor] < self.arreglo[posicion]:
                self.arreglo[posicion], self.arreglo[hijo_menor] = (
                    self.arreglo[hijo_menor], self.arreglo[posicion]
                )
                posicion = hijo_menor
            else:
                break

    def _dibujar(self):
        """Muestra el estado actual del heap como un árbol binario."""
        import matplotlib.pyplot as plt
        from matplotlib.patches import Circle

        cantidad = len(self.arreglo) - 1
        if cantidad == 0:
            fig, ax = plt.subplots(figsize=(5, 1.8))
            ax.text(0.5, 0.5, "Heap vacío", ha="center", va="center", fontsize=13)
            ax.axis("off")
            plt.show()
            return

        ultimo_nivel = cantidad.bit_length() - 1
        espacio_y = 1.5   # separación vertical entre niveles
        radio = 0.4       # las hojas quedan separadas 1 unidad en x

        ancho = max(4, 0.7 * 2 ** ultimo_nivel)
        alto = max(2.5, (ultimo_nivel + 1) * 1.4)
        fig, ax = plt.subplots(figsize=(ancho, alto))

        # Posición de cada nodo, todo en la misma escala.
        posiciones = {}
        for i in range(1, cantidad + 1):
            nivel = i.bit_length() - 1
            columna = i - 2 ** nivel
            x = (columna + 0.5) * 2 ** (ultimo_nivel - nivel)
            y = -nivel * espacio_y
            posiciones[i] = (x, y)

        # Aristas primero, para que queden detrás de los nodos.
        for i in range(1, cantidad + 1):
            x1, y1 = posiciones[i]
            for hijo in (2 * i, 2 * i + 1):
                if hijo <= cantidad:
                    x2, y2 = posiciones[hijo]
                    ax.plot([x1, x2], [y1, y2], color="black",
                            linewidth=1.5, zorder=1)

        # Nodos con su valor.
        for i in range(1, cantidad + 1):
            x, y = posiciones[i]
            ax.add_patch(Circle((x, y), radius=radio, facecolor="white",
                                edgecolor="black", linewidth=1.5, zorder=2))
            ax.text(x, y, str(self.arreglo[i]), ha="center", va="center",
                    fontsize=10, zorder=3)

        ax.set_xlim(0, 2 ** ultimo_nivel)
        ax.set_ylim(-ultimo_nivel * espacio_y - 0.8, 0.8)
        ax.set_aspect("equal")
        ax.axis("off")
        ax.set_title("Min-heap")
        plt.tight_layout()
        plt.show()
