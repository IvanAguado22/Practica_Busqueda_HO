from constraint import *

problem = Problem()

satelites = ['SAT1', 'SAT2', 'SAT3', 'SAT4', 'SAT5', 'SAT6']

problem.addVariables(satelites[1:3], ['A1F1', 'A2F1', 'A3F1', 'A4F1'])
print(satelites[:3])
