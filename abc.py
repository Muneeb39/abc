# import Pythom Modules --> [ libraries ]
from os import system as cmd 
from time import sleep as slp
import sys,platform
from datetime import date,datetime
# Create Different Function --> [ Def ]
def clear_screen():
    if sys.platform.lower() == "linux":
        slp(0.5)
        cmd("clear")
    elif sys.platform.lower() == "win":
        slp(0.5)
        cmd("cls")
    else:
        slp(0.5)
        cmd("clear")
        # Create logo -->
##    ## ########  ##    ## 
##   ##  ##     ## ##   ##  
##  ##   ##     ## ##  ##   
#####    ########  #####    
##  ##   ##        ##  ##   
##   ##  ##        ##   ##  
##    ## ##        ##    ## 
def logo():
  ckear_screen()
  print(" ")
   # Create Main menu --> [ Function ]
def print_menu():
	print( "-------------------------------------------" )
	
print("[01]")
print("[02]")
print("[03]")
print("[04]")

print( "-------------------------------------------------" )
ch = input('\n[->] Choose : ')
if ch in ["1","01"]:
        pass
else:
        menu()
if __name__=='__main__':
 def menu():
    print("Welcome, \n 1. Method1 \n 2. Method2 \n 3. Method3")
print menu()
 
