from builtins import range, len
from operator import abs

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

    def goHome(self, map, move):
        move.Point = (0,0)

        home = []

        for i in range(len(map)):
            for j in range(len(map[i])):
                if map[i][j] == 2:
                    home.append(Node(i, j))

        drows = home.x
        dcols = home.y

        if drows < 0:
            move = Point(1, 0)
        elif drows > 0:
            move = Point(-1, 0)
        elif dcols < 0:
            move = Point(0, 1)
        elif dcols > 0:
            move = Point(0, -1)

        return move

    def allerChercherRessource(self, map, move):

        """
        :param gameMap: Map with value of each tile
        :return: closest resource available
        """
        resource = []
        bot = [0][0]
        for i in range(len(map)):
            for j in range(len(map[i])):
                if  map[i][j] == 4:
                    resource.append(Node(i, j))

        closest = None

        for node in resource:
            if closest is None or node.distTo(bot) < closest.distTo(bot):
                closest = node

        drows = closest.x - bot.x
        dcols = closest.y - bot.y

        if drows < 0:
            move = Point(1, 0)
        elif drows > 0:
            move = Point(-1, 0)
        elif dcols < 0:
            move = Point(0, 1)
        elif dcols > 0:
            move = Point(0, -1)

        return move

    def tileType(self, gameMap):

        """
        Create a map with value of each tile
        :param gameMap:
        :return: a map with value of each tile
        """

        self.visionRange = 21

        self.weigthedMap = [self.visionRange, self.visionRange]
        for i in range(self.visionRange):
            for j in range(self.visionRange):
                Point.x = i
                Point.y = j
                self.weigthedMap[i][j] = gameMap.getTileAt(Point)

        return self.weigthedMap

    def __init__(self):
        self.state = 1

    def before_turn(self, playerInfo):
        """
        Gets called before ExecuteTurn. This is where you get your bot's state.
            :param playerInfo: Your bot's current state.
        """
        self.PlayerInfo = playerInfo


    def execute_turn(self, gameMap, visiblePlayers):
        """
        This is where you decide what action to take.
            :param gameMap: The gamemap.
            :param visiblePlayers:  The list of visible players.
        """

        # Write your bot here. Use functions from aiHelper to instantiate your actions.
        if self.PlayerInfo.CarryingCapacity == self.PlayerInfo.carriedResources:
            state = 1

        self.map = self.tileType(gameMap)


        if state == 1 :
            #State aller maison
            if gameMap[1][0] == 2 or gameMap[-1][0] == 2 or gameMap[0][1] == 2 or gameMap[0][-1] == 2:
                self.state = 2
                if gameMap[1][0] == 2:
                    move = Point(1,0)
                elif gameMap[-1][0] == 2:
                    move = Point(-1,0)
                elif gameMap[0][1] == 2:
                    move = Point(0,1)
                elif gameMap[0][-1] == 2:
                    move = Point(0,-1)
                self.state = 2
                return create_empty_action(move)
            else:
                self.move, self.state = self.goHome(self.map, self.move)
                return create_move_action(Point(1, 0))
        elif state == 2:
            #State aller chercher resource
            if gameMap[1][0] == 4 or gameMap[-1][0] == 4 or gameMap[0][1] == 4 or gameMap[0][-1] == 4:
                if gameMap[1][0] == 4:
                    self.move = Point(1,0)
                elif gameMap[-1][0] == 4:
                    self.move = Point(-1,0)
                elif gameMap[0][1] == 4:
                    self.move = Point(0,1)
                elif gameMap[0][-1] == 4:
                    self.move = Point(0,-1)
                return create_collect_action(self.move)
            else:
                self.move, self.state = self.allerChercherRessource(self.map, self.move)
                return create_move_action(Point(1, 0))



    def after_turn(self):
        """
        Gets called after executeTurn
        """
        pass

