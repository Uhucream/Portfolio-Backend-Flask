import click
from flask.cli import AppGroup, with_appcontext
from models import User
from database import db

user_cli = AppGroup('user')

@user_cli.command('create')
@with_appcontext
def create_user():
    user_name = click.prompt('Please input user name', type=str)
    user_email = click.prompt('Please input email', type=str)
    user_password = click.prompt('Please input password', hide_input=True, value_proc=password_confirmation)

    user_record = User(name=user_name, email=user_email, password=user_password)
    db.session.add(user_record)
    db.session.commit()

    click.echo('Done.')

def password_confirmation(pwd):
    confirmation_password = click.prompt('Please input password again', hide_input=True, type=str)
    if confirmation_password != pwd:
      raise click.BadParameter('Passwords doesn\'t match. Please input again\n', param=pwd)
    else:
      return pwd
