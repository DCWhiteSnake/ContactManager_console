from src.ContactManager_DSA.DataStructures.sortedlist import SortedList
from src.ContactManager_DSA.Models.contact import Contact
import logging

logging.basicConfig(filename=r'..\..\Logs\log.txt', filemode='a', format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.DEBUG)


class ContactStore:

    def __init__(self):
        self._contacts = SortedList()
        self._nextId = 1

    def get_contacts(self):
        return self._contacts

    def add(self, contact):
        # todo: add time elapsed to log
        if not isinstance(contact, Contact):
            logging.info("Invalid Contact")
        else:
            if not contact.identification:
                contact.identification = self._nextId
                self._nextId = self._nextId + 1
                self._nextId = max(contact.identification, self._nextId)
                cont = Contact(contact.firstname, contact.lastname, contact.street, contact.city, contact.state,
                               contact.code, contact.identification)

                logging.info(f"Add: adding new contact: {cont}");
                self._contacts.add(cont)
                return cont.identification
            else:
                self._nextId = contact.identification + 1
                logging.info(f"Add: adding new contact: {contact}");
                self._contacts.add(contact)
                return contact.identification



    def add_contacts(self, contacts):
        for contact in contacts:
            self.add(contact)

    def load(self, new_contacts):
        self._nextId = 1
        return self.add_contacts(new_contacts)

    def remove(self, contact):
        if not isinstance(contact, Contact):
            logging.info("Remove: Contact not found, no action taken")
            raise ValueError
        else:
            removed_contact = self._contacts.remove(contact).getdat
            if removed_contact:
                logging.debug(
                    f"Remove: ({removed_contact.firstname}, {removed_contact.lastname})")
                return removed_contact

    def search(self, identity):
        temp = self._contacts.get_head()[1]
        temp_data= temp.getdata()
        while temp:
            if temp_data._identification == int(identity):
                return temp_data
            else:
                temp = temp.next()

