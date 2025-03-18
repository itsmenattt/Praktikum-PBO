class Calculator:
    def __init__(self, angka):
        self.angka = angka
    
    def __add__(self, other):
        return Calculator(self.angka + other.angka)
    
    def __sub__(self, other):
        return Calculator(self.angka - other.angka)
    
    def __mul__(self, other):
        return Calculator(self.angka * other.angka)
    
    def __truediv__(self, other):
        if other.angka == 0:
            raise ValueError("Tidak bisa membagi dengan nol!")
        return Calculator(self.angka / other.angka)
    
    def __pow__(self, other):
        return Calculator(self.angka ** other.angka)
    
    def log(self, other):
        from math import log
        return Calculator(log(other.angka, self.angka))
    
    def __str__(self):
        return str(self.angka)

if __name__ == "__main__":
    a = Calculator(16)
    b = Calculator(2)
    
    print(f"a + b = {a + b}")
    print(f"a - b = {a - b}")  
    print(f"a * b = {a * b}") 
    print(f"a / b = {a / b}")  
    print(f"a ^ b = {a ** b}") 
    print(f"log b(a) = {b.log(a)}") 
