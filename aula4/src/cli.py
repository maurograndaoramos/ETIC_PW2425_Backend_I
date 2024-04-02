import click

@click.group
def cli():
    pass

@cli.command()
def show():
    pass

@cli.command()
@click.argument("name")
def add(name:str):
    # cria um ficheiro de texto e adiciona o que foi escrito 
    # no argumento 'name' para dentro do ficheiro
    # NOTA: caso o ficheiro exista acresenta 
    pass


if __name__ == "__main__":
    cli()
