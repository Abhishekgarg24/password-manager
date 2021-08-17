#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#version 2.1
#Autor: Nitish Garg 
#Date: 04.08.2021
import random #getting random variables from library
import string #getting string containing all the alphabets,numbers and special charecters
import re #reading multiple lines and comapring with needed one
from cryptography.fernet import Fernet # encryption
import getpass # reads the input from the user as Password
import os  #the listing of the related files on the disk.
import pathlib #various classes representing file system paths
import sys # to get search in for the required module
import time#return no. of second since last approch
import clipboard #automaticaly copies or remove files

s = os.getcwd()#return to the curreunt working file
path = s.replace('\\', '/')#will replace / by \\

class total_security:#class declared
    
    def __init__(self, name, general_password):#defining function which will ask intial username and password
        
        self.name = name#starting name
        self.general_password = general_password#password to acess that
        
    def login(self):#help identifing name and password used initially
        
        try:#exception handle for base class
            
            website = ''#variale website defined named website ehich is a empty string
        
            if(os.path.isfile(self.name +"/" +self.name + "_"+ website+ "secret.key")):#selecting the file that contain registed name and password and decripting done
            
                f = open(self.name +"/" +self.name + "secret.txt", "rt")#openinf the file which contain regester name and password
                message = f.read().rstrip('\n')#reading that file
                f.close()#closing that file
                password1 = self.decryption(message = message.encode(),website = website)#password that was saved in file is selected for comarision

                if(self.general_password == password1.decode()):#typed and saved are equal
                    print("Login successful")#msg printed
                    return True
                else:#if not true
                    print("Wrong password")#wrong password
                    return False
            else: 
                print("Not Registered. Kindly register first")#if typed name file is not present
                return False
        except:
            print("Unknown error contact admin")#if user type any this else can't be used so will come out of try function
    def register(self):#making regester function for intial log in
        
        website = ''
        try:
            #pathlib.Path('C:/Users/HP/opencv/Scripts/Password Manager/dist/PasswordManager/' + self.name).mkdir(parents=True, exist_ok=False)
            #pathlib.Path('C:/Users/'+ getpass.getuser() +'/PasswordM
            #anager/Scripts/PasswordManager/dist/PasswordManager/' + self.name).mkdir(parents=True, exist_ok=False)
            pathlib.Path( path +'/' + self.name).mkdir(parents=True, exist_ok=False)#making adress of file that will contain regeration passssword and name
            #pathlib.Path(path + '/' + self.name).mkdir(parents=True, exist_ok=False)
            self.encrypt_key(website)#encrypting it
            password = self.encryption(message = self.general_password, website = website)#mentioning password
            
            f = open(self.name +"/" +self.name + "secret.txt", "a")#tried to open the file
            f.write(password.decode())#written password mention without encryption
            f.close()#closing of file
            print("Thank you for registering \n Kindly login again to continue")
        
        except:
            print("username already exist or Wrong Directory")
        

    def save_password(self,website, email, password = "None"):     #delration of save passsword
        
        try:
            f = open(self.name +"/" +self.name + ".txt", "a")                           #opening a text file in which we want to save all inputs
            f.write(website + ';' + email + ";") #printing all those in it
            f.write(password.decode())#writing password without encryption
            f.write("\n")#next line
            f.close()  #closing text file
            print("Password saved successfully")#msg printed
        except: print("Error in saving password \n try again later")

    def genrate_password(self,password_length = 12):                    #declared genrate function
        
        try:
            words = string.ascii_letters + string.digits + string.punctuation#choosing random variables
            #password_length = int(input("what is the password length: "))#length of password we want
            empty_list = []                                       #list to save password after every circle of for loop
            for password in range(0, password_length):            #loop for making limit of length
                empty_list.append(random.choice(words))           #choosing random variable and putting it in list
                password = "".join(empty_list)                    #converting list into string
                #save_password = True                             #making it save
            return password
        except: print("Error in generating Passowrd. \n Kindly try again later")

    def search_password(self,website):#declaring search function
        
        try:

            pdata = []                                                             #empty list which get searched value
            pattern = re.compile(website, re.IGNORECASE)                         # Compile a case-insensitive regex
            with open (self.name +"/" +self.name + '.txt', 'rt') as myfile:    #opening the file from which we will search
                for line in myfile:                                            #starting loop for going through file
        .            if pattern.search(line) != None:                           # If a match is found
                        pdata.append(line.rstrip('\n').split(';'))              #changing line after ;
            return pdata        #returing required data
        except: return "Error in Searching"

    def save_website(self):                                                     #declaring save website

        try:

            wdata = []                                          #declared valiable

            with open (self.name +"/" +self.name + '.txt', 'rt') as f:#opening file for read
                wdata=[line.split(";")[0] for line in f]#spliting line into charecters and put in wdata

            return wdata#returning wdarta

        except:
            print("Kindly ignore if you are new user else contact Admin.")


    def delete_password(self,linenum):#for deleting some password set

        try:

            with open(self.name +"/" +self.name + '.txt', 'r') as read_file:#opening file as read file
                lines = read_file.readlines()#reading line by line

            currentline = 1#starting with line 1
            with open(self.name +"/" +self.name + '.txt', 'w') as write_file:#opening the file
                for line in lines:#opening loop
                    if(currentline == linenum):#if line number matches so it will pass that line so that will be deleted
                        pass
                    else:
                        write_file.write(line)#as it is

                    currentline +=1#current line number will increase by 1
            print("Password Deleted successfully")
            #os.remove(self.name +"/" +self.name + "_"+ website+ "secret.key")
        except:
            print("Erorr in deleting. Contact Admin")


    
    def encrypt_key(self,website):#making encryption key
        
        key = Fernet.generate_key() #fernet will genrate a key
        with open(self.name +"/" +self.name + "_"+ website+ "secret.key", "wb") as key_file:#opening the file with secret key for writing
            key_file.write(key)#writing key in that file
    
    def load_key(self, website):
        if(os.path.isfile(self.name +"/" +self.name + "_"+ website+ "secret.key")):#loading the file is key  is correct
            
            return open(self.name +"/" +self.name + "_"+ website+ "secret.key", "rb").read()#opening file
        else: 
            print("File not found")#else error
            quit(abs)
    
    def encryption(self,message,website):#encrypting the text
        
        key = self.load_key(website)#opening the file for loading fernet
        encoded_message = message.encode()#specifing encoding
        f = Fernet(key)#called key for encryption
        encMessage = f.encrypt(encoded_message)#encryption done
        
        return encMessage#returning after encrypted done
    
    def decryption(self,message,website):#calling for decryption
        
        key = self.load_key(website)#opening the file loading fernet again
        f = Fernet(key)#called key for decryption
        decMessage = f.decrypt(message)#decryption done
        
        return decMessage#returning after decrypted done
    
        


if __name__ == "__main__": #intiating main function
    
    while (1):#staring while loop so that run alteast once if started
        try:
            print("\n Welcome to your Personal Password Manager \n \n")
            print("Enter Login Details or Press ctrl-C to exit")
            p1 = total_security(name = input("Enter Username: "),general_password = getpass.getpass('Password:'))#called total sequirty function
            if(not p1.login()):#if login function condition doesnot able to work
                print("Options: \n 1. Login \n 2. Register \n ")#asking for new registration and retry of login
                argument = int(input("Enter choice number: "))#asking foe choice

                if argument == 1:#if said login so will retry for logging in

                    continue#?

                elif argument == 2:#for new registration

                    name = input("Username: ")#entering name
                    user_password = getpass.getpass('Password: ')#entering password
                    user_repeat_password = getpass.getpass('Repeat Password: ')#repeting password
                    if user_password == user_repeat_password:#if both matched then go forward
                        p2 = total_security(name, user_password)#making variable which will be able to be in our class
                        p2.register()#using register function
                    else:
                        print("Password not matched. Kindly try again")
                    continue#ignore and move forward

                else:
                    print("Wrong choice. \n Program Exiting")
                    break


        except:
                print("Unknown Error. Contact Admin")
                break

        while (1):

            print("Options: \n 1. save password \n 2. Generate password \n 3. Search Password \n 4. Delete Password \n Press 5 to log out")
    
            argument = int(input("Enter choice number: "))
    

            if argument == 1:#if pressed 1 save password
                web = input(" unique website/source name : ") #site we want to save
                wdata = p1.save_website()#defining variable for every saved web to save website function

                if(wdata != None):#checking if website is not repeating
                    for data in wdata:#starting loop which contain all the websites
                        if data == web:#if enter web maches with already existing
                            print("website already exist. Modifying name automatically")#then it will modify the name by its own
                            web = web + "1"#for changing name
                            break
                mail = input("email/username : ")                              #mail we want save
                pas = getpass.getpass('Password :')                         #password we want to save
                p1.encrypt_key(web + mail[1:5])#making enkrypt key for mail and web
                password1 = p1.encryption(message = pas, website = web + mail[1:5])#encryption done
                p1.save_password(website = web,email = mail,password = password1)#saved password set

            elif argument == 2:#for genrating password
                password_length = int(input("Select password length: "))#length of password we want
                password = p1.genrate_password(password_length)#genrating password
                print("password:",password)#printing made password
                save_generated_password = input("Press 1 to save this password and press 0 to exit")#asking for saving it
                if(save_generated_password =="1"):
                
                    web = input("unique website/source name: ")#site we want to save
                    wdata = p1.save_website()#same as done above

                    if(wdata != None):

                        for data in wdata:

                            if data == web:
                                print("website already exist. Modifying name automatically")
                                web = web + "1"
                                break

                    mail = input("email/username : ")                          #mail we want save
                    p1.encrypt_key(website = web+ mail[1:5])
                    password1 = p1.encryption(message = password, website = web+ mail[1:5])
                    p1.save_password(website = web,email = mail,password = password1)
        
                else:
                    print("Password generated successfully but not saved")
                
            elif argument == 3:#for searching password

                wdata = p1.save_website()#using save website to get info of all websites
                for count,data in enumerate(wdata):#showing website with counting
                    print(count+1, ":", data)#increasing counting by 1

                inp = int(input("Enter number for which website you want a Password: "))#asking for for which site u want

                data1 = []#made a list for found paswword set
                
                try:
                    web = wdata[inp-1]#adress of it
                    print(web)#print that web
                except: 
                    print("Please enter the correct option")
                    continue

                data = p1.search_password(website = web)#got that website which we want to search
            
                if data != data1:#if searched web not
                    for num,item in enumerate(data):
                        #print(data) #optional- for testing purpose only
                        print("\n \n ")
                        print("Entry:", num+1)
                        print("website:",item[0])
                        print("email:", item[1])
                        mail = item[1]
                        decrypt_pass = item[2].encode()
                        password = p1.decryption(message = decrypt_pass, website = item[0] + mail[1:5]).decode()
                        clipboard.copy(password)
                        print("Passowrd copied to clipboard")

                        if(input("Press 1 to see password") == '1'):

                            print("password:",password,end='')
                            sys.stdout.flush()
                            time.sleep(2)
                            print("\r password:",''.join('#' for i in range(len(password))))

                        print("\n \n ")
                else:
                    print("Details not found")

            elif argument ==4:#for deleting website

                wdata = p1.save_website()#opening list of website
                for count,data in enumerate(wdata):#putting counting on start
                    print(count+1, ":", data)

                inp = int(input("Enter number for which website you want to delete entry: "))#website no. added

                p1.delete_password(inp) #called delete password function
            
            elif argument == 5:#for exit
                if(input("Do you really want to log out?[y/n]") == "y"):#asking yes or no
                    print("Log out Successful")# exited succsessfully
                    break
            else:
                print("wrong entry")#any thing else done then wrong password
                