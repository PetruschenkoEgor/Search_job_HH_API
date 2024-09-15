import pytest

from src.vacancy import Vacancy


@pytest.fixture
def get_json():
    return {'items': [{'id': '94216601', 'premium': False, 'name': 'Менеджер (стажер)', 'department': None, 'has_test': False, 'response_letter_required': False, 'area': {'id': '2', 'name': 'Санкт-Петербург', 'url': 'https://api.hh.ru/areas/2'}, 'salary': {'from': None, 'to': 86000, 'currency': 'RUR', 'gross': False}, 'type': {'id': 'open', 'name': 'Открытая'}, 'address': {'city': 'Санкт-Петербург', 'street': 'улица Ефимова', 'building': '4', 'lat': 59.925692, 'lng': 30.322318, 'description': None, 'raw': 'Санкт-Петербург, улица Ефимова, 4', 'metro': {'station_name': 'Садовая', 'line_name': 'Фрунзенско-Приморская', 'station_id': '18.250', 'line_id': '18', 'lat': 59.926739, 'lng': 30.317753}, 'metro_stations': [{'station_name': 'Садовая', 'line_name': 'Фрунзенско-Приморская', 'station_id': '18.250', 'line_id': '18', 'lat': 59.926739, 'lng': 30.317753}, {'station_name': 'Сенная площадь', 'line_name': 'Московско-Петроградская', 'station_id': '15.218', 'line_id': '15', 'lat': 59.927135, 'lng': 30.320316}, {'station_name': 'Спасская', 'line_name': 'Правобережная', 'station_id': '17.237', 'line_id': '17', 'lat': 59.927135, 'lng': 30.320316}], 'id': '3827648'}, 'response_url': None, 'sort_point_distance': None, 'published_at': '2024-09-13T10:31:50+0300', 'created_at': '2024-09-13T10:31:50+0300', 'archived': False, 'apply_alternate_url': 'https://hh.ru/applicant/vacancy_response?vacancyId=94216601', 'branding': {'type': 'MAKEUP', 'tariff': None}, 'show_logo_in_search': True, 'insider_interview': None, 'url': 'https://api.hh.ru/vacancies/94216601?host=hh.ru', 'alternate_url': 'https://hh.ru/vacancy/94216601', 'relations': [], 'employer': {'id': '2748', 'name': 'Ростелеком', 'url': 'https://api.hh.ru/employers/2748', 'alternate_url': 'https://hh.ru/employer/2748', 'logo_urls': {'240': 'https://img.hhcdn.ru/employer-logo/2812976.jpeg', '90': 'https://img.hhcdn.ru/employer-logo/2812975.jpeg', 'original': 'https://img.hhcdn.ru/employer-logo-original/592930.jpg'}, 'vacancies_url': 'https://api.hh.ru/vacancies?employer_id=2748', 'accredited_it_employer': False, 'trusted': True}, 'snippet': {'requirement': 'Нам не важен твой опыт работы, мы готовы быстро обучить. Но нам нужны твои амбиции, желание расти, постоянно обучаться и...', 'responsibility': 'Консультировать клиентов по услугам компании (интернет, телевидение, сотовая связь, видеонаблюдение). Принимать заявки на подключение. Готовы изучать и учиться новому.'}, 'contacts': None, 'schedule': {'id': 'flexible', 'name': 'Гибкий график'}, 'working_days': [], 'working_time_intervals': [{'id': 'from_four_to_six_hours_in_a_day', 'name': 'Можно сменами по\xa04-6\xa0часов в\xa0день'}], 'working_time_modes': [{'id': 'start_after_sixteen', 'name': 'С\xa0началом дня после 16:00'}], 'accept_temporary': True, 'professional_roles': [{'id': '70', 'name': 'Менеджер по продажам, менеджер по работе с клиентами'}], 'accept_incomplete_resumes': True, 'experience': {'id': 'noExperience', 'name': 'Нет опыта'}, 'employment': {'id': 'probation', 'name': 'Стажировка'}, 'adv_response_url': None, 'is_adv_vacancy': False, 'adv_context': None}]}


@pytest.fixture
def vacancy():
    return Vacancy("Разработчик", "Москва", "http:...", "Описание", "Требования", 10000, 20000)


@pytest.fixture
def vacancy1():
    return Vacancy("Разработчик1", "Москва", "http:...", "Описание", "Требования", 30000, 40000)
