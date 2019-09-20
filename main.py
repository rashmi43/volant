import pandas
import numpy
import argparse
from analysis import Analysis

class Volant:
    instance = None
    def __init__(self):
        pass

    def run(self,path):
        self.path = path
        data = pandas.read_csv(self.path)
        data.dropna(inplace=True)
        Analysis().boxplot(data)



if __name__ == "__main__":
    path = "./vehicle-1.csv"
    Volant().run(path)