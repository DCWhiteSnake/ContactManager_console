from src.ContactManager_DSA.DataStructures.doublylinkedlist import Dll


class Dequeue(Dll):

    def enqueue_head(self, item):
        self.add_head(item)

    def enqueue_tail(self, item):
        self.add_tail(item)

    def dequeue_head(self):
        value = self.get_head()
        if (value):
            self.remove_head()
            return value
        raise IOError

    def dequeue_tail(self):
        value = self.get_tail()
        if (value):
            self.remove_tail()
            return value
        raise IOError

    def peek_head(self):
        return self.get_head()

    def peek_tail(self):
        return self.get_tail()
