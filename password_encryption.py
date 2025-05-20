import typer
from cryptography.fernet import Fernet

partition = "-"*100

def main(password: str = typer.Argument("1234", help="password to encrypt")):
    print(partition)

    encpassword, passkey = _encrypt(password)
    typer.echo(f"Your encrypted password is {encpassword}")

    decrypt = typer.confirm("Would you like to decode your password ?")
    if decrypt :
        _decrypt(encpassword, passkey)
        decpassword = passkey.decrypt(encpassword).decode()
        typer.echo(f"Your original password was: {decpassword}")

    print(partition)

         


def _encrypt(password):
    key = Fernet.generate_key()
    passkey = Fernet(key)
    encpassword = passkey.encrypt(password.encode())

    return encpassword, passkey


def _decrypt(encpassword, fernet):
    decpassword = fernet.decrypt(encpassword).decode()

    return decpassword

if __name__ == "__main__":
    typer.run(main)