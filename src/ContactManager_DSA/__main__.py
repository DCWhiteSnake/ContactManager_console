import logging
from src.ContactManager_DSA.Models.contactstore import ContactStore
from repl import Repl
import sys
import time

class app:
    """
    The entry point into the contact manager application.
    """
    # todo: search for timing module and integrate into logs
    logging.basicConfig(filename=r'C:/Users/David Okeke/source/repos/ContactManagerLogs/log1.txt', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
    logging.log(msg=f"Starting app. @{time.gmtime().tm_hour}:{time.gmtime().tm_min}, {time.gmtime().tm_wday}/{time.gmtime().tm_mday}/{time.gmtime().tm_mon}/{time.gmtime().tm_year}", level=logging.INFO)

    def __init__(self):
        self._storage = ContactStore()

    def run(self):
        repl = Repl(sys.stdout, self._storage)
        repl.run()


try:
    application = app()
    application.run()
    print("goodbye")
    logging.log(msg=f"End session. @{time.gmtime().tm_hour}:{time.gmtime().tm_min}, {time.gmtime().tm_wday}/{time.gmtime().tm_mday}/{time.gmtime().tm_mon}/{time.gmtime().tm_year}", level=logging.INFO)

except KeyboardInterrupt:
    logging.log(msg=f"End session. @{time.gmtime().tm_hour}:{time.gmtime().tm_min}, {time.gmtime().tm_wday}/{time.gmtime().tm_mday}/{time.gmtime().tm_mon}/{time.gmtime().tm_year}", level=logging.INFO)
    print("goodbye")
