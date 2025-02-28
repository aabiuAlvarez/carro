class Coche:
    def __init__(self, marca, modelo):
        self.__marca = marca  
        self.__modelo = modelo  
        self.__combustible = 100  

    def conducir(self, km):
        
        combustible_consumido = km / 10
        
        
        if combustible_consumido > self.__combustible:
            print(f"\n{self.__marca} {self.__modelo}: No hay suficiente combustible para recorrer {km} km.")
            print(f"Solo puedes recorrer {self.__combustible * 10} km con el combustible actual.")
            self.__combustible = 0  
        else:
            self.__combustible -= combustible_consumido
            print(f"\n{self.__marca} {self.__modelo}: Has recorrido {km} km. Combustible restante: {self.__combustible:.2f} litros.")

    def repostar(self, litros):
        
        if self.__combustible + litros > 100:
            self.__combustible = 100
            print(f"\n{self.__marca} {self.__modelo}: El depósito está lleno (100 litros).")
        else:
            self.__combustible += litros
            print(f"\n{self.__marca} {self.__modelo}: Has repostado {litros} litros. Combustible actual: {self.__combustible:.2f} litros.")

    def estado(self):
        
        print(f"\n{self.__marca} {self.__modelo}: Combustible restante: {self.__combustible:.2f} litros.")

    
    def get_marca(self):
        return self.__marca

    def get_modelo(self):
        return self.__modelo

    def get_combustible(self):
        return self.__combustible

    
    def set_marca(self, marca):
        self.__marca = marca

    def set_modelo(self, modelo):
        self.__modelo = modelo

    def set_combustible(self, combustible):
        if 0 <= combustible <= 100:
            self.__combustible = combustible
        else:
            print("Error: El combustible debe estar entre 0 y 100 litros.")



def mostrar_menu():
    print("\n--- Menú del Coche ---")
    print("1. Conducir")
    print("2. Repostar combustible")
    print("3. Ver estado del coche")
    print("4. Salir")



def main():
    
    marca = input("Ingresa la marca del coche: ")
    modelo = input("Ingresa el modelo del coche: ")
    mi_coche = Coche(marca, modelo)

    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción (1-4): ")

        if opcion == '1':
            km = float(input("Ingresa los kilómetros a conducir: "))
            mi_coche.conducir(km)
        elif opcion == '2':
            litros = float(input("Ingresa los litros a repostar: "))
            mi_coche.repostar(litros)
        elif opcion == '3':
            mi_coche.estado()
        elif opcion == '4':
            print(f"\nGracias por usar el coche {mi_coche.get_marca()} {mi_coche.get_modelo()}.")
            break
        else:
            print("\nOpción no válida. Por favor, selecciona una opción del 1 al 4.")



if __name__ == "__main__":
    main()