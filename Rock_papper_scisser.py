from random import randint
def rps():
    c_points=0
    p_points=0
    for i in range(3):
      try:  
        player_option=int(input('''Enter 1 to choose Rock\nEnter 2 to choose paper\nEnter 3 to choose scisser\n'''))
        if player_option not in(1,2,3):
              print('Invalid syntax,you lose your points')
              continue
        computer_option=randint(1,3)
        options=['rock','paper','scissor']
        print('your choice is:',options[player_option-1])
        print('computer choice is:',options[computer_option-1])
        if computer_option==player_option:
           print('It is a draw')
           print('------------------------------------------------')      
           
        elif(computer_option==1 and player_option==2)or (computer_option==2 and player_option==3)or (computer_option==3 and player_option==1):
           print('player wins')
           print('------------------------------------------------')      
           p_points+=1
        else:
           print('computer wins')
           c_points+=1
           print('------------------------------------------------')
      except:
          ('something went wrong')
    print('---------------------------------------------------')      
    print('FINAL RESULT')      
    if computer_option > player_option:
        print('computer win')
    elif player_option>computer_option :
        print('player win')
    else:
        print('draw match')
        
rps()    
           
