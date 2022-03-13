#!/usr/bin/env python
import time
import flask


app = flask.Flask(__name__)


@app.after_request
def set_response_headers(response):
    """ Ensures no cache """
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    response.headers['server'] = 'nginx'
    return response


@app.route('/wplogin.cgi')
def wplogin():

    response_str = "Not Found\n\r"

    def generate(response_str):
        while True:
            yield response_str
            time.sleep(5)

    return flask.Response(flask.stream_with_context(generate(response_str)), mimetype='text/html')


# if __name__ == "__main__":
#     app.run(host='0.0.0.0', port=8080)
