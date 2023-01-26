import pandas as pd
import os
import re
import matplotlib.pyplot as plt
dir_structure = "test_cases/{}/{}_consol/results/{}_consol/"

for name in ["mpm","gimp"]:
    dir_full = dir_structure.format(name,name,name)
    files = os.listdir(dir_full)
    p = re.compile('.*\.h5') 
    h5_files = [f for f in files if p.match(f)]
    df = pd.read_hdf(dir_full+h5_files[-1])
    print("Type: {}".format(name))
    print("Total shear stress: {}".format(df["tau_xy"].abs().sum()))
