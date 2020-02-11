from flask import Flask

import utils

app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello():
    """"""
    print('Received Request at index!')
    count = utils.update_and_get_hit_count()
    return f'Hello Shukuji, I have been seen "{count}" times!'


@app.route('/clear', methods=['GET'])
def clear_hits():
    """"""
    print('Received request at /clear')
    response = utils.clear_hit_count()
    print('Hits counter cleared!')
    return f'Hello Shukuji, I have reset the count. Response is: "{response}"'
