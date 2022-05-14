#This is a python automation for Terraform & Ansible
#install terraform and Ansible 
#call and execute terraform script
#After infrastructures deploys, python copy’s Ansible pub keys to the servers
#After copying keys, it executes a ping and install Apache server
import os
import subprocess


print ("---------Welcome---------")
#check if os == debian or ubuntu | then install terraform and ansible
terrainstall = (os.system("sudo apt-get install terraform"))
ansinstall = (os.system("sudo apt-get install ansible"))

checkansiversion =  (os.system("ansible --version >> ansiblecheck.txt"))
checkterraversion = (os.system("terraform -v >>terraformcheck.txt"))
chanv = open("ansiblecheck.txt, 'r")
if chanv != str(""): ##check for readlines command in python
    print ("[+] Ansible is not installed")
elif checkterraversion != str(""):
    print ("[+] Terraform is not installed")