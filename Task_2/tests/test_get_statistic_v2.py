import pytest
import requests
import re

BASE_URL_v1 = "https://qa-internship.avito.com/api/1/item"
BASE_URL = "https://qa-internship.avito.com/api/2"
ITEM_URL = f"{BASE_URL}/item"
STATISTIC_URL = f"{BASE_URL}/statistic"
HEADERS = {
    "Content-Type": "application/json", 
    "Accept": "application/json"
}

@pytest.fixture
def test_ad_data():
    """Фикстура с тестовыми данными объявления"""
    return {
        "sellerID": 344623,
        "name": "Тестовый ноутбук",
        "price": 10000,
        "statistics": {
            "likes": 150,
            "viewCount": 750,
            "contacts": 25
        }
    }

@pytest.fixture
def created_ad_id(test_ad_data):
    """Создает объявление и возвращает его ID"""
    response = requests.post(BASE_URL_v1, json=test_ad_data, headers=HEADERS)
    assert response.status_code == 200, f"Ошибка создания объявления: {response.text}"
    
    data = response.json()
    match = re.search(r"Сохранили объявление - (.+)$", data["status"])
    assert match, "Не удалось извлечь ID объявления"
    ad_id = match.group(1)
    
    yield ad_id
    
    # Удаление объявления после теста
    requests.delete(f"{ITEM_URL}/{ad_id}", headers={"Accept": "application/json"})

def get_statistics_with_retry(ad_id, retries=3):
    """Повторные попытки получить статистику"""
    for _ in range(retries):
        response = requests.get(f"{STATISTIC_URL}/{ad_id}", headers={"Accept": "application/json"})
        if response.status_code == 200:
            return response.json()
    pytest.fail(f"Не удалось получить статистику после {retries} попыток")

# Тест-кейс 1: Позитивные тесты проверки статистики созданного объявления
class TestPositiveStatistics:
    def test_check_contacts(self, created_ad_id, test_ad_data):
        """Проверка количества контактов"""
        stats = get_statistics_with_retry(created_ad_id)
        assert stats[0]["contacts"] == test_ad_data["statistics"]["contacts"]

    def test_check_likes(self, created_ad_id, test_ad_data):
        """Проверка количества лайков"""
        stats = get_statistics_with_retry(created_ad_id)
        assert stats[0]["likes"] == test_ad_data["statistics"]["likes"]

    def test_check_views(self, created_ad_id, test_ad_data):
        """Проверка количества просмотров"""
        stats = get_statistics_with_retry(created_ad_id)
        assert stats[0]["viewCount"] == test_ad_data["statistics"]["viewCount"]


# Тест-кейс 2: Негативные тесты с невалидными ID
class TestInvalidIds:
    @pytest.mark.parametrize("invalid_id,expected_code", [
        (None, 400),                  # Null ID
        ("%00", 400),                 # Null byte
        ("invalid_id", 400),          # Неверный формат
        ("nonexistent-id-123", 400),  # Несуществующий ID
        (" " + "eeaded93-1634-448e-9f8a-72e14763da70", 400)  # ID с пробелом
    ])
    def test_invalid_statistic_requests(self, invalid_id, expected_code):
        """Тесты для невалидных запросов статистики"""
        response = requests.get(f"{STATISTIC_URL}/{invalid_id}", 
                              headers={"Accept": "application/json"})
        assert response.status_code == expected_code

# Тест-кейс 3: Тесты неверных методов запроса
class TestWrongMethods:
    def test_post_method(self, created_ad_id):
        """Тест неверного метода POST"""
        response = requests.post(f"{STATISTIC_URL}/{created_ad_id}", headers=HEADERS)
        assert response.status_code == 405

    def test_put_method(self, created_ad_id):
        """Тест неверного метода PUT"""
        response = requests.put(f"{STATISTIC_URL}/{created_ad_id}", headers=HEADERS)
        assert response.status_code == 405

    def test_delete_method(self, created_ad_id):
        """Тест неверного метода DELETE"""
        response = requests.delete(f"{STATISTIC_URL}/{created_ad_id}", headers=HEADERS)
        assert response.status_code == 405

# Тест-кейс 4: Тесты формата ответа
class TestResponseFormat:
    def test_response_structure(self, created_ad_id):
        """Проверка структуры ответа"""
        stats = get_statistics_with_retry(created_ad_id)
        assert isinstance(stats, list)
        assert all(key in stats[0] for key in ["likes", "viewCount", "contacts"])

    def test_response_content_type(self, created_ad_id):
        """Проверка Content-Type ответа"""
        response = requests.get(f"{STATISTIC_URL}/{created_ad_id}", 
                              headers={"Accept": "application/json"})
        assert response.headers["Content-Type"] == "application/json"