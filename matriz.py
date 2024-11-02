import numpy as np

class CMatFloat:
    """
    Clase que representa una matriz dinámica 1D/2D.

    Atributos:
        _Matriz       # Almacena la matriz (utilice numpy)
        _m_nFilas     # Almacena el número de filas de la matriz
        _m_nColumnas  # Almacena el número de columnas de la matriz
    """

    def __init__(self):
        """Inicializa la matriz como None y filas y columnas a 0."""
        self._Matriz = None
        self._m_nFilas = 0
        self._m_nColumnas = 0

    def CrearMatriz2D(self, nFilas, nColumnas):
        """Crea una matriz bidimensional de ceros."""
        self._Matriz = np.zeros((nFilas, nColumnas))
        self._m_nFilas = nFilas
        self._m_nColumnas = nColumnas

    def CrearMatriz1D(self, nElementos):
        """Crea una matriz unidimensional de ceros."""
        self.CrearMatriz2D(1, nElementos)

    def Introducir(self):
        """Introduce los elementos de la matriz."""
        if self.Existe():
            for i in range(self._m_nFilas):
                for j in range(self._m_nColumnas):
                    self._Matriz[i, j] = float(input(f"Ingrese el elemento ({i},{j}): "))

    def Mostrar(self):
        """Muestra los elementos de la matriz."""
        if self.Existe():
            print(self._Matriz)

    def Existe(self):
        """Verifica si la matriz está creada y no está vacía."""
        return self._Matriz is not None and self._Matriz.size > 0

    def SumarMatrices(self, otra_matriz):
        """Suma la matriz actual con otra matriz."""
        if self.Existe() and otra_matriz.Existe():
            if self._Matriz.shape == otra_matriz._Matriz.shape:
                return self._Matriz + otra_matriz._Matriz
            else:
                raise ValueError("Las dimensiones de las matrices deben coincidir.")
        else:
            raise ValueError("Una de las matrices no existe.")

    def RestarMatrices(self, otra_matriz):
        """Resta la matriz actual con otra matriz."""
        if self.Existe() and otra_matriz.Existe():
            if self._Matriz.shape == otra_matriz._Matriz.shape:
                return self._Matriz - otra_matriz._Matriz
            else:
                raise ValueError("Las dimensiones de las matrices deben coincidir.")
        else:
            raise ValueError("Una de las matrices no existe.")

def leer_int(mensaje="Introduce un número entero: "):
    """Lee un número entero del teclado."""
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Entrada no válida. Inténtalo de nuevo.")

def leer_float(mensaje="Introduce un número decimal: "):
    """Solicita al usuario un número decimal."""
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Entrada no válida. Inténtalo de nuevo.")

def crear_menu(opciones_menu):
    """Muestra un menú de opciones y solicita al usuario una opción válida."""
    for i, opcion in enumerate(opciones_menu, start=1):
        print(f"{i}. {opcion}")
    return leer_int("Seleccione una opción: ")

def main():
    matrices = {}
    while True:
        opcion = crear_menu([
            "Construir matriz 1D",
            "Construir matriz 2D",
            "Introducir matriz",
            "Mostrar matriz",
            "Operaciones con matrices",
            "Terminar"
        ])
        
        if opcion == 1:
            nElementos = leer_int("Introduce el número de elementos para la matriz 1D: ")
            matriz = CMatFloat()
            matriz.CrearMatriz1D(nElementos)
            matrices['matriz1D'] = matriz
        
        elif opcion == 2:
            nFilas = leer_int("Introduce el número de filas para la matriz 2D: ")
            nColumnas = leer_int("Introduce el número de columnas para la matriz 2D: ")
            matriz = CMatFloat()
            matriz.CrearMatriz2D(nFilas, nColumnas)
            matrices['matriz2D'] = matriz
        
        elif opcion == 3:
            nombre = input("¿Qué matriz quieres introducir (matriz1D/matriz2D)? ")
            if nombre in matrices:
                matrices[nombre].Introducir()
            else:
                print("Matriz no encontrada.")

        elif opcion == 4:
            nombre = input("¿Qué matriz quieres mostrar (matriz1D/matriz2D)? ")
            if nombre in matrices:
                matrices[nombre].Mostrar()
            else:
                print("Matriz no encontrada.")

        elif opcion == 5:
            nombre1 = input("Seleccione la primera matriz (matriz1D/matriz2D): ")
            matriz_aux = CMatFloat()
            if nombre1 in matrices:
                matriz_aux = CMatFloat()
                if nombre1 == 'matriz1D':
                    matriz_aux.CrearMatriz1D(nElementos)
                    print("Introduzca los elementos de la matriz auxiliar 1D de ", nElementos, " elementos")
                    matriz_aux.Introducir()

                elif nombre1 == 'matriz2D':

                    matriz_aux.CrearMatriz2D(nFilas, nColumnas)
                    print("Introduzca los elementos de la matriz auxiliar de dimensiones: ", nFilas, "x", nColumnas,"\n")
                    matriz_aux.Introducir()

                sub_opcion = crear_menu(["Sumar matrices", "Restar matrices", "Volver"])

                if sub_opcion == 1:
                    resultado = matrices[nombre1].SumarMatrices(matriz_aux)
                    print("Resultado de la suma:")
                    print(resultado)
                elif sub_opcion == 2:
                    resultado = matrices[nombre1].RestarMatrices(matriz_aux)
                    print("Resultado de la resta:")
                    print(resultado)
            else:
                print("Matriz no encontrada.")
        
        elif opcion == 6:
            print("Fin del programa.")
            break

if __name__ == "__main__":
    main()
