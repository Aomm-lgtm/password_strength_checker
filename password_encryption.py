import random 
import string


def _make_key() -> int:
    """
    uses random and string modules to generate a random string (8 to 12 characters long) to be used in _encryption function as a key

    Returns:
        key: the key that will be used to encryot
    """

    length = random.randint(8, 12)
    key = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
    int_key = ""
    for character in key:
        int_key += str(ord(character))

    int_key = int(int_key)%255
    return int_key
        

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

secret, key = _encyrpt("banana", _make_key())
print(secret)
print(_decrypt(secret, key))