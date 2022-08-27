from unittest.mock import MagicMock
import pytest

from dao.director import DirectorDAO
from dao.model.director import Director
from service.director import DirectorService


@pytest.fixture()
def director_dao():
    director_dao = DirectorDAO(None)

    director_1 = Director(id=1, name='user_1')
    director_2 = Director(id=2, name='user_2')

    director_dao.get_one = MagicMock(return_value=director_1)
    director_dao.get_all = MagicMock(return_value=[director_1, director_2])
    director_dao.create = MagicMock(return_value=director_1)
    director_dao.delete = MagicMock()
    director_dao.update = MagicMock()

    return director_dao


class TestDirectorSrvice:
    @pytest.fixture(autouse=True)
    def director_service(self, director_dao):
        self.director_service = DirectorService(director_dao)

    def test_get_one(self):
        director = self.director_service.get_one(1)
        assert director != None
        assert director.name == 'user_1'

    def test_get_all(self):
        director = self.director_service.get_all()
        assert len(director) > 0
        assert len(director) == 2

    def test_create(self):
        director_d = {
            "name": "user_1"
        }

        director = self.director_service.create(director_d)
        assert director.name != None

    def test_delete(self):
        self.director_service.delete(1)

    def test_update(self):
        director_d = {
            "id": 3,
            "name": "user_3"
        }

        self.director_service.update(director_d)
