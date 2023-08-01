##https://github.com/meraki-analytics/cassiopeia
import random

import cassiopeia as cass

cass.set_riot_api_key("RGAPI-0cf4bdb0-e932-49ee-a309-8e8d266ce6a4")  # This overrides the value set in your configuration/settings.

summoner = cass.get_summoner(name="SirYum", region="NA")
print("{name} is a level {level} summoner on the {region} server.".format(name=summoner.name,
                                                                          level=summoner.level,
                                                                          region=summoner.region))

champions = cass.get_champions(region="NA")
random_champion = random.choice(champions)
print("He enjoys playing champions such as {name}.".format(name=random_champion.name))

