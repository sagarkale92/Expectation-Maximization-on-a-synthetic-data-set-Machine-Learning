import sys
import math
import random
import numpy as np
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt
from scipy.stats.kde import gaussian_kde

class Driver(object):
    """Driver class to implements em algorithm and generates histogram.
    """
    iterator = 1
    """int: iterator.
    """
    
    def expectation(self, x, u, hypothesis):
        """Computes expectation from hypothesis list.

        Args:
            param1: x (value).
            param2: u (distribution).
            param3: hypothesis (distributions list)

        Returns:
            float.

        """
        num = math.exp(self.diffSquareProduct(x, u))
        din = 0
        for i in range(len(hypothesis)):
            din = din + math.exp(self.diffSquareProduct(x, hypothesis[i]))
        res = num / din
        return res

    def diffSquareProduct(self, x, u):
        """Computes square of difference from hypothesis list.

        Args:
            param1: x (value).
            param2: u (distribution).

        Returns:
            float.

        """
        diff = x - u
        res = math.pow(diff, 2)
        res = res * (-0.5)
        return res

    def sumExpValue(self, mydata, mat, j):
        """Sums expecations and inputs.

        Args:
            param1: mydata (input values).
            param2: mat (expectations).
            param3: j (mat index)

        Returns:
            float.

        """
        sum = 0
        for i in range(len(mydata)):
            sum = sum + mat[i][j] * mydata[i]
        return sum

    def sumExp(self, l, mat, j):
        """Sums expectations.

        Args:
            param1: mydata (input values).
            param2: mat (expectations).
            param3: j (mat index)

        Returns:
            float.

        """
        sum = 0
        for i in range(l):
            sum = sum + mat[i][j]
        return sum

    def average(self, list):
        """Averages list.

        Args:
            param1: list.

        Returns:
            float.

        """
        res = 0
        num = sum(list)
        div = len(list)
        res = num / div
        return res

    def maxDiff(self, list1, list2):
        """Calculates maximum difference between list for each index.

        Args:
            param1: list1 (list).
            param2: list2 (list).

        Returns:
            float.

        """
        max = 0
        for i in range(len(list1)):
            diff = abs(list1[i] - list2[i])
            if diff > max:
                max = diff
        return max

    def printu(self, hypothesis):
        sys.stdout.write("(")
    	for i in range(len(hypothesis)):
            	sys.stdout.write("u"+str(i+1))
            	if i < len(hypothesis) - 1:
            		sys.stdout.write(", ")
            	else:
            		sys.stdout.write("): ")

    def iteration(self, mydata, hypothesis, improvement):
        """Iterative function that calculates new hypothesis in each iteration.

        Args:
            param1: mydata (input values).
            param2: hypothesis (distributions list).
            param3: improvement (float)

        Returns:

        """
        delta = 0.001
        if(improvement < delta):
            print ("******************************************************************************************************************")
            print
            sys.stdout.write("The final estimated values for ")
            self.printu(hypothesis)
            print hypothesis
            return
        if self.iterator < 6:
            print ("Iteration: " + str(self.iterator))
        mat = []
        for k in range(len(mydata)):
            list = []
            for j in range(len(hypothesis)):
                list.append(self.expectation(mydata[k], hypothesis[j], hypothesis))
            mat.append(list)
        hypothesisNew = []
        for j in range(len(hypothesis)):
            myu = self.sumExpValue(mydata, mat, j) / self.sumExp(len(mydata), mat, j)
            hypothesisNew.append(myu)
        if self.iterator < 6:
            sys.stdout.write("The estimated values for ")
            self.printu(hypothesis)
            print (hypothesisNew)
        improvement = self.maxDiff(hypothesis, hypothesisNew)
        self.iterator = self.iterator + 1
        self.iteration(mydata, hypothesisNew, improvement)

    def histogram(self, data, binsCount):
        """Plots histogram from input values.

        Args:
            param1: data (input values).
            param2: binsCount (integer).

        Returns:

        """
        plt.xlim([min(data), max(data)])
        bins = np.linspace(math.ceil(min(data)), math.floor(max(data)), binsCount)
        plt.title('Gaussian Mixture unlabeled data with bins='+str(binsCount))
        plt.xlabel('Data points')
        plt.ylabel('Frequency')
        gkde = gaussian_kde(data)
        plt.plot(bins, gkde(bins), 'r', linewidth=2)
        plt.hist(data, normed=1, bins=bins, alpha=0.5)
        plt.savefig('histogram'+str(binsCount))
        plt.gcf().clear()

    def __init__(self):
        """Implements EM algorithm and generates histogram of data.
        """
        if len(sys.argv) < 3:
            print 'Invalid Arguments'
            sys.exit(-1)
        inputfile = sys.argv[1]
        numOfClusters = int(sys.argv[2])
        randomSeed = int(sys.argv[3])
        mydata = np.loadtxt(inputfile)
        hypothesis = random.sample(range(randomSeed), numOfClusters)
        sys.stdout.write ("The initial Guess of ")
        self.printu(hypothesis)
        print hypothesis
        print ("******************************************************************************************************************")
        print
        improvement = float('inf')
        self.iteration(mydata, hypothesis, improvement)
        print ("******************************************************************************************************************")
        binsCount = 25
        self.histogram(mydata, binsCount)
        print
        print ("Histogram of data is Generated successfully")
        uinput = raw_input("Do you want to generate histogram of data with different bins count (yes/no)? ")
        while uinput.lower() == 'yes' or uinput.lower() == 'y':
            binsCount = raw_input ("Enter bins count [1-299] (Eg.15): ")
            self.histogram(mydata, binsCount)
            print ("Histogram of data is Generated successfully")
            uinput = raw_input("Do you want to generate histogram of data with different bins count (yes/no)? ")

"""New instance of class
"""
driver = Driver()