from datetime import datetime
from api.load import start_import
from flask import Flask, render_template, request
from tools import table_number, table_opener, table_time_day, table_opener_number, table_opener_time

app = Flask(__name__)


# TODO надо переделать, чтобы при каждом обновлении он не шел в api
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Получаем данные из формы
        start_date = request.form["start_date"]
        end_date = request.form["end_date"]
        print(start_date)
        print(end_date)

        date_object = datetime.strptime(start_date, '%Y-%m-%d').date()
        start_date = date_object.strftime('%d-%m-%Y')

        date_object = datetime.strptime(end_date, '%Y-%m-%d').date()
        end_date = date_object.strftime('%d-%m-%Y')

        # Вызываем функцию для получения данных с api
        start_import(start_date, end_date)
        return render_template("index.html")

    # Если запрос GET, показываем форму выбора даты
    return render_template("index.html")


@app.route('/numbers')
def show_numbers():
    pivot_table = table_number()
    table_html = pivot_table.to_html(classes='table table-striped table-bordered')
    return render_template('numbers.html', table=table_html)


@app.route('/openers')
def show_openeres():
    pivot_table = table_opener()
    table_html = pivot_table.to_html(classes='table table-striped table-bordered')
    return render_template('openers.html', table=table_html)


@app.route('/hours')
def show_hours():
    pivot_table = table_time_day()
    table_html = pivot_table.to_html(classes='table table-striped table-bordered')
    return render_template('hours.html', table=table_html)


@app.route('/openernumber')
def show_opener_number():
    pivot_table = table_opener_number(2)
    table_html = pivot_table.to_html(classes='table table-striped table-bordered')
    return render_template('openernumber.html', table=table_html)


@app.route('/openerhours')
def show_opener_hours():
    pivot_table = table_opener_time(2)
    table_html = pivot_table.to_html(classes='table table-striped table-bordered')
    return render_template('openerhours.html', table=table_html)


if __name__ == '__main__':
    app.run(debug=True)
