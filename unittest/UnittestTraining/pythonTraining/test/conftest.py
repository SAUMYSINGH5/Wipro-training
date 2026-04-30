import pytest

@pytest.fixture(scope='module', autouse=True)
def setup_teardown():
    print('Fixture.....')
    #return
    yield
    print('Ending.....')









