def test_vacancy_init(vacancy):
    """Тест конструктора Vacancy"""
    assert vacancy.name == "Разработчик"
    assert vacancy.area == "Москва"
    assert vacancy.link == "http:...r"
    assert vacancy.description == "Описание"
    assert vacancy.requirements == "Требования"
    assert vacancy.salary_from == 10000
    assert vacancy.salary_to == 20000


def test_vacancy_lt(vacancy, vacancy1):
    """Тест в какой вакансии зарплата больше"""
    vac = vacancy > vacancy1
    assert vac is False


def test_vacancy_eq(vacancy, vacancy1):
    """Тест на равенство зарплат"""
    vac = vacancy == vacancy1
    assert vac is False
