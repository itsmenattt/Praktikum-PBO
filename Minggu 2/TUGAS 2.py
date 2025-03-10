import random

class Robot:
    def __init__(self, name, hp, attack, accuracy):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.ulti_damage = 100
        self.accuracy = accuracy  # Tambahkan accuracy sebagai atribut
        self.action_count = 0
        self.is_defending = False

    def attack_enemy(self, enemy, action_type):
        if random.randint(1, 100) > self.accuracy:  # Cek apakah serangan meleset
            print(f"{self.name} mencoba menyerang {enemy.name}, tapi serangannya meleset!")
            return  # Serangan gagal jika lebih besar dari accuracy
        
        damage = 0
        if action_type == "attack":
            damage = self.attack
        elif action_type == "ulti":
            if self.action_count >= 5:
                damage = self.ulti_damage
                self.action_count = 0
            else:
                print(f"{self.name} tidak bisa menggunakan ulti, belum cukup aksi.")
                return
        
        print(f"{self.name} menyerang {enemy.name} dengan {damage} kerusakan.")
        
        if enemy.is_defending:
            damage = damage // 2
            print(f"{enemy.name} menahan serangan dan hanya menerima {damage} kerusakan!")
        else:
            print(f"{enemy.name} menerima {damage} kerusakan!")
        
        enemy.hp -= damage

class Game:
    def __init__(self, robot1, robot2):
        self.robot1 = robot1
        self.robot2 = robot2
        self.round = 1

    def display_status(self):
        print(f"\nRound-{self.round} ==========================================================")
        print(f"{self.robot1.name} [HP: {self.robot1.hp} | ATK: {self.robot1.attack} | ACC: {self.robot1.accuracy}%]")
        print(f"{self.robot2.name} [HP: {self.robot2.hp} | ATK: {self.robot2.attack} | ACC: {self.robot2.accuracy}%]")

    def start_game(self):
        print("\nPertarungan Robot dimulai!")
        print("==========================")
        
        while self.robot1.hp > 0 and self.robot2.hp > 0:
            self.display_status()
            
            try:
                action1 = int(input(f"{self.robot1.name}, pilih aksi (1. Attack, 2. Defense, 3. GiveUp, 4. Ultimate): "))
                if action1 == 3:
                    print(f"\n{self.robot1.name} menyerah!")
                    print(f"{self.robot2.name} memenangkan pertarungan!")
                    break
                
                action2 = int(input(f"{self.robot2.name}, pilih aksi (1. Attack, 2. Defense, 3. GiveUp, 4. Ultimate): "))
                if action2 == 3:
                    print(f"\n{self.robot2.name} menyerah!")
                    print(f"{self.robot1.name} memenangkan pertarungan!")
                    break
            except ValueError:
                print("Input harus berupa angka 1-4.")
                continue
            
            if action1 == 2:
                self.robot1.is_defending = True
                print(f"{self.robot1.name} bersiap menahan serangan!")
            if action2 == 2:
                self.robot2.is_defending = True
                print(f"{self.robot2.name} bersiap menahan serangan!")

            print("\nHasil aksi:")
            if action1 != 2:
                self.robot1.action_count += 1
                if action1 == 1:
                    self.robot1.attack_enemy(self.robot2, "attack")
                elif action1 == 4:
                    self.robot1.attack_enemy(self.robot2, "ulti")

            if action2 != 2:
                self.robot2.action_count += 1
                if action2 == 1:
                    self.robot2.attack_enemy(self.robot1, "attack")
                elif action2 == 4:
                    self.robot2.attack_enemy(self.robot1, "ulti")

            self.robot1.is_defending = False
            self.robot2.is_defending = False

            if self.robot1.hp <= 0:
                print(f"\n{self.robot2.name} memenangkan pertarungan!")
                break
            elif self.robot2.hp <= 0:
                print(f"\n{self.robot1.name} memenangkan pertarungan!")
                break

            self.round += 1

robot1 = Robot("Ochobot", 500, 50, 80)  # 80% akurasi
robot2 = Robot("Optimus", 750, 40, 90)  # 90% akurasi
game = Game(robot1, robot2)
game.start_game()
