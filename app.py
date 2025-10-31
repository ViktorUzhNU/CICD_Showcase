from flask import Flask, request, render_template_string

app = Flask(__name__)

HTML = '''
<form method="POST">
    <input type="number" name="num1" required placeholder="Число 1">
    <select name="operation">
        <option value="add">+</option>
        <option value="subtract">-</option>
        <option value="multiply">×</option>
        <option value="divide">÷</option>
    </select>
    <input type="number" name="num2" required placeholder="Число 2">
    <input type="submit" value="Обчислити">
</form>
{% if result is not none %}
    <h3>Результат: {{ result }}</h3>
{% endif %}
'''

@app.route('/', methods=['GET', 'POST'])
def calculator():
    result = None
    if request.method == 'POST':
        try:
            num1 = float(request.form['num1'])
            num2 = float(request.form['num2'])
            operation = request.form['operation']
            
            if operation == 'add':
                result = num1 + num2 + 1
            elif operation == 'subtract':
                result = num1 - num2
            elif operation == 'multiply':
                result = num1 * num2
            elif operation == 'divide':
                result = num1 / num2 if num2 != 0 else 'Помилка: ділення на нуль'
        except:
            result = 'Помилка вводу'
    
    return render_template_string(HTML, result=result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)