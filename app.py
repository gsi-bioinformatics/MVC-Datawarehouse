from flask import Flask
from src.views.catalog_entry_views import catalog_list

app = Flask(__name__)


@app.route('/catalog')
def show_catalog():
    return catalog_list()

if __name__ == '__main__':
    app.run(debug=True)

