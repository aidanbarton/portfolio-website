from flask import Flask, render_template, redirect, url_for, abort
import os
from os import listdir

app = Flask(__name__)
app.url_map.strict_slashes = False

gallery_names = (
    'oil',
    'water',
    'charcoal',
    'draw',
    'sketch',
)
home_dir = '/root/portfolio-website/app'
gallery_path = '/static/photos/gallery/'

def get_libraries():
    libs = dict()
    for n in gallery_names:
        path = gallery_path + n + '/'
        items = list()
        for i in listdir(home_dir + path):
            item = dict()
            item['path'] = path + i
            item['name'] = i.split('.')[0]
            items.append(item)

        items.sort(reverse=True)
        libs[n] = items
    return libs

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
   return render_template('about.html')

@app.route('/gallery')
def gallery():
    return render_template('gallery.html',
                            libraries=get_libraries())

@app.route('/gallery/<name>')
def gallery_name(name):
    lib = get_libraries()
    if name not in lib:
        return abort(404)

    return render_template('gallery-name.html',
                            library_name=name,
                            library=lib[name])

@app.route('/gallery/<name>/<item>')
def gallery_name_item(name, item):
    lib = get_libraries()
    if name not in lib:
        return abort(404)

    for i in lib[name]:
        if item in i['name']:
            return render_template('gallery-item.html',
                                item=i)

    return abort(404)


if __name__ == '__main__':
    app.run()
