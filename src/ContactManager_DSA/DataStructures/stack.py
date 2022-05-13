from src.ContactManager_DSA.DataStructures.dequeue import Dequeue


class Stack(Dequeue):
    def pop(self):
        return self.dequeue_head()

    def push(self, value):
        self.enqueue_head(value)

    def peek(self):
        try:
            value = self.peek_head()
            if value:
                return value
        except IOError:
            raise IOError
