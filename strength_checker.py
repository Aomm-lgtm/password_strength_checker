import typer
from rich import print
from rich.text import Text


partition = "-"*100

strength_style = {
    "STRONG": "[bold green]STRONG[/bold green]",
    "FAIR": "[bold yellow]FAIR[/bold yellow]",
    "WEAK": "[bold red]WEAK[/bold red]",
}

def main(password: str = typer.Argument("1234", help="Password to assess" )):
    """
    Assesses your password's strength and makes suggestions if necessary. It is suggested to put the password between quotes, especially if it contains special characters
    """

    print(partition)
    strength = _check_strength(password)
    
    password_text = Text(password)
    password_text.stylize("bold blue")

    print(f"\nYour password is: ", end="")
    print(password_text)
    print(f"Your password's strength is: {strength_style[strength]} \n")

    if strength == "WEAK" or strength == "FAIR":
        typer.echo("Here is how your password could be improved : \n"
        "- be sure that less than half of your password is composed of intergers\n" \
        "- add special characters\n" \
        "- make sure your password is at least 13 characters long\n")
    
    else:
        typer.echo("Congratulations! You have a strong password!")

    print(partition)


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
        bool: if there is at least one special character, True will be returned, if not then False will be returned
    """
    special_characters = "!@#$%^&*()-+?_=,<>;:/"
    for character in password:
        if character in special_characters:
            return True
    return False
    
if __name__ == "__main__":
    typer.run(main)