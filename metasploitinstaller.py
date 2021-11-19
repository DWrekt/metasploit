
import sys
import os
R='\033[91m'
Y='\033[93m'
G='\033[92m'
CY='\033[96m'
W='\033[97m'
B='\033[95m'

print(CY+"""                  𝙒𝙚𝙡𝙡𝙘𝙤𝙢𝙚 𝙩𝙤 𝙢𝙚𝙩𝙖𝙨𝙥𝙡𝙤𝙞𝙩 𝙞𝙣𝙨𝙩𝙖𝙡𝙡𝙚𝙧
""")
print(G+"                     Created by : Wolf")
q = input(G+"~"+W+"Do u want to install Metasploit ["+G+"y"+W+"/"+G+"n"+W+"] ")
if(q=="y"or q=="Y"):
	os.system("pkg uninstall ruby -y")
	
	print(G+"\nCopy this command and paste it.")
	print(Y+"""\nbash <(curl -fsSL "https://git.io/abhacker-repo") --install ruby=2.7.2 -r apt install metasploit -y"""
