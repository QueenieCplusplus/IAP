

from auth import user
from flask import Flask, render_template, request

app = Flask(__name__)


# Disable browser caching so changes in each step are always shown
@app.after_request
def set_response_headers(response):
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response

@app.route('/', methods=['GET'])
def say_hello():
    user_email = request.headers.get('X-Goog-Authenticated-User-Email')
    user_id = request.headers.get('X-Goog-Authenticated-User-ID')

    verified_email, verified_id = user()

    page = render_template('index.html',
        email=user_email,
        id=user_id,
        verified_email=verified_email,
        verified_id=verified_id)
    return page

@app.route('/privacy', methods=['GET'])
def show_policy():
    page = render_template('privacy.html')
    return page


if __name__ == '__main__':
    # This is used when running locally, only to verify it does not have
    # significant errors. It cannot demonstrate restricting access using
    # Identity-Aware Proxy when run locally, only when deployed.
    #
    # When deploying to Google App Engine, a webserver process such as
    # Gunicorn will serve the app. This can be configured by adding an
    # `entrypoint` to app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
