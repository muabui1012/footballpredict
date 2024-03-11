import asyncio
import json

import aiohttp

from understat import Understat

async def main():
  async with aiohttp.ClientSession() as session:
    understat = Understat(session)
    player = await understat.get_league_players(
      "epl", 2018,
      player_name="Paul Pogba",
      team_title="Manchester United"
    )
    print(json.dumps(player))
