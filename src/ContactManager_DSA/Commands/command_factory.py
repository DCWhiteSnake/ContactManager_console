from src.ContactManager_DSA.Models.contact import Contact
from src.ContactManager_DSA.DataStructures.doublylinkedlist import Dll

"""
class ContactFieldFilter:
    def __init__(self):
        pass
"""


class CommandResult:
    def __init__(self, command, result):
        if isinstance(command, Command) and (isinstance(result, (Dll, list))):
            self._command = command
            self._result = result
        else:
            raise TypeError

    def get_undo_command(self):
        pass


class NonUndoCommandResult(CommandResult):
    def __init__(self, command, result):
        super(NonUndoCommandResult, self).__init__(command, result)

    def get_undo_command(self):
        pass


class CommandFactory:
    def __init__(self, store):
        self._store = store

    def list(self):
        return List(self._store)

    def search(self, id):
        return self._store.search(id)

    def add(self, fields):
        return Add(self._store, fields)

    def remove(self, fields):
        return Remove(self._store, fields)

    def quit(self):
        return Quit()

    def load(self, csv_file_name):
        return Load(self._store, csv_file_name)


class Command:
    def __init__(self):
        pass

    def execute(self):
        pass

    def get_undo_command(self):
        pass


class List(Command):
    def __init__(self, store):
        self._contacts = store.get_contacts()

    def execute(self):
        vals = []
        for x in self._contacts:
            vals.append(str(x))
        return vals


class Load(Command):
    def __init__(self, store, field):
        self._storage = store
        try:
            self._filename = field["file"]
        except KeyError:
            raise

    def execute(self):
        try:
            with open(file=f"..\\..\\{self._filename}", mode="rt", encoding="utf-8") as csv_file:

                raw_contacts_from_file = [contact.split(',') for contact in [x for x in csv_file]]
                for raw_contact in raw_contacts_from_file:
                    fn, ln, street, city, state, code, id = raw_contact
                    contact = Contact.create_with_identification(fn, ln, street, city, state,
                                                                 code, int(id.strip()))

                    self._storage.add(contact)
                print("Contacts successfully added, enter 'list' to view them")
        except TypeError:
            raise
        except FileNotFoundError:
            print("The file doesn't exit")


class Quit(Command):
    def execute(self):
        pass


class Add(Command):
    def __init__(self, store, fields):

        self.store = store
        self.firstname = "Nil"
        self.lastname = "Nil"
        self.street = "Nil"
        self.city = "Nil"
        self.state = "Nil"
        self.code = "Nil"
        self.fields = fields
        super().__init__()

    def execute(self):
        if self.map_input_to_contact(self.fields):
            contact_to_add = Contact.create(self.firstname, self.lastname, self.street, self.city, self.state,
                                            self.code)
        else:
            raise ValueError
        self.store.add(contact_to_add)
        return AddCommandResult(self, self.store, contact_to_add)

    def map_input_to_contact(self, fields):
        return_val = True
        try:
            for field, value in fields.items():
                if field in ["fn", "firstname", "FirstName"]:
                    self.firstname = value
                elif field in ["ln", "lastname", "LastName"]:
                    self.lastname = value
                elif field in ["street", "str"]:
                    self.street = value
                elif field in ["cty, city"]:
                    self.city = value
                elif field in ["state", "territory"]:
                    self.state = value
                elif field in ["code, zip, zipcode"]:
                    self.code = value
        except:
            return_val = False
        return return_val


class AddCommandResult(CommandResult):
    def __init__(self, command, store, contact):
        self._store = store
        self._command = command
        self._contact = contact
        self._can_undo = True

    def get_undo_command(self):
        return DirectRemove(self._store, self._contact)


class Remove(Command):
    def __init__(self, store, fields):
        self._store = store
        self._id = fields["identity"]

    def execute(self):
        contact_to_remove = self._store.search(self._id)
        removed_contact = self._store.remove([contact_to_remove])
        return RemoveCommandResult(self, self._store, removed_contact)

    def map_input_to_contact(self, fields):
        return_val = True
        try:
            for field, value in fields.items():
                if field in ["fn", "firstname", "FirstName"]:
                    self._fn = value
                elif field in ["ln", "lastname", "LastName"]:
                    self._ln = value
                elif field in ["street", "str"]:
                    self._streets = value
                elif field in ["cty, city"]:
                    self._cty = value
                elif field in ["state", "territory"]:
                    self._state = value
                elif field in ["code, zip, zipcode"]:
                    self._code = value
        except:
            return_val = False
        return return_val


class DirectRemove(NonUndoCommandResult):
    def __init__(self, store, contact):
        self._store = store
        self._contact = contact
        self._verb = "direct remove, not undoable"

    def execute(self):
        removed = []
        removed_contact = self._store.remove(self._contact)
        if removed_contact:
            removed.append(removed_contact)
        return [removed, self._verb]


class RemoveCommandResult(CommandResult):
    def __init__(self, command, store, contacts_id, contact):
        self._store = store
        self._command = command
        self._contact_id = contacts_id
        # self._can_undo = True
        self._contact = contact

    def get_undo_command(self):
        return DirectAdd(self._store, self._contact)


class DirectAdd(NonUndoCommandResult):
    def __init__(self, store, contact):
        self._store = store
        self._contact = contact
        self._verb = "add"

    def execute(self):
        added = []
        added_contact = self._store.add(self._contact)
        if added_contact:
            added.append(added_contact)
        super(NonUndoCommandResult, self).__init__(self._verb, [added, self._verb])
        return [added, self._verb]

# todo
# class DirectRemove_ContactList()
