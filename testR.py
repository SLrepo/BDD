from BDDnode import *
from algorithmR import *


truthTable = [False, False, False, True, False, True, True, True]
bdd = BDD(truthTable)
bdd.plotBDD('test-output.gv')
algorithmR(bdd)
bdd.plotBDD('test-output-reduced.gv')
