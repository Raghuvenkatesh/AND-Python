import getpass
import sys
import telnetlib

user = raw_input("Enter your username:")
password = getpass.getpass()

HOST = ("172.16.126.132","172.16.126.133","172.16.126.131")

for i in HOST:
    print ("\n\nconnecting to "+i)
    tn = telnetlib.Telnet(i, timeout = 15)
    if i is "172.16.126.132":

        tn.read_until("login:")
        tn.write(user + "\n")
        if password:
            tn.read_until("Password:")
            tn.write(password + "\n")

        tn.write("sh configuration | display set\n") 
        tn.write("exit\n") 
    elif i is "172.16.126.131":

        tn.read_until("Username:")
        tn.write(user + "\n")

        if password:
            tn.read_until("Password:")
            tn.write(password + "\n")


        tn.write("terminal length 0\n")        
        tn.write("show runni\n")
        tn.write("exit\n")
     
    elif i is "172.16.126.133":        
        tn.read_until("Username:")
        tn.write(user + "\n")
        if password:
            tn.read_until("Password:")
            tn.write(password + "\n")

        tn.write("en\n")
        tn.write("terminal length 0\n")        
        tn.write("show runni\n")
        tn.write("exit\n")
        #print(tn.read_all())
    readall = tn.read_all()
    File = open("File"+str(i), "w")
    File.write(readall)
    File.write("\n")     
    File.close()
    print("Backup of "+i+" completed")

