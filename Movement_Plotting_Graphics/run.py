import os
import subprocess

class bcolors:
    PASS = '\033[92m'
    FAIL = '\033[91m'
    OKBLUE = '\033[94m'
    BOLD = '\033[1m'
    ENDC = '\033[0m'
os.system("cd Source && python3 main.py")
exit()

Packages = ["math","matplotlib","numpy","random","json","scipy","datetime","urllib3"]
Files = ["Input/input.txt", "Source/operations_Functions.py", "Source/data_Creator.py", "Source/main.py", "Source/simulator.py"]

check = True
print("\n"+bcolors.OKBLUE +bcolors.BOLD + "Check installed packages and modules"+ bcolors.ENDC+ bcolors.ENDC)
out = subprocess.Popen(['python3.7','--version'],stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
stdout,stderr = out.communicate()
if "not" in str(stdout):
    print(" "+bcolors.FAIL + u'\u2718'+ bcolors.ENDC+" Python 3 ")
    check = False
else:
    print(" "+bcolors.PASS + u'\u2714'+ bcolors.ENDC+" Python 3 ")

out = subprocess.Popen(['pydoc','modules'],stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
installedPackages,stderr = out.communicate()
for package in Packages:
    if package not in str(installedPackages):
        print(" "+bcolors.FAIL + u'\u2718'+ bcolors.ENDC+" "+str(package))
        check = False
    else:
        print(" "+bcolors.PASS + u'\u2714'+ bcolors.ENDC+" "+str(package))

print("\n"+bcolors.OKBLUE +bcolors.BOLD +"Check Source files"+ bcolors.ENDC+ bcolors.ENDC)
for files in Files:
    if os.path.exists(files) == False:
        print(" "+bcolors.FAIL + u'\u2718'+ bcolors.ENDC+" "+str(files))
        check = False
    else:
        print(" "+bcolors.PASS + u'\u2714'+ bcolors.ENDC+" "+str(files))

if check == True:
    print("\n"+bcolors.PASS +"Start simulation\n"+ bcolors.ENDC)

else:
    print("\n"+bcolors.FAIL +"Please install required packages and modules"+ bcolors.ENDC)
      

