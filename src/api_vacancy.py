import requests

from src.abstract_class import ApiVacancy


class HeadHunterAPI(ApiVacancy):
    """Взаимодействие с API, получение вакансий"""

    def __init__(self):
        """Конструктор для класса HeadHunterAPI"""
        self.__url = "https://api.hh.ru/vacancies"
        self.__headers = {"User-Agent": "HH-User-Agent"}
        self.__params = {"text": "", "page": 0, "per_page": 100}
        self.__vacancies = []

    def __connect_to_api(self):
        """Подключение к API hh.ru"""
        # Гет-запрос
        response = requests.get(self.__url, headers=self.__headers, params=self.__params)
        # Проверка на успешность запроса
        if response.status_code == 200:
            return response.json()
        else:
            return response.status_code

    @property
    def connect_to_api(self):
        """Геттер для метода отправляющего гет-запрос"""
        return self.__connect_to_api()

    def get_vacancies(self, word: str, per_page: int) -> list[dict[str | int]]:
        """Получение вакансий с hh.ru в формате JSON(как есть, не обработанные)"""
        # Если per_page > 100, то это вызовет ошибку. Условие предотвращает эту ошибку
        if per_page > 100:
            per_page = 100

        # В параметрах запроса меняем слово для поиска
        self.__params["text"] = word
        self.__params["per_page"] = per_page
        while self.__params.get("page") != 20:
            # Получение вакансий
            vacancies = self.connect_to_api["items"]
            # Добавление вакансий в список
            self.__vacancies.extend(vacancies)
            # Следующая страница
            self.__params["page"] += 1

        return self.vacancies

    @property
    def vacancies(self) -> list:
        """Геттер для вакансий"""
        return self.__vacancies
