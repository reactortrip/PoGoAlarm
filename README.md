
# kvangent's original PokemonGo Alarm - Updated Slack Alarm

## How to setup

Install PokemonGo-Map and verify you have it working. (https://github.com/PokemonGoMap/PokemonGo-Map)

Install Templarian's slack emoji's using the :pokemon- prefix. (https://github.com/Templarian/slack-emoji-pokemon)

Add your own custom Pokeball emoji to slack and name it :pokeball:

Configure the alarms.sample.json and rename alarms.json, then put it in the root directory of PokemonGo-Map.

Put the rest of the files in the pogom/alarm directory of PokemonGo-Map.

Add to requirements.txt and rerun it:

```
pushbullet.py==0.10.0
slacker==0.9.24
twilio==5.4.0
telepot==8.3
```

Edit pogom/search.py with the changes below:

Below "from pgoapi.exceptions import AuthException", add:

```
from alarm.notifications import Notifications
```

Below "
TIMESTAMP = '\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000'", add:

```
alarms = Notifications()
```

Delete "parsed = parse_map(response_dict, step_location)", replace with:

```
pokemons, pokestops, gyms = parse_map(response_dict, step_location)
alarms.notify_pkmns(pokemons)
```

Add this line to pogom/model.py below "bulk_upsert(ScannedLocation, scanned)":

```
return (pokemons, pokestops, gyms)
```

## Warnings

Using this software is against the ToS of the game. You can get banned, use this tool at your own risk.


## Contributions

Using kvangent's Original PokeAlarm code, he doesn't support this anymore so don't bug him (https://github.com/kvangent) 