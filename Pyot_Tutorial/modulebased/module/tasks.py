from typing import List
import statistics

from pyot.core.queue import Queue
from pyot.models import lol
from pyot.core.resources import resource_manager


async def get_matches(summoner, number=10):
    """
    Returns a number of matches played by summoner (determined by value of number)
    """
    async with Queue() as queue:
        history = await summoner.match_history.get()
        for match in history.matches[:number]:
            await queue.put(match.get())
        list_matches: List[lol.Match] = await queue.join()
    return list_matches

@resource_manager.as_decorator
async def average_win_rate_10_matches(summoner_name: str):
    summoner = await lol.Summoner(name=summoner_name).get()
    first_10_matches = await get_matches(summoner, 10)
    wins = []
    for match in first_10_matches:
        for participant in match.info.participants:
            if participant.puuid == summoner.puuid:
                wins.append(int(participant.win))
    return statistics.mean(wins or [0])

@resource_manager.as_decorator
async def last_played_champs(summoner_name: str):
    summoner = await lol.Summoner(name=summoner_name).get()
    first_10_matches = await get_matches(summoner, 10)
    champ_names = []
    for match in first_10_matches:
        for participant in match.info.participants:
            if participant.puuid == summoner.puuid:
                champ_names.append(participant.champion_name)
    return champ_names

@resource_manager.as_decorator
async def average_match_duration_millis(summoner_name: str):
    # Before entering scope, resources are acquired for this event loop
    summoner = await lol.Summoner(name=summoner_name).get()
    first_5_matches = await get_matches(summoner, 5)
    return statistics.mean([match.info.duration_millis for match in first_5_matches] or [0])
    # After exiting scope, resources are released for this event loop