# Password Manager

A password manager simulation.
- check a password's strength
- encrypt it 
- store it 


## Password Strength Checker

This is a password strength checker. 
This command line application is part of a password manager simulation project 

It rates the password's security level based on these criterias :
- WEAK: contains digits only or contains less than 8 characters
- FAIR: contains between 8 and 12 characters, at most 50% of the password is digits
- STRONG: contains more than 12 characters, at most 40% of the password is digits, contains at least on special character

If the password is not at the most secure level, it can make suggestions 


## Password Encryption 

This programm uses the cryptography library and the Fernet class to encrypt and decrypt a password.
