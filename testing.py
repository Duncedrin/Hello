#Evan Delmolino edd1717@rit.edu
#tester.py
#python3
import os
#use "> /dev/null" to suppres output of commands
#local gateway test
print("Testing Default Gateway...")
if os.system("ping -c 1 GATEWAY > /dev/null") == 0:
    print("Success!")
else:
    print("Failure!")
#remote test 8.8.8.8
print("Testing remote connectivity, pinging 8.8.8.8...")
if os.system("ping -c 1 8.8.8.8 > /dev/null") == 0:
    print("Success!")
else:
    print("Failure!")
#DNS test google.com
print("Testing DNS, pinging google.com")
if os.system("ping -c 1 google.com > /dev/null") == 0:
    print("Success!")
else:
    print("Failure!")