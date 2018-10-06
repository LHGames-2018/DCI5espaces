from helper import *
from helper.structs import Point

class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distTo(self, target):
        return abs(target.x - self.x) + abs(target.y - self.y)

class Bot:

    def phaseOne(self, gameMap):

        """

        :param gameMap: Map with value of each tile
        :return: closest resource available
        """
        resource = list()
        bot = (0, 0)
        for i in range(21):
            for j in range(21):
                if (gameMap[i][j] == 4):
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

        visionRange = 21

        weigthedMap = [visionRange, visionRange]
        for i in range(visionRange):
            for j in range(visionRange):
                Point.x = i
                Point.y = j
                weigthedMap[i][j] = gameMap.getTileAt(Point)

        return weigthedMap

    def __init__(self):
        pass

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

        map = self.tileType(gameMap)
        move = self.phaseOne(map)

        return create_move_action(move)

    def after_turn(self):
        """
        Gets called after executeTurn
        """
        pass

