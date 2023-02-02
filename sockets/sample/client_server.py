#!/usr/bin/env python

import asyncio
from websockets import connect
import json

async def hello(uri):
    async with connect(uri) as websocket:
        await websocket.send("Hello world!")
        await websocket.send("Hi world!")
        await websocket.send("Hello there!")
        await websocket.send(json.dumps({"teste": "opa"}))
        # await websocket.send([7, 1, 4])

        print(await websocket.recv())

asyncio.run(hello("ws://localhost:8765"))