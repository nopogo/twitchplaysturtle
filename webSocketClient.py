import websockets
import asyncio
import uuid
import json
import settings, secrets, message_handler
import logging

class WebSocketClient():

    def __init__(self):
        # list of topics to subscribe to
        self.topics = settings.topics
        self.auth_token = "{}".format(secrets.access_token)
        
        pass

    async def connect(self, connection_address):
        '''
           Connecting to webSocket server
           websockets.client.connect returns a WebSocketClientProtocol, which is used to send and receive messages
        '''

        self.connection = await websockets.client.connect(connection_address)
        if self.connection.open:
            print('Connection stablished. Client correcly connected')
            # Send greeting
            message = {"type": "LISTEN", "nonce": str(self.generate_nonce()), "data":{"topics": self.topics, "auth_token": self.auth_token}}
            json_message = json.dumps(message)
            await self.sendMessage(json_message)
            return self.connection

    def generate_nonce(self):
        '''Generate pseudo-random number and seconds since epoch (UTC).'''
        nonce = uuid.uuid1()
        oauth_nonce = nonce.hex
        return oauth_nonce

    async def sendMessage(self, message):
        '''Sending message to webSocket server'''
        await self.connection.send(message)

    async def localLogic(self, message):
        while True:
            try:
                message = await connection.recv()
                print('Received message from server: ' + str(message))
            except websockets.exceptions.ConnectionClosed:
                print('Connection with server closed')
                break
            except Exception as e:
                print(e)
                break

    async def receiveMessage(self, connection):
        '''Receiving all server messages and handling them'''
        while True:
            try:
                message = await connection.recv()
                # print('Received message from server: ' + str(message))
                await message_handler.parse_message(message)
            except websockets.exceptions.ConnectionClosed:
                print('Connection with server closed')
                break
            except BaseException:
                logging.exception("message exception thrown")
                break

    async def heartbeat(self, connection):
        '''
        Sending heartbeat to server every 1 minutes
        Ping - pong messages to verify/keep connection is alive
        '''
        while True:
            try:
                data_set = {"type": "PING"}
                json_request = json.dumps(data_set)
                # print(json_request)
                await connection.send(json_request)
                await asyncio.sleep(60)
            except websockets.exceptions.ConnectionClosed:
                print('Connection with server closed')
                break
            except Exception as e:
                print(e)
                break