import logging
from typing import List
from pydantic.dataclasses import dataclass
from dataclass_map_and_log.mapper import DataclassMapper


@dataclass
class Definition:
    name: str
    surname: str


@dataclass
class MultipleDefinitions:
    definitions: List[Definition]


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


class TestDataclassMapper:
    def test_mapping_a_simple_object(self, caplog):
        data = {"name": "foo", "another": "bar", "surname": "qix"}
        caplog.set_level(logging.WARNING)

        # The dictionary is correctly mappped
        definition = DataclassMapper.map(Definition, data)
        assert definition.name == "foo"
        assert definition.surname == "qix"

        # And extra attributes are logged
        assert [
            "Unexpected attribute another on class <class 'tests.test_dataclass_map_and_log.Definition'> with value bar"
        ] == [rec.message for rec in caplog.records]

    def test_none_values_rendering(self, caplog):
        data = {"name": "foo", "another": None, "surname": "qix"}
        caplog.set_level(logging.WARNING)

        # The dictionary is correctly mappped
        definition = DataclassMapper.map(Definition, data)
        assert definition.name == "foo"
        assert definition.surname == "qix"

        # And extra attributes are logged
        assert [
            "Unexpected attribute another on class <class 'tests.test_dataclass_map_and_log.Definition'> with value None"
        ] == [rec.message for rec in caplog.records]

    def test_mapping_a_list_object(self, caplog):
        data = {
            "definitions": [
                {"name": "foo1", "another": "bar", "surname": "qix1"},
                {"name": "foo2", "surname": "qix2"},
            ],
        }
        caplog.set_level(logging.WARNING)

        # The list is correctly mappped
        definitions = DataclassMapper.map(MultipleDefinitions, data)
        assert definitions.definitions[0].name == "foo1"
        assert definitions.definitions[0].surname == "qix1"
        assert definitions.definitions[1].name == "foo2"
        assert definitions.definitions[1].surname == "qix2"

        # And extra attributes are logged
        assert [
            "Unexpected attribute another on class <class 'tests.test_dataclass_map_and_log.Definition'> with value bar"
        ] == [rec.message for rec in caplog.records]

    def test_mapping_a_nested_object(self, caplog):
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
        caplog.set_level(logging.WARNING)

        # The whole tree is correctly mappped
        definition = DataclassMapper.map(Parent, data)
        assert definition.name == "parent_name"
        assert definition.surname == "parent_surname"
        assert definition.children[0].name == "child1_name"
        assert definition.children[0].surname == "child1_surname"
        assert definition.children[1].name == "child2_name"
        assert definition.children[1].surname == "child2_surname"
        assert definition.single_child.name == "test"

        # And extra attributes are logged
        assert [
            "Unexpected attribute extra on class <class 'tests.test_dataclass_map_and_log.Parent'> with value parent_extra_data",
            "Unexpected attribute extra on class <class 'tests.test_dataclass_map_and_log.Child'> with value child_extra_data",
        ] == [rec.message for rec in caplog.records]
