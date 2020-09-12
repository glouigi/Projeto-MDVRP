from depots import Depots as dpts
from customers import Customers as csts
from splitDepots import SplitDepots
from split_algorithms import Split_algorithms as split
from solution import Solution
import numpy as np

class InitialPopulation:

    def __init__(self):
        self._population = [] #lista de Solution ordenada em ordem crescente de custo

    '''
    Método define população inicial
    '''
    def definePopulation(self):
        #“cluster first and then route”
        clusters = SplitDepots.GilletJohnson() #divisão por depósitos
        #individual = split.mountRoutes(clusters) #criação de rotas por depósitos, individual é um Solution
        individual = split.splitLinearBounded(clusters) #criação de rotas por depósitos, individual é um Solution
        self._population.append(individual)

        #formação de rotas aleatórias
        for i in range(100):
            seed = int(5000 * np.random.random())
            sd = SplitDepots()
            sp = split()
            clusters = SplitDepots.randomDistribution(seed)
            individual = split.splitLinearBounded(clusters) #criação de rotas por depósitos, individual é um Solution
            if individual is not None and self.is_different(individual):
                self._population.append(individual)

        self._population = sorted(self._population, key = Solution.get_cost)
        for i in self._population:
            print(i)


    def get_population(self):
        return self._population


    '''
    Método verifica se há outro indivíduo com mesmo custo
    '''
    def is_different(self,solution):
        for p in self._population:
            if solution.get_cost() == p.get_cost():
                return False
        return True
