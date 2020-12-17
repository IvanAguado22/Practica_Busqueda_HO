from constraint import *

problem = Problem()

satelites = ['SAT1_F1', 'SAT2_F1', 'SAT3_F1', 'SAT3_F2' 'SAT4_F1', 'SAT5_F1', 'SAT6_F1', 'SAT6_F2']

antenas = ['ANT1', 'ANT2', 'ANT3', 'ANT4', 'ANT5', 'ANT6', 'ANT7', 'ANT8', 'ANT9', 'ANT10', 'ANT11', 'ANT12']

satelitesPre12 = [satelites[0], satelites[1], satelites[2], satelites[5], satelites[6]]

satelitesPre12 = [satelites[3], satelites[4], satelites[7]]

problem.addVariables(satelites[0], antenas[:4])
problem.addVariables(satelites[1], antenas[:3])
problem.addVariables(satelites[2], antenas[3:6:2])
problem.addVariables(satelites[3], (antenas[6], antenas[8], antenas[9]))
problem.addVariables(satelites[4], (antenas[7], antenas[10], antenas[11]))
print(satelites[:3])
