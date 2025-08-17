from project import reader, display, get_max_id, reminder
import pytest   


def test_reader():
    filename = 'nonexistent.csv'
    with pytest.raises(SystemExit) as info:
        reader(filename, [])
    assert info.value.code == "File not found."


def test_get_max_id():
    data = [
        {'id': 1, 'value': 10},
        {'id': 2, 'value': 5},
        {'id': 3, 'value': 15}
        ]
    assert get_max_id(data, 'id') == 3


def test_reminder():
    data = [
        {'id': 1, 'value': 1},
        {'id': 2, 'value': 0},
        {'id': 3, 'value': 1}
        ]
    assert len(reminder(data, 'value')) == 1