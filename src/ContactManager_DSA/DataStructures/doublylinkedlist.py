class DllNode:
    def __init__(self, data, nxt=None, prev=None):
        """A doubly linked-list node"""
        self.data = data
        self.nxt = nxt
        self.prev = prev

    def next(self):
        return self.nxt

    def prev(self):
        return self.prev

    def getdata(self):
        return  self.data

    getdat = property(getdata)

class Dll:
    """
    A doubly linked list class
    """

    def __init__(self):
        self.length = 0
        self.head = None
        self.tail = None

    def add(self, item):
        """item: a linked list node
           default to add head method
        """
        return self.add_head(item)

    def add_head(self, data):
        try:
            newhead = DllNode(data)
            temp = self.head
            self.head = newhead
            self.head.nxt = temp
            if self.length == 0:
                self.tail = self.head
                self.length = 1
            else:
                temp.prev = self.head
        except ValueError:
            print("Invalid input")

    def addtail(self, data):
        try:
            newtail = DllNode(data)
            if self.length == 0:
                self.head = newtail
            else:
                self.tail.nxt = newtail
                newtail.prev = self.tail
            self.tail = newtail
        except ValueError:
            print("Invalid input")

    def remove(self, item):
        found = self.find(item)
        if not found:
            return False

        prev_item = found.prev
        next_item = found.nxt

        if not prev_item:
            # removing head
            self.head = next_item
            if self.head:
                self.head.prev = None
        else:
            prev_item.nxt = next_item

        if not next_item:
            # removing tail
            self.tail = prev_item
            if self.tail:
                self.tail.nxt = None
        else:
            next_item.prev = prev_item
        self.length = self.length - 1
        return found

    def removehead(self):
        if self.length == 0:
            pass
        else:
            self.head = self.head.next()
            self.length = self.length - 1
            if self.length == 0:
                self.tail = None
            else:
                self.head.prev = None

    def removetail(self):
        if self.length == 0:
            pass
        elif self.length == 1:
            self.tail = None
            self.head = None
        else:
            self.tail.prev.nxt = None
            self.tail = self.tail.prev()

            if self.length == 0:
                self.tail = None
            else:
                self.head.prev = None

        self.length = self.length - 1

    def gethead(self):
        if self.length > 0:
            return [True, self.head]
        return [False, None]

    def gettail(self):
        if self.length > 0:
            return [True, self.tail]
        return [False, None]

    def clear(self):
        self.head = None
        self.tail = None
        self.length = 0

    def find(self, contact):
        currdata = self.head.getdata()
        curr = self.head
        while curr:
            if currdata == contact:
                return curr
            curr = curr.next()
            currdata = curr.getdata()
        return None


    def __iter__(self):
        return self

    def __next__(self):
        if not self._curr:
            self._curr = self.head
            raise StopIteration
        else:
            item = self._curr.data
            self._curr = self._curr.nxt
            return item

    def __reversed__(self):
        current = self.tail
        while current:
            yield current.data
            current = current.prev

    def __len__(self):
        return self.length

    def __contains__(self, item):
        return not self.find(item) == None

