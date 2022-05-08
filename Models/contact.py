from utils import comparator


class Contact:
    def __init__(self, firstname, lastname, street, city, state, code, identification=None):
        self._identification = identification
        self._fn = firstname
        self._ln = lastname
        self._street = street
        self._cty = city
        self._state = state
        self._code = code

    def __str__(self):
        return str.strip(f"{self._identification}, {self._fn},{self._ln},{self._street},{self._cty},{self._state},"
                         f" {self._code}")
    def __eq__(self, other):
        if not isinstance(other, Contact):
            return False
        return self.compare_to(other) == 0



    def compare_to(self, other):
        comp = comparator(self._fn, other._fn)
        if comp != 0:
            return comp
        comp = comparator(self._ln, other._ln)
        if comp != 0:
            return comp
        comp = comparator(self._street, other._street)
        if comp != 0:
            return comp
        comp = comparator(self._cty, other._cty)
        if comp != 0:
            return comp
        comp = comparator(self._state, other._state)
        if comp != 0:
            return comp
        comp = comparator(self._code, other._code)
        if comp != 0:
            return comp

        if self._identification and other._identification:
            comp = comparator(self._identification, other._identification)
            if comp != 0:
                return comp
        elif not (not self._identification and not other._identification):
            if self._identification:
                return 1
            else:
                return -1

        return 0


def create(firstname, lastname, street, city, state, code):
    return Contact(firstname, lastname, street, city, state, code)


def create_with_identification(code, contact):
    return Contact(contact._fn, contact._ln, contact._street, contact._cty, contact._state, code)
