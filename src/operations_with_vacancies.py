import re

from src.vacancy import Vacancy


def cast_hh_to_object_list(vacancies: list[dict[str | int]]) -> list[Vacancy]:
    """ Преобразование набора данных из JSON полученного по API с HH в список экземпляров класса Vacancy """
    vacancies_list = []

    for vacancy in vacancies:
        vacancy_list = []

        # Добавление названия вакансии
        name = vacancy.get("name")
        if name:
            vacancy_list.append(name)
        else:
            vacancy_list.append("Название вакансии не указано")

        # Добавление города
        area = vacancy.get("area").get("name")
        if area:
            vacancy_list.append(area)
        else:
            vacancy_list.append("Название города не указано")

        # Добавление ссылки на вакансию
        url = vacancy.get("url")
        if url:
            vacancy_list.append(url)
        else:
            vacancy_list.append("Ссылка на вакансию не указана")

        # Добавление краткого описания вакансии
        description = vacancy.get("snippet").get("responsibility")
        if description:
            # Убираем HTML-теги
            description = re.sub(r'<.*?>', '', description)
            vacancy_list.append(description)
        else:
            vacancy_list.append("Описание вакансии отсутствует")

        # Добавление требований к кандидату
        requirements = vacancy.get("snippet").get("requirement")
        if requirements:
            # Убираем HTML-теги
            requirements = re.sub(r'<.*?>', '', requirements)
            vacancy_list.append(requirements)
        else:
            vacancy_list.append("Требования к кандидату отсутствуют")

        # Проверка указана ли зарплата и добавление зарплаты
        salary = vacancy.get("salary")
        if salary:
            salary_from = vacancy.get("salary").get("from")
            salary_to = vacancy.get("salary").get("to")
            if isinstance(salary_from, int) and salary_from > 0:
                vacancy_list.append(salary_from)
                if isinstance(salary_to, int) and salary_to >= salary_from:
                    vacancy_list.append(salary_to)
                else:
                    vacancy_list.append(salary_from)
            else:
                vacancy_list.append(0)
                if isinstance(salary_to, int) and salary_to > 0:
                    vacancy_list.append(salary_to)
        else:
            vacancy_list.append(0)
            vacancy_list.append(0)

        # Добавление вакансии(в виде экземпляра класса Vacancy) в список вакансий
        vacancies_list.append(Vacancy(*vacancy_list))

    return vacancies_list


def get_vacancy_words(vacancy_list: list[Vacancy], words: str) -> list[Vacancy]:
    """ Получение вакансий по указанным критериям """
    data_list = []
    # Преобразуем критерии поиска в список
    words = words.lower().split(",")

    # Ищем в списке вакансий совпадения с введенными критериями поиска
    for word in words:
        for vacancy in vacancy_list:
            if (word in vacancy.name.lower() or word in vacancy.area.lower() or word in vacancy.description.lower()
                    or word in vacancy.requirements.lower() and vacancy not in data_list):
                data_list.append(vacancy)

    return data_list


def get_vacancies_by_salary(vacancies_list: list[Vacancy], salary: str) -> list[Vacancy]:
    """ Вакансии по диапазону зарплат, на вход подается отфильтрованный список
    экземпляров класса Vacancy и диапазон зарплат """
    # Преобразование диапазона зарплаты
    salary = salary.split("-")

    salary_from = int(salary[0])
    if len(salary) == 1:
        salary_to = salary_from
    else:
        salary_to = int(salary[1])

    vacancy_list = []
    # Поиск подходящих вакансий по диапазону зарплат
    for vacancy in vacancies_list:
        if salary_from <= vacancy.salary_from <= salary_to or salary_from <= vacancy.salary_to <= salary_to:
            vacancy_list.append(vacancy)
        elif salary_from > vacancy.salary_from and salary_to < vacancy.salary_to:
            vacancy_list.append(vacancy)

    return vacancy_list


def sort_vacancies(vacancies_list: list[Vacancy]) -> list[Vacancy]:
    """ Сортировка вакансий по зарплате, на вход подается список экземпляров класса Vacancy,
    отобранный по диапазону зарплат """
    sort_list = sorted(vacancies_list, key=lambda x: x.salary_from)

    return sort_list


def get_top_vacancies(vacancies_list: list[Vacancy], n: int) -> list[Vacancy]:
    """ Топ вакансий, на вход подается список экземпляров класса Vacancy, отсортированный по зарплате """
    n = n + 1

    return [vacancy for vacancy in vacancies_list[:-n:-1]]


def print_vacancies(vacancies_list: list[Vacancy]) -> None:
    """ Вывод вакансий в консоль """
    for vacancy in reversed(vacancies_list):
        print(f"Название вакансии: {vacancy.name}. Город: {vacancy.area}. Ссылка на вакансию: {vacancy.link}. "
              f"Краткое описание вакансии: {vacancy.description}. Требования к кандидату: {vacancy.requirements}. "
              f"Заработная плата: {vacancy.salary_from} - {vacancy.salary_to}.")
