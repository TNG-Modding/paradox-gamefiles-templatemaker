import click
from intemplator import templateProcessor

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
    templateProcessor.processOrder(template, input, output, isBom)

@cli.command()
def go():
    """Process the orders.json file here."""
    print("The Intemplator issues their orders!\n")
    templateProcessor.processOrders()

@cli.group()
def create():
    """Create Content."""
    pass

@cli.command()
def init():
    """Initialize a Project"""
    templateProcessor.setup()

@create.command()
@click.option('--name', prompt='Display Name', required=True, help='The name of the resource.')
def resource(name):
    """Create a Resource"""
    templateProcessor.createNewOrder(name, "RESOURCE")

@create.command()
@click.option('--name', prompt='Display Name', required=True, help='The name of the resource.')
def event(name):
    """Create an Event"""
    templateProcessor.createNewOrder(name, "EVENT")