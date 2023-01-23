import time
from asgiref.wsgi import WsgiToAsgi
from flask import Flask, jsonify
from aiohttp import ClientSession
import asyncio

app = Flask(__name__)


async def fetch(url):

    async with ClientSession() as client:
        async with client.get(url) as resp:
            return resp.status


async def send_requests():
    urls = [
        "https://api.github.com/gists/6a14e36729167d827dd9aae17a6b03f1",
        "https://api.github.com/gists/0dc4bc76f8f0016ea27284e9cd60ba2f",
        "https://api.github.com/gists/c0bde21cb279c492b2fe3dbf98749f77",
        "https://api.github.com/gists/b28c550684423527f0cdc889ae3377f4",
        "https://api.github.com/gists/1049602ddd0b80dd9fc868f8d4f94965",
        "https://api.github.com/gists/1e868f03f3c71e787ea6b5d630ca8e99",
        "https://api.github.com/gists/d362549b60770385e7b236b521739393",
        "https://api.github.com/gists/8e1f4174346d5cd437431b6603fbb9be",
        "https://api.github.com/gists/b52172274d7693631079dfd901f10993",
        "https://api.github.com/gists/50daee91e8d4452cfa5ebb84b2f67d41",
        "https://api.github.com/gists/eac2730e2a3c38361ed2d6730c3fb8bd",
        "https://api.github.com/gists/6a8f8b18daf742cbe8519036efd3c0bd",
        "https://api.github.com/gists/0f53d27cfeef96258386b5b18470dd10",
        "https://api.github.com/gists/7d1176afb0077ac9991bc2eb0b2a3d78",
        "https://api.github.com/gists/305494861cc3f3cc71f108fc353e0d94",
        "https://api.github.com/gists/1479d515b69b5896c188a665bae8de4f",
        "https://api.github.com/gists/0a22701329208ee0bba0584074709a9c",
        "https://api.github.com/gists/20b3f755ef11f04c8702af92c57d536c",
        "https://api.github.com/gists/f4cc4bc39b5a6f19657084b6f291f7a8",
        "https://api.github.com/gists/c6b7117dae98359cc281dfeae4e54edf",
        "https://api.github.com/gists/793e8d6c28aab2d159c33c0a2722634c",
        "https://api.github.com/gists/68f2da3d3df5eb42527fb3abb0375372",
        "https://api.github.com/gists/fbaff86c4dcf443593d1dcb1a492801c",
        "https://api.github.com/gists/5d370873a4685fe8de883f88fab21ec6",
        "https://api.github.com/gists/cb5945ae9c5bbfc50e3e4af104b3fe06",
        "https://api.github.com/gists/9e118b765043f3408cf5ba5356829780",
        "https://api.github.com/gists/fa1efdaf2c76920433321f676426eaf8",
        "https://api.github.com/gists/c559360334d6129323c97d5472b214a9",
        "https://api.github.com/gists/fab40380fa3ebe54e828fed4b6e62d32",
        "https://api.github.com/gists/f80dacf3584be2847a5d66c94183d343"
    ]

    requests = [fetch(url) for url in urls]

    results = await asyncio.gather(*requests)
    return results


@app.route("/")
async def home():
    print("working on it")
    start_time = time.time()
    data = await send_requests()
    print("--- %s seconds ---" % (time.time() - start_time))
    return jsonify(data)

"""
This sample works pretty well, using it you can sending multiples requests
in one request time, if that was required for you.

Warning: flask seems work pretty well this way but it lost a few things when
we talk about perfomance. warnings...


perfomance: https://flask.palletsprojects.com/en/2.2.x/async-await/#when-to-use-quart-instead
https://flask.palletsprojects.com/en/2.2.x/async-await/#performance

warnings: https://github.com/django/asgiref#wsgi-to-asgi-adapter
"""

asgi_app = WsgiToAsgi(app)