#this file contains all the functions except main used in this program
import random
from block import *

def makeGrid(num_column, num_bombs): #creates 9x9 grid with 10 randomly placed mines

    n = num_column+2       #2 rows and 2 columns are added in order to ease
                  #the process of counting bombs. These columns and rows will not be printed or have
                  #any interaction with a player
    
    grids = []
    for row_num in range(n):
        row=[]
        for column in range(n):
            element = Block(False,row_num,column)#calls block class
            row.append(element)#puts block into a list
        grids.append(row)#creates list of list(2D array)
    
    for i in range(num_bombs):
        randomMine(grids)#call randomMine function

        
#rest of the code is to create the outer shell to help the user identify
        #row and columns they want to choose
    edge_row_up=grids[0] #create the list of blocks of upper part of outer shell
    for block in edge_row_up:
        block.block_state = block.column #change the state to the number of columns

    edge_row_bot=grids[n-1]
    for block in edge_row_bot:
        block.block_state = block.column
    edge_columns=[]
    
    for row in grids:
       edge_columns.append(row[0])
       edge_columns.append(row[n-1])
       
    for block in edge_columns:
        block.block_state = block.row

    return grids
        
    

def randomMine(grids): #puts down a mine in a random spot on the grid
    size =len(grids)-1
#gets a random spot in grid
    a = random.randint(1, size-1)
    b = random.randint(1, size-1)

    myRow = grids[a]
    if myRow[b].bomb != True:#conditional to avoid puting a mine on the same place twice
        myRow.remove(myRow[b]) #replace the normal block with block with bomb
        myRow.insert(b,Block(True,a,b))
        
    else: #if mine already exists on that spot, try again (so we get 10 mines)
        randomMine(grids)

def print_grid(grids): #a function to print a gird
    for row in grids:
        row_display=[]
        for block in row:
            row_display.append(str(block.block_state))
        print(row_display)

def block_counter(grid): #a function to count the number of block remained unopend but not a bomb
    block_counter =0
    for row_counter in range(1,len(grid)-1):#range defined to count only blocks that player has interaction
        for col_counter in range(1,len(grid)-1):
            if grid[row_counter][col_counter].block_open == False:
                block_counter += 1
                
    return block_counter

def openBlock(grid,row,column): #a function to judge whether the bomb is in the chosen block and if so
                                #returns False, otherwise chanege the state of block to be open and show the numebr
                                #of surrounding blocks with bombs.
    
        block = grid[row][column] #takes the block element from the list
        if block.bomb==True:
            return False
        elif block.bomb_counter(grid)!=0:
                block.block_open = True#set the value of block to be open
                block.block_state = block.bomb_counter(grid) #will show the number of surrounding bomb
                return True
            
        else: #if the number of surrounding bombs are zero, clears all the surrounding blocks
                if row >=1 and column>=1 and row<len(grid)-1 and column < len(grid)-1:
                    #since there is an outer shell(the elements out side of the specified region),
                    #all of the blocks that could be chosen is surrounded by 8 blocks. Hence,
                    #we do not have to think about the case where chosen block is at the corner or
                    #the edge of the array. it is sufficient to take care of only the case 
                        for counter in range(-1,2): 
                                grid[row -1][column + counter].block_open = True
                                grid[row -1][column + counter].block_state = grid[row -1][column + counter].bomb_counter(grid)

                        for counter in range(-1,2,2):
                                grid[row ][column + counter].block_open = True
                                grid[row][column + counter].block_state = grid[row][column + counter].bomb_counter(grid)

        
                        for counter in range(-1,2):
                                grid[row +1][column + counter].block_open = True
                                grid[row +1][column + counter].block_state = grid[row +1][column + counter].bomb_counter(grid)
                                
                                
                block.block_open = True#set the value of block to be open
                block.block_state = block.bomb_counter(grid) #will show the number of surrounding bomb
                return True



