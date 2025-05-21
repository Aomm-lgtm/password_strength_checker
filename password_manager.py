import json
from json import JSONEncoder

from cryptography.fernet import Fernet 
import typer
import rich 



partition = "-"*100

strength_style = {
    "STRONG": "[bold green]STRONG[/bold green]",
    "FAIR": "[bold yellow]FAIR[/bold yellow]",
    "WEAK": "[bold red]WEAK[/bold red]",
}

app = typer.Typer()


class PasswordEncoder(JSONEncoder):
        def default(self, o):
            return o.__dict__

@app.command("save")
def save():

    save_name = typer.prompt("Please enter a save name to be associated to your password")
    key = typer.prompt("Please enter your decryption key")
    while True:
        password = typer.prompt("Please enter your password")
        strength = _check_strength(password)
        if strength != "STRONG" and typer.confirm("Your password is vulnerable. Are you sure you wish to use it?"):
    
            password = _encrypt(password, int(key))
            with open('passwords.json', 'r') as f:
                data = json.load(f)

                data[save_name] = {
                "save name": save_name,
                "key": key,
                "password": password[0]
                }

            with open('passwords.json', 'w') as f:
                json.dump(data, f, indent=6)
    
            break

            

@app.command("get_password")
def get_password():
    password_to_get = typer.prompt("What password do you want to see?")

    with open('passwords.json', "r") as f:
        data = json.load(f)
        if password_to_get in data:
            encpassword = data[password_to_get]["password"]
            key = data[password_to_get]["key"]

            password = _decrypt(encpassword, int(key))
            typer.echo(f"The password is: {password}")

@app.command("delete")
def delete():
    password_to_delete = typer.prompt("What password do you want to delete?")

    with open('passwords.json', "r") as f:
        data = json.load(f)
        if password_to_delete in data:
            data.pop(password_to_delete)

            with open('passwords.json', "w") as f:
                json.dump(data, f, indent=6)
    
            typer.echo(f"Password: '{password_to_delete}' deleted")

    typer.echo("No passwords are saved under this name")
        


@app.command("delete_all")
def delete_all():
    if typer.confirm("Are you sure you wish to delete all your saved passwords?"):

        with open('passwords.json',"w") as f:
            json.dump({}, f)

            typer.echo("All your passwords have been deleted")

    typer.echo("Your passwords will not be deleted")

def main(password: str = typer.Argument("1234", help="Password to assess" ),
         check_strength: str = typer.Option(),
         save = typer.Option(),
         get_password: str = typer.Option(),
         ):
    pass














def _check_strength(password: str) -> str:
    """
    checks your passwords strength and assigns a level to it (WEAK, FAIR, STRONG)

    Args:
        password: the password you want to be assessed

    Returns:
        strength: your password strength, can either be WEAK, FAIR or STRONG.
    """

    if password.isdigit() or len(password) < 8:
        return "WEAK"
    elif 8<= len(password) <= 12:
        if _get_digit_percentage(password) > 0.5:
            return "WEAK"
        else:
            return "FAIR"
    elif _get_digit_percentage(password) <= 0.4 and _is_special_character(password):
        return "STRONG"
    else:
        return "FAIR"

def _get_digit_percentage(password: str) -> float:
    """
    counts the number of digits in your password and returns 

    Args:
        password: the password you want to be assessed

    Returns:
        digit_percentage: the ratio of digits over the total number of characters in your password
    """
    digit = 0
    for character in password:
        if character.isdigit():
            digit += 1
  
    digit_percentage = digit/len(password)
    return digit_percentage


def _is_special_character(password: str) -> bool :
    """
    checks if the password contains at leats one special character

    Args:
        password: the password you want to be assessed

    Returns:
        bool: True if there is at least one special character, False otherwise
    """
    special_characters = "!@#$%^&*()-+?_=,<>;:/"
    for character in password:
        if character in special_characters:
            return True
    return False

def _encrypt(password: str, key: int):
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
        enccharacter = chr(ord(character) + key)
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


if __name__ == "__main__":
    app()
