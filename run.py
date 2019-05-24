from glob import glob
from argparse import ArgumentParser
from pprint import pprint
from tqdm import tqdm
from subprocess import check_output
import os

FILE_DIR  = "config/wafr_tests/test_instances/{}/*"


def order(val):
    str = val.split("/")
    str = str[-1].split("_")
    key = int(str[-1])
    return key
def createOutput(path):
    fullpath = os.path.join(os.curdir,path)
    if(os.path.isdir(fullpath)):
        os.makedirs(fullpath,exist_ok=True)



class TestInstance:
    BENCHMARK_OUTPUT_FORMAT ="--benchmark_out_format=json"
    BENCHMARK_REPEAT ="--benchmark_repetitions=3"
    LOG_FILE = "./benchmark.log"

    def __init__(self, file, max_k, threshold):
        self.file = file
        self.max_k = max_k
        self.threhold = threshold
        self.folder_name =file.split("/")[-2]
        self.BENCHMARK_OUTPUT_FILE ="--benchmark_out_file=output/{}/{}.json".format(self.folder_name,order(file))
    def __repr__(self):
        return "filename = {}, max_k {}, threshold {}".format(self.file, self.max_k, self.threhold)
    def param(self):
        arguments = []
        arguments.append(self.BENCHMARK_OUTPUT_FORMAT)
        arguments.append(self.BENCHMARK_OUTPUT_FILE)
        arguments.append(self.BENCHMARK_REPEAT)
        return arguments
    def write(self):
        with open(file=self.LOG_FILE, mode='w') as f:
            f.write("{}\n".format(self.threhold))
            f.write("{}\n".format(self.max_k))
            f.write("{}\n".format(self.file))



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
    check_output(tests.param())


if __name__ == '__main__':
    parser = ArgumentParser("T-ASE Batch Experiment")
    parser.add_argument('--max_k',type=int,default=30)
    parser.add_argument('--threshold', type=float,default=1.0)
    parser.add_argument('--folder',type=str,required=True)

    arg = parser.parse_args()
    print(FILE_DIR.format(arg.folder))


    files =read_dir(FILE_DIR.format(arg.folder))
    tests = [TestInstance(f,arg.max_k,arg.threshold) for f in files]

    output_path = "output/{}".format(tests[0].folder_name)
    createOutput(output_path)

    for t in tqdm(tests):
        run_exp(t)

