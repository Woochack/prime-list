from flask import Flask, render_template
from flask_paginate import Pagination, get_page_args
import math

app = Flask(__name__)
app.template_folder = ''


@app.route('/<int:num>')
def paginate_list(num):
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


def get_primes(num, offset=1, per_page=10):
    primes = get_list(num)
    return primes[offset: offset + per_page]


def get_list(num):
    primes = []
    for prime in range(1, num):
        if prime > 1:
            for i in range(2, prime):
                if (prime % i) == 0:
                    break
            else:
                primes.append(prime)

    return primes


if __name__ == '__main__':
    app.run(debug=True)
