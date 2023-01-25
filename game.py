import random

life_icon, medkit_icon, money_icon = '\u2665', '[+] ', '$'

class Player:
    def __init__(self):
        self.life = 3
        self.money = 3
        self.medkits = 2
        self.score = 0

    def ennemy_killed(self):
        self.money += 1
        self.score += 1
        print('the ennemy has missed. You have killed him!')

    def received_medkit(self):
        self.money -= 1
        self.medkits += 1
        print('you have received one medkit. -1 money warning')

    def hurt(self):
        self.life -= 1
        print("ouch, you are hurt!")

    def medkit_misuse(self):
        self.medkits -= 1
        print('you dit not use your medkit properly...')

    def use_medkit(self):
        self.medkits -= 1
        self.life += 1
        print('you have received a heart. -1 medkit warning!')

    def medkit_gift(self):
        self.money -= 1
        self.medkits += 1
        print('you have received one medkit. -1 money warning')
    
    def medkit_hustle(self):
        self.money -= 1
        print('the seller of medkits is a hustler!!')


def draw(p):
    if p.life == 0:
        print(f""" ___________________________________________________
      >_<    money: {p.money * money_icon}
      -|-    life : {p.life * life_icon}
      / \\    medkits: {p.medkits * medkit_icon}
      you    score: {p.score}

     you are dead. your score is : {p.score}
___________________________________________________
""")
        quit()      

    print(f"""___________________________________________________
       0_0    money: {p.money * money_icon}
       -|-    life : {p.life * life_icon}
       / \\    medkits: {p.medkits * medkit_icon}
       you    score: {p.score}                                
___________________________________________________              
""")

def prompt(player):
    choice = input("""___________________
    What's next? 
    - <a> battle
    - <b> medkit
    - <y> buy medkit
___________________
""")
    if choice == 'a':
        c = random.choice([0, 1, 1, 2])
        if c == 1:
            p.hurt()
        if c == 0:
            p.ennemy_killed()
        if c == 2:
            print('no enemies in sight...')
            return
    if choice == 'b':
        c = random.choice([0, 1])
        if p.medkits == 0:
            print('you do not have any medkit!')
            return
        if c == 1:
            p.medkit_misuse()
            return
        p.use_medkit()

    if choice == 'y':
        buy = input('buy 1 medkit [+] for 1 money $ ? y or n\n' )
        if buy == 'y':
            if p.money == 0:
                print('you do not have any money!')
                return
        c = random.choice([0, 1, 0 , 0, 1, 0, 2])
        if c == 1:
            print('the seller of medkits has no medkits. Sorry...')
            return
        if c == 0:
            p.medkit_gift()
        if c == 2:
            p.medkit_hustle()
        

def loop(player):
    draw(player)
    prompt(player)
    loop(player)

if __name__ == '__main__':
    p = Player()
    loop(p)