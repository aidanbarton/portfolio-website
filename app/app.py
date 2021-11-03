from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)
app.url_map.strict_slashes = False

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/gallery')
def exper():
    return render_template('gallery.html')


if __name__ == '__main__':
    app.run()
