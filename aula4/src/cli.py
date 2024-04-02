import click

TODO_FILE = 'todo_list.txt'
todo_list = []

def load_todo_list():
    """Load the To-Do list from a file."""
    try:
        with open(TODO_FILE, 'r') as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        return []

def save_todo_list():
    """Save the To-Do list to a file."""
    with open(TODO_FILE, 'w') as file:
        for item in todo_list:
            file.write(f"{item}\n")

@click.group()
def cli():
    global todo_list
    todo_list = load_todo_list()

@cli.command()
@click.argument('item')
def add(item):
    """Add a new item to the To-Do list."""
    todo_list.append(item)
    save_todo_list()
    click.echo(f"Item added: {item}")

@cli.command()
@click.argument('index', type=int)
def remove(index):
    """Remove an item from the To-Do list by its index."""
    try:
        if 0 <= index - 1 < len(todo_list):
            removed_item = todo_list.pop(index - 1)
            save_todo_list()
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
    save_todo_list()
    click.echo("To-Do list saved.")

if __name__ == "__main__":
    cli()
