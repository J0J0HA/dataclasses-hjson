from dataclasses import dataclass
from dataclasses_json import Undefined, LetterCase
from dataclasses_hjson import DataClassHjsonMixin, using_config


@using_config(
    undefined=Undefined.EXCLUDE, letter_case=LetterCase.CAMEL
)  # (These are the default values)
@dataclass
class Person(DataClassHjsonMixin):
    first_name: str
    age: int


person = Person(first_name="Guido", age=42)
person_json = person.to_hjson()
print(person_json)
# {
#   firstName: Guido
#   age: 42
# }
person_copy = Person.from_hjson(person_json)
print(person_copy)
# Person(name='Guido', age=42)
