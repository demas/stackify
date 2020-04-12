from unittest import mock

import pytest

from cli import Command, CommandType, Parser


def test_equal_command():
    func = mock.MagicMock()
    c = Command(command_type=CommandType.EQUAL, value="a", action=func)
    parser = Parser()
    parser.add_command(c)

    parser.process_message("a")

    assert func.called


def test_equal_command_not_ok():
    func = mock.MagicMock()
    c = Command(command_type=CommandType.EQUAL, value="a", action=func)
    parser = Parser()
    parser.add_command(c)

    parser.process_message("b")

    assert not func.called


@pytest.mark.parametrize("message", ["foo", "foo 10", "foo10", "foo --include"])
def test_start_with_command(message):
    func = mock.MagicMock()
    c = Command(command_type=CommandType.START_WITH, value="foo", action=func)
    parser = Parser()
    parser.add_command(c)

    parser.process_message(message)

    assert func.called


@pytest.mark.parametrize("message", ["test foo", " foo", " foo10", " foo --include", "bar"])
def test_start_with_command_not_ke(message):
    func = mock.MagicMock()
    c = Command(command_type=CommandType.START_WITH, value="foo", action=func)
    parser = Parser()
    parser.add_command(c)

    parser.process_message(message)

    assert not func.called


@pytest.mark.parametrize("message", ["a", "b", "c"])
def test_in_list_command(message):
    func = mock.MagicMock()
    c = Command(command_type=CommandType.IN_LIST, value=["a", "b", "c"], action=func)
    parser = Parser()
    parser.add_command(c)

    parser.process_message(message)

    assert func.called


@pytest.mark.parametrize("message", ["a ", "a1", " a", "e"])
def test_in_list_command_not_ok(message):
    func = mock.MagicMock()
    c = Command(command_type=CommandType.IN_LIST, value=["a", "b", "c"], action=func)
    parser = Parser()
    parser.add_command(c)

    parser.process_message(message)

    assert not func.called


def test_call_first_command():
    func = mock.MagicMock()
    c1 = Command(command_type=CommandType.EQUAL, value="a", action=func.foo)
    c2 = Command(command_type=CommandType.START_WITH, value="a", action=func.bar)
    parser = Parser()
    parser.add_command(c1)
    parser.add_command(c2)

    parser.process_message("a")

    assert func.foo.called
    assert not func.bar.called
