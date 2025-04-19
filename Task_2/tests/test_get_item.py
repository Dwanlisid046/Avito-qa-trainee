import pytest
import requests
import re

BASE_URL = "https://qa-internship.avito.com/api/1"
DEL_URL = "https://qa-internship.avito.com/api/2/item"
ITEM_URL = f"{BASE_URL}/item"
HEADERS = {
    "Content-Type": "application/json", 
    "Accept": "application/json"
}

@pytest.fixture
def test_ad_data():
    return {
        "sellerId": 789472,
        "name": "Ноутбук Мощный, Красивый, Косынку тянет",
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
    response = requests.post(f"{BASE_URL}/item", json=test_ad_data, headers=HEADERS)
    assert response.status_code == 200, f"Ошибка создания объявления: {response.text}"
    
    data = response.json()
    match = re.search(r"Сохранили объявление - (.+)$", data["status"])
    assert match, "Не удалось извлечь ID объявления"
    ad_id = match.group(1)
    
    yield ad_id
    
    # Удаление объявления после теста
    requests.delete(f"{DEL_URL}/{ad_id}", headers={"Accept": "application/json"})

def get_statistics_with_retry(ad_id, retries=3):
    """Повторные попытки получить статистику"""
    for _ in range(retries):
        response = requests.get(f"{ITEM_URL}/{ad_id}", headers={"Accept": "application/json"})
        if response.status_code == 200:
            return response.json()

# Тест-кейс 1: Позитивные тесты проверка JSON ответа
class TestPositiveStatistics:
    def test_check_sellerId(self, created_ad_id, test_ad_data):
        stats = get_statistics_with_retry(created_ad_id)
        assert stats[0]["sellerId"] == test_ad_data["sellerId"]

    def test_check_name(self, created_ad_id, test_ad_data):
        stats = get_statistics_with_retry(created_ad_id)
        assert stats[0]["name"] == test_ad_data["name"]

    def test_check_price(self, created_ad_id, test_ad_data):
        stats = get_statistics_with_retry(created_ad_id)
        assert stats[0]["price"] == test_ad_data["price"]

# Тест-кейс 2: Позитивный тест, существующий ID
@pytest.mark.parametrize("item_id", ["81ca955a-bb82-4517-be97-b9aa668c599e"])
def test_get_item_success(item_id):
    response = requests.get(f"{BASE_URL}/item/{item_id}", headers={"Accept": "application/json"})
    assert response.status_code == 200

# Тест-кейс 3: Неверный формат ID
@pytest.mark.parametrize("item_id", ["incorrect_id"])
def test_get_item_invalid_format(item_id):
    response = requests.get(f"{BASE_URL}/item/{item_id}", headers={"Accept": "application/json"})
    assert response.status_code == 400

# Тест-кейс 4: Неподдерживаемый метод
@pytest.mark.parametrize("item_id", ["81ca955a-bb82-4517-be97-b9aa668c599e"])
def test_get_item_wrong_method(item_id):
    response = requests.delete(f"{BASE_URL}/item/{item_id}", headers={"Accept": "application/json"})
    assert response.status_code == 405

# Тест-кейс 5: Нулевое значение ID
@pytest.mark.parametrize("item_id", [None])
def test_get_item_null_id(item_id):
    response = requests.get(f"{BASE_URL}/item/{item_id}", headers={"Accept": "application/json"})
    assert response.status_code == 400  

# Тест-кейс 6: ID в виде %00
@pytest.mark.parametrize("item_id", ["%00"])
def test_get_item_null_byte(item_id):
    response = requests.get(f"{BASE_URL}/item/{item_id}", headers={"Accept": "application/json"})
    assert response.status_code == 400

# Тест-кейс 7: Несуществующий ID
@pytest.mark.parametrize("item_id", ["81ca955a-bb82-4517-be97-b9aa668c5993"])
def test_get_item_not_found(item_id):
    response = requests.get(f"{BASE_URL}/item/{item_id}", headers={"Accept": "application/json"})
    assert response.status_code == 404

# Тест-кейс 8: ID без символов "-"
@pytest.mark.parametrize("item_id", ["81ca955abb824517be97b9aa668c599e"])
def test_get_item_no_dashes(item_id):
    response = requests.get(f"{BASE_URL}/item/{item_id}", headers={"Accept": "application/json"})
    assert response.status_code == 200

# Тест-кейс 9: Лишний пробел в ID
@pytest.mark.parametrize("item_id", [" 81ca955a-bb82-4517-be97-b9aa668c599e", "81ca955a-bb82-4517-be97-b9aa668c599e "])
def test_get_item_extra_space(item_id):
    response = requests.get(f"{BASE_URL}/item/{item_id.strip()} ", headers={"Accept": "application/json"})
    assert response.status_code == 400
