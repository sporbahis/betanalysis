from flask import (Flask, render_template)



app = Flask(__name__)


@app.route('/')
def index():
    # Use a list here so we can do "if posts" efficiently in the template.
    return render_template('index.html')


def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()
