import random

life_count, life_icon = 3, '\u2665'
medkit_count, medkit_icon = 2, '[+] '
money_count, money_icon = 3, '$'
score_count = 0

def draw():
    global life_count
    if life_count == 0:
        print(f""" ___________________________________________________
      >_<    money: {money_count * money_icon}
      -|-    life : {life_count * life_icon}
      / \\    medkits: {medkit_count * medkit_icon}
      you    score: {score_count}

     you are dead. your score is : {score_count}
___________________________________________________
""")
        quit()      

    print(f"""___________________________________________________
       I_I    money: {money_count * money_icon}
       -|-    life : {life_count * life_icon}
       / \\    medkits: {medkit_count * medkit_icon}
       you    score: {score_count}                                
___________________________________________________              
""")

def prompt():
    global life_count, medkit_count, money_count, score_count

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
            print('ouch!Your hurt!')
            life_count = life_count - 1
        if c == 0:
            money_count = money_count + 1
            score_count = score_count + 1
            print('the enemi has missed.You have killed him!')
        if c == 2:
            print('no enemis at vue...')
            return
    if choice == 'b':
        if medkit_count == 0:
            print('you don t have any medkit!')
            return
        life_count = life_count + 1
        medkit_count = medkit_count - 1
        print('you have received a heart.-1 medkit warning!')
    if choice == 'y':
        buy = input('buy 1 medkit [+] for 1 money $ ? y or n\n' )
        if buy == 'y':
            if money_count == 0:
                print('you don t have any money!')
                return
        c = random.choice([0, 1, 0 , 0, 1, 0, 2])
        if c == 1:
            print('the seller of medkits has no medkits. Sorry...')
            return
        if c == 0:
            money_count = money_count - 1
            medkit_count = medkit_count + 1
            print('you have received one medkit.-1 money warning')
        if c == 2:
            print('the seller of medkits is a hustler!!')
            money_count = money_count - 1


def loop():
    draw()
    prompt()
    loop()

if __name__ == '__main__':
    loop()