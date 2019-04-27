from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello Azure Platform!'


@app.route('/endpoint0')
def endpoint_zero():
    return render_template('AzureEndpointFlaskTest.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0")
