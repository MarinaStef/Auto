import pytest
from string_utils import StringUtils
utils = StringUtils()

"""capitalize"""
def test_capitalize():
    """Positive"""
    assert utils.capitilize("homework") == "Homework"
    assert utils.capitilize("123") == "123"
    assert utils.capitilize("29 april") == "29 april"
    """Negative"""
    assert utils.capitilize("")==""
    assert utils.capitilize(" ")== " "
    assert utils.capitilize("123446testingtest") == "123446testingtest"

"""trim"""
def test_trim():
    """Positive"""
    assert utils.trim("    Homework") == "Homework"
    assert utils.trim("  123") == "123"
    assert utils.trim("  29 april") == "29 april"
    """Negative"""
    assert utils.trim("") == ""

@pytest.mark.xfail()
def test_trim_with_numbers_input():
    assert utils.trim(989569)=="989569"

@pytest.mark.xfail()
def test_trim_with_spaces_output():
    assert utils.trim(" HomeWork ")==" HomeWork "

"""to_list"""
@pytest.mark.parametrize('string, delimeter, result',[
    # """Positive"""
    ("pen,pan,pencil", ",", ["pen","pan","pencil"]),
    ("1,2,3", ",", ["1", "2", "3"]),
    ("*@$@%&", ",", ["*", "$", "%", "&"]),
    # """Negative"""
    ("",None, []), 
    ("1,2,3", None, ["1", "2", "3"]),])
def test_to_list(string, delimeter,result):
    if delimeter is None:
        result = utils.to_list(string)
    else:
        result = utils.to_list(string, delimeter)

"""contains"""
@pytest.mark.parametrize('string, symbol, result', [
    ("peace", "p",True),
    ("world", "l",True),
    ("785", "5",True),
    ("sweet-chili", "-",True),
    ("", "",True),
    ("Novosibirsk", "s",True),
    ("Moscow", "m",False),
    ("Hello", "f",False),
    ("bird", "*",False),
    ("", "z",False),
])
def test_contains(string, symbol, result):
    res = utils.contains(string, symbol)
    assert res == result

"""delite_symbol"""
@pytest.mark.parametrize('string, symbol, result', [
    ("orange", "o", "range"),
    ("sweet papper", " ", "sweetpapper"),
    ("987", "9", "87"),
    (" ", " ", " "),
    ("", "", ""),
    ("coffee", " ", "coffee"),
    ("paper ", " ", "paper"),
])
def test_delite_symbol(string, symbol, result):
    res = utils.delete_symbol(string, symbol)
    assert res == result

"""starts_with"""
@pytest.mark.parametrize('string, symbol, result', [
     ("peace", "p",True),
     ("world", "w",True),
     ("785", "7",True),
     ("sweet-chili", "s",True),
     ("", "",True),
     ("Novosibirsk", "N",True),
     ("Moscow", "m",False),
     ("Hello", "f",False),
     ("bird", "*",False),
     ("", "z",False),
])
def test_starts_with(string, symbol, result):
    res = utils.starts_with(string, symbol)
    assert res == result

"""end_with"""
@pytest.mark.parametrize('string, symbol, result', [
     ("peace", "e",True),
     ("world", "d",True),
     ("785", "5",True),
     ("sweet-chili", "i",True),
     ("", "",True),
     ("Novosibirsk", "k",True),
     ("Moscow", "m",False),
     ("Hello", "f",False),
     ("bird", "*",False),
     ("", "z",False),
])
def test_end_with(string, symbol, result):
    res = utils.end_with(string, symbol)
    assert res == result

"""is_empty"""
@pytest.mark.parametrize('string, result', [
    ("", True),
    (" ", True),
    ("    ", True),
    ("not empty", False),
    ("no no no it isn't empty", False),
    ("4568", False),
])
def test_is_empty(string, result):
    res = utils.is_empty(string)
    assert res == result

"""list_to_string"""
@pytest.mark.parametrize('lst, joiner, result', [
    (["9", "1", "1"], "", "911"),
    (["nine", "one", "one"], "-", "nine-one-one"),
    (["Pupa", "Lupa"], " and ", "Pupa and Lupa"),
    ([], None, ""),
    ([], ",", ""),
    ([], "like", ""),
])
def test_list_to_string(lst, joiner, result):
    if joiner == None:
        res = utils.list_to_string(lst)
    else:
        res = utils.list_to_string(lst, joiner)
    assert res == result