# файл для написания чек-листа
# Данил Богучава, 15-я когорта - Финальный проект. Инженер по тестированию плюс

import order_parametrs
import data

# Создание и проверка статуса заказа
def test_status_of_order_is_200():
    response_order = order_parametrs.post_new_order(data.order_body_complete)
    track = {"t": response_order.json()["track"]}
    response = order_parametrs.getting_order_data(track)
    assert response.status_code == 200