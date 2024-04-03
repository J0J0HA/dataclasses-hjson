# dataclasses-hjson

This package provides a simple way to serialize and deserialize dataclasses to and from Hjson, using ``dataclasses-json`` and ``hjson``.

Opposed to ``dataclasses-json``, this package does only provide a mixin class to add the functionality to a dataclass, instead of a decorator. You can change the configuration of ``dataclasses-json`` by either using the ``with_config`` decorator or by manually setting the ``dataclasses_json_config`` attribute on the dataclass, using the ``hjson_config`` function.

## Installation

```bash
pip install dataclasses-hjson
```

## Usage

Adding config using the ``with_config`` decorator:

```python
from dataclasses import dataclass
from dataclasses_json import Undefined, LetterCase
from dataclasses_hjson import DataClassHjsonMixin, with_config


@with_config(undefined=Undefined.EXCLUDE, letter_case=LetterCase.CAMEL) # (These are the default values)
@dataclass
class Person(DataClassHjsonMixin):
    name: str
    age: int
```

Alternatively, you can use the ``hjson_config`` function:

```python
from dataclasses import dataclass
from dataclasses_json import Undefined, LetterCase
from dataclasses_hjson import DataclassHjsonMixin, hjson_config


@dataclass
class Person(DataclassHjsonMixin):
    dataclasses_json_config = hjson_config(undefined=Undefined.EXCLUDE, letter_case=LetterCase.CAMEL) # (These are the default values)

    name: str
    age: int
```

Now you can serialize and deserialize the dataclass to and from Hjson:

```python
person = Person(name='John', age=30)
