import click

filename = "compras.txt"

@click.command()
def hello():
    click.echo("Hello", color=True)

@click.command()
@click.argument("Product")
def add(product:str):
    breakpoint
    with open(filename, "a") as file:
        file.write(f"{product}\n")

if __name__ == "__main__":
    hello()