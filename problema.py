import copy
# definimos la clase satelite


class Satelite():
    def __init__(self, number, rowA, rowB,  obsCost, turnCost, transferCost, unitCharge, totalBatt):
        self.number = number  # numero de satelite
        if self.number == 1:
            self.rowA = 0  # banda de observacion 1 del satelite 1
            self.rowB = 1  # banda de observacion 2 del satelite 2
        elif self.number == 2:
            self.rowA = 2  # banda de observacion 1
            self.rowB = 3  # banda de observacion 2

        self.hour = 0  # columna del grid
        self.obsCost = obsCost  # coste de observacion
        self.turnCost = turnCost  # coste de giro
        self.transferCost = transferCost  # coste de transferencia
        self.unitCharge = unitCharge  # unidades que se recargan
        self.totalBatt = totalBatt  # capacidad maxima de la bateria
        self.actualBatt = totalBatt  # capacidad actual de la bateria
        self.observations = []  # Observaciones que va realizando

    def canCharge(self):
        if self.hour < 12:
            if self.actualBatt < self.totalBatt:
                return True

        return False

    def charge(self):
        if self.canCharge():
            self.actualBatt += self.unitCharge
            self.hour = (1 + self.hour) % 24

    def canTurn(self):
        if self.hour < 12 and self.actualBatt >= 1:
            return True

        return False

    def turn(self):
        if self.canTurn():
            if self.number == 1:
                if self.rowA == 0 and self.rowB == 1:
                    self.rowA = 1
                    self.rowB = 2
                elif self.rowA == 1 and self.rowB == 2:
                    self.rowA = 0
                    self.rowB = 1
            elif self.number == 2:
                if self.rowA == 2 and self.rowB == 3:
                    self.rowA = 1
                    self.rowB = 2
                elif self.rowA == 1 and self.rowB == 2:
                    self.rowA = 2
                    self.rowB = 3
            self.hour = (1 + self.hour) % 24
            self.actualBatt -= self.turnCost

    def canObserve(self, objective):
        if self.hour < 12 and self.actualBatt >= 1:
            if objective.posY == self.rowA or objective.posY == self.rowB:
                if self.observations.__contains__(objective) != False:
                    return True
        return False

    def observe(self, objective):
        if self.canObserve(objective):
            self.observations.append(objective)
            self.hour = (1 + self.hour) % 24
            self.actualBatt -= self.obsCost

    def canTransfer(self):
        if self.hour < 12 and self.actualBatt >= 1:
            if len(self.observations) > 0:
                return True
        return False

    def transfer(self, StationBase):
        if self.canTransfer(StationBase):
            x = self.observations.pop()  # mirar porque a lo mejor depende de la busqueda
            StationBase.addObjective(x)
            self.hour = (1 + self.hour) % 24
            self.actualBatt -= self.transferCost

    def idle(self):
        self.hour = (1 + self.hour) % 24


# definimos la clase objetivo
class Objective():
    def __init__(self, posX, posY):

        self.posX = posX
        self.posY = posY


# definimos la clase Estacion Base
class StationBase():
    def __init__(self, totalObjective):
        self.totalObjectives = totalObjective
        # self.numObjectives = 0
        self.objStation = []  # lista de objetivos

    def addObjective(self, objective):
        if len(self.objStation) < self.totalObjectives:
            # self.numObjectives +=1
            self.objStation.append(objective)

# definimos la clase estado


class State():
    def __init__(self, sat1, sat2, StationBase, grid):
        self.sat1 = sat1
        self.sat2 = sat2
        self.StationBase = StationBase
        self.grid = grid
        self.successors = []
        self.sat1Action = None  # Accion que toma el satelite 1 en ese estado
        self.sat2Action = None  # Accion que toma el satelite 2 en ese estado
        self.g = 0
        self.h = 0

    def isGoalState(self):
        """si el tamaño de la lista de objetivos de la estacion
            base es igual al numero de objetivos totales y si el numero de observaciones
            de ambos satelites es 0 entonces es estado final"""
        if len(self.StationBase.objStation) == self.StationBase.totalObjectives:
            if len(self.sat1.observations) == 0 and len(self.sat2.observations) == 0:
                return True
        return False

    def getSuccessors(self, state):
        if state.sat1.canCharge():
            if state.sat2.canCharge():
                state11 = copy.deepcopy(state)
                state11.sat1.charge()
                state11.sat2.charge()
                successors.append(state11)
            if state.sat2.canTurn():
                state12 = copy.deepcopy(state)
                state12.sat1.charge()
                state12.sat2.turn()
                successors.append(state12)
            for obj in grid:
                if state.sat2.canObserve(obj):
                    state13 = copy.deepcopy(state)
                    state13.sat1.charge()
                    state13.sat2.observe()
                    successors.append(state13)

            if state.sat2.canTranfer():
                state14 = copy.deepcopy(state)
                state14.sat1.charge()
                state14.sat2.transfer(state.StationBase)
                successors.append(state14)
            else:
                state15 = copy.deepcopy(state)
                state15.sat1.charge()
                state15.sat2.idle()
                successors.append(state15)

            if state.sat1.canTurn():
                if state.sat2.canCharge():
                    state21 = copy.deepcopy(state)
                    state21.sat1.turn()
                    state21.sat2.charge()
                    succesors.append(state21)

            if state.sat2.canTurn():
                state11 = copy.deepcopy(state)
                state1.sat1New.turn()
                state1.sat2New.turn()
                return state1

            if state.sat2.canObserve():
                state11 = copy.deepcopy(state)
                state1.sat1New.turn()
                state1.sat2New.observe()
                return state1

            if state.sat2.canTranfer():
                state11 = copy.deepcopy(state)
                state1.sat1New.turn()
                state1.sat2New.transfer()
                return state1
            else:
                state11 = copy.deepcopy(state)
                state.sat1New.turn()
                state.sat2New.idle()
                return state1

            if state.sat1.canObserve():
                if state.sat2.canCharge():
                    state11 = copy.deepcopy(state)
                    state1.sat1New.observe()
                    state1.sat2New.charge()
                return state1

            if state.sat2.canTurn():
                state11 = copy.deepcopy(state)
                state1.sat1New.observe()
                state1.sat2New.turn()
                return state1

            if state.sat2.canObserve():
                state11 = copy.deepcopy(state)
                state1.sat1New.observe()
                state1.sat2New.observe()
                return state1

            if state.sat2.canTranfer():
                state11 = copy.deepcopy(state)
                state1.sat1New.observe()
                state1.sat2New.transfer()
                return state1
            else:
                state11 = copy.deepcopy(state)
                state.sat1New.observe()
                state.sat2New.idle()
                return state1

            if state.sat1.canTransfer():
                if state.sat2.canCharge():
                    state11 = copy.deepcopy(state)
                    state1.sat1New.transfer()
                    state1.sat2New.charge()
                    return state1

            if state.sat2.canTurn():
                state11 = copy.deepcopy(state)
                state1.sat1New.transfer()
                state1.sat2New.turn()
                return state1

            if state.sat2.canObserve():
                state11 = copy.deepcopy(state)
                state1.sat1New.transfer()
                state1.sat2New.observe()
                return state1

            if state.sat2.canTranfer():
                state11 = copy.deepcopy(state)
                state1.sat1New.transfer()
                state1.sat2New.transfer()
                return state1
            else:
                state11 = copy.deepcopy(state)
                state.sat1New.transfer()
                state.sat2New.idle()
                return state1

        else:
            if state.sat2.canCharge():
                state11 = copy.deepcopy(state)
                state1.sat1New.idle()
                state1.sat2New.charge()
                return state1

            if state.sat2.canTurn():
                state11 = copy.deepcopy(state)
                state1.sat1New.idle()
                state1.sat2New.turn()
                return state1

            if state.sat2.canObserve():
                state11 = copy.deepcopy(state)
                state1.sat1New.idle()
                state1.sat2New.observe()
                return state1

            if state.sat2.canTranfer():
                state11 = copy.deepcopy(state)
                state1.sat1New.idle()
                state1.sat2New.transfer()
                return state1
            else:
                state11 = copy.deepcopy(state)
                state.sat1New.idle()
                state.sat2New.idle()
                return state1


class Search():

    def f(state):
        g = state.getCostOfActions()
        h = 0
        return g+h
    """def manhattanDistance( xy1, xy2 ):
        "Returns the Manhattan distance between points xy1 and xy2"
        return abs( xy1[0] - xy2[0] ) + abs( xy1[1] - xy2[1] )"""

    def AstarSearch(initialState):
        openList = [initialState]
        closedList = []
        success = False
        B = f(initialState)
        while openList != [] or success == False:
            currentState = openList.pop()
            if currentState.isGoalState:
                success = True
            else:
                # expand n --> como se generan sucesores¿?
                successors = getSuccessors(currentState)
                closedList.append(currentState)
                openList.append(successors)
                for s in successors:
                    if openList.__contains__(s) == False and closedList.__contains__(s) == False:
                        openList.append(s)
                        nObservations -= nObservations
                        elif openList.__contains__() and f(s) < B
                        x = openList.pop(s):
                        B = f(s)
                        closedList.append(x)
                        nObs -= nObs
                        elif closedList.__contains__(s):
                            #nObs = nObs-1;
                            None
                if success = True:
                    return closedList  # ¿ Cómo devolver el camino ?
                else:
                    return None


class main():
    # creamos los objetivos
    O1 = Objective(0, 1)
    O2 = Objective(0, 3)
    O3 = Objective(1, 3)

    grid = [O1, O2, O3]  # lista con los objetivos que tiene el grid
    # creamos el tablero
    grid2 = [[None, O1, None, O2, None, None, None, None, None, None, None, None],
             [None, None, None, O3, None, None, None, None, None, None, None, None],
             [None, None, None, None, None, None,
                 None, None, None, None, None, None],
             [None, None, None, None, None, None, None, None, None, None, None, None]]

    # Creamos los satelites y la estacion base para este problema

    # number, hour, rowA, rowB,  obsCost, turnCost, transferCost, unitCharge, totalBatt
    sat1 = Satelite(1, 0, 0, 1, 1, 1, 1, 1)
    # number, hour, rowA, rowB,  obsCost, turnCost, transferCost, unitCharge, totalBatt
    sat2 = Satelite(2, 0, 2, 3, 1, 1, 1, 8)
    stationBase = StationBase(3)

    # Creamos el estado inicial
    initialState = State(sat1, sat2, stationBase, grid)
