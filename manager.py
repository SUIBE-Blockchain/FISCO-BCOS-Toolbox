  
from fisco_bcos_toolbox import create_app
from fisco_bcos_toolbox.extensions import db
from fisco_bcos_toolbox.models import User

from flask_script import Manager, Server, Shell
import click
app = create_app()

banner = r"""
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
    User.create(
        username='admin',
        email='admin@admin.com',
        password='admin',
        active=True,
    )
    db.session.add(admin)
    db.session.commit()
    click.echo('Success Add Admin Count.')

@manager.command
def init_db():
    db.create_all()
    click.echo('Initialized database.')
    User.create(
        username='admin',
        email='admin@admin.com',
        password='admin',
        active=True,
    )
    db.session.add(admin)
    db.session.commit()
    click.echo('Success Add Admin Count.')

@manager.command
def set_user(username, email, password):
    """Add A New User."""
    pass


if __name__ == "__main__":
    manager.run()