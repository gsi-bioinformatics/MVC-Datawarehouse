from flask import render_template
from src.models.catalog_entry import CatalogEntry

def catalog_list():
    entries = CatalogEntry.get_all()
    return render_template('catalog_list.html', entries=entries)
