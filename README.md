# dataclasses-hjson

This package provides a simple way to serialize and deserialize dataclasses to and from Hjson.

This uses ``dataclasses-json`` to serialize and deserialize dataclasses, and ``hjson`` to parse and generate Hjson.

Opposed to ``dataclasses-json``, this package does only provide a mixin class to add the functionality to a dataclass, instead of a decorator. You can change the configuration of ``dataclasses-json`` by either using the ``using_config`` decorator or by manually setting the ``dataclasses_json_config`` attribute on the dataclass, using the ``hjson_config`` function.

If you have any problems, ideas or suggestions, feel free to open an issue or a pull request!

## Installation

```bash
pip install dataclasses-hjson
```

## Usage

Example adding config using the ``using_config`` decorator:

```python
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

```

Alternatively, you can use the ``hjson_config`` function:

```python
from dataclasses import dataclass
from dataclasses_json import Undefined, LetterCase
from dataclasses_hjson import DataClassHjsonMixin, hjson_config


@dataclass
class Person(DataClassHjsonMixin):
    dataclasses_json_config = hjson_config(undefined=Undefined.EXCLUDE, letter_case=LetterCase.CAMEL) # (These are the default values)

    first_name: str
    age: int
```

Adding the config is optional however!

Now you can serialize and deserialize the dataclass to and from Hjson:

```python
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

```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
