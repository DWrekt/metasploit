#!/bin/bash
#colors
red=$(tput setaf 1)
green=$(tput setaf 2)
yellow=$(tput setaf 3)
cyan=$(tput setaf 6)
bold=$(tput bold 5)
clear

echo
echo "${yellow}${bold} ~ Installing... "
echo
sleep 2
chmod 777 dw
echo
cp -r dw $PREFIX/bin
echo
sleep 1
echo "${green}${bold} ~ Successfully Installed"
echo
sleep 1
echo "${cyan}${bold} ~ Type dw for start hacking "
echo 
sleep 1
echo "${cyan}${bold} ~ Made By DarkWolf"
echo 