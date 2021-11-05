import random
item = ['','','']
item[0] = ''' 
   ____
  / __ \
 ( (__) |___ ___
  \________,'        """""----....____
   _______<  () dd         ____----'
  / __   __`.___-----""""
 ( (__) |
  \____/
'''
item[1] = '''
 __________
|  PAPER   |
|&&& ======|
|=== ======|
|=== == %%$|
|[_] ======|
|=== ===!##|
|__________|

'''

item[2] = '''
     .------.         
   .'      //`.    
  /       //   \  
 |       //     :
 :      //      | 
  \    //      /   
   `._//    _.'   rock
     `"----"'   

'''
choice = int(input('Enter any number \n 0 for scissor \n 1 for paper \n 2 for rock\n'))
random_number_for_computer = random.randint(0,2)
# print(random_number_for_computer)
if choice == 0:
    if random_number_for_computer == 1:
        print("you win")
    elif random_number_for_computer == 2:
        print("computer win")
    else:
        print("its a draw")
elif choice == 1:
    if random_number_for_computer == 1:
        print("its a daw")
    elif random_number_for_computer == 2:
        print("you win")
    else:
        print("computer win")
else:
    if random_number_for_computer == 1:
        print("computer win")
    elif random_number_for_computer == 2:
        print("its a draw")
    else:
        print("you win")
print(f'you selected {item[choice]}  and computer selected  {item[random_number_for_computer]}')