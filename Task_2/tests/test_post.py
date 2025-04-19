import pytest
import requests

BASE_URL = "https://qa-internship.avito.com/api/1/item"

# Тест-кейс 1: Позитивный, корректные данные
@pytest.mark.parametrize("payload", [
    {
        "sellerID": 344623, 
        "name": "Ноутбук Мощный", 
        "price": 80401,
        "statistics": {
            "likes": 678,
            "viewCount": 5000,
            "contacts": 4
        }
    }])

def test_post_valid_ad(payload):
    response = requests.post(BASE_URL, json=payload, headers={"Content-Type": "application/json", "Accept": "application/json"})
    assert response.status_code == 200
    data = response.json()
    assert "status" in data

    # Тест-кейс 2: Негативный, использование GET вместо POST
def test_post_invalid_method():
    response = requests.get(BASE_URL, headers={"Accept": "application/json"})
    assert response.status_code == 405

    # Тест-кейс 3: Позитивный, без идентификатора продавца
@pytest.mark.parametrize("payload", [
    {
        "name": "Ноутбук Мощный", 
        "price": 80401,
        "statistics": {
            "likes": 678,
            "viewCount": 5000,
            "contacts": 4
        }
    }])
def test_post_missing_sellerID(payload):
    response = requests.post(BASE_URL, json=payload, headers={"Content-Type": "application/json", "Accept": "application/json"})
    assert response.status_code == 200

# Тест-кейс 4: Позитивный, без названия товара
@pytest.mark.parametrize("payload", [
    {
        "sellerID": 344673, 
        "price": 80401,
        "statistics": {
            "likes": 678,
            "viewCount": 5000,
            "contacts": 4
        }
    }])
def test_post_missing_name(payload):
    response = requests.post(BASE_URL, json=payload, headers={"Content-Type": "application/json", "Accept": "application/json"})
    assert response.status_code == 200

# Тест-кейс 5: Позитивный, без стоимости товара
@pytest.mark.parametrize("payload", [
    {
        "sellerID": 344673, 
        "name": "Ноутбук Мощный",
        "statistics": {
            "likes": 678,
            "viewCount": 5000,
            "contacts": 4
        }
    }])
def test_post_missing_price(payload):
    response = requests.post(BASE_URL, json=payload, headers={"Content-Type": "application/json", "Accept": "application/json"})
    assert response.status_code == 200

# Тест-кейс 6: Негативный, отрицательная стоимость
@pytest.mark.parametrize("payload", [
    {
        "sellerID": 344673, 
        "name": "Ноутбук Мощный", 
        "price": -80401,
        "statistics": {
            "likes": 678,
            "viewCount": 5000,
            "contacts": 4
        }
    }])
def test_post_negative_price(payload):
    response = requests.post(BASE_URL, json=payload, headers={"Content-Type": "application/json", "Accept": "application/json"})
    assert response.status_code == 200

# Тест-кейс 7: Негативный, некорректный идентификатор продавца
@pytest.mark.parametrize("payload", [
    {
        "sellerID": -344673, 
        "name": "Ноутбук Мощный", 
        "price": 80401,
        "statistics": {
            "likes": 678,
            "viewCount": 5000,
            "contacts": 4
        }
    }])
def test_post_invalid_sellerID(payload):
    response = requests.post(BASE_URL, json=payload, headers={"Content-Type": "application/json", "Accept": "application/json"})
    assert response.status_code == 200

# Тест-кейс 8: Негативный, некорректное имя товара
@pytest.mark.parametrize("payload", [
    {
        "sellerID": 344673, 
        "name": 332, 
        "price": 80401,
        "statistics": {
            "likes": 678,
            "viewCount": 5000,
            "contacts": 4
        }
    }])
def test_post_invalid_name(payload):
    response = requests.post(BASE_URL, json=payload, headers={"Content-Type": "application/json", "Accept": "application/json"})
    assert response.status_code == 400

# Тест-кейс 9: Негативный, строковый идентификатор продавца
@pytest.mark.parametrize("payload", [
    {
        "sellerID": "344673", 
        "name": "Ноутбук Мощный", 
        "price": 80401,
        "statistics": {
            "likes": 678,
            "viewCount": 5000,
            "contacts": 4
        }
    }])
def test_post_string_sellerID(payload):
    response = requests.post(BASE_URL, json=payload, headers={"Content-Type": "application/json", "Accept": "application/json"})
    assert response.status_code == 400

# Тест-кейс 10: Негативный, строковая стоимость
@pytest.mark.parametrize("payload", [
    {
        "sellerID": 344673, 
        "name": "Ноутбук Мощный", 
        "price": "80401",
        "statistics": {
            "likes": 678,
            "viewCount": 5000,
            "contacts": 4
        }
    }])
def test_post_string_price(payload):
    response = requests.post(BASE_URL, json=payload, headers={"Content-Type": "application/json", "Accept": "application/json"})
    assert response.status_code == 400

        # Тест-кейс 11: Негативный, строковое значение лайков
@pytest.mark.parametrize("payload", [
    {
        "sellerID": 344673, 
        "name": "Ноутбук Мощный", 
        "price": 80401,
        "statistics": {
            "likes": "678",
            "viewCount": 5000,
            "contacts": 4
        }
    }])
def test_post_string_price(payload):
    response = requests.post(BASE_URL, json=payload, headers={"Content-Type": "application/json", "Accept": "application/json"})
    assert response.status_code == 400

        # Тест-кейс 12: Негативный, строковое значение просмотров
@pytest.mark.parametrize("payload", [
    {
        "sellerID": 344673, 
        "name": "Ноутбук Мощный", 
        "price": 80401,
        "statistics": {
            "likes": 678,
            "viewCount": "5000",
            "contacts": 4
        }
    }])
def test_post_string_price(payload):
    response = requests.post(BASE_URL, json=payload, headers={"Content-Type": "application/json", "Accept": "application/json"})
    assert response.status_code == 400

        # Тест-кейс 13: Негативный, строковое значение контактов
@pytest.mark.parametrize("payload", [
    {
        "sellerID": 344673, 
        "name": "Ноутбук Мощный", 
        "price": 80401,
        "statistics": {
            "likes": 678,
            "viewCount": 5000,
            "contacts": "4"
        }
    }])
def test_post_string_price(payload):
    response = requests.post(BASE_URL, json=payload, headers={"Content-Type": "application/json", "Accept": "application/json"})
    assert response.status_code == 400

    # Тест-кейс 14: Негативный, отрицательное количество лайков
@pytest.mark.parametrize("payload", [
    {
        "sellerID": 344673, 
        "name": "Ноутбук Мощный", 
        "price": 80401,
        "statistics": {
            "likes": -678,
            "viewCount": 5000,
            "contacts": 4
        }
    }])
def test_post_string_price(payload):
    response = requests.post(BASE_URL, json=payload, headers={"Content-Type": "application/json", "Accept": "application/json"})
    assert response.status_code == 400

        # Тест-кейс 15: Негативный, отрицательное количество просмотров
@pytest.mark.parametrize("payload", [
    {
        "sellerID": 344673, 
        "name": "Ноутбук Мощный", 
        "price": 80401,
        "statistics": {
            "likes": 678,
            "viewCount": -5000,
            "contacts": 4
        }
    }])
def test_post_string_viewCount(payload):
    response = requests.post(BASE_URL, json=payload, headers={"Content-Type": "application/json", "Accept": "application/json"})
    assert response.status_code == 400

        # Тест-кейс 16: Негативный, отрицательное количество контактов
@pytest.mark.parametrize("payload", [
    {
        "sellerID": 344673, 
        "name": "Ноутбук Мощный", 
        "price": 80401,
        "statistics": {
            "likes": 678,
            "viewCount": 5000,
            "contacts": -4
        }
    }])
def test_post_string_contacts(payload):
    response = requests.post(BASE_URL, json=payload, headers={"Content-Type": "application/json", "Accept": "application/json"})
    assert response.status_code == 400

