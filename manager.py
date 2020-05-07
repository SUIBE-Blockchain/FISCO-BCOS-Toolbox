  
from fisco_bcos_toolbox import create_app
from fisco_bcos_toolbox.extensions import db
from fisco_bcos_toolbox.models import User

from flask_script import Manager, Server, Shell
import click
app = create_app()

banner = r"""
 ______     ________      ______       ______       ______          _______       ______       ______       ______      
/_____/\   /_______/\    /_____/\     /_____/\     /_____/\       /_______/\     /_____/\     /_____/\     /_____/\     
\::::_\/_  \__.::._\/    \::::_\/_    \:::__\/     \:::_ \ \      \::: _  \ \    \:::__\/     \:::_ \ \    \::::_\/_    
 \:\/___/\    \::\ \      \:\/___/\    \:\ \  __    \:\ \ \ \      \::(_)  \/_    \:\ \  __    \:\ \ \ \    \:\/___/\   
  \:::._\/    _\::\ \__    \_::._\:\    \:\ \/_/\    \:\ \ \ \      \::  _  \ \    \:\ \/_/\    \:\ \ \ \    \_::._\:\  
   \:\ \     /__\::\__/\     /____\:\    \:\_\ \ \    \:\_\ \ \      \::(_)  \ \    \:\_\ \ \    \:\_\ \ \     /____\:\ 
    \_\/     \________\/     \_____\/     \_____\/     \_____\/       \_______\/     \_____\/     \_____\/     \_____\/ 
                
"""

manager = Manager(app)


def make_shell_context():
    return {
        "app": app,
    }

manager.add_command("runserver", Server(host="0.0.0.0", port=5000, use_debugger=True))
manager.add_command("shell", Shell(banner=banner, make_context=make_shell_context))


@manager.command
def reset_db():
    """Initialize the database."""
        
    click.confirm('This operation will delete the database, do you want to continue?', abort=True)
    db.drop_all()
    click.echo('Drop tables.')
    db.create_all()
    click.echo('Initialized database.')
    admin = User(
        username='admin',
        email='admin@admin.com',
        is_admin=True,
        active=True,
    )
    admin.set_password('admin')
    db.session.add(admin)
    db.session.commit()
    click.echo('Success Add Admin Count.')

@manager.command
def init_db():
    db.create_all()
    click.echo('Initialized database.')
    admin = User(
        username='admin',
        email='admin@admin.com',
        is_admin=True,
        active=True,
    )
    admin.set_password('admin')
    db.session.add(admin)
    db.session.commit()
    click.echo('Success Add Admin Count.')

@manager.command
def set_user(username, email, password, active=True):
    """Add A New User."""
    if User.query.filter(User.username==username).first() and User.query.filter(User.email==email).first() and active:
        user = User.query.filter(User.username==username).first()
        user.active = True
        click.echo('Success Update A New User to Active')
    else:
        user = User(username=username, email=email, active=active, id=None)
        # add a User(active = False)
        user.set_password(password)
        user.set_password(password)
        db.session.add(user)
        db.session.commit(user)
        click.echo("Success Add A New Active User.")

if __name__ == "__main__":
    manager.run()