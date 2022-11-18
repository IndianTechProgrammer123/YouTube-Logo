import colorama
from colorama import Fore 
colorama.init(autoreset=True)

max_row = 17
max_col = 60
right = 22
left = 22

for row in range(max_row):
    flag=False
    for col in range(max_col):
        if(row>=3 and row<=18 and (col>=left and col<=right)):
            print(f"{Fore.WHITE}@",end="")
            flag=True 
        else:
            if(row==0 and (col in [0,1,max_col-2,max_col-1]))or (row==1 and (col in [0,max_col-1])):
                print(" ",end="")
            elif (row==max_row-1 and (col in [0,1,max_col-2,max_col-1])) or (row==max_row-2 and (col in [0,max_col-1])):
                print(" ",end="")
            else:
                print(f"{Fore.RED}@",end="")

    if flag:
        if row>=8:
            right-=3
        else:
            right+=3
    print()
