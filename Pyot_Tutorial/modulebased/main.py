import asyncio
from module.tasks import *
summoner = "SirYum"

if __name__ == "__main__":
    print("Summoner name: {}".format(summoner))
    average_win_rate = asyncio.run(average_win_rate_10_matches(summoner))
    last_10_champion = asyncio.run(last_played_champs(summoner))

    print(
        "Average win rate (last 10 matches): ",
        average_win_rate * 100, "%"

    )

    print("Last 10 Champions Played: ", last_10_champion)