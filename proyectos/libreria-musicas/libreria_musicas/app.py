import sys
import json
config_path: str = (
    sys.path[0] + '/' +
    __name__.split('.')[0] +  '/' +
    '.config/config.json'
)

with open(config_path, 'r') as f:
    conf = f.read()
try:
    benchmark = json.loads(conf)['benchmark']
except:
    benchmark = False

if benchmark:
    import tracemalloc
    tracemalloc.start()

from flask import Flask
from .controllers.controller import bp, index, save
from werkzeug.middleware.proxy_fix import ProxyFix

app = Flask(__name__.split('.')[0])
app.register_blueprint(bp)
app.add_url_rule('/', endpoint=index)

app.wsgi_app = ProxyFix(
    app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1
)

if benchmark:
    filename: str = (
            sys.path[0] + '/'
            + __name__.split('.')[0]
            + '/benchmark/memory-benchmark.txt'
        )
    with open(filename, 'w') as f:
        f.write('Program Memory Usage (bytes)\n')

    def bench_memory(args):
        with open(filename, 'a') as f:
            traced = tracemalloc.get_traced_memory()
            tracemalloc.reset_peak()
            f.write(f"Current: {traced[0]} , Peak: {traced[1]}\n")
else:
    def bench_memory(args):
        return

@app.teardown_appcontext(bench_memory)

@app.teardown_appcontext(save)

def main():
    pass

if __name__ == "__main__":
    main()