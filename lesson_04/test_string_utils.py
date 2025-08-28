import pytest
from string_utils import StringUtils


string_utils = StringUtils()


@pytest.mark.positive
@pytest.mark.parametrize("string, result", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world")
])
def test_capitalize_positive(string, result):
    assert string_utils.capitalize(string) == result


@pytest.mark.negative
@pytest.mark.parametrize("string, result", [
    ("", ""),
    (" ", " "),
])
def test_capitalize_negative(string, result):
    assert string_utils.capitalize(string) == result


@pytest.mark.positive
@pytest.mark.parametrize("string, result", [
    (" skypro", "skypro"),
    (" hello world", "hello world")
])
def test_trim_positive(string, result):
    assert string_utils.trim(string) == result


@pytest.mark.negative
@pytest.mark.parametrize("string, result", [
    ("", ""),
    (" ", ""),
])
def test_trim_negative(string, result):
    assert string_utils.trim(string) == result


@pytest.mark.positive
@pytest.mark.parametrize("string, symbol, result", [
    ("skypro", "p", True),
    ("skypro1", "1", True)
])
def test_contains_positive(string, symbol, result):
    assert string_utils.contains(string, symbol) == result


@pytest.mark.negative
@pytest.mark.parametrize("string, symbol, result", [
    (" ", "a", False),
    ("skypro", "S", False)
])
def test_contains_negative(string, symbol, result):
    assert string_utils.contains(string, symbol) == result


@pytest.mark.positive
@pytest.mark.parametrize("string, symbol, result", [
    ("skypro", "pro", "sky"),
    ("hello world", " world", "hello")
])
def test_delete_symbol_positive(string, symbol, result):
    assert string_utils.delete_symbol(string, symbol) == result


@pytest.mark.negative
@pytest.mark.parametrize("string, symbol, result", [
    (" ", " ", ""),
    ("skypro", "!", "skypro")
])
def test_delete_symbol_negative(string, symbol, result):
    assert string_utils.delete_symbol(string, symbol) == result
