from DataStructures.doublylinkedlist import Dll, DllNode


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
        itemtoadd = SortedListNode(item)
        if self._length == 0:
            self._head = itemtoadd
            self._tail = self._head
            self._curr = self._head
        else:
            if item.compare_to(self._head._data) < 0:
                new_head = itemtoadd
                new_head._nxt = self._head
                self._head._prev = new_head
                self._head = new_head
                self._curr = new_head
            elif item.compare_to(self._tail._data) > 0:
                new_tail = SortedListNode(item)
                new_tail._prev = self._tail
                self._tail._nxt = new_tail
                self._tail = new_tail
            else:
                insert_before = self._head
                while insert_before._data.compare_to(item) < 0:
                    insert_before = insert_before._nxt

                to_insert = SortedListNode(item)
                to_insert._nxt = insert_before
                to_insert._prev = insert_before.prev()
                insert_before._prev._nxt = to_insert
                insert_before._prev = to_insert
        self._length = self._length + 1



    def __iter__(self):
        return self

    def __next__(self):
        if self._length == 0:
            raise StopIteration
        if not self._curr:
            self._curr = self._head
            raise StopIteration
        else:
            item = self._curr._data
            self._curr = self._curr._nxt
            return item




