import logging
from Models.contactstore import ContactStore
from repl import Repl
import sys


class app:
    """
    The entry point into the contact manager application.
    """
    # todo: search for timing module and integrate into logs
    logging.basicConfig(filename=r'C:/Users/David Okeke/source/repos/ContactManagerLogs/log1.txt', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
    logging.log(msg="Starting app", level=logging.INFO)

    def __init__(self):
        self._storage = ContactStore()

    def run(self):
        repl = Repl(sys.stdout, self._storage)
        repl.run()


try:
    application = app()
    application.run()
except KeyboardInterrupt:
    print("goodbye")
