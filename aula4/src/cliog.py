import click

todo_list = []

@click.group()
def cli():
    pass

@cli.command()
@click.argument('item')
def add(item):
    """Add a new item to the To-Do list."""
    todo_list.append(item)
    click.echo(f"Item added: {item}")

@cli.command()
@click.argument('index', type=int)
def remove(index):
    """Remove an item from the To-Do list by its index."""
    try:
        if 0 <= index - 1 < len(todo_list):
            removed_item = todo_list.pop(index - 1)
            click.echo(f"Removed item: {removed_item}")
        else:
            click.echo("Invalid item number.")
    except ValueError:
        click.echo("Please enter a valid number.")

@cli.command()
def view():
    """View all items in the To-Do list."""
    if not todo_list:
        click.echo("The To-Do list is empty.")
    else:
        for index, item in enumerate(todo_list, start=1):
            click.echo(f"{index}. {item}")

@cli.command()
def export():
    """Export the To-Do list to a .txt file."""
    with open('todo_list.txt', 'w') as file:
        for item in todo_list:
            file.write(f"{item}\n")
    click.echo("To-Do list exported to todo_list.txt.")

if __name__ == "__main__":
    cli()
 