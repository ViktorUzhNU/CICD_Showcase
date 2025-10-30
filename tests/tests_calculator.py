from app import app

def test_addition():
    client = app.test_client()
    response = client.post('/', data={'num1': '5', 'num2': '3', 'operation': 'add'})
    assert b'Result: 8.0' in response.data

def test_division_by_zero():
    client = app.test_client()
    response = client.post('/', data={'num1': '10', 'num2': '0', 'operation': 'divide'})
    assert b'division by zero' in response.data.lower()