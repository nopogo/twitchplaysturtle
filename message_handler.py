# example_message = {"type":"MESSAGE","data":{"topic":"channel-bits-events-v2.28092036","message":"{\"data\":{\"user_name\":\"neekses\",\"channel_name\":\"nopogo_tv\",\"user_id\":\"30555403\",\"channel_id\":\"28092036\",\"time\":\"2021-03-21T20:55:33.014272606Z\",\"chat_message\":\"Cheer1\",\"bits_used\":1,\"total_bits_used\":1401,\"is_anonymous\":false,\"context\":\"cheer\",\"badge_entitlement\":null},\"version\":\"1.0\",\"message_type\":\"bits_event\",\"message_id\":\"4525d8f2-b08f-5758-a81b-18e54251dc5e\"}"}}

# Received message from server: 
# {"type":"MESSAGE","data":{
# "topic":"channel-bits-events-v2.28092036",
# "message":"{\"data\":{\"user_name\":\"neekses\",\"channel_name\":\"nopogo_tv\",\"user_id\":\"30555403\",\"channel_id\":\"28092036\",\"time\":\"2021-03-21T20:55:33.014272606Z\",\
# "chat_message\":\"Cheer1\",\"bits_used\":1,\"total_bits_used\":1401,\"is_anonymous\":false,\"context\":\"cheer\",\"badge_entitlement\":null},\"version\":\"1.0\",\"message_type\":\"bits_event\",
# \"message_id\":\"4525d8f2-b08f-5758-a81b-18e54251dc5e\"}"}}



import json, websockets, asyncio, settings, logging

channel_point_key = "channel-points-channel-v1.28092036"
channel_sub_key   = "channel-subscribe-event-v1.28092036"
channel_bits_key  = "channel-bits-events-v2"

async def parse_message(message_string):
	message_dict = json.loads(message_string)

	if "error" in message_dict or "data" not in message_dict:
		return

	type_string  = message_dict["type"]

	if type_string == "PONG" or type_string == "RESPONSE":
		return

	topic = message_dict["data"]["topic"]
	message = json.loads(message_dict["data"]["message"]) #this is required otherwise this gets interperted as a string
		
	
	if topic == channel_point_key:
		redeem_title = message["data"]["redemption"]["reward"]["title"]
		if redeem_title == "forward":
			await send_command_to_roomba("move:f")
			pass
		if redeem_title == "back":
			await send_command_to_roomba("move:b")
			pass
		if redeem_title == "left":
			await send_command_to_roomba("move:l")
			pass
		if redeem_title == "right":
			await send_command_to_roomba("move:r")
			pass
		if redeem_title == "up":
			await send_command_to_roomba("move:u")
			pass
		if redeem_title == "down":
			await send_command_to_roomba("move:d")
			pass
			# pass forward command to turtle
			# 	
	if topic == channel_sub_key:
		print("channel sub redeemed")

	if topic == channel_bits_key:
		print("channel bits redeemed")



async def send_command_to_roomba(command_string):
	async with websockets.connect(settings.ws_local) as websocket:
		await websocket.send(command_string)
		return