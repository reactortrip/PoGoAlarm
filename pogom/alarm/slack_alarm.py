import logging

from alarm import Alarm, gmaps_link, pkmn_time_text
from slacker import Slacker
from geopy.geocoders import Nominatim

log = logging.getLogger(__name__)

class Slack_Alarm(Alarm):
	
	def __init__(self, api_key, channel):
		self.client = Slacker(api_key) 
		self.channel = channel
		log.info("Slacker_Alarm intialized.")
		self.client.chat.post_message(self.channel, 'PokeAlarm activated!', username='PokeAlarm', icon_emoji=':pokeball:')
		
	def pokemon_alert(self, pokemon):
                user_icon = ':pokemon-' + pokemon['name'].lower() + ':'
                address = Nominatim().reverse(str(pokemon["lat"])+", "+str(pokemon["lng"])).address
		notification_text = pokemon['name'].title() + " found!"
		google_maps_link = gmaps_link(pokemon["lat"], pokemon["lng"])
		time_text =  pkmn_time_text(pokemon['disappear_time']) + "  Address: " + address + "."
		self.client.chat.post_message(self.channel, notification_text + " " + time_text + " " + google_maps_link, username=pokemon['name'], icon_emoji=user_icon)