def display_game(game_list):
    print('Here is the current list:')
    print(game_list)


def position_choice():
    choice = 'wrong'
    while choice not in ['0', '1', '2']:
        choice=input("Please pick a position 0,1 or 2:")
        if choice not in ['0', '1', '2']:
            print("Sorry,Invalid chocie")
    return int(choice)
def replacement_chooice(game_list,position):
    user_replacement=input("Please choose a string to replace: ")
    game_list[position]=user_replacement
    return game_list
def gameon_choice():
    choice='wrong'
    while choice not in ['Y','N']:
        choice=input("Would you like to keep playing? Y or N: ")
        if choice not in ['Y','N']:
            print("Sorry,I dont understand,please choose Y or N")
    if choice=='Y':
        return True
    else:
        return False
game_list=[0,1,2]
gameon=True
while gameon:
    display_game(game_list)
    positiom=position_choice()
    game_list=replacement_chooice(game_list,positiom)
    display_game(game_list)
    gameon=gameon_choice()