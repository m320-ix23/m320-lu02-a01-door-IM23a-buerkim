"""
Created on
"""
import pytest

from door import Door, DoorLock

@pytest.fixture
def a_door():
    """
    Fixture to
    """
    return Door(DoorLock(), 'green')


def test_initial(a_doora):
    """
    Test initialization
    """
    assert a_doora.color == 'green'


def test_get_set_color(a_doorx):
    """
    Testen der Tür farbe
    """
    a_doorx.color = 'red'
    assert a_doorx.color == 'red'


def test_door_open(a_doorb):
    """
    Testen der
    """
    a_doorb.open_the_door()
    assert a_doorb.door_is_open


def test_door_close(a_doorc):
    """

    :param a_doorc:
    :return:
    """
    a_doorc.close_the_door()
    assert a_doorc.door_is_open is False


def test_door_locking(a_doord):
    """

    :param a_door:
    :return:
    """
    a_doord.lock_the_door()
    assert a_doord._door_is_locked


def test_door_unlock(a_doore):
    """

    :param a_door:
    :return:
    """
    a_doore.unlock_the_door()
    assert a_doore._door_is_locked is False
