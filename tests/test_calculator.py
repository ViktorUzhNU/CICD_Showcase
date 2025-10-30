from ..app import app

def test_addition():
    client = app.test_client()
    response = client.post('/', data={'num1': '5', 'num2': '3', 'operation': 'add'})
    html = response.data.decode('utf-8')
    assert 'Результат: 8.0' in html

def test_division_by_zero():
    client = app.test_client()
    response = client.post('/', data={'num1': '10', 'num2': '0', 'operation': 'divide'})
    html = response.data.decode('utf-8')
    assert 'Помилка: ділення на нуль' in html