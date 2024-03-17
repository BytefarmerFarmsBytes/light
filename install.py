#importing modules
import time
import os

#files list

#end locations
end = [
"/bin/light", #script wrapper
"/bin/light.py", #light interfacing script
"/etc/systemd/system/light.service", #light service
"/lib/systemd/system-sleep/light.sleep", #wake from sleep file
"/bin/light.start", #light service wrapper
"/etc/light-current.conf", #light current state used on screen open
"/etc/light-default.conf", #light default state used on boot
"/bin/lightscript" #actuall command script
]

#start locations
start = [
"files/light", #script wrapper
"files/light.py", #light interfacing script
"files/light.service", #light service
"files/light.sleep", #wake from sleep file
"files/light.start", #light service script
"files/light-current.conf", #light current state used on screen open
"files/light-default.conf", #light default state used on boot
"files/lightscript" #actuall command script
]

#start program
print("starting...\n")

time.sleep(1) #fake wait

print("checking for systemd...\n")
systemd = os.popen("readlink /sbin/init").read().strip() #check for systemd
print(systemd)

if systemd == "/lib/systemd/systemd": #if exists then say
    print("systemd exists\n")
else:
    print("not a systemd based system, exiting\n")
    quit() #end if no systemd

time.sleep(1)

print("checking for previous installs...\n")

if os.path.exists("/bin/light"): #check for the light command
    y = 0 #while loop iteratios

    while y == 0 : #input loop

        print("previous install exists, remove?\n")
        print("!WARNING! this uses rm -rf and could be dangerous, reveiw the changes to make to system carefully\n")
        print("changes to make to system:\n")

        a = 0
        for x in end :
            print("remove " + end[a])
            a = a + 1
        
        confirmation = input("\nContinue [Y/N] ") #ask if we should remove the old install

        if ((confirmation == "Y") or (confirmation == "y")) : #if yes then remove
            print("removing...")
            
            for x in end: #iterate and remove
                os.system("rm -rf " + end[y])
                y = y + 1

            time.sleep(1)

            print("removed...")
            break

        elif ((confirmation == "N") or (confirmation == "n")) : #if no then exit
            print("exiting")
            quit()
else :
    print("light is not currently installed\n")

print("starting install\n")


print("!WARNING! this moves files to system folders and could be dangerous, reveiw the changes to make to system carefully\n")
print("changes to make to system:\n")

a = 0
for x in end :
    print("copy " + start[a] + " to " + end[a])
    a = a + 1

confirmation = input("Continue [Y/N] ")

b = 0 #loop exit variable

while b == 0 : #input loop

    if ((confirmation == "Y") or (confirmation == "y")) : #confirmation for install yes
        b = 1 #end loop
        print("installing...")
        time.sleep(1) #fake wait

    elif ((confirmation == "N") or (confirmation == "n")) : #confirmation for install no
        b = 1 #end loop
        print("quiting")
        quit() #quit program


a = 0 #temporary loop counter
for x in end : #loop through files to copy
    os.system("cp " + start[a] + " " + end[a])
    a = a + 1


print("!WARNING! if you are a sys admin, check for permissions that will be changed in the next step\n")
print("changes to make to system:\n")

a = 0
for x in end :
    print("chmod +x " + end[a])
    a = a + 1 #temp varable for perm change loop

confirmation = input("Continue [Y/N] ") #ask for perm change 

b = 0 #loop exit variable perm change

while b == 0 : #input loop

    if ((confirmation == "Y") or (confirmation == "y")) : #confirmation for perm change yes
        b = 1 #end loop
        print("changing permissions...")
        time.sleep(1) #fake wait

    elif ((confirmation == "N") or (confirmation == "n")) : #confirmation for install no
        b = 1 #end loop
        print("quiting")
        quit() #quit program


a = 0 #temporary loop counter
for x in end : #loop through files to perm change
    os.system("chmod +x " + end[a])
    a = a + 1



print("would you like to use the systemd scripts? this will allow you to turn on the light on screen open and set a default for on boot\n")
print("changes to make to system:\n")
print("systemctl enable light")
print("systemctl daemon-reload")
print("systemctl start light")

confirmation = input("Continue [Y/N] ") #ask for systemd script change 

b = 0 #loop exit variable perm change

while b == 0 : #input loop

    if ((confirmation == "Y") or (confirmation == "y")) : #confirmation for systemd change yes
        b = 1 #end loop
        print("starting systemd service")
        time.sleep(1) #fake wait

    elif ((confirmation == "N") or (confirmation == "n")) : #confirmation for systemd no
        b = 1 #end loop
        print("quiting")
        quit() #quit program


a = 0 #temporary loop counter
os.system("systemctl enable light")
os.system("systemctl daemon-reload")
os.system("systemctl start light")



if os.path.exists("/bin/python"):
    print("python exists\n")
else
    if os.path.exists("/bin/python3"):
        print("/bin/python does not exist")
        print("symlinking /bin/python3 to /bin/python\n")
        os.system("ln -s /bin/python3 /bin/python")
    else
        print("missing python3 please, install it using your package manager\n")
        print("quiting")
        quit()


print("DONE!\n")
print("run \"light -h\" to get started")