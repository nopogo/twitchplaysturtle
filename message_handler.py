example_message = {"type":"MESSAGE","data":{"topic":"channel-bits-events-v2.28092036","message":"{\"data\":{\"user_name\":\"neekses\",\"channel_name\":\"nopogo_tv\",\"user_id\":\"30555403\",\"channel_id\":\"28092036\",\"time\":\"2021-03-21T20:55:33.014272606Z\",\"chat_message\":\"Cheer1\",\"bits_used\":1,\"total_bits_used\":1401,\"is_anonymous\":false,\"context\":\"cheer\",\"badge_entitlement\":null},\"version\":\"1.0\",\"message_type\":\"bits_event\",\"message_id\":\"4525d8f2-b08f-5758-a81b-18e54251dc5e\"}"}}

# Received message from server: 
# {"type":"MESSAGE","data":{
# "topic":"channel-bits-events-v2.28092036",
# "message":"{\"data\":{\"user_name\":\"neekses\",\"channel_name\":\"nopogo_tv\",\"user_id\":\"30555403\",\"channel_id\":\"28092036\",\"time\":\"2021-03-21T20:55:33.014272606Z\",\
# "chat_message\":\"Cheer1\",\"bits_used\":1,\"total_bits_used\":1401,\"is_anonymous\":false,\"context\":\"cheer\",\"badge_entitlement\":null},\"version\":\"1.0\",\"message_type\":\"bits_event\",
# \"message_id\":\"4525d8f2-b08f-5758-a81b-18e54251dc5e\"}"}}



import json


def parse_message(message_string):
	print(message_string)



# parse_message(example_message)