from flask import Flask, Response
import logging


logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)


@app.route('/chop', methods=['GET'])
def chop(find, set_to_search):
    if len(set_to_search) == 0:
        return -1


if __name__ == "__main__":
    app.run()