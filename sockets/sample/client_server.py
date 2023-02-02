#!/usr/bin/env python

import asyncio
import websockets
import json

messages = [
    {"teste": "opa"},
    {"teste": "opa", "event": "imagine this is a col event"},
    {"teste": "opa2"},
    {"teste": "opa2", "event": "2imagine this is a col event"},
]

async def start_clients():
    uri = "ws://localhost:8765"
    client1 = await websockets.connect(uri)
    print(await client1.ping())

    print("client1 started")
    client2 = await websockets.connect(uri)
    print("client2 started")
    return (client1, client2)


async def send_message(socket, message):
    await socket.send(json.dumps(message))
    return await socket.recv()


async def run():
    client1, client2 = await start_clients()

    for msg in messages:
        print(await send_message(client1, msg))
        # await client1.wait_closed()
    
    for msg in messages:
        print(await send_message(client2, msg))

    # client1.
    await client1.close()
    await client2.close()

asyncio.run(run())