from functions import *
import webbrowser as web
from time import sleep

#main function to executes the functions
def main():
    print("              _                            _          ")         
    print("__      _____| | ___ ___  _ __ ___   ___  | |_ ___      ")       
    print("\ \ /\ / / _ \ |/ __/ _ \| '_ ` _ \ / _ \ | __/ _ \       ")     
    print(" \ V  V /  __/ | (_| (_) | | | | | |  __/ | || (_) |        ")   
    print("  \_/\_/ \___|_|\___\___/|_| |_| |_|\___|  \__\___/           ") 
    print("")                                                           
    print("           _                                                   ")
    print(" _ __ ___ (_)_ __   ___  _____      _____  ___ _ __   ___ _ __ ")
    print("| '_ ` _ \| | '_ \ / _ \/ __\ \ /\ / / _ \/ _ \ '_ \ / _ \ '__|")
    print("| | | | | | | | | |  __/\__ \\ V  V /  __/  __/ |_) |  __/ |   ")
    print("|_| |_| |_|_|_| |_|\___||___/ \_/\_/ \___|\___| .__/ \___|_|   ")
    print("                                              |_|              ")
          
    print('                              This game was created by Cheldima')
    print('')
    print('')
    print("Instructions: To play this game, pick a row and a column. \n Once you decide on a block, decide whether you’d like to \n 1. Open It or\n 2. Flag It")
    print('')
    print('')
    print('The level options are:\n1: Easy\n2: Medium\n3: Hard \n')
    lvl_choice = int(input('Enter the integer of the level you want to play: '))
    if lvl_choice == 1:
        grid = makeGrid(5,6)#make 2D arrays
        num_column = 5
    elif lvl_choice == 2:
        grid = makeGrid(9,10)
        num_column = 9
    elif lvl_choice == 3:
        grid = makeGrid(15,30)
        num_column = 15
    else:
        print('Your input is invalid. Hence, we set up a spicy game for you')
        grid = makeGrid(20,50)
        num_column = 20
    print("   _          _   _       _                _ ")
    print("  | |        | | ( )     | |              (_)  ")     
    print("  | |     ___| |_|/ ___  | |__   ___  __ _ _ _ __")   
    print("  | |    / _ \ __| / __| | '_ \ / _ \/ _` | | '_ \ ") 
    print("  | |___|  __/ |_  \__ \ | |_) |  __/ (_| | | | | | ")
    print("  |______\___|\__| |___/ |_.__/ \___|\__, |_|_| |_| ")
    print("                                      __/ |         ")
    print("                                     |___/")
    print_grid(grid) #print the array
    while(block_counter(grid) >0):
        print('Number of remaining blocks:',block_counter(grid))
        row_valid = False
        col_valid = False
        choice_valid = False
        while(row_valid == False): #while loop to make sure user choose row number in appropriate range
            row = int(input('Enter the row number of block you want to open or put a flag: '))
            if row <= num_column and row >= 1:
                row_valid = True
            else:
                print('Invalid input. Enter an integer between 1 and', num_column)
                
        while(col_valid == False): #while loop to make sure user choose column number in appropriate range
            column = int(input('Enter the column number of block you want to open or put a flag: '))
            if  column <= num_column and column >= 1:
                col_valid = True
            else:
                print('Invalid input. Enter an integer between 1 and', num_column)
                
        while(choice_valid == False):
            choice = int(input('1: Open \t 2: Flag \nYour Choice: '))
            if choice == 1 or choice == 2:
                choice_valid = True

        if choice ==1:
            if openBlock(grid,row,column)==False: #calls openBlock function and if it returns False, 
                print('BOOOOOOOOOOOOM!!!')       #then break the loop
                web.open("https://www.youtube.com/watch?v=zsTRxXvQY0s") #explosion video
                sleep(10) #pauses while video plays
                print('GAME OVER')
                break
            elif block_counter(grid) == 0:
                print_grid(grid)
                print('Congratulations! You sweeped all the mines!')
                web.open('https://www.youtube.com/watch?v=hT94urc-MVw') #once the player wins, it shows them this clip to congratulate them
                sleep(10) #stop the program while the song is playing
            else:
                print_grid(grid)
        else:
            grid[row][column].flag()
            print_grid(grid)


    print(" _   _                 _                           ") 
    print("| |_| |__   __ _ _ __ | | __  _   _  ___  _   _     ")
    print("| __| '_ \ / _` | '_ \| |/ / | | | |/ _ \| | | |    ")
    print("| |_| | | | (_| | | | |   <  | |_| | (_) | |_| |    ")
    print(" \__|_| |_|\__,_|_| |_|_|\_\  \__, |\___/ \__,_|    ")
    print("                              |___/                 ")
    print("  __                    _             _             ")
    print(" / _| ___  _ __   _ __ | | __ _ _   _(_)_ __   __ _ ")
    print("| |_ / _ \| '__| | '_ \| |/ _` | | | | | '_ \ / _` |")
    print("|  _| (_) | |    | |_) | | (_| | |_| | | | | | (_| |")
    print("|_|  \___/|_|    | .__/|_|\__,_|\__, |_|_| |_|\__, |")
    print("                 |_|            |___/         |___/ ")
    print("                 Cheldima appreciates your effort")

if __name__=='__main__':
   main()
