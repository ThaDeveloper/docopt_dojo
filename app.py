
"""
This is Dojo!
Usage:
    create_room (L|O) <room_name>...
<<<<<<< 058f5058da19486feb7de360e0899791ba41ddb8
    add_person <first_name> <last_name> <role> [<accomodate>]
=======
    add_person <first_name> <last_name> <role> [--accomodate=N]
>>>>>>> [Fix] Syntax error
    (-i | --interactive)
Options:
    -h --help     Show this screen.
    -v --version
"""
import os
import click
import cmd
from docopt import docopt, DocoptExit
#from ui import enter_dojo, exit_bar
from dojo import Dojo


dojo = Dojo()


def parse(func):
    """
    Essentially a decorator that simplifies the try/except block relays result
    of the docopt parsing to the called action.
    i.e @args_cmd thereafter.
    """

    def fn(self, arg):
        try:
            opt = docopt(fn.__doc__, arg)

        except DocoptExit as e:
            # Throws an Invalid Command message when arguments
            # do not match what is outlined in the __doc__ string.
            msg = 'Invalid Command'
            print(msg)
            print(e)
            return

        except SystemExit:
            # Show help
            return

        return func(self, opt)

    fn.__name__ = func.__name__
    fn.__doc__ = func.__doc__
    fn.__dict__.update(func.__dict__)
    return fn


def start():

    #enter_dojo()
    arguments = __doc__
    print(arguments)


dojo = Dojo()


class Interactive_Dojo(cmd.Cmd):

<<<<<<< 058f5058da19486feb7de360e0899791ba41ddb8
    prompt = '(Dojo)===> '
=======
    prompt = '(dojo)===> '
>>>>>>> [Fix] Syntax error

    @parse
    def do_create_room(self, args):
        """
        Usage: create_room <room_type> <room_name>...
        """
        try:
            for r in args['<room_name>']:
                dojo.create_room(args['<room_type>'], r)
        except Exception:
            msg = 'Oops!An error occurred in running'
            msg += ' the command. Please try again.'
            click.secho(msg, fg='red', bold=True)

    @parse
    def do_add_person(self, args):
<<<<<<< 058f5058da19486feb7de360e0899791ba41ddb8
        """Usage: add_person <first_name> <last_name> <role> [<accomodate>] """
        if args['<accomodate>'] is None:
            args['<accomodate>'] = 'N'

        try:
            validated_details = dojo.validate_person(args['<first_name>'],
                                                      args['<last_name>'],
                                                      args['<role>'],
                                                      args['<accomodate>'])
=======
        """Usage: add_person <first_name> <other_name> <role> [--accomodate=N] """
        if args['--accomodate'] is None:
            args['--accomodate'] = 'N'

        try:
            validated_details = dojo.validate_person(args['<first_name>'],
                                                      args['<other_name>'],
                                                      args['<role>'],
                                                      args['--accomodate'])
>>>>>>> [Fix] Syntax error
            if isinstance(validated_details, list):
                person = dojo.generate_identifier(validated_details)
                dojo.allocate_room(person)
        except Exception as e:
            print(e)
            msg = 'Oops!An error occurred in running'
            msg += ' the command. Please try again.'
            click.secho(msg, fg='red', bold=True)

    def do_exit(self, arg):
        """Quits out of Interactive Mode."""
        print('Good Bye!')
        exit()
if __name__=="__main__":
    print(__doc__)
    Interactive_Dojo().cmdloop()