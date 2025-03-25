from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name, age):
        if not name or not isinstance(name, str):
            raise ValueError("Nama hewan harus berupa string dan tidak boleh kosong.")
        if not isinstance(age, int) or age <= 0:
            raise ValueError("Usia harus berupa angka positif.")
        
        self.__name = name
        self.__age = age
    
    @abstractmethod
    def make_sound(self):
        pass
    
    def get_name(self):
        return self.__name
    
    def get_age(self):
        return self.__age

class Dog(Animal):
    def make_sound(self):
        return "Whoop! Whoop!"

class Cat(Animal):
    def make_sound(self):
        return "rawr!"

class Bird(Animal):
    def make_sound(self):
        return "Knik! Knik!"

if __name__ == "__main__":
    dog = Dog("Buddy", 3)
    cat = Cat("Whiskers", 2)
    bird = Bird("Tweety", 1)

    print("Daftar Hewan:")
    print(f"{dog.get_name()} ({dog.__class__.__name__}), Usia: {dog.get_age()}, Suara: {dog.make_sound()}")
    print(f"{cat.get_name()} ({cat.__class__.__name__}), Usia: {cat.get_age()}, Suara: {cat.make_sound()}")
    print(f"{bird.get_name()} ({bird.__class__.__name__}), Usia: {bird.get_age()}, Suara: {bird.make_sound()}")