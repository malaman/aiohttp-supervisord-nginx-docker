#! /usr/bin/env python
import argparse
from collections import Coroutine

from aiohttp import web
from aiohttp.web_request import Request
from aiohttp_swagger import setup_swagger
from aiohttp_swaggerify import swaggerify


async def health_handler(request: Request) -> Coroutine:
    """
    ---
    description: This end-point allow to test that service is up.
    tags:
    - Meta data about the service
    produces:
    - application/json
    responses:
        "200":
            description: successful operation. Returns json object with code(0) and color(green)
        "405":
            description: invalid HTTP Method
    """
    return web.json_response({'code': 0, 'color': 'green'})


def get_opts():
    parser = argparse.ArgumentParser()
    parser.add_argument('--path')
    parser.add_argument('--port')
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    args = get_opts()
    app = web.Application()
    app.add_routes([
        web.get('/health', health_handler)]
    )
    setup_swagger(swaggerify(app), swagger_url="/api/doc")

    web.run_app(app, path=args.path, port=args.port)
