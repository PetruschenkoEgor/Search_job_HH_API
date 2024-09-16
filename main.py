from src.api_vacancy import HeadHunterAPI
from src.interaction_with_files import JSONSaver, PATH_TO_FILE
from src.operations_with_vacancies import cast_hh_to_object_list, get_vacancy_words, get_vacancies_by_salary, \
    sort_vacancies, get_top_vacancies, print_vacancies

# Создание экземпляра класса JSONSaver
json_saver = JSONSaver(PATH_TO_FILE)


def user_interaction():
    """ Функция взаимодействия с пользователем(HeadHunter) """
    search_query = input("Введите поисковый запрос: ")
    per_page = int(input("Сколько страниц показать(введите цифру от 1 до 100): "))
    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    filter_words = input("Введите ключевые слова или фразы для фильтрации вакансий через запятую: ")
    salary_range = input("Введите диапазон зарплат(пример: 100000-150000): ")

    # Создание экземпляра класса для работы с API сайтов с вакансиями
    hh_api = HeadHunterAPI()

    # Получение вакансий с hh.ru в формате JSON
    hh_vacancies = hh_api.get_vacancies(search_query, per_page)

    # Преобразование набора данных из JSON в список экземпляров класса Vacancy
    vacancies_list = cast_hh_to_object_list(hh_vacancies)

    # Запись в файл полученных данных
    json_saver.add_vacancy_to_json(vacancies_list)

    # Получение данных по указанным критериям
    filter_vacancies_list = get_vacancy_words(vacancies_list, filter_words)

    # Фильтрация вакансий по зарплате
    ranged_vacancies = get_vacancies_by_salary(filter_vacancies_list, salary_range)

    # Сортировка вакансий по зарплате
    sorted_vacancies = sort_vacancies(ranged_vacancies)

    # Топ вакансий
    top_vacancies = get_top_vacancies(sorted_vacancies, top_n)

    # Вывод вакансий в консоль
    print_vacancies(top_vacancies)


if __name__ == '__main__':
    user_interaction()
