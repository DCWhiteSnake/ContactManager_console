from src.ContactManager_DSA.DataStructures.doublylinkedlist import Dll


class Dequeue(Dll):

    def enqueue_head(self, item):
        self.add_head(item)

    def enqueue_tail(self, item):
        self.addtail(item)

    def dequeue_head(self):
        value = self.head
        if (value):
            self.removehead()
            return value
        raise IOError

    def dequeue_tail(self):
        value = self.tail
        if (value):
            self.removetail()
            return value
        raise IOError

    def peek_head(self):
        return self.gethead()

    def peek_tail(self):
        return self.gettail()
