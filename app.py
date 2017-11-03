"""
    Usage:
        create_room <type_room> <room_name>...
        add_person <person_name> <FELLOW|STAFF> [wants_accommodation]
        dojo (-h | --help | --version)
    Options:
        -h, --help  Show this screen and exit.
"""

import sys
import cmd
from termcolor import colored
from docopt import docopt, DocoptExit

def docopt_cmd(func):
    """
    This decorator is used to simplify the try/except block and pass the result
    of the docopt parsing to the called action.
    Credit to Docopt doumentation examples.(interactive example)
    """
    def fn(self, arg):
        try:
            opt = docopt(fn.__doc__, arg)

        except DocoptExit as e:
            # The DocoptExit is thrown when the args do not match.
            # We print a message to the user and the usage block.

            print('Invalid Command!')
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

class DojoInteractive(cmd.Cmd):
    intro = colored('Starting Dojo App.....', 'green', attrs=['bold'])
    prompt = colored('DOJO >>>', 'red', attrs=['bold','blink'])

    @docopt_cmd
    def do_create_room(self, args):
        """create_room <room_type> <room_name>..."""
        for name in args['<name>']:
            print(name)

    @docopt_cmd
    def do_add_person(self, arg):
        """ add_person <person_name> <FELLOW|STAFF> [wants_accommodation] """
        print(arg)

    def do_exit(self, arg):
        """Quits out of Interactive Mode."""
        print('Good Bye!')
        exit()
if __name__=="__main__":
    print(__doc__)
    DojoInteractive().cmdloop()