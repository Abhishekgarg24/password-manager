# Password-manager
save your passwords with encryption



## Introduction
password manager is the application which will be very useful because in this modern life we have myltiple accounts on multiple website and every account have differnt user names and diffent passwords. its very tough to meomorise all of them so we made this project will will save your password , id , websites with encryption

We had not linked this with internet because there is a high probability of breeching of our passwords so to get rid from that we made it personal for every pc and we can alse save in perdrive which will be highly secured
## Installation
For running this program we will alot of directories or liberaries. Some of them are as follows
* py installer
* cryptography
* clipboard
### py installer
Py installer is very useful for our program by this we will be able give the path of code to a image by which our our image will convert into the application . which will be very easy  to use


![im](https://user-images.githubusercontent.com/79128626/129908587-843d8adc-2099-4999-b752-af4a3476b6a2.jpg)

### cryptography
cryptography is the library which is used for encrypting our file . we are using fernet from this library which is very save and can't be cracked by any one . so it will make our program safe and secure
### clipboard
clipboard help to automate some specific function lijke opening or creating file which make this project very exciting and useful.
![2021-08-17 (3)](https://user-images.githubusercontent.com/79128626/129910813-38a2bff6-71ba-44b2-8178-5a3f494ae12e.png)

## Functions
* init function
* login function
* register function
* save password function
* genrate password function
* search password function
* save website function
* delete password function
* encrypt key function
* load key  function
* encryption function
* decryption function

### init
This function made for storing the initial username and password into some variables which will be further used for entering in the program
![2021-08-17 (5)](https://user-images.githubusercontent.com/79128626/129912431-baf5bb09-4302-48e1-8683-2cda1b9e76fc.png)

### login function
This function is used for checking the registered record and matching it with username and password inputed , If it find some match then program  will run if not then move for further steps.
![login](https://user-images.githubusercontent.com/79128626/130022062-d3f0fecd-fb66-4bc8-b068-158fa22ef471.png)


### register function
This function is for resgistering new user. This function registers for new user and a confirmed password .which will be  save by computer with safe encryption
![register](https://user-images.githubusercontent.com/79128626/130022127-ef6f833c-67ca-469b-8935-7357b3bc428b.png)


### save password function
This function will ask for new website , mail , password which will be saved in a notepad named by your register user name with encryption ,one benefit is that there is no limit of entries in it, So we can save many more websites, passwords, mail .
![save pass](https://user-images.githubusercontent.com/79128626/130021392-f0bdbb50-9814-4f17-96e9-305c8177cfb9.png)


### genrate password function
This function will help us for genrating a random password which will consist alphabets , numbers and even special chracters by just asking the length we want to keep for password.
![genrate](https://user-images.githubusercontent.com/79128626/130021435-4fc94e7b-b336-4fe1-b284-e1674e7bae7f.png)


### search password function
This feature of program is very useful because it makes this project very heelpful and handy .We all know that we need one password at a time so this function just ask that site site and returns password of that site.
![search](https://user-images.githubusercontent.com/79128626/130021489-c9fc53f5-e3d7-4ae0-acac-7dc787f24e79.png)


### save website function
This function creates the list of websites saved by the user . This function just takes the site saved in notepad and makes the list for several options 
![save site](https://user-images.githubusercontent.com/79128626/130021554-695bdd0b-e342-4ca1-ab83-5e34f2409e6b.png)


### delete password function
This function use save website function and put numbering on it then ask for the number which site we want delete . That site password set will be deleted from everywhere in the program
![delete](https://user-images.githubusercontent.com/79128626/130021603-1fe87df2-f9b3-475b-abab-7a0f09975baa.png)


### encrypt key function
This function creates a key for for encryption which will lead us to encrypting set up.
![2021-08-19 (5)](https://user-images.githubusercontent.com/79128626/130021709-3d4e62f6-a475-4666-b86d-85a22fd0ddc9.png)


### load key function
This function will check the path of file if path is correct then erypting will go further for encrypting.
![2021-08-19 (6)](https://user-images.githubusercontent.com/79128626/130022289-ea58efd1-6334-45dc-aa7c-59488c223c3a.png)


### encryption function
This function will encrypt every thing using fernet which will assure us that no second person can breach or data and our data is safely handled.
![2021-08-19 (7)](https://user-images.githubusercontent.com/79128626/130022311-1a8b4d19-6cf3-40e3-883e-4b3cf51e5e7a.png)


### decryption function
This function is used for decrypting the file when ever needed.
![2021-08-19 (8)](https://user-images.githubusercontent.com/79128626/130022333-d94df514-edc6-45c1-9a4a-f148d7cb9b0e.png)


## MAIN body the program
This function firstly ask us for the user name and password using init function . if typed user id and password is incorrect then it will ask for new registraion and retry using login function then if we ask for register then function will register new user but if we choose retry then will go back login again.one thing more after registration also function send you login
Now our is succussfully done from feature of the function start
it will ask for 
1. save password
2. genrate password
3. search password
4. delete password
5. exit

* If we press 1 the function ask website, email , password for input then it will savee password function save that set to text file
* If we press 2 the function will ask for length of password and the send to genrate password function which make a password consist of alphabets,numerics, special charcter of given lenth and returns it then it will ask for saving if want to save then press 1 if not press 2
* If we press 3 the function will start by making a list of website user by user using save website function then put numbering on that list and ask for which website we are finding password then by using search password function we will get password of that websie
* If we press 4 the function will start by making a list of website user by user using save website function then put numbering on that list and ask for which website password  and mail set we want to delete which will done by delete password function
* If we press 5 we will be out of the loop
 ![2021-08-19 (16)](https://user-images.githubusercontent.com/79128626/130023242-1f51e225-9c6e-41f4-bb96-d75d6a678dc7.png)
![2021-08-19 (17)](https://user-images.githubusercontent.com/79128626/130023254-814fceca-59cd-4925-9dbb-511daf55b447.png)
![2021-08-19 (18)](https://user-images.githubusercontent.com/79128626/130023260-d5117efa-b559-4ca0-adc7-010de9c0d14f.png)
![2021-08-19 (19)](https://user-images.githubusercontent.com/79128626/130023265-0988225f-0876-4cf9-942c-060f3e254c89.png)
![2021-08-19 (20)](https://user-images.githubusercontent.com/79128626/130023269-ddad4bcc-d402-4577-bb51-007b5c851354.png)
![2021-08-19 (21)](https://user-images.githubusercontent.com/79128626/130023271-86a93636-ce0e-494f-a418-29dcf164a444.png)
