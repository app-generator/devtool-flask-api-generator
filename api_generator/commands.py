import click
import api_generator.manager as manager
from flask.cli import with_appcontext


@click.command(name="gen_api")
@with_appcontext
def gen_api():
    try:
        manager.generate_forms_file()
        manager.generate_routes_file()
        print("APIs have been generated successfully.")
    except Exception as e:
        print(f"Generation API failed because: {str(e)}")
