import json
from pprint import pprint
from glob import glob
import numpy as np
from math import *
from PlotResult import PlotResult

DP_TEST_MEAN = 3
DP_TEST_STD = 5
RE_TEST_MEAN = 9
RE_TEST_STD = 11
NANO_SEC = 1.0e9



FILENAME ="./output/{}/*.json"
AVOID_FILE = "./p_3/32.json"


def DpTest(data):
    mean = data["benchmarks"][DP_TEST_MEAN]["cpu_time"]/NANO_SEC
    stdev = data["benchmarks"][DP_TEST_STD]["cpu_time"]/NANO_SEC
    # print("DpTest: \t\t{:.3f} +/- {:.3f}".format(mean,stdev))
    return [mean, stdev]

def RecursionTest(data):
    mean = data["benchmarks"][RE_TEST_MEAN]["cpu_time"]/NANO_SEC
    stdev = data["benchmarks"][RE_TEST_STD]["cpu_time"]/NANO_SEC
    # print("RecursionTest: \t{:.3f} +/- {:.3f}".format(mean,stdev))
    return [mean, stdev]

def improvement(DP, RECUR):
    d = np.mean(DP[:,0])
    r = np.mean(RECUR[:,0])

    sd = np.std(DP[:,0])
    sr = np.std(RECUR[:,0])

    i= 1 - (d/r)
    print(f"DP={np.mean(DP[:,0]):.3f} +/- {np.std(DP[:,0]):.3f} | RECUR ={np.mean(RECUR[:,0]):.3f} +/- {np.std(RECUR[:,0]):.3f}")
    print("improvement {:.3f} % | {:.3f} faster".format(100*i, r/d) )
    return [log(d), log(sd)], [log(r), log(sr)]

def getResult(filename):
    DP = []
    RECUR = []
    files = glob(filename)
    for f in files:
        if(f==AVOID_FILE):
            continue
        with open(f, "r") as file:
            data = json.load(file)
        DP.append(DpTest(data))
        RECUR.append(RecursionTest(data))
    DP = np.array(DP)
    RECUR = np.array(RECUR)
    return DP, RECUR

if __name__ == '__main__':

    labels = ["p_1", "p_2", "p_3", "p_4"]
    dp_mean, dp_std = [],[]
    recur_mean, recur_std = [], []
    for f in labels:
        DP, RECUR = getResult(FILENAME.format(f))
        d,r = improvement(DP, RECUR)
        dp_mean.append(d[0])
        dp_std.append(d[1])
        recur_mean.append(r[0])
        recur_std.append(r[1])

    legends = ["DP", "RECURSION"]
    disp = PlotResult(labels,legends)
    print(dp_mean, recur_mean)

    disp(dp_mean, dp_std, recur_mean, recur_std)
    disp.plot()