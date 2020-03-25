from os import system, name
from time import sleep
from random import random
import mc
HashIdentity = mc.init()
print("WELCOME TO ULTRACODEshV2 - LOADING...")
def clear(): 
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear')
sleep(2)
clear()
for i in range(1,101):
    print ("LOADING["+str(i)+"%]")
    sleep(0.1)
    clear()
while True:
  command = input('root/users/admin: ')
  if command == "shutdown":
    print("root.shutdown.sudo")
    break
  else:
   if command == "server.status":
     print("SERVER STATE: [PLEASE RESTART IF LARGER THAN 0.100000000]")
     print(str(random()))
mc.exit(HashIdentity)