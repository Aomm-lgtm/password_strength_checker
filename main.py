import typer
from rich import print
from rich.text import Text


partion = "-"*100


def main(password: str = typer.Argument("1234", help="Password to assess" )):
    """
    Assesses your password's strength and makes suggestions if necessary. It is suggested to put de password between quotes, especially if it contains special characters
    """

    print(partion)
    strength = _style_strength(password)
    
    password_text = Text(password)
    password_text.stylize("bold blue")

    print("Your password is: ", end="")
    print(password_text)
    print("Your password's strength is: ", end="")
    print(strength)



    # print(f"Your password is: {password_text}. Your password's strength is {strength}")  
    # if strength == "WEAK" or strength == "FAIR":
    #    typer.confirm


def _check_strength(password: str) -> str:
    """
    checks your passwords strength and assigns a level to it (WEAK, FAIR, STRONG)

    Args:
        password: the password you want to be assessed

    Returns:
        strength: your password strength, can either be WEAK, FAIR or STRONG. The minimum requirements for each strength are: 
        - WEAK: contains digits only or contains less than 8 characters
        - FAIR: contains between 8 and 12 characters, at most 50% of the password is digits
        - STRONG: contains more than 12 characters, at most 40% of the password is digits, contains at least on special character
        
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
    

def _style_strength(password: str) -> str:
    """
    Takes the password's strength and assigns a particular style to it

    Args:
        password: your password
    Returns:
        strength: your password strength (determined by _check_strength function) in a particular style
    """
    strength = _check_strength(password)

    if strength == "WEAK":
        strength = "[bold red]WEAK[/bold red]"
    elif strength == "FAIR":
        strength = "[bold yellow]FAIR[/bold yellow]"
    else:
        strength = "[bold green]STRONG[/bold green]"

    return strength

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
        bool: if there is at least one special character, True will be returned, if not then False will be returned
    """
    special_characters = "!@#$%^&*()-+?_=,<>;:/"
    for character in password:
        if character in special_characters:
            return True
    return False
    
if __name__ == "__main__":
    typer.run(main)