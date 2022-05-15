#This is a python automation for Terraform & Ansible
#install terraform and Ansible 
#call and execute terraform script
#After infrastructures deploys, python copy’s Ansible pub keys to the servers
#After copying keys, it executes a ping and install Apache server
import os
import subprocess


print ("---------Welcome---------")
#check if os == debian or ubuntu | then install terraform and ansible
#terrainstall = (os.system("sudo apt-get install terraform"))
#ansinstall = (os.system("sudo apt-get install ansible"))

checkansiversion =  (os.system("ansible --version |grep core > ansiblecheck.txt"))
checkterraversion = (os.system("terraform -v > terraformcheck.txt"))

with open('ansiblecheck.txt') as chanv :
    chanvlines = chanv.readlines()
with open('terraformcheck.txt') as chter :
    chterlines = chter.readlines()
for line in chanvlines and  chterlines:

    if str("ansible [core 2.12.4]") in line: ##check for readlines command in python
        print ("[+] Ansible Is Installed on Host")
    else:
        print ("[-] Ansible is not installed, install Ansible with the command 'sudo apt-get install ansible'")
    if str("Terraform v") in line:
        print ("[+] Terraform is installed")
    else:  ##check why Terraform
        print ("[-]Terraform is not installed, install Terraform with the command 'sudo apt-get install Terraform'")


def terracall():
    os.system("terraform init")



terracall()
