print( " THE LOST TREASURE ")

print(""" Welcome, Adventurer!
You have discovered an ancient chamber containing three mysterious doors.
Somewhere beyond these doors lies a legendary treasure. But beware: every choice has consequences.
- Your starting health: 100 HP
- Your treasure: 0 gold coins
- Your mission: Find the legendary treasure and escape alive.
Choose your first door:
🔴 Red Door
🔵 Blue Door
🟢 Green Door """)

print("click 1 to open Red Door ")
print("click 2 to open Blue Door")
print("Click 3 to open Green Door ")
print("Click 4 to restart the game ")
print("Click 5 to exit the game ")

import random 

while True :

    Gold_coin = 0
    Hp = 100

    while Hp>0 :

        Door_choosed = int(input("Enter your Door number : "))


        if (Door_choosed == 1 ):
            print("🔴 Red Door — The Fire Trap") 

            chance = random.randint(1,100)

            if (chance <= 30):
                print("Congratulations !! , You discover a small gold chest !")
                print("You gain 20 gold coins !! ")
                Gold_coin += 20 
                Gold_coin = max(0, Gold_coin)
                print("Your total gold coins are : " , Gold_coin)
                print("Your total Hp is : " ,Hp)
                

            else:
                print("OOPS !! ,A fire trap activates. Lose 30 HP ,  You got injured ")
                Hp -= 30
                Hp = max(0, min(Hp, 100))
                print("Your total Hp is : " ,Hp)
                print("Your total gold coins are : " , Gold_coin)


        if(Door_choosed == 2):
            print("🔵 Blue Door — The Crystal Cave")

            chance = random.randint(0,100)

            if(1<= chance <= 10):
                print("Congratulations !! , You found the legendry treasure and won the game !!")
                print("ADVENTURE COMPLETE!!")
                exit()
    
            elif (11<= chance <= 40):
                print("Congratulations !! ,You find a pile of gold. Gain 40 gold coins.")
                Gold_coin += 40
                Gold_coin = max(0, Gold_coin)
                print("Your total gold coins are : " ,Gold_coin)
                print("Your total Hp is : " ,Hp)
                

            else:
                print("OOPPS !! , Falling rocks injure you .Lose 20 HP.  ")
                Hp -= 20 
                Hp = max(0, min(Hp, 100))
                print("Your total Hp is : " ,Hp)
                print("Your total gold coins are : " , Gold_coin)

        if(Door_choosed == 3 ):
            print("🟢 Green Door — The Secret Garden")

            chance = random.randint(0,100)

            if(chance <= 20):
                print("A poisonous plant damages you. Lose 15 HP.")
                Hp -= 15 
                Hp = max(0, min(Hp, 100))
                print("Your total Hp is : " ,Hp)
                print("Your total gold coins are : " , Gold_coin)

            elif(20< chance <= 50):
                print("You discover a hidden gold chest. Gain 30 gold coins.")
                Gold_coin += 30
                Gold_coin = max(0, Gold_coin)
                print("Your total gold coins are : " ,Gold_coin)
                print("Your total Hp is : " ,Hp)
                

            elif(50 <chance <=100 ):
                print("You discover healing herbs. Gain 25 HP, but health cannot exceed 100.")
                Hp += 25 
                Hp = max(0, min(Hp, 100))
                print("Your total Hp is : " ,Hp)
                print("Your total gold coins are : " , Gold_coin)


        if(Door_choosed == 4):
            print("Restarting the game...")
            break # this will break the current game and restart the new one ...

        if (Door_choosed ==  5 ):
            print("Exiting...")
            exit()

        if Hp == 0:
            print("You lose! Your adventure has ended.")
            break 
            exit()
