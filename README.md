# Password Manager

A command line application password manager simulation.

## commands are:

### save
### get password
### delete 
### delete all 

## Most basic features 
[x] can encrypt a password using the most basic encryption 
[x] can save an encrypted password
[ ] can retrieve and decryt a saved password
[ ] can delete a password in particular
[ ] can delete all passwords

## More features

[x] can tell a password's strength and prevent a user from using a weak password
[] can generate passwords for the user 
[] storing the password elsewhere ?
[] more sophisticated encryption 


## Currently known bugs
[] if two passwords have the same save name, the first will me overwritten by the second

## save command
This command follows multiple steps :

- The app asks the user for : the password name, the password itself and the password key
- The password's strength is assessed, if it is deemed too vulnerable, the user will be made aware of it
- The password is encrypted using a ceasar cipher like function called _encryption, it uses an interger key to shift the characters ord
- The name, key and encrypted password are stored in a json file

## get password
WIP
Idea is to ask the user for the password's name, find it in the json file, retrieve encrypted password and key and decrypt it (using _decrypt function which is oposite of _encrypt)

## delete
WIP
Idea is to ask for the password's name, find it in the json file and the lazy idea would be to just make an empty password with the same name (bad idea, i'm going to fix this issue), the better idea would be to erase the information related.

## delete all
WIP
Idea would be to basicly overwrite the whole json file with empty data

