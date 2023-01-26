import pandas as pd
import os
import re
import numpy as np
import matplotlib.pyplot as plt

from matplotlib.ticker import (AutoMinorLocator, MultipleLocator)
dir_structure = "test_cases/{}/{}_consol/results/{}_consol/"
plt.close("all")
for name in ["mpm","gimp"]:
    dir_full = dir_structure.format(name,name,name)
    files = os.listdir(dir_full)
    p = re.compile('.*\.h5') 
    h5_files = [f for f in files if p.match(f)]
    df = pd.read_hdf(dir_full+h5_files[-1])
    print("Type: {}".format(name))
    print("Total shear stress: {}".format(df["tau_xy"].abs().sum()))
    plt.figure()
    plt.scatter(df["coord_x"],df["coord_y"],c=df["tau_xy"])
    ax = plt.gca()
    plt.xlim([0,5])
    plt.ylim([0,50])
    plt.grid()
    ax.set_aspect('equal')
    ax.set_xticks([0,5])
    ax.set_yticks(np.arange(0,50,5))
    plt.colorbar()
    plt.title(name)
plt.show()
