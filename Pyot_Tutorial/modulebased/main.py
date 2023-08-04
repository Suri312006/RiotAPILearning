import asyncio
from module.tasks import *

summoner = "SirYum"

if __name__ == "__main__":
    print("Summoner name: {}".format(summoner))
    average_win_rate = asyncio.run(average_win_rate_10_matches(summoner))
    print("Average win rate (last 10 matches): ", average_win_rate * 100, "%")
    last_10_champion = asyncio.run(last_played_champs(summoner))
    print("Last 10 Champions Played: ", last_10_champion)
    avg_match_duration = asyncio.run(average_match_duration_millis(summoner))
    print("Avg match duration {}".format(avg_match_duration))
    



