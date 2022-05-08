import re
import logging
from Commands import command_factory
from Commands.command_factory import CommandFactory
from DataStructures.stack import Stack

logging.basicConfig(filename=r'./Logs/log.txt', encoding="utf-8", filemode='a', format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.DEBUG)


def print_collection(result):
    """
    Prints a command and then the result of that command
    :param result: The result of a successful command
    :return:
    """
    for x in result:
        print(x[1], " ", x[0][0])


def print_list(result):
    """
    Prints all items in a list
    :param result: The result of a successful command
    :return:
    """
    for x in result:
        print(x)


class Repl:
    """
    Description:
        repl = Read Evaluate Print Loop.
        Gets you input, evaluates it, returns a response and asks for your input again
    """

    def __init__(self, standard_out, contact_store):
        """
        Args:

        :param standard_out: The standard output stream of your current working environment
        :param contact_store: The repo containing the contacts
        """
        self._verb_regex = r"^(?P<verb>\w+)"
        self._fields_regex = r"(?P<field>\w+)=(?P<value>[^;]+);"
        self._standard_output = standard_out
        self._storage = contact_store
        self._factory = CommandFactory(self._storage)  # A factory class that returns command objects
        self._undoable_commands = Stack()  # Stacks recent (undoable) commands to enable an undo action

    def run(self):
        quit_seen = False
        while not quit_seen:
            cmd = self.get_next_cmd()
            if isinstance(cmd, command_factory.Quit):
                quit_seen = True
            elif isinstance(cmd, command_factory.Load) or isinstance(cmd, command_factory.List):
                cmd.execute()
            else:
                command_result = cmd.execute()
                self._undoable_commands.push(command_result)

    def prompt(self):
        """
        Outputs the right arrow to mimic an old-school style console, and allows you to input commands inline
        """
        self._standard_output.write("> ")

    def get_next_cmd(self):
        self.prompt()
        return self.map_cmd(input())

    def map_cmd(self, usr_input):
        """
        Maps the verb int user input to the appropriate factory method

        :param usr_input: The user input
        :return: a command in the case of add, remove but prints the result otherwise
        """
        if self.parse_line(usr_input):
            try:
                if self._verb in ["list", "lst", "l", "ls"]:
                    print_list(self._factory.list().execute())
                    self.run()
                elif self._verb in ["find", "f"]:
                    return print_list([self._factory.search(self._fields)])
                elif self._verb in ["ad", "add", "a"]:
                    add_cmd = self._factory.add(self._fields)
                    return add_cmd
                elif self._verb in ["rm", "remove", "r"]:
                    remove_cmd = self._factory.remove(self._fields)
                    return remove_cmd
                elif self._verb in ["q", "close", "quit", "exit"]:
                    return self._factory.quit()
                elif self._verb in ["load", "l"]:
                    return self._factory.load(self._fields)
                elif self._verb in ["undo", "u"]:
                    print_collection([self.undo_last_action()])
                    self.run()
                else:
                    print("Unknown command, please enter a valid command")
                    self.get_next_cmd()
            except KeyError:
                logging.critical(f"{usr_input}")
                print("You need to specify the file parameter i.e., 'load file=contacts.csv;'")

    def undo_last_action(self):
        """
        Description:
        Performs a roll-back of an undoable action

        :return: A description of what was undone
        """
        x = self._undoable_commands.pop()[1].getdat.get_undo_command().execute()
        return x

    def parse_line(self, usr_input):
        """
        Description:
            Uses regex with named fields eg.,p<field> to parse verb and fields from user input
        :param usr_input: The users input
        :return: The 'True' in the case of a successful parsing or false otherwise
        """
        logging.info(f"input: {usr_input}")
        parsed_verb = False
        fields = {}
        verb = None
        verb_match = re.match(self._verb_regex, usr_input)
        if verb_match:
            verb = verb_match[0]
            parsed_verb = True

            try:
                field_matches = re.findall(self._fields_regex, usr_input)
                if field_matches:
                    for field, value in field_matches:
                        fields[field] = value
            except:
                logging.log(f"bad input => '{usr_input}'")

        # todo: refactor into a property that takes these fields instead of creating instance fields on the fly
        self._fields = fields
        self._verb = verb
        return parsed_verb