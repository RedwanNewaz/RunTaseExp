
from glob import glob
from argparse import ArgumentParser
from pprint import pprint
from tqdm import tqdm
import subprocess
import os
FILE_DIR  = "./config/wafr_tests/test_instances/{}/*"

#    --benchmark_repetitions=3 --benchmark_out_format=json --benchmark_out=1.json


def order(val):
   str = val.split("/")
   str = str[-1].split("_")
   key = int(str[-1])
   return key

class TestInstance(object):
   BENCHMARK_OUTPUT_FROMAT ="--benchmark_out_format=json"
   BENCHMARK_REPEAT ="--benchmark_repetitions=3"
   LOG_FILE = "./benchmark.log"

   def __init__(self, file, max_k, threshold):
       self.file = file
       self.max_k = max_k
       self.threhold = threshold

       splitnames = file.split("/")
       self.FOLDER = splitnames[-2]

       self.BENCHMARK_OUTPUT_FILE = "--benchmark_out=output/{}/{}.json".format(self.FOLDER,order(file))

   def __repr__(self):
       return "filename = {}, max_k {}, threshold {}".format(self.BENCHMARK_OUTPUT_FROMAT, self.max_k, self.threhold)

   def write(self):
       with open(file=self.LOG_FILE, mode='w') as f:
           f.write("{}\n".format(self.threhold))
           f.write("{}\n".format(self.max_k))
           f.write("{}\n".format(self.file))
   def arg(self):
       fullpath = os.path.join(os.curdir, "output/{}".format(self.FOLDER))
       if(not os.path.isdir(fullpath)):
           os.makedirs(fullpath,exist_ok=True)

       arguments = ["./T_ASE_SERVER_PREBUILD_Benchmark"]
       arguments.append(self.BENCHMARK_REPEAT)
       arguments.append(self.BENCHMARK_OUTPUT_FROMAT)
       arguments.append(self.BENCHMARK_OUTPUT_FILE)
       return arguments



def read_dir(filename):
   files = glob(filename)
   files = [str(f) for f in files]
   files.sort(key=order)
   return files

def run_exp(test):
   '''
   :param test: TestInstance
   :return: Excecute T_ASE_Benchmark with arguments
   '''
   test.write()
   subprocess.check_output(test.arg(), stderr=subprocess.STDOUT)
   # subprocess.run(test.arg(), capture_output=True)




if __name__ == '__main__':
   parser = ArgumentParser("T-ASE Batch Experiment")
   parser.add_argument('--max_k',type=int,default=30)
   parser.add_argument('--threshold', type=float,default=1.0)
   parser.add_argument('--folder',type=str,required=True)

   arg = parser.parse_args()
   print(FILE_DIR.format(arg.folder))

   files =read_dir(FILE_DIR.format(arg.folder))
   tests = [TestInstance(f,arg.max_k,arg.threshold) for f in files]
   for t in tqdm(tests):
       run_exp(t)


