import click
from .lib import templateProcessor as templatorProcessor

@click.group()
def cli():
    """Intemplator CLI"""
    pass

@cli.command()
@click.option('--template', prompt='Template name', help='The name of the template used.')
@click.option('--input', prompt='Input filepath', help='The filepath of the json file of the service.')
@click.option('--output', prompt='Output path', help='The path of where the templated service will go.')
def run(template, input, output):
    """Produces a set of files based on a template and input file."""
    print("Create template")
    # ProcessTemplate(template, input, output)

if __name__ == '__main__':
    cli()