
"""
This is Dojo!
Usage:
    create_room (L|O) <room_name>...
    add_person <first_name> <last_name> <role> [<accomodate>]
    print_room <room_name>
    print_allocations [--o=filename]
    print_unallocated [--o=filename]
    reallocate_person <person_id> <room_name>
    reallocate_unallocated <person_id> <room_name>
    load_people <filename>
    (-i | --interactive)
Options:
    -h --help     Show this screen.
    -v --version
"""
import os
import click
import cmd
from docopt import docopt, DocoptExit
from dojo import Dojo

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
            # The DocoptExit is thrown when the args do not match.
            # We print a message to the user and the usage block.
            msg = 'Invalid Command'
            print(msg)
            print(e)
            return

        except SystemExit:
            # The SystemExit exception prints the usage for --help
            # We do not need to do the print here.
            return

        return func(self, opt)

    fn.__name__ = func.__name__
    fn.__doc__ = func.__doc__
    fn.__dict__.update(func.__dict__)
    return fn


def start():

    #enter_dojo(): dunder doc simply fetches the doctsring and print out all the arguments
    arguments = __doc__
    print(arguments)


dojo = Dojo()


class Interactive_Dojo(cmd.Cmd):
    intro = 'Welcome to Dojo Interactive Program!' \
        + ' (type help for a list of commands.)'
    prompt = '(Dojo)==> '
    #decorators to conver functions to commands
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
        """Usage: add_person <first_name> <last_name> <role> [<accomodate>] """
        if args['<accomodate>'] is None:
            args['<accomodate>'] = 'N'

        try:
            validated_details = dojo.validate_person(args['<first_name>'],
                                                      args['<last_name>'],
                                                      args['<role>'],
                                                      args['<accomodate>'])
            if isinstance(validated_details, list):
                person = dojo.generate_identifier(validated_details)
                dojo.allocate_room(person)
        except Exception as e:
            print(e)
            msg = 'Oops!An error occurred in running'
            msg += ' the command. Please try again.'
            click.secho(msg, fg='red', bold=True)
    
    @parse
    def do_print_room(self, args):
        """Usage: print_room <room_name>"""
        dojo.print_room(args['<room_name>'])

    @parse
    def do_print_allocations(self, args):
        """Usage: print_allocations [--o=filename]"""
        filename = args['--o']
        if filename:
            dojo.print_allocations(filename)
        else:
            dojo.print_allocations()

    @parse
    def do_print_unallocated(self, args):
        """Usage: print_unallocated [--o=filename]"""
        filename = args['--o']
        if filename:
            dojo.print_unallocated(filename)
        else:
            dojo.print_unallocated()
    @parse
    def do_reallocate_person(self, args):
        """Usage: reallocate_person <person_id> <room_name>"""
        dojo.reallocate_person(args['<person_id>'], args['<room_name>'])
    @parse
    def do_reallocate_unallocated(self, args):
        """ Usage: reallocate_unallocated <person_id> <room_name> """
        dojo.reallocate_unallocated(args['<person_id>'], args['<room_name>'])

    @parse
    def do_load_people(self, args):
        """Usage: load_people <filename>"""

        if os.path.exists(args['<filename>']):
            filename = args['<filename>']
            with open(filename, "r") as file:
                lines = file.readlines()
                for line in lines:
                    person_details = line.split()
                    if len(person_details) == 3:
                        first_name = person_details[0]
                        last_name = person_details[1]
                        role = person_details[2]
                        accomodate = "N"
                        validated_details = dojo.validate_person(first_name=first_name,
                                                                  last_name=last_name,
                                                                  role=role,
                                                                  accomodate=accomodate)
                        if isinstance(validated_details, list):
                            person = dojo.generate_identifier(
                                validated_details)
                            dojo.allocate_room(person)
                    elif len(person_details) == 4:
                        first_name = person_details[0]
                        last_name = person_details[1]
                        role = person_details[2]
                        accomodate = person_details[3]
                        validated_details = dojo.validate_person(first_name=first_name,
                                                                  last_name=last_name,
                                                                  role=role,
                                                                  accomodate=accomodate)
                        if isinstance(validated_details, list):
                            person = dojo.generate_identifier(
                                validated_details)
                            dojo.allocate_room(person)
                    else:
                        print("An error occurred")

    def do_exit(self, arg):
        """Quits out of Interactive Mode."""
        click.secho("Thank you for stopping by, Goodbye!", fg='yellow', bold=True)
        exit()
if __name__=="__main__":
    print(__doc__)
    Interactive_Dojo().cmdloop()