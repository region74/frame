from flask import Flask, render_template
from tools import table_number

app = Flask(__name__)


@app.route('/')
def display_pivot_table():
    pivot_table = table_number()
    table_html = pivot_table.to_html(classes='table table-striped table-bordered')
    return render_template('first.html',table=table_html)

if __name__ == '__main__':
    app.run(debug=True)
