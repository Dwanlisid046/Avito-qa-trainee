# Лист1

|№|Название теста|Тип|Описание|Входные данные|Ожидаемый результат|Фактический результат|Примечания|
|---|---|---|---|---|---|---|---|
|1|test_check_contacts|Позитивный|	Проверка, что количество контактов совпадает|GET /statistic/{id} после создания объявления с contacts = 25|contacts == 25|contacts == 1|Ненормальное поведение, данные полученны неправильно|
|2|test_check_likes|Позитивный|Проверка количества лайков|	GET /statistic/{id} после создания объявления с likes = 150|likes == 150|likes == 1|Ненормальное поведение, данные полученны неправильно|
|3|test_check_views|Позитивный|Проверка количества просмотров|	GET /statistic/{id} после создания объявления с viewCount = 750|viewCount == 750|viewCount == 3|Ненормальное поведение, данные полученны неправильно|
|4|test_invalid_statistic_requests - null id|Негативный|Запрос с None в качестве ID|None|400 Bad Request|400 Bad Request|Нормальное поведение|
|5|test_invalid_statistic_requests - null byte|Негативный|Символ null byte в ID|0%|400 Bad Request|400 Bad Request|Нормальное поведение|
|6|test_invalid_statistic_requests - bad format|Негативный|Невалидная строка, не являющаяся UUID|invalid_id|400 Bad Request|400 Bad Request|Нормальное поведение|
|7|test_invalid_statistic_requests - nonexistent id|Негативный|ID с UUID-форматом, но несуществующий|nonexistent-id-123|400 Bad Request|400 Bad Request|Нормальное поведение|
|8|test_invalid_statistic_requests - whitespace|Негативный|ID начинается с пробела|' eeaded93-1634-448e-9f8a-72e14763da70'|400 Bad Request|400 Bad Request|Нормальное поведение|
|9|test_post_method|Негативный|Попытка использовать POST вместо GET|POST|405 Method Not Allowed|405 Method Not Allowed|Нормальное поведение|
|10|test_put_method|Негативный|Попытка использовать PUT|PUT|405 Method Not Allowed|405 Method Not Allowed|Нормальное поведение|
|11|test_delete_method|Негативный|Попытка использовать DELETE|DELETE|405 Method Not Allowed|405 Method Not Allowed|Нормальное поведение|
|12|test_response_structure|Позитивный|Ответ должен быть списком со всеми нужными ключами|Ответ — список, элементы которого содержат likes, viewCount, contacts|Проверка JSON структуры|Структура ответа верна|Нормальное поведение|
|13|test_response_content_type|Позитивный|Проверка, что Content-Type равен application/json|Content-Type == application/json|Проверка , что Content-Type равен application/json| Content-Type равен application/json|Нормальное поведение|
