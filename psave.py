import json
import operator

def getleaderboard():
  # author: luka
  # date: aug 8, 2023
  # get leaderboard from json
  # v1.1
  with open("save.json", "r") as file:
      allplayers = json.load(file)

  ordered = sorted(allplayers, key= lambda x: x["score"], reverse=True)
  top5 = ordered[:5]
  return top5