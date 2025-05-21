def _encyrpt(password: str, key: int) -> tuple[str, int]:
    """
    Basic, ceasar cipher like encrypt function

    Args:
        password: password you wish to encrypt
        key: the key to encrypt and decrypt the password (shifts the characters)

    Returns:
        encpassword: your now encrypted password
        key: the key to encrypt and decrypt the password
    """
    encpassword = ""
    for character in password:
        enccharacter = chr(ord(character)+key)
        encpassword = encpassword + enccharacter
    
    return encpassword, key

def _decrypt(encpassword: str, key: int) -> str:
    """
    Basic, ceasar cipher like decrypt function 

    Args:
        encpassword: the returned password of the _encrypt function
        key: the returned key of the _encrypt function

    Returns:
        decpassword: your original password
    """
    decpassword = ""
    for character in encpassword:
        deccharacter = chr(ord(character) - key)
        decpassword = decpassword + deccharacter
    
    return decpassword

secret, key = _encyrpt("banana", 2)
print(secret)
print(_decrypt(secret, key))
