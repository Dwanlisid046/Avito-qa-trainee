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


class TestDeleteItem:
    # ===== Test Case 1: Удаление существующего объявления =====
    def test_delete_existing_item(self, created_ad_id):
        response = requests.delete(
            f"{ITEM_URL}/{created_ad_id}",
            headers={"Accept": "application/json"}
        )
        assert response.status_code == 200

    # ===== Test Case 2: Попытка удаления с невалидными ID =====
    @pytest.mark.parametrize("invalid_id, expected_code", [
        (None, 400),                  # TC-2.1: Null ID
        ("invalid_id", 400),          # TC-2.2: Неверный формат UUID
        ("nonexistent-id-123", 400),  # TC-2.3: Несуществующий ID (некорректный формат)
        (" " + "3aebf338-a9b6-4c0b-8f95-c6f1f4ae7374", 400),  # TC-2.4: ID с пробелом
        ("", 404),                    # TC-2.5: Пустой ID
    ])
    def test_delete_with_invalid_ids(self, invalid_id, expected_code):
        """TC-2: Попытка удаления с невалидными ID (ожидается 400/404)"""
        response = requests.delete(
            f"{ITEM_URL}/{invalid_id}",
            headers={"Accept": "application/json"}
        )
        assert response.status_code == expected_code

    # ===== Test Case 3: Повторное удаление уже удаленного объявления =====
    def test_delete_already_deleted_item(self, created_ad_id):
        # Первое удаление (должно пройти успешно)
        response = requests.delete(
            f"{ITEM_URL}/{created_ad_id}",
            headers={"Accept": "application/json"}
        )
        assert response.status_code == 200

        # Второе удаление (должно вернуть 404)
        response = requests.delete(
            f"{ITEM_URL}/{created_ad_id}",
            headers={"Accept": "application/json"}
        )
        assert response.status_code == 404

    # ===== Test Case 4: Неверные HTTP-методы для удаления =====
    def test_delete_with_wrong_methods(self, created_ad_id):
        # TC-4.1: GET запрос (должен вернуть 405)
        response = requests.get(
            f"{ITEM_URL}/{created_ad_id}",
            headers={"Accept": "application/json"}
        )
        assert response.status_code == 405

        # TC-4.2: POST запрос (должен вернуть 405)
        response = requests.post(
            f"{ITEM_URL}/{created_ad_id}",
            headers={"Accept": "application/json"},
            json={"name": "Should not work"}
        )
        assert response.status_code == 405

        # TC-4.3: PUT запрос (должен вернуть 405)
        response = requests.put(
            f"{ITEM_URL}/{created_ad_id}",
            headers={"Accept": "application/json"},
            json={"name": "Should not work"}
        )
        assert response.status_code == 405