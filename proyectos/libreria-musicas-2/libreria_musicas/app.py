from flask import Flask
from .controllers.controller import bp, index, save
from werkzeug.middleware.proxy_fix import ProxyFix

app = Flask(__name__.split('.')[0])
app.register_blueprint(bp)
app.add_url_rule('/', endpoint=index)

app.wsgi_app = ProxyFix(
    app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1
)

@app.teardown_appcontext(save)

def main():
    pass

if __name__ == "__main__":
    main()