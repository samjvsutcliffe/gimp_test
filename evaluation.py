import pandas as pd
import os
import re
import numpy as np
import matplotlib.pyplot as plt

from matplotlib.ticker import (AutoMinorLocator, MultipleLocator)
dir_structure = "test_cases/{}/{}_consol/results/{}_consol/"
plt.close("all")
sim_names = ["mpm","gimp"]
sim_files = []
for name in ["mpm","gimp"]:
    dir_full = dir_structure.format(name,name,name)
    files = os.listdir(dir_full)
    p = re.compile('.*\.h5') 
    h5_files = [f for f in files if p.match(f)]
    df = pd.read_hdf(dir_full+h5_files[-1])
    sim_files.append(df)
#Compared to another GIMP implementation
#sim_names.append("own")
#df = pd.read_csv("column_mpm.csv")
#sim_files.append(df)

plt.figure()
plt.suptitle("Shear stress")
for i,(name,df) in enumerate(zip(sim_names,sim_files)):
    print("Type: {}".format(name))
    print("Total shear stress: {}".format(np.sqrt(df["tau_xy"].pow(2).mean())))
    #plt.figure()
    plt.subplot(1,len(sim_names),i+1)
    plt.scatter(df["coord_x"],df["coord_y"],c=df["tau_xy"])
    ax = plt.gca()
    resolution = 10
    plt.xlim([0,resolution])
    plt.ylim([0,50])
    plt.grid()
    ax.set_aspect('equal')
    ax.set_xticks([0,resolution])
    ax.set_yticks(np.arange(0,50,resolution))
    plt.colorbar()
    plt.title(name)

plt.figure()
plt.suptitle("Vertical stress")
for i,(name,df) in enumerate(zip(sim_names,sim_files)):
    #print("Type: {}".format(name))
    #print("Total shear stress: {}".format(df["tau_xy"].abs().sum()))
    #plt.figure()
    plt.subplot(1,len(sim_names),i+1)
    plt.scatter(df["coord_x"],df["coord_y"],c=df["stress_yy"])
    ax = plt.gca()
    plt.xlim([0,resolution])
    plt.ylim([0,50])
    plt.grid()
    ax.set_aspect('equal')
    ax.set_xticks([0,resolution])
    ax.set_yticks(np.arange(0,50,resolution))
    plt.colorbar()
    plt.title(name)
plt.show()
