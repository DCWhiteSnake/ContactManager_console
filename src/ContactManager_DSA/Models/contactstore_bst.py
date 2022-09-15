from src.ContactManager_DSA.DataStructures.binarysearchtree import BST
from src.ContactManager_DSA.Models.contact import Contact
import logging

logging.basicConfig(filename=r'./Logs/log.txt', filemode='a', format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.DEBUG)


class ContactStore:

    def __init__(self):
        self._contacts = BST()
        self._nextId = 1

    def get_contacts(self):
        return self._contacts

    def add(self, contact):
        # todo: add time elapsed to log
        if not isinstance(contact, Contact):
            logging.info("Invalid Contact, time elapsed = 0.005s")
        else:
            if not contact.identification:
                contact.identification = self._nextId
                self._nextId = self._nextId + 1
                self._nextId = max(contact.identification, self._nextId)
            else:
                self._nextId = contact.identification + 1
        try:
            cont = Contact(contact._fn, contact._ln, contact._street, contact._cty, contact._state,
                           contact._code, contact.identification)
        except:
            print("Bad Input, invalid contact")
            logging.info("Invalid Contact, time elapsed = 0.005s")

        logging.info(f"Add: adding new contact with ID {cont.identification} ({cont.fn} {cont.ln})");
        self._contacts.add(cont)

        logging.info(f"Add: complete ({cont.identification})", )

        return cont.identification

    def add_contacts(self, contacts):
        for contact in contacts:
            self.add(contact)

    def load(self, new_contacts):
        self._nextId = 1
        return self.add_contacts(new_contacts)

    def remove(self, contact):
        if not contact:
            logging.info("Remove: Contact not found, no action taken")
            raise ValueError
        else:
            removed_contact = self._contacts.remove(contact).getdat
            if removed_contact:
                logging.debug(
                    f"Remove: {removed_contact._identification} ({removed_contact._fn}, {removed_contact._ln})")
                return removed_contact

    def search(self, identity):
        temp = self._contacts.get_head()[1]
        temp_data= temp.getdata()
        while temp:
            if temp_data._identification == int(identity):
                return temp_data
            else:
                temp = temp.next()

