# Dataclass Map and Log

Map dictionaries to pydantic dataclasses, log any extra attributes.

## Example
```python
from dataclass_map_and_log.mapper import DataclassMapper

@dataclass
class Child:
    name: str
    surname: str


@dataclass
class SingleChild:
    name: str


@dataclass
class Parent:
    name: str
    surname: str
    children: List[Child]
    single_child: SingleChild
    
data = {
    "name": "parent_name",
    "surname": "parent_surname",
    "extra": "parent_extra_data",
    "children": [
        {
            "name": "child1_name",
            "surname": "child1_surname",
            "extra": "child_extra_data",
        },
        {
            "name": "child2_name",
            "surname": "child2_surname",
        },
    ],
    "single_child": {"name": "test"},
}

definition = DataclassMapper.map(Parent, data)
```
