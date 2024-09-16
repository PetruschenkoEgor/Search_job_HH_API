from abc import ABC, abstractmethod


class ApiVacancy(ABC):
    """Абстрактный класс(взаимодействия с API)"""

    @abstractmethod
    def connect_to_api(self):
        """Абстрактный метод. Подключение к API"""
        pass

    @abstractmethod
    def get_vacancies(self, word, per_page):
        """Абстрактный метод. Получение вакансий в формате JSON"""
        pass


class Files(ABC):
    """Абстрактный класс(взаимодействие с файлами)"""

    @abstractmethod
    def add_vacancy_to_json(self, obj):
        """Абстрактный метод(добавление вакансий в файл)"""
        pass

    @abstractmethod
    def get_vacancy_from_json(self, words):
        """Абстрактный метод(получение данных из файла по указанным критериям)"""
        pass

    @abstractmethod
    def delete_vacancy_from_json(self):
        """Абстрактный метод(удаление информации о вакансиях из файла)"""
        pass
