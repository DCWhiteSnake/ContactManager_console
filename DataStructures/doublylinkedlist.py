class DllNode:
    def __init__(self, data, nxt=None, prev=None):
        """A doubly linked-list node"""
        self._data = data
        self._nxt = nxt
        self._prev = prev

    def next(self):
        return self._nxt

    def prev(self):
        return self._prev

    def getdata(self):
        return  self._data

    getdat = property(getdata)

class Dll:
    """
    A doubly linked list class
    """

    def __init__(self):
        self._length = 0
        self._head = None
        self._tail = None

    def add(self, item):
        """item: a linked list node
           default to add head method
        """
        return self.add_head(item)

    def add_head(self, data):
        try:
            newhead = DllNode(data)
            temp = self._head
            self._head = newhead
            self._head._nxt = temp
            if self._length == 0:
                self._tail = self._head
                self._length = 1
            else:
                temp._prev = self._head
        except ValueError:
            print("Invalid input")

    def add_tail(self, data):
        try:
            newtail = DllNode(data)
            if self._length == 0:
                self._head = newtail
            else:
                self._tail._nxt = newtail
                newtail._prev = self._tail
            self._tail = newtail
        except ValueError:
            print("Invalid input")

    def remove(self, item):
        found = self.find(item)
        if not found:
            return False

        prev_item = found._prev
        next_item = found._nxt

        if not prev_item:
            # removing head
            self._head = next_item
            if self._head:
                self._head._prev = None
        else:
            prev_item._nxt = next_item

        if not next_item:
            # removing tail
            self._tail = prev_item
            if self._tail:
                self._tail._nxt = None
        else:
            next_item._prev = prev_item
        self._length = self._length - 1
        return found

    def remove_head(self):
        if self._length == 0:
            pass
        else:
            self._head = self._head.next()
            self._length = self._length - 1
            if self._length == 0:
                self._tail = None
            else:
                self._head._prev = None

    def remove_tail(self):
        if self._length == 0:
            pass
        elif self._length == 1:
            self._tail = None
            self._head = None
        else:
            self._tail._prev._nxt = None
            self._tail = self._tail.prev()

            if self._length == 0:
                self._tail = None
            else:
                self._head._prev = None

        self._length = self._length - 1

    def get_head(self):
        if self._length > 0:
            return [True, self._head]
        return [False, None]

    def get_tail(self):
        if self._length > 0:
            return [True, self._tail]
        return [False, None]

    def clear(self):
        self._head = None
        self._tail = None
        self._length = 0

    def find(self, contact):
        curr_data = self._head.getdata()
        curr = self._head
        while curr:
            if curr_data == contact:
                return curr
            curr = curr.next()
            curr_data = curr.getdata()
        return None


    def __iter__(self):
        return self

    def __next__(self):
        if not self._curr:
            self._curr = self._head
            raise StopIteration
        else:
            item = self._curr._data
            self._curr = self._curr._nxt
            return item

    def __reversed__(self):
        current = self._tail
        while current:
            yield current._data
            current = current.prev

    def __len__(self):
        return self._length

    def __contains__(self, item):
        return not self.find(item) == None

