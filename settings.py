
channel_name = "nopogo_tv"
server_ip = "0.0.0.0"
server_port = 8000
channel_id = 28092036
ws_host = "wss://pubsub-edge.twitch.tv"

topics = [
	"channel-bits-events-v2.{}".format(channel_id), 
	"channel-points-channel-v1.{}".format(channel_id),
	"channel-subscribe-events-v1.{}".format(channel_id)
]

