
import pytest


@pytest.fixture()
def before_each(request):
    print("Called before each test" + request.node.name)


def test_first(before_each):
    assert 1 == 1


def test_second(before_each):
    assert 1 == 2, "Единица не должна быть равна двойке!"




