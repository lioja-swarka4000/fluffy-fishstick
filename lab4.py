class Benzopila:
    def __init__(self, nazva="ніхто", potuzhnist=1500, oberty=10000):
        self.__nazva = nazva
        self.__potuzhnist = potuzhnist
        self.__oberty = oberty
        self.vaga = 0.0      
        self.kolir = ""      

    def get_nazva(self):
        return self.__nazva

    def get_potuzhnist(self):
        return self.__potuzhnist

    def get_oberty(self):
        return self.__oberty

    def __str__(self):
        return f"{self.__nazva}, {self.__potuzhnist} Вт, {self.__oberty} об/хв, вага {self.vaga}, колір {self.kolir}"

    def __repr__(self):
        return f"Benzopila('{self.__nazva}', {self.__potuzhnist}, {self.__oberty})"

    def __del__(self):
        print("Зламали бензопилу:", self.__nazva)

def main():
    pila1 = Benzopila()
    pila1.vaga = 5.2
    pila1.kolir = "червоний"

    pila2 = Benzopila("Stihl MS 180", 1500, 12000)
    pila2.vaga = 4.1
    pila2.kolir = "помаранчевий"

    pila3 = Benzopila("Husqvarna 135", 1600, 11500)
    pila3.vaga = 4.5
    pila3.kolir = "зелений"

    for pila in (pila1, pila2, pila3):
        print("Назва:", pila.get_nazva())
        print("Потужність:", pila.get_potuzhnist())
        print("Оберти:", pila.get_oberty())
        print("Вага:", pila.vaga)
        print("Колір:", pila.kolir)
        print(pila)
        print(repr(pila))
        print()

if __name__ == "__main__":
    main()