from src.operations_with_vacancies import cast_hh_to_object_list, get_vacancy_words, get_vacancies_by_salary, \
    sort_vacancies, get_top_vacancies, print_vacancies
from src.vacancy import Vacancy


def test_cast_hh_to_object_list(get_json_vacancy):
    """ Тест на правильное преобразование набора данных """
    lst_vacancy = cast_hh_to_object_list(get_json_vacancy)
    assert type(lst_vacancy) == list
    for vacancy in lst_vacancy:
        assert vacancy.name == "Программист Python (Junior)"
        assert vacancy.area == "Москва"
        assert vacancy.link == "https://api.hh.ru/vacancies/107283454?host=hh.ru"
        assert vacancy.description == "Исправление существующих и возникающих багов. Взаимодействие с командой по проекту. Работа с системой контроля версий Git. Разработка и тестирование backend..."
        assert vacancy.requirements == "Уверенное владение Python. Умение писать SQL запросы. Аналитический склад ума. Навык работы с технической документацией и требованиями. Умение разбираться в..."
        assert vacancy.salary_from == 100000
        assert vacancy.salary_to == 120000


def test_get_vacancy_words(vacancy, vacancy1):
    """ Тест на получение вакансий по указанным критериям """
    assert get_vacancy_words([vacancy, vacancy1], "программист") == [vacancy1]


def test_get_vacancies_by_salary(vacancy, vacancy1):
    """ Тест на получение вакансий по диапазону зарплат """
    assert get_vacancies_by_salary([vacancy, vacancy1], "5000-15000") == [vacancy]


def test_sort_vacancies(vacancy, vacancy1):
    """ Тест на сортировку вакансий по зарплате """
    assert sort_vacancies([vacancy1, vacancy]) == [vacancy, vacancy1]


def test_get_top_vacancies(vacancy, vacancy1):
    """ Тест вывода топ-вакансий """
    assert get_top_vacancies([vacancy, vacancy1], 1) == [vacancy1]


def test_print_vacancies(capsys, vacancy):
    """ Тест на вывод информации о вакансиях """
    print_vacancies([vacancy])
    message = capsys.readouterr()
    assert message.out.strip() == "Название вакансии: Разработчик. Город: Москва. Ссылка на вакансию: http:...r. Краткое описание вакансии: Описание. Требования к кандидату: Требования. Заработная плата: 10000 - 20000."
