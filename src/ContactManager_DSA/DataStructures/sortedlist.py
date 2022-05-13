from src.ContactManager_DSA.DataStructures.doublylinkedlist import Dll, DllNode


class SortedListNode(DllNode):
    def __str__(self):
        pass


class SortedList(Dll):
    """ This class will be used to store contacts"""

    def add_head(self, data):
        pass

    def add_tail(self, data):
        pass

    def add(self, item):
        item_to_add = SortedListNode(item)
        if self.length == 0:
            self.head = item_to_add
            self.tail = self.head
            self.curr = self.head
        else:
            if item.compare_to(self.head.data) < 0:
                new_head = item_to_add
                new_head.nxt = self.head
                self.head.prev = new_head
                self.head = new_head
                self.curr = new_head
            elif item.compare_to(self.tail.data) > 0:
                new_tail = SortedListNode(item)
                new_tail.prev = self.tail
                self.tail.nxt = new_tail
                self.tail = new_tail
            else:
                insert_before = self.head
                while insert_before.data.compare_to(item) < 0:
                    insert_before = insert_before.nxt

                to_insert = SortedListNode(item)
                to_insert.nxt = insert_before
                to_insert.prev = insert_before.prev
                insert_before.prev.nxt = to_insert
                insert_before.prev = to_insert
        self.length = self.length + 1



    def __iter__(self):
        return self

    def __next__(self):
        if self.length == 0:
            raise StopIteration
        if not self.curr:
            self.curr = self.head
            raise StopIteration
        else:
            item = self.curr.data
            self.curr = self.curr.nxt
            return item




