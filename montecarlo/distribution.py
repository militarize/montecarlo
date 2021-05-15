# Placeholder for Distribution class.

# Imports
import math

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

class Distribution:

    #def __init__(self, n_datasets = 1, dataset = dataset):
        # Testing on just arrays
        #self.dist_type = dist_type
        #self.n_datasets = n_samples
        #self.dataset = dataset

    def __init__(self):
        pass

    def normal(dataset):
        # Working on proper binwidths
        binwidth = ((max(dataset) - min(dataset)) /
            (round(math.sqrt(len(dataset)))))
        
        # This plot can definitely be improved
        return sns.histplot(
            dataset,
            kde = True,
            bins = (np.arange(min(dataset), max(dataset) + binwidth, binwidth)),
            stat = "probability",
            discrete = True)
