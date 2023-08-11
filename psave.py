import json
import operator


def createplayer(name):
  # author: luka
  # date: aug 4, 2023
  # get leaderboard from json
  # v1
  player = {"name": name, "score": 0}
  return player


def loadplayer(name):
  with open("save.json", "r") as file:
    allplayers = json.load(file)

  for p in allplayers:
    if (p["name"] == name):
      return p 

  return "not found"

def saveplayer(player):
  # author: luka
  # date: aug 4, 2023
  # save player 
  # v1
  with open("save.json", "r") as file:
    allplayers = json.load(file)

  playerindex = None 
  for i, p in enumerate(allplayers):
    if p["name"] == player["name"]:
      playerindex = i

  if (playerindex == None):
    allplayers = allplayers + [player]
  else:
    allplayers = allplayers[:playerindex] + [player] + allplayers[playerindex + 1:]

  with open("save.json", "w") as file:
    json.dump(allplayers, file)


def getleaderboard():
  # author: luka
  # date: aug 4, 2023
  # get leaderboard from json
  # v1.1
  with open("save.json", "r") as file:
    allplayers = json.load(file)

  ordered = sorted(allplayers, key=lambda x: x["score"], reverse=True)
  top5 = ordered[:5]
  return top5
