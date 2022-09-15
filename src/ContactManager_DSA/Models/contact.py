from attr import dataclass


@dataclass(frozen=False, eq=True, repr=True)
class Contact:
    firstname: str
    lastname: str
    street: str
    city: str
    state: str
    code: str
    identification: int

    @staticmethod
    def typename(obj):
        return type(obj).__name__

    def __str__(self):
        return str.strip(f"{self.firstname},{self.lastname},{self.street},{self.city},{self.state},"
                         f" {self.code}, {self.identification}")

    @classmethod
    def create(cls, firstname, lastname, street, city, state, code):
        return cls(firstname, lastname, street, city, state, code, 0)

    @classmethod
    def create_with_identification(cls, firstname, lastname, street, city, state, code, identity):
        return cls(firstname, lastname, street, city, state, code, identity)


if __name__ == '__main__':
    david = Contact.create_with_identification("David", "Okeke", "Apple Street", "Lagos-Mainland", "Lagos",
                                               "432fe", 1)
    print(repr(david))
