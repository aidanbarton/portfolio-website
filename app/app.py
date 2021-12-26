from flask import Flask, render_template, redirect, url_for, abort
from os import listdir

from library import Library

app = Flask(__name__)
app.url_map.strict_slashes = False

home_dir = '/root/portfolio-website/app'
library_path = '/static/photos/gallery/'
galleries = (
    'oil',
    'water',
    'charcoal',
    'draw',
    'sketch',
)
library = Library(home_dir, library_path, galleries)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
   return render_template('about.html')

@app.route('/gallery')
def gallery():
    return render_template('gallery.html',
                            library=library.libraries)

@app.route('/gallery/<name>')
def gallery_name(name):
    lib = get_libraries()
    if name not in lib:
        return abort(404)

    return render_template('gallery-name.html',
                            gallery_name=name,
                            gallery=library.libraries[name])

@app.route('/gallery/<name>/<item>')
def gallery_name_item(name, item):
    lib = get_libraries()
    if name not in library.libraries:
        return abort(404)

    if item not in library.libraries[name]:
        return abort(404)

    return render_template('gallery-item.html',
                        item=library.libraries[name][item])

    return abort(404)


if __name__ == '__main__':
    app.run()
