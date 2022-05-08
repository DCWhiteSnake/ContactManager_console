from DataStructures.dequeue import Dequeue


class Queue(Dequeue):

    def enqueue(self, value):
        self.enqueue_tail(value)

    def dequeue(self, value):
        self.dequeue_head(value)

    def peek(self):
        try:
            value = self.peek_head()
            if value:
                return value
        except IOError:
            raise IOError
