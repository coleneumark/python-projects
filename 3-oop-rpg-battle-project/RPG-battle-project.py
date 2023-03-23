import random

# Exercise One - The Creature, The Fighter, and the Archer
# Task 1

class Creature:
    
    def __init__(self, name, maxhp = 10):
        self.name = name
        self.hp = maxhp
        self.maxhp = maxhp
        self.abilities = {"Attack": 1, "Defense": 5, "Speed": 10}
    
    def __str__(self):
        s = f"{self.name} currently has {self.hp} HP, with a Max HP of {self.maxhp}.\n"
        s += f"{self.name} has an Attack of {self.abilities['Attack']}, a Defense of {self.abilities['Defense']}, and a Speed of {self.abilities['Speed']}."
        return s
    
    def check_life(self):         
        if self.hp > self.maxhp:
            self.hp = self.maxhp
        elif self.hp <= 0:
            self.hp = 0
            print(f"{self.name} fainted...")
        return self.hp
        
    def attack(self, target):
        roll = random.randint(1,20)
        if roll > (int(target.abilities["Defense"]) + int(target.abilities["Speed"])):
            damage = int(self.abilities["Attack"]) + random.randint(1,4)
            target.hp -= damage
            print(f"Attack hits for {damage} damage!")
        else:
            print("Attack missed...")            
        
    def turn(self, target, round_num):
        print(f"{self.name} attacks {target.name}.")
        self.attack(target)
        if target.check_life() == 0:
            return False
        else:
            return True
    
#gollum1 = Creature("Gollum")
#bilbo = Creature("Bilbo")
# Check for correct parameters
#print(gollum1)
#print(bilbo)
#print()

# Script for Fight
#for i in range(1,20):
#    print("Round " + str(i) + ":")
#    if gollum1.turn(bilbo, i) == False:
#        break
#    else:
#        if bilbo.turn(gollum1, i) == False:
#            break

########################################################################

# Task 2
class Fighter(Creature):
    
    def __init__(self, name, maxhp=50):
        super().__init__(name, maxhp)
        self.abilities = {"Attack": 5, "Defense": 10, "Speed": 3}
        self.shield = False
    
    def shield_up(self):
        if not self.shield:
            self.abilities["Attack"] -= 5
            self.abilities["Defense"] += 5
            print(f"{self.name} takes a defensive stance.")
            self.shield = True
    
    def shield_down(self):
        if self.shield:
            self.abilities["Attack"] += 5
            self.abilities["Defense"] -= 5
            print(f"{self.name}'s stance returns to normal.")
            self.shield = False
    
    def turn(self, target, round_num):
        if round_num > 4:
            round_num %= 4
        if round_num == 1: 
            print(f"{self.name} attacks {target.name}.")
            self.attack(target)
            self.shield_up()
        elif round_num in [2, 3]:
            print(f"{self.name} attacks {target.name}.")
            self.attack(target)
        else:
            self.shield_down()
            print(f"{self.name} attacks {target.name}.")
            self.attack(target)
        if target.check_life() != 0:        
            return True
        else:
            return False

# Check the fighter class
#print()
#aragon1 = Fighter("Aragon")
#gollum2 = Creature("Gollum")
#print(aragon1)
#print(gollum2)
#print()

# Script for Fight
#for i in range(1,21):
#    print("Round " + str(i) + ":")
#    if gollum2.turn(aragon1, i) == False:
#        break
#    else:
#        if aragon1.turn(gollum2, i) == False:
#            break

#######################################################################
# Task 3
class Archer(Creature):
    
    def __init__(self, name, maxhp = 30):
        super().__init__(name, maxhp)
        self.abilities = {"Attack": 7, "Defense": 8, "Speed": 8}
        self.sneak = False
    
    def sneak_attack(self, target):
        roll1 = random.randint(1,20)
        roll2 = random.randint(1,20)
        roll = max(roll1, roll2)
        if int(self.abilities["Speed"]) > int(target.abilities["Speed"]):
            extra = int(self.abilities["Speed"]) - int(target.abilities["Speed"])
            self.abilities["Speed"] += extra
        if not self.sneak:
            self.abilities["Attack"] += 3
            self.abilities["Defense"] -= 3
            print(f"{self.name}'s attack rose.")
            print(f"{self.name}'s defense reduced.")
            self.sneak = True
        if roll > (int(target.abilities["Defense"]) + int(target.abilities["Speed"])):
            damage = int(self.abilities["Attack"]) + random.randint(1,8)
            target.hp -= damage
            print(f"Attack hits for {damage} damage!")
        else:
            print("Attack missed...")

    def attack(self, target):
        roll = random.randint(1,20)
        if self.sneak:
            self.abilities["Attack"] -= 3
            self.abilities["Defense"] += 3
            print(f"{self.name}'s attack reduced.")
            print(f"{self.name}'s defense rose.")
            self.sneak = False
        if roll > (target.abilities["Defense"] + target.abilities["Speed"]):
            damage = self.abilities["Attack"] + random.randint(1,4)
            target.hp -= damage
            print(f"Attack hits for {damage} damage!")
        else:
            print("Attack missed...")

    def turn(self, target, round_num):
        round_num %= 4
        if round_num == 1: 
            print(f"{self.name} attacks {target.name}.")
            self.attack(target)
        else: 
            print(f"{self.name} sneak attacks {target.name}...")
            self.sneak_attack(target)
        return target.check_life() != 0

# Check the archer class
#print()
#aragon2 = Fighter("Aragon")
#legolas = Archer("Legolas")
#print(aragon2)
#print(legolas)
#print()

# Script for Fight
#for i in range(1,21):
#    print("Round " + str(i) + ":")
#    if legolas.turn(aragon2, i) == False:
#        break
#    else:
#        if aragon2.turn(legolas, i) == False:
#            break

#######################################################################
# Exercise 2 - Enemies' Classes
# Task 1
class Goblin(Creature):

    def __init__(self, name, maxhp = 15):
        super().__init__(name, maxhp)
        self.abilities = {"Attack": 4, "Defense": 6, "Speed": 6}


class Orc(Creature):

    def __init__(self, name, maxhp = 50):
        super().__init__(name, maxhp)
        self.abilities = {"Attack": 10, "Defense": 6, "Speed": 2}
        self.rage = False

    def heavy_attack(self, target):
        roll = random.randint(1,20)
        if not self.rage:
            self.abilities["Attack"] += 5
            self.abilities["Defense"] -= 3
            print(f"{self.name} is in rage.")
            self.rage = True
        if roll > (int(target.abilities["Defense"]) + int(target.abilities["Speed"])):
            damage = self.abilities["Attack"] + random.randint(1, 4)
            target.hp -= damage
            print(f"Attack hits for {damage} damage!")
        else:
            print("Attack missed...")

    def attack(self, target):
        roll = random.randint(1,20)
        if self.rage:
            self.abilities["Attack"] -= 5
            self.abilities["Defense"] += 3
            print(f"{self.name} has cooled down.")
            self.rage = False
        if roll > (target.abilities["Defense"] + target.abilities["Speed"]):
            damage = self.abilities["Attack"] + random.randint(1,4)
            target.hp -= damage
            print(f"Attack hits for {damage} damage!")
        else:
            print("Attack missed...")
    
    def turn(self, target, round_num):
        round_num %= 4
        if round_num in [1, 2, 3]: 
            print(f"{self.name} attacks {target.name}.")
            self.attack(target)
        else: 
            print(f"{self.name} attacks {target.name}.")
            self.heavy_attack(target)
        return target.check_life() != 0

# Check the fighter class
#print()
#goblin = Goblin("Goblin")
#orc = Orc("Orc")
#print(goblin)
#print(orc)
#print()

# Script for Fight
#for i in range(1,21):
#    print("Round " + str(i) + ":")
#    if goblin.turn(orc, i) == False:
#        break
#    else:
#        if orc.turn(goblin, i) == False:
#            break

########################################################################
# Task 2
class OrcGeneral(Fighter, Orc):

    def __init__(self, name, maxhp = 100):
        Fighter.__init__(self, name, maxhp)
        Orc.__init__(self, name, maxhp)         # order for abilities!

    def turn(self, target, round_num):
        round_num %= 4
        if round_num == 1: 
            print(f"{self.name} attacks {target.name}.")
            self.attack(target)
            self.shield_up()
        elif round_num == 2:
            print(f"{self.name} attacks {target.name}.")
            self.attack(target)
        elif round_num == 3:
            self.shield_down()
            print(f"{self.name} attacks {target.name}.")
            self.attack(target)
        else: 
            print(f"{self.name} attacks {target.name}.")
            self.heavy_attack(target)
        return target.check_life() != 0

#########################################################################
# Task 3

class GoblinKing(Archer, Goblin):

    def __init__(self, name, maxhp = 50):
        Archer.__init__(self, name, maxhp)
        Goblin.__init__(self, name, maxhp)      # order for abilities!


# Check Orc General and Goblin King classes
#print()
#goblinKing = GoblinKing("King Gob")
#orcGeneral = OrcGeneral("General Orc")
#print(goblinKing)
#print(orcGeneral)
#print()

# Script for Fight
#for i in range(1,21):
#    print("Round " + str(i) + ":")
#    if goblinKing.turn(orcGeneral, i) == False:
#        break
#    else:
#        if orcGeneral.turn(goblinKing, i) == False:
#            break

########################################################################
# Exercise Three - The Wizard
# Task 1 and 2

class Wizard:

    def __init__(self, name, maxhp = 100, mana = 100):
        self.name = name
        self.hp = maxhp
        self.maxhp = maxhp
        self.abilities = {"Attack": 3, "Defense": 5, "Speed": 5, "Arcana": 10}
        self.mana = mana
        self.maxmana = mana

    def getMana(self, manaPoints = 0):
        self.mana += manaPoints
        if self.mana <= 0:
            self.mana = 0
            print("Mana is empty.")
        elif self.mana > self.maxmana:
            self.mana = self.maxmana
            print("Mana is full.")
    
    def printMana(self):    
        if self.mana == 0:
            return False
        elif self.mana == self.maxmana:
            return True
        else:
            return None
    
    def __str__(self):
        s = f"{self.name} currently has {self.hp} HP, with a Max HP of {self.maxhp}, and Mana of {self.mana}.\n"
        s += f"{self.name} has an Attack of {self.abilities['Attack']}, a Defense of {self.abilities['Defense']}, and an Arcana of {self.abilities['Arcana']}."
        return s

    def attack(self, target):
        if not self.printMana():
            print("Mana: +20!")
        self.getMana(20)
        print(f"{self.name} attacks {target.name}.")
        roll = random.randint(1,20)
        if roll > (target.abilities["Defense"] + target.abilities["Speed"]):
            damage = self.abilities["Attack"] + random.randint(1,4)
            target.hp -= damage
            print(f"Attack hits for {damage} damage!")
        else:
            print("Attack missed...")  

    def recharge(self):
        print(f"{self.name} channels magical energy...")
        if not self.printMana():
            print("Mana: +30!")
        self.getMana(30)

    def fire_bolt(self, target):
        roll = random.randint(1,20) + (self.abilities["Arcana"] // 2)
        if roll > (target.abilities["Defense"] + target.abilities["Speed"]):
            damage = int(self.abilities["Attack"]) + random.randint(1,self.abilities["Arcana"])
            target.hp -= damage
            print(f"{self.name} fires a fire bolt at {target.name}...")
            print(f"Fire bolt hits for {damage} fire damage!")
            self.getMana(10)
            if not self.printMana():
                print("Mana: +10!")
        else:
            print("Attack missed...")

    def check_life(self):         # same as in Creature class
        if self.hp > self.maxhp:
            self.hp = self.maxhp
        elif self.hp <= 0:
            self.hp = 0
            print(f"{self.name} fainted...")
        return self.hp

    def heal(self, target):
        if self.mana >=20:
            if self.printMana() in (True, None):
                print("Mana: -20!")
            self.getMana(-20)
            healNum = random.randint(0,8) + (self.abilities["Arcana"] // 2)
            if target.hp != target.maxhp and target.hp != 0:
                target.hp = target.hp + healNum
                target.check_life()
                print(f"{self.name} heals {target.name} for {healNum} HP!")
            elif target.hp == 0:
                print(f"{self.name} cannot resurrect {target.name}.")
            else:
                print(f"{target.name} is at full health.")
        else:
            print(f"{self.name} does not have enough Mana.")

    def mass_heal(self, allies):    # provide allies in list of objects
        if self.mana >=30:
            if self.printMana() in (True, None):
                print("Mana: -30!")
            self.getMana(-30)
            for ally in allies:
                healNum = random.randint(0,8) + (self.abilities["Arcana"] // 2)
                if ally.hp != ally.maxhp and ally.hp != 0:
                    ally.hp += healNum
                    ally.check_life()
                    print(f"{self.name} heals {ally.name} for {healNum} HP!")
                elif ally.hp == 0:
                    print(f"{self.name} cannot resurrect {ally.name}.")
                else:
                    print(f"{ally.name} is at full health.")
            if self.hp != self.maxhp:
                self.hp += healNum
                self.check_life()
                print(f"{self.name} heals {self.name} for {healNum} HP!")
            else:
                    print(f"{ally.name} is at full health.")
        else:
            print(f"{self.name} does not have enough Mana.")

    def fire_storm(self, enemies):  # provide enemies in list of objects
        if self.mana >=50:
            if not self.printMana():
                print("Mana: -50!")
            self.getMana(-50)
            for enemy in enemies:
                roll = random.randint(1,20) + self.abilities["Speed"]
                damage = random.randint(5,20) + self.abilities["Arcana"]
                if roll >= self.abilities["Arcana"]:
                    damage = damage // 2
                    enemy.hp -= damage 
                    print(f"Fire Storm deals {damage} fire damage to {enemy.name}!")
                else:
                    enemy.hp -= damage 
                    print(f"Fire Storm deals {damage} fire damage to {enemy.name}!")
        else:
            print(f"{self.name} does not have enough Mana.")

# Script for Fight (manual calls and checks cuz no turn method)
#print()
#gandalf = Wizard("Gandalf")
#goblinKing2 = GoblinKing("Goblin King")
#orcGeneral2 = OrcGeneral("Gothmog")
#aragon3 = Fighter("Aragon")
#legolas2 = Archer("Legolas")
#allies = [aragon3, legolas2, gandalf]
#enemies = [goblinKing2, orcGeneral2]
#print(gandalf)
#print()
#print("Using attack:")
#gandalf.mana = 50
#gandalf.attack(goblinKing2)
#print("Goblin King's HP is now: " + str(goblinKing2.hp))
#print()
#print("Using recharge:")
#gandalf.recharge()
#print()
#print("Using firebolt:")
#gandalf.fire_bolt(orcGeneral2)
#print("Gothmog's HP is now: " + str(orcGeneral2.hp))
#print()
#print("Using heal:")
#aragon3.hp = 30
#gandalf.heal(aragon3)
#print("Aragon's HP is now: " + str(aragon3.hp))
#print()
#print("Using mass heal:")
#gandalf.mass_heal(allies)
#print("Aragon's HP is now: " + str(aragon3.hp))
#print("Legolas's HP is now: " + str(legolas2.hp))
#print()
#print("Using fire storm:")
#gandalf.fire_storm(enemies)
#print("Goblin King's HP is now: " + str(goblinKing2.hp))
#print("Gothmog's HP is now: " + str(orcGeneral2.hp))


######################################################################
# Exercise Four - Battle in the Middle Earth

class Battle:

    # Task 1
    def __init__(self):
        question = input("Name characters yourself? (y/n) \n\n")
        if question == "y" or question == "Y":
            # Creating enemies
            self.orcgen = OrcGeneral(input("Enter the Orc General's name: "))
            self.orc1 = Orc(input("Enter the first Orc's name: "))
            self.orc2 = Orc(input("Enter the second Orc's name: "))
            self.gobkin = GoblinKing(input("Enter the Goblin King's name: "))
            self.goblin1 = Goblin(input("Enter the first Goblin's name: "))
            self.goblin2 = Goblin(input("Enter the second Goblin's name: "))
            # Creating allies
            self.archer = Archer(input("Enter the Archer's name: "))
            self.fighter = Fighter(input("Enter the Fighter's name: "))
            # Creating player's character
            self.wizard = Wizard(input("Enter your Wizard's name: "))
        else:
            # Creating enemies
            self.orcgen = OrcGeneral("Gothmog")
            self.orc1 = Orc("Grunt")
            self.orc2 = Orc("Punch")
            self.gobkin = GoblinKing("King Shriek")
            self.goblin1 = Goblin("Fang")
            self.goblin2 = Goblin("Rust")
            # Creating allies
            self.archer = Archer("Legolas")
            self.fighter = Fighter("Aragorn")
            # Creating player's character
            self.wizard = Wizard("Gandalf")
        self.enemies = [self.orcgen, self.orc1, self.orc2, self.gobkin, self.goblin1, self.goblin2]   
        self.allies = [self.archer, self.fighter]
        self.alliesWizard = [self.archer, self.fighter, self.wizard]
        
    def __str__(self):
        s = f"\n\nA BATTLE in MIDDLE EARTH is fast approaching!\n"
        s += f"You are the legendary WIZARD {self.wizard.name}. "
        s += f"The ARCHER {self.archer.name} and the FIGHTER {self.fighter.name} are your ALLIES.\n"
        s += f"You must defeat the  ORC GENERAL {self.orcgen.name} and his ORCS, {self.orc1.name} and {self.orc2.name},"
        s += f" as well as the GOBLIN KING {self.gobkin.name} and his GOBLINS, {self.goblin1.name} and {self.goblin2.name}.\n"
        s += f"DEFEAT the ENEMIES, and SAVE MIDDLE EARTH!\n"
        return s

    # Task 2
    def auto_select(self, target_list):
        if len(target_list) != 0:                           
            return target_list[random.randint(0,len(target_list)-1)]
        else:
            return None

    def select_target(self, target_list):
        print("Select target:")
        for i, target in enumerate(target_list):
            print(f"{i+1}: {target.name}, HP: {target.hp}/{target.maxhp}")
        num = input("Enter choice: ")
        while not num.isdigit() or int(num) > len(target_list):
            num = input("Enter choice: ")
        return target_list[int(num)-1]

    # Task 3
    def turn_order(self):
        self.turn_list = []
        self.turn_list.extend(self.enemies)
        self.turn_list.extend(self.alliesWizard)
        self.turn_list.sort(key=lambda x:x.abilities["Speed"], reverse=True)
        return self.turn_list

    def checkDefeated(self, list):
        for creature in list:
            if creature.check_life() == 0:
                return True

    # Task 4
    def player_turn(self):
        print(f"Player: {self.wizard.name} HP: {self.wizard.hp}/{self.wizard.maxhp} Mana: {self.wizard.mana}/{self.wizard.maxmana}")
        print("Allies:", end="")
        for ally in self.allies:
            print(f" {ally.name} HP: {ally.hp}/{ally.maxhp}", end="")
        print("\n============================================")
        print("Actions. F: Attack  R: Recharge Mana")
        print("Spells. 1: Heal  2: Firebolt  3: Mass Heal  4: Fire Storm")
        print("To Quit game type: Quit")
        selection = input("Enter action: ")
        print("============================================")
        while selection not in "FfRr1234quitQuit":
            selection = input("Enter action: ")
        else:
            if selection == "F" or selection == "f":
                attack_target = self.select_target(self.enemies)
                self.wizard.attack(attack_target)
                if attack_target.check_life() == 0:
                    self.enemies.remove(attack_target)
                    return [attack_target]
                else:
                    return []
            elif selection == "R" or selection == "r":
                self.wizard.recharge()
                return []
            elif selection == "1":
                heal_ally = self.select_target(self.alliesWizard)
                self.wizard.heal(heal_ally)
                return []
            elif selection == "2":
                fire_target = self.select_target(self.enemies)
                self.wizard.fire_bolt(fire_target)
                if fire_target.check_life() == 0:
                    self.enemies.remove(fire_target)
                    return [fire_target]
                else:
                    return []
            elif selection == "3":
                self.wizard.mass_heal(self.allies)
                return []
            elif selection == "4":
                self.wizard.fire_storm(self.enemies)
                list = []
                for enemy in self.enemies:
                    if enemy.check_life() == 0:
                        self.enemies.remove(enemy)
                        list.append(enemy)
                return [list]
            elif selection == "quit" or selection == "Quit":
                print("YOU QUIT THE BATTLE. Will MIDDLE EARTH be doomed?")
                print("============================================")
        print("============================================")
                

    def start(self):
        print(f"{self}\n============================================")
        print("THE BATTLE BEGINS")
        print("============================================")
        turn_order = self.turn_order()
        round_count = 1                                               
        while len(self.enemies) != 0 and len(self.allies) != 0 and self.wizard.hp > 0:
            print(f"Round {round_count}.")
            print("============================================")
            for creature in turn_order:
                if creature in self.enemies:
                    ally1 = self.auto_select(self.alliesWizard)
                    if ally1 is not None:
                        print("============================================")
                        if creature.turn(ally1, round_count) is False:
                            self.alliesWizard.remove(ally1)
                            turn_order.remove(ally1)
                            if self.wizard not in self.alliesWizard:
                                break
                    else:
                        break
                elif creature in self.allies:
                    enemy1 = self.auto_select(self.enemies)
                    if enemy1 is not None:
                        if creature.turn(enemy1, round_count) is False:
                            self.enemies.remove(enemy1)
                            turn_order.remove(enemy1)
                    else:
                        break
                elif creature == self.wizard:
                    print("============================================")
                    defeated_enemies = self.player_turn()
                    print("============================================")
                    if defeated_enemies != "":
                        for enemy in defeated_enemies:
                            if enemy in turn_order:
                                turn_order.remove(enemy)
                    if self.checkDefeated(self.enemies):
                        break
            print("============================================")
            print(f"End of round {round_count}.")
            print("============================================")
            round_count += 1
        if self.checkDefeated(self.enemies):
            print("The HEROES won the battle! MIDDLE EARTH is saved!")
            print("============================================")
        elif self.checkDefeated(self.allies):
            print("The HEROES lost the battle! MIDDLE EARTH is doomed...")
        print("============================================")
        print("THE BATTLE ENDS")

    

# Battle script
battle = Battle()
battle.start()