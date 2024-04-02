import click

@click.command()
def hello():
    click.echo("Hello", color=True)

if __name__ == "__main__":
    hello()