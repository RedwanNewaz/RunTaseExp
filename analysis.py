from glob import glob
from run import order
import json

class Analyzer:
    def __init__(self, data):
        self.file = data
    def read(self):
        with open(self.file, 'r') as file:
            # jsonData = json.loads(file)
            print(file)


if __name__ == '__main__':
    # folders = [  "megamedes", "styx", "oceanus", "tethys"]
    # for f in folders:
    #     files = glob("{}/OUT/*.json".format(f))
    #     # results = [Analyzer(d) for d in files]
    #     # results[0].read()
    #     for f in files:
    #         with open(f) as json_file:
    #             data = json.load(json_file)
    #             print(data)

    with open("oceanus/OUT/1.json") as json_file:
        data = json.load(json_file)
        print(data)