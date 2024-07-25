def check():
    print('who will go first?')
    print('Enter 1 if player1 want to start or 2 if player2 want to start!')
    num = int(input('select 1 or 2 :'))
    while num not in [1,2]:
         num = int(input('select 1 or 2 :'))
    if num == 1:
        print('player1 will start.')
        player1 = input('select X or O: ')
        while player1 not in ['X','O']:
            player1 = input('select X or O: ')
        if player1 == 'X':
            player2 = 'O'
        else:
            player2 = 'X'
    else:
        print('player2 will start.')
        player2 = input('select X or O: ')
        while player2 not in ['X','O']:
            player2 = input('select X or O: ')
        if player2 == 'X':
            player1 = 'O'
        else:
            player1 = 'X'
    return num,player1,player2

def display_board(board):
    print(board[1]+'|'+board[2] +'|'+board[3])
    print('-----')
    print(board[4]+'|'+board[5] +'|'+board[6])
    print('-----')
    print(board[7]+'|'+board[8] +'|'+board[9])
    

def index_select():
    index = int(input('select an index from (1 to 9): '))
    while index not in range(1,10):
        print('Index must be from 1 to 9 only!')
        index = int(input('select an index from (1 to 9): '))
    return index
        
    

def place_choice(board,index,player):
    while board[index] != ' ':
        print('This index has been occupied already.')
        index = index_select()
    board[index] = player

def check_win(board):
    #horizontal
    if (board[1] == board[2] == board[3]) and board[3] in ['X','O']:
        return True
    elif (board[4] == board[5] == board[6]) and board[6] in ['X','O']:
        return True
    elif (board[7] == board[8] == board[9]) and board[9] in ['X','O']:
        return True 
    #vertical
    elif (board[1] == board[4] == board[7]) and board[7] in ['X','O']:
        return True
    elif (board[2] == board[5] == board[8]) and board[8] in ['X','O']:
        return True 
    elif (board[3] == board[6] == board[9]) and board[9] in ['X','O']:
        return True 
    #diagonal
    elif (board[1] == board[5] == board[9]) and board[5] in ['X','O']:
        return True 
    elif (board[3] == board[5] == board[7]) and board[5] in ['X','O']:
        return True 
    return False

def check_draw(board):
    if ' ' not in board:
        return True
    return False
    
def start_game():
    play = input('Do you want to play the game(YES or NO): ')
    l1 = ['YES','yes','Yes','yEs','yeS','yES','YeS','YEs','NO','no','No','nO']
    while play not in l1:
        play = input('Do you want to play the game(YES or NO): ')
    if play in l1[0:8]:
        return True
    return False

def player_shift(player):
    if player == 'X':
        player = 'O'
    else:
        player = 'X'
    return player 

def game():
    game = start_game()
    while game:
        board = [' ']*10
        board[0] = '#'
        num,player1,player2 = check()
        display_board(board)
        if num == 1:
            player = player1
            loop = True
            while loop:
                index = index_select()
                place_choice(board,index,player)
                display_board(board)
                win = check_win(board)
                if win == True:
                    if player == player1:
                        print('player1 won the game.')
                    else:
                        print('player2 won the game.')
                    break
                draw = check_draw(board)
                if draw == True:
                    print('Game drawn.')
                    break 
                player = player_shift(player)
            game = start_game()
        else:
            player = player2
            loop = True
            while loop:
                index = index_select()
                place_choice(board,index,player)
                display_board(board)
                win = check_win(board)
                if win == True:
                    if player == player2:
                        print('player2 won the game.')
                    else:
                        print('player1 won the game.')
                    break
                draw = check_draw(board)
                if draw == True:
                    print('Game drawn.')
                    break 
                player = player_shift(player)
            game = start_game()
            

game()
                
                
                        
                    
                
                    
                    
            
    

        
    

    
    
    
    

        
            

    
        
    
    
             
        