class AutomataFD:
    def __init__(self, path_csv):
        """Inicialización del autómata determinista desde un archivo CSV"""
        self.path_csv = path_csv
        self.estados, self.alfabeto, self.transiciones, self.estado_inicial, self.estados_aceptacion = self.extraer_datos_csv()
        self.estado_actual = self.estado_inicial
        
        self.mostrar_informacion()

    def extraer_datos_csv(self):
        """Extraer datos del archivo CSV y definir estados, alfabeto, transiciones, estado inicial y de aceptación"""
        import pandas as pd

        df = pd.read_csv(self.path_csv)
        
        # Definir estados y alfabeto
        estados = []
        alfabeto = list(df.columns[1:])  # Obtener el alfabeto desde la segunda columna en adelante
        
        transiciones = {}
        estado_inicial = None
        estados_aceptacion = []

        # Definir transiciones y determinar estado inicial y de aceptación
        for indice, fila in df.iterrows():
            estado = fila[df.columns[0]].strip()  # Obtener el estado

            if estado.startswith('-'):
                estado = estado[1:]  # Quitar el "-" del estado inicial
                estado_inicial = estado

            if estado.startswith('*'):
                estado = estado[1:]  # Quitar el "*" del estado de aceptación
                estados_aceptacion.append(estado)
            
            estados.append(estado)
            transiciones[estado] = {}

            for i, simbolo in enumerate(alfabeto):
                transiciones[estado][simbolo] = fila.iloc[i + 1].strip()  # Almacenar la transición
                
        return estados, alfabeto, transiciones, estado_inicial, estados_aceptacion
    
    def procesar_cadena(self):
        """Pedir la cadena al usuario y procesarla"""
        cadena = input('Ingrese una cadena utilizando el alfabeto {}: '.format(self.alfabeto))
        
        # Recorrer la cadena
        for caracter_actual in cadena:
            print('Procesando el carácter: ', caracter_actual)
            # Validar que los caracteres de la cadena pertenezcan al alfabeto
            if caracter_actual not in self.alfabeto:
                print('La cadena es inválida porque', caracter_actual, 'no pertenece al alfabeto {}'.format(self.alfabeto))
                return False
            
            # Verificar si la transición es válida
            siguiente_estado = self.transiciones[self.estado_actual].get(caracter_actual, "ESTADO_INVALIDO")
            print('Transición a: ', siguiente_estado)

            # Verificar si la transición lleva a un estado indefinido
            if siguiente_estado == "ESTADO_INVALIDO":
                print('La cadena es inválida porque llegamos a un estado indefinido')
                return False
            
            print('Estado actual: {} con {}'.format(self.estado_actual, caracter_actual), 'Transición a ->', siguiente_estado)
            # Actualizar el estado actual
            self.estado_actual = siguiente_estado

        # Verificar si la cadena es aceptada
        if self.estado_actual in self.estados_aceptacion:
            print('La cadena "{}" es válida'.format(cadena))
            return True
        else:
            print('La cadena "{}" no es válida'.format(cadena))
            return False 

    def mostrar_informacion(self):
        """Mostrar información sobre el autómata"""
        print("Estados:", self.estados)
        print("Alfabeto:", self.alfabeto)
        print("Estado inicial:", self.estado_inicial)
        print("Estados de aceptación:", self.estados_aceptacion)
        
        print("\nFunción de transición:")
        print("Estado actual \t Símbolo \t Estado siguiente")
        for estado in self.transiciones:
            for simbolo in self.alfabeto:
                print(f"{estado} \t\t {simbolo} \t\t {self.transiciones[estado][simbolo]}")

    def menu(self):
        """Mostrar el menú de opciones"""
        print('\nOpciones')
        print('1. Cargar nuevo autómata')
        print('2. Verificar cadena con autómata actual')
        print('3. Salir')

if __name__ == "__main__":
    print("Autómata Determinista Finito desde un archivo CSV")
    automata = AutomataFD("automata.csv")

    while True:
        automata.menu()
        opcion = input('Seleccione una opción: ')
        
        if opcion == '1':
            # Solicitar la ruta del nuevo CSV y crear un nuevo autómata
            ruta_csv = input("Ingrese la ruta del archivo CSV para el nuevo autómata: ")
            automata = AutomataFD(ruta_csv)
            
        elif opcion == '2':
            # Verificar la cadena con el autómata actual
            automata.procesar_cadena()
        
        elif opcion == '3':
            print('Saliendo...')
            break
        
        else:
            print(f'{opcion} no es una opción válida')