import click
from .lib import templateProcessor as operations

@click.group()
def cli():
    """Intemplator CLI"""
    pass

@cli.command()
@click.option('--template', prompt='Template name', help='The name of the template used.')
@click.option('--input', prompt='Input filepath', help='The filepath of the json file of the service.')
@click.option('--output', prompt='Output path', help='The path of where the templated service will go.')
@click.option('--bom', prompt='Output bom?', help='Whether we prepend \ ufeff to our file to indicate utf8-BOM.')
def run(template, input, output, isBom):
    """Produces a set of files based on a template and input file."""
    print("The Intemplator issues an order!\n")
    operations.ProcessOrder(template, input, output, isBom)

@cli.command()
def go():
    """Process the intemplator.json file here."""
    print("The Intemplator issues their orders!\n")
    operations.ProcessOrders()

if __name__ == '__main__':
    cli()