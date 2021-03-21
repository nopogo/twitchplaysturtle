
channel_name = "nopogo_tv"
server_ip = "0.0.0.0"
server_port = 8000
channel_id = 28092036
ws_host = "wss://pubsub-edge.twitch.tv"

topics = [
	"channel-bits-events-v2.{}".format(channel_id), 
	"channel-points-channel-v1.{}".format(channel_id),

]


#access token was gained by requesting:
#https://id.twitch.tv/oauth2/authorize?client_id=4tftgx7d1luly2w1j11ylhw7yrl26r&redirect_uri=http://localhost&response_type=token&scope=bits:read%20channel:read:redemptions%20channel:read:subscriptions%20channel:moderate