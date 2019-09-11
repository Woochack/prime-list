from flask import Flask

app = Flask(__name__)


@app.route('/<int:num>')
def get_list(num):
    primes = []
    for prime in range(1, num):
        if prime > 1:
            for i in range(2, prime):
                if (prime % i) == 0:
                    break
            else:
                primes.append(prime)
    return {'Prime numbers in given range are as follows': primes}


if __name__ == '__main__':
    app.run(debug=True)
