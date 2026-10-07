from flask import Flask
from .controllers.controller import bp, index

app = Flask(__name__.split('.')[0])
app.register_blueprint(bp)
app.add_url_rule('/', endpoint=index)

def main():
    pass

if __name__ == "__main__":
    main()