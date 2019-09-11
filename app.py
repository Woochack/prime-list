from flask import Flask, render_template

app = Flask(__name__)
app.template_folder = ''


@app.route('/<int:num>')
def index(num):
    primes = get_list(num)

    return render_template('index.html',
                           primes=primes)


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
