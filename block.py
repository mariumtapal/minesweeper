class Block:
    # a class of 'block'. this takes prameters of bomb.bool(boolean value that
    # shows whether the block contains bomb or not) and the position of the block
    # in (row, clomn)
    def __init__(self, bomb_bool, row, column):
        self.block_open = False #shows whether block is open or not
        self.bomb = bomb_bool #shows whether the block has a bomb or not
        if self.bomb == True:
            self.block_open = True 
        self.block_state = 'x' #value that will be printed
        self.row = row
        self.column  = column
      
    def bomb_counter(self,array): #a method to count the number of surrounding bombs
        bomb_counter = 0

        if self.row >=1 and self.column>=1 and self.row<len(array)-1 and self.column < len(array) -1:
            #conditional to restrict the region to count the bombs to the region necessary
            for counter in range(-1,2): #upper blocks
                block = array[self.row -1][self.column + counter]
                if block.bomb == True: #in each case if surrounding box contains
                    bomb_counter += 1  #bomb, then increments the value of bomb
                                       #counter by 1

            for counter in range(-1,2,2):#surrounding blocks that are in the same row
                block = array[self.row][self.column + counter]
                if block.bomb == True:
                    bomb_counter += 1
            for counter in range(-1,2):#lower (surrounding)blocks
                block = array[self.row + 1][self.column + counter]
                if block.bomb == True:
                    bomb_counter += 1
                    
            
        return bomb_counter
    

    def flag(self): #method to change the printed value of the block to be flagged
        self.block_state = 'f'
            
    
