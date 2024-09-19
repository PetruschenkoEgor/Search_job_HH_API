import os

from src.interaction_with_files import JSONSaver

PATH_TO_FILE_EMPTY = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "test.json")
PATH_TO_FILE = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "test1.json")


def test_transformation_vacancy(vacancy, vacancy_result):
    """Тест преобразования для записи в файл экземпляра класса"""
    js1 = JSONSaver(PATH_TO_FILE_EMPTY)
    assert js1.transformation_vacancy(vacancy) == vacancy_result


def test_transformation_vacancy_list(vacancy, vacancy1, vacancy_result1):
    """Тест преобразования для записи в файл списка экземпляров класса"""
    js1 = JSONSaver(PATH_TO_FILE_EMPTY)
    assert js1.transformation_vacancy([vacancy, vacancy1]) == vacancy_result1


def test_checking_for_duplication_empty(vacancy, vacancy1, vacancy2, vacancy_result1):
    """Тест на проверку дублирования"""
    js1 = JSONSaver(PATH_TO_FILE_EMPTY)
    assert js1.checking_for_duplication([vacancy, vacancy1, vacancy2]) == vacancy_result1


def test_checking_for_duplication(vacancy, vacancy1, vacancy2, vacancy_result1):
    """Тест на проверку дублирования"""
    js1 = JSONSaver(PATH_TO_FILE)
    assert js1.checking_for_duplication([vacancy, vacancy1, vacancy2]) == vacancy_result1


def test_get_from_json_empty():
    """Тест на получение данных из пустого файла"""
    js2 = JSONSaver(PATH_TO_FILE_EMPTY)
    assert js2.get_from_json() == []


def test_get_from_json_not_found():
    """Тест на получение данных, если файла нет"""
    js2 = JSONSaver("123")
    assert js2.get_from_json() == []


def test_get_from_json(vacancy_result):
    """Тест на получение данных"""
    js2 = JSONSaver(PATH_TO_FILE)
    assert js2.get_from_json() == vacancy_result


def test_get_vacancy_from_json(vacancy_result):
    """Тест на удаление"""
    js2 = JSONSaver(PATH_TO_FILE)
    assert js2.get_vacancy_from_json("Разработчик") == vacancy_result
