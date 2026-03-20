#Room system Explanation----------------------------------------------------------------
# The room system string of numbers works in the way that the start is "the start"
# option one from the start is roomA
# option two from the start is roomB
# After that the option number will be the next character in the room code
# For example roomB option 2 would be RoomB2
# roomB2 option 1 would be roomB21
#---------------------------------------------------------------------------------------

#Variables and Ending Varibles---------------
onascr = 1
room = 0
start = False
a1 = False
a2 = False
a3 = False
a4 = False
#--------------------------------------------

#Beginning Screen and Endings-----------------------------------------------------------
while True:
    print("Welcome to my Game I made it for practice")
    print("What would you like to do: \nStart(1) Quit(2) View Unlocked Endings(3)")
    option = int(input())
    
    if option == 1:
        start = True
    elif option == 2:
        print("Thanks for playing!")
        break
    elif option == 3:
        room = -2
        onascr = 0
        if a1 == True:
            print("=== You killed yourself, Why (Ending 1) ===")
        if a2 == True:
            print("=== The Sun God (Ending 2) ===")
        if a3 == True:
            print("=== Sleepyhead (Ending 3)")
        if a4 == True:
            print("=== Crybaby (Ending 4) ===")
        onascr = int(input("Leave(1)"))
        if onascr == 1:
            room = 0
        continue
    else:
        print("Invalid option, please choose 1, 2, or 3")
        continue
#-----------------------------------------------------------------------------------------------

#Actual Game---------------------------------------------------------------------------
    while start == True:
        match room:
            case 0:
                # The Start
                print("\n=== You wake up in a white room ===")
                print("(1)KYS  (2) Try to escape")
                option1 = int(input("What do you do? "))
                if option1 == 1:
                    room = 1
                elif option1 == 2:
                    room = 2
                else:
                    room = -1
            case 1:
                #roomA Ending
                print("\n=== You Died, should we celebrate ===")
                print("Game Over!")
                if a1 == False:
                    print("You've unlocked Ending 1")
                a1 = True
                play_again = int(input("Play again? (1) Yes (2) Return to Main Menu: "))
                if play_again == 1:
                    room = 0
                elif play_again == 2:
                    start = False
                    room = 0
                else:
                    print("Invalid input, please choose 1 or 2")
            
            case 2:
                #roomB
                print("\n=== What now?! ===")
                print("You can't really do anything yes?")
                option2 = int(input("(1)Punch The Wall (2)Meditate in hopes that it gvies you the right energy:  "))
                if option2 == 1:
                    room = 3
                elif option2 == 2:
                    room = 4
                else:
                    room = 2
                    print("Invalid Room Number")
            
            case 3:
                #RoomB1
                print("\n=== Do you think you're Rocky? ===")
                print("You repeatedly punch the wall and realize it is made of pillows.\nYou collect the cotton but the pillows seem endless so you eventually stop punching.")
                option3 = int(input("Make a cotton pillow fort(1) Keep on punching(2)"))
                if option3 == 1:
                    room = 7
                elif option3 == 2:
                    room = 8
                else:
                    print("Invalid input")
                    room =3

            case 4:
                #roomB2
                print("\n=== Meditation ===")
                print("You meditate and slowly gain peace of mind")
                option4 = int(input("Meditate Further(1) Stop meditating and try somethig else(2)"))
                if option4 == 1:
                    room = 5
                elif option4 == 2:
                    room = 6
                else:
                    print("Invalid Room Number")
                    room = 4
            case 5:
                #roomB21 Ending
                print("\n=== You became the sun god through profuse meditation, the heat was too much for you human body though so you incinerated ===")
                print("Game Over!")
                if a2 == False:
                    print("You've unlocked Ending 2")
                a2 = True
                play_again = int(input("Play again? (1) Yes (2) Return to Main Menu: "))
                if play_again == 1:
                    room = 0
                elif play_again == 2:
                    start = False
                    room = 0
                else:
                    print("Invalid input, please choose 1 or 2")
                
            case 6:
                #roomB22
                print("\n=== What are you gonna try? ===")
                option5 = int(input("Start ripping at the floor(1) Cry in a corner(2)"))
                if option5 == 1:
                    room = 12
                elif option5 ==2:
                    room = 13
                else:
                    room = 6
                    print("Invalid Input")

            case 7:
                #RoomB11
                print("\n=== You made your pillow fort out of the cotton ===")
                print("The fort is pretty cozy and it makes you feel safe")
                option6 = int(input("Fall Asleep(1) Dwell in your fort(2) Kick the fort down(3)"))
                if option6 == 1:
                    room =9
                elif option6 ==2:
                    room =10
                elif option6 ==3:
                    room = 11
                else:
                    room = 7
                    print("Invalid input")

            case 8:
                #RoomB12
                print("\n=== you punch further ===")
                print("A cave of cotton starts to form")
                option7 = int(input("Keep punching(1) Leave your cave(2)"))
                if option7 == 1:
                    room = 14
                elif option7 == 2:
                    room =15
                else:
                    print("Invalid Input")
                    room = 8
            case 9:
                #roomB111
                print("\n=== You fell asleep and never woke up ===")
                print("Game Over!")
                if a3 == False:
                    print("You've unlocked Ending 3")
                a3 = True
                play_again = int(input("Play again? (1) Yes (2) Return to Main Menu: "))
                if play_again == 1:
                    room = 0
                elif play_again == 2:
                    start = False
                    room = 0
                else:
                    print("Invalid input, please choose 1 or 2")
            
            case 10:
                #roomB112
                print("\n=== Sans. starts to play ===")
                print("The music floods your ears and you might fall asleep if you stay any longer")
                option8 = int(input("Listen to the Music Further(1) Leave the fort(2)"))
                if option8 == 1:
                    room = 16
                elif option8 ==2:
                    room =17
                else:
                    print("Invalid Input")
                    room = 10
                
            case 11:
                #roomB113
                print("\n=== The Fort goes down ===")
                print("You watch as it falls endlessly crying as you watch\nyou creation die. Nothing will save it.\nThe tears won't stop pouring for hours.\nYou eventually are too dehrdrated to live.")
                print("Game Over")
                if a4 == False:
                    print("You've unlocked Ending 4")
                a4 = True
                play_again = int(input("Play again? (1) Yes (2) Return to Main Menu: "))
                if play_again == 1:
                    room = 0
                elif play_again == 2:
                    start = False
                    room = 0
                else:
                    print("Invalid input, please choose 1 or 2")
                    
            case 12:
                #roomB221
                print("\n=== You tear through the floor===")
                print("Nothing much came from the experience other than a hole")
                option9 = int(input("jump out the hole(1) Dig Deeper(2)"))
                if option9 == 1:
                    room = 18
                elif option9 == 2 :
                    room = 19
                else:
                    print("invalid Input")
                    room = 12

            case 13:
                #roomB222
                print("test")
                room = 0

            case 14:
                #roomB121
                print("69")
                room = 0

            case 15:
                #roomB122
                print('test')
                room = 0

            case 16:
                #roomB1121
                print("test")
                room = 0

            case 17:
                #roomB1122
                print("test")
                room = 0
            
            case 18:
                print("test")
                room = 0
            
            case 19:
                print("test")
                room = 0

            case _:
                print("Invalid room number!")
                room = 0
#---------------------------------------------------------------------------------------------------------

#Functions
