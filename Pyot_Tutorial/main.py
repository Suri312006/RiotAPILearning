import asyncio
import sys

from module.tasks import average_win_rate_10_matches

summoner = "SirYum"

if __name__ == "__main__":
    print("Summoner name: {}".format(summoner))
    average_win_rate = asyncio.run(average_win_rate_10_matches(summoner))
    print(
        "Average win rate (last 10 matches):",
        average_win_rate * 100, "%"
    )