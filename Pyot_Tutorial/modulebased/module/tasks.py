from typing import List
import statistics

from pyot.core.queue import Queue
from pyot.models import lol


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


async def average_win_rate_10_matches(summoner_name: str):
    summoner = await lol.Summoner(name=summoner_name).get()
    first_10_matches = await get_matches(summoner, 10)
    wins = []
    for match in first_10_matches:
        for participant in match.info.participants:
            if participant.puuid == summoner.puuid:
                wins.append(int(participant.win))
    return statistics.mean(wins or [0])


async def last_played_champs(summoner_name: str):
    summoner = await lol.Summoner(name=summoner_name).get()
    first_10_matches = await get_matches(summoner, 10)
    champ_names = []
    for match in first_10_matches:
        for participant in match.info.participants:
            if participant.puuid == summoner.puuid:
                champ_names.append(participant.champion_name)
    return champ_names
