
from flask import Flask

owca = Flask(__name__)


@owca.route('/')
def index():
    return 'Cześć, tu Python! Wyświetlam napis'

if __name__ == '__main__':
    owca.run(debug=True)