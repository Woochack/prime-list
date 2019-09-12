from flask import Flask, render_template, jsonify
from flask_paginate import Pagination, get_page_args
import math

app = Flask(__name__)
app.template_folder = ''


@app.route('/')
def get_foo():
    raise InvalidUsage('Please input the range at the end of URL to print Prime Numbers for it, '
                       'example: http://127.0.0.1:5000/1000', status_code=400)


@app.route('/<int:num>')
def paginate_list(num):
    if num > 1:
        page, per_page, offset = get_page_args(page_parameter='page',
                                               per_page_parameter='per_page')
        pagination_primes = get_primes(num, offset=offset, per_page=per_page)
        total = math.ceil(len(get_list(num)))
        pagination = Pagination(page=page, per_page=per_page, total=total,
                                css_framework='bootstrap4')
        return render_template('index.html',
                               primes=pagination_primes,
                               page=page,
                               per_page=per_page,
                               pagination=pagination,
                           )
    else:
        raise InvalidUsage('Invalid range, please input positive integer bigger than 1.', status_code=400)


def get_primes(num, offset=1, per_page=10):
    if num > 1:
        primes = get_list(num)
        return primes[offset: offset + per_page]
    elif num == 1 or num < 1:
        raise InvalidUsage('Invalid range, please input integer bigger than 1.', status_code=400)


def get_list(num):
    primes = []
    if num > 1:
        for prime in range(1, num):
            if prime > 1:
                for i in range(2, prime):
                    if (prime % i) == 0:
                        break
                else:
                    primes.append(prime)

        return primes
    elif num == 1 or num < 1:
        raise InvalidUsage('Invalid range, please input integer bigger than 1.', status_code=400)


class InvalidUsage(Exception):
    status_code = 400

    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        return rv


@app.errorhandler(InvalidUsage)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


if __name__ == '__main__':
    app.run(debug=True)
