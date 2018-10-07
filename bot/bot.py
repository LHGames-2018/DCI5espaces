from builtins import range, len

from helper import *
from helper.structs import Point
import math


class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distTo(self, target):
        return abs(target.x - self.x) + abs(target.y - self.y)

class Bot:

    def getStandardMap(self, gameMap, bot):

        map = [[j for j in range(21)] for i in range(21)]

        for i in range(21):
            for j in range(21):
                map[i][j] = gameMap.getTileAt(Point(i,j))

        return map

    def next_move(self, map, bot):

        move = Point(0,0)
        resource = []
        
        for i in range(21):
            for j in range(21):
                if map[i][j] == 4 :
                    resource.append(Node(i,j))
                    print("Resource en : ")
                    print(i+j)

        closest = Node(999,999)
        for node in resource:
            if closest is None or node.distTo(bot) < closest.distTo(bot):
                closest = node

        drows = closest.x - bot.x
        dcols = closest.y - bot.y

        if drows < 0 :
            return Point(0,-1)
        elif drows > 0 :
            return Point(0,-1)
        elif dcols < 0 :
            return Point(-1,0)
        elif dcols > 0 :
            return Point(0,-1)

    def __init__(self):
        self.actionList =[1,1,1,1,1,1,1,1,1,1,1,1,1,3,5,4,2,2,2,2]
        self.action = 0

    def before_turn(self, playerInfo):
        """
        Gets called before ExecuteTurn. This is where you get your bot's state.
            :param playerInfo: Your bot's current state.
        """
        self.PlayerInfo = playerInfo


    def execute_turn(self, gameMap, visiblePlayers):

        if(self.actionList[self.action] == 1): #Droite
            action+=1
            return create_move_action(Point(1,0))

        elif(self.actionList[self.action] == 2): #Gauche
            action+=1
            return create_move_action(Point(-1,0))
            
        elif(self.actionList[self.action] == 3): #Up
            action+=1
            return create_move_action(Point(0,-1))
            
        elif(self.actionList[self.action] == 4): #Down
            action+=1
            return create_move_action(Point(0,1))
            
        elif(self.actionList[self.action] == 5): #miner
            action+=1
            return create_collect_action(Point(0,-1))
        #move = Point(0,0)

        #bot = self.PlayerInfo.Position
        #bot = Node(bot.x , bot.y)

        #map = self.getStandardMap(gameMap, bot)
        #move = self.next_move(map, bot)
        #return create_move_action(move)
        #if(map[bot.x+1][bot.y] == 4 or map[bot.x-1][bot.y] == 4 or map[bot.x][bot.y+1] == 4 or map[bot.x][bot.y-1]==4):
         #   if map[bot.x+1][bot.y] == 4:
          #    return create_collect_action(Point(-1,0))
          #  elif map[bot.x-1][bot.y] == 4:
          #      return create_collect_action(Point(1,0))
          #  elif map[bot.x][bot.y+1] == 4:
          #      return create_collect_action(Point(0,1))
          #  elif map[bot.x][bot.y-1] == 4:
          #      return create_collect_action(Point(0,-1))
        #else:
         #   move = self.next_move(map)
         #   return create_move_action(move)
   



    def after_turn(self):
        """
        Gets called after executeTurn
        """
        pass

