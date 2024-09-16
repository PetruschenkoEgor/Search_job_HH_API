import json
import os
from typing import Any

from src.abstract_class import Files
from src.vacancy import Vacancy

PATH_TO_FILE = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "vacancy.json")


class JSONSaver(Files):
    """Взаимодействие с файлами"""

    def __init__(self, file):
        """Конструктор класса JSONSaver"""
        self.__file = file

    @staticmethod
    def transformation_vacancy(obj: list[Vacancy] | Vacancy) -> list[dict[str, Any]]:
        """Преобразование экземпляра класса Vacancy/списка экземпляров класса Vacancy
        для записи в JSON-файл(список словарей)"""
        list_dict = []

        # Если на вход подается экземпляр класса Vacancy, преобразуем его в список
        if isinstance(obj, Vacancy):
            obj = [obj]

        for vacancy in obj:
            dict_obj = {
                "name": vacancy.name,
                "area": vacancy.area,
                "link": vacancy.link,
                "description": vacancy.description,
                "requirements": vacancy.requirements,
                "salary_from": vacancy.salary_from,
                "salary_to": vacancy.salary_to,
            }
            list_dict.append(dict_obj)

        return list_dict

    def checking_for_duplication(self, obj: list | Vacancy) -> list[dict]:
        """Проверка на дублирование вакансий в файле"""
        # Загружаем вакансии из файла
        vacancies_from_file = self.get_from_json()
        obj = self.transformation_vacancy(obj)

        # Если json-файл изначально пустой
        if not vacancies_from_file:

            # Инициализируем пустые множество и список
            unique_links = set()
            filtered_obj = []

            # Проверяем уникальная ли вакансия
            for link in obj:
                if link.get("link") not in unique_links:
                    filtered_obj.append(link)
                    unique_links.add(link.get("link"))
            # return unique_links
            sorted_list = sorted(filtered_obj, key=lambda x: x.get("salary_to"))
            return sorted(sorted_list, key=lambda x: x.get("salary_from"))
        # Если json-файл изначально не пустой
        else:
            # Соединяем оба списка в один(полученный из JSON-файла и добавляемый к нему)
            list_vacancy = vacancies_from_file + obj

            # Инициализируем пустые множество и список
            unique_links = set()
            vacancies = []

            # Проверяем уникальная ли вакансия
            for link in list_vacancy:
                if link.get("link") not in unique_links:
                    vacancies.append(link)
                    unique_links.add(link.get("link"))
            # return unique_links
            sorted_list = sorted(vacancies, key=lambda x: x.get("salary_to"))
            return sorted(sorted_list, key=lambda x: x.get("salary_from"))

    def add_vacancy_to_json(self, obj: list | Vacancy) -> None:
        """Добавление вакансии в файл"""
        vacancy = self.checking_for_duplication(obj)
        self.delete_vacancy_from_json()

        with open(self.__file, "a", encoding="utf-8") as outfile:
            json.dump(vacancy, outfile, ensure_ascii=False, indent=4)

    def get_from_json(self) -> list[dict[str | int]]:
        """Получение данных из файла"""
        try:
            with open(self.__file, "r", encoding="utf-8") as file:
                data = json.load(file)

            return data
        # Если файл пустой
        except json.decoder.JSONDecodeError:
            return []
        # Если файл не найден
        except FileNotFoundError:
            return []

    def get_vacancy_from_json(self, words: str) -> list[dict[str | int]]:
        """Получение данных из файла по указанным критериям"""
        data_list = []
        # Получение данных из JSON-файла
        data = self.get_from_json()

        # Преобразуем критерии поиска в список
        words = words.lower().split(",")

        # Ищем в списке словарей совпадения с введенными критериями поиска
        for word in words:
            for vacancy in data:
                for key, value in vacancy.items():
                    if word in str(value).lower() and vacancy not in data_list:
                        data_list.append(vacancy)

        return data_list

    def delete_vacancy_from_json(self):
        """Удаление информации о вакансиях из файла"""
        with open(self.__file, "w"):
            pass
