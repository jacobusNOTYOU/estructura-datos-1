from flask import Flask
from .controllers.controller import bp, index, save

app = Flask(__name__.split('.')[0])
app.register_blueprint(bp)
app.add_url_rule('/', endpoint=index)

@app.teardown_appcontext(save)

def main():
    pass

if __name__ == "__main__":
    main()