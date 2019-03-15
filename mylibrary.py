from __future__ import division
#----------Libraries Commonly Used--------------
import numpy as np
import scipy as sp
from scipy.special import gamma as Gamma
from math import *
from sympy import *
from pylab import *
from numpy import linalg as la
import matplotlib.pyplot as plt

#---------------Symbolic Examples---------------
#--------------------Vector---------------------
f = np.array(symbols('x(1:4)'))
#print "f(x1, x2, x3) = ", f
#
#---------------2D Stress Matrix----------------
sig = np.array(symbols('sig1:4(1:4)')).reshape((3,3))
#sig  = np.reshape(sig, (3,3))
#print "Stress matrix = \n", sig

#-----------------Functions---------------------
def eigen(matrix):
    #     gets eigenpairs where the vectors are normalized
    [eigenvalues, eigenvectors] = la.eig(matrix)
    #     sorts and rearranges eigenpairs 
    idx = eigenvalues.argsort()[::-1]   
    #     Avals are the values for lambda, or equivalently, the eigenvals
    Avals = eigenvalues[idx]*np.eye(len(eigenvalues))
    #     Mo is the corresponding Modal Matrix
    Mo = eigenvectors[:,idx]
    print ('[Lambda] = \n', Avals,'\n')
    print ('[Modal] or [M^o] = \n', Mo,'\n')
    return gam_vals, Mo
#
def inwc(inches):
    inh2o = inches
    psi = np.array([inh2o * 0.036091])
    print (inh2o, "Inch of Water is equal to ", psi , " psi.")
    return psi
#
def area_rect(length, width):
    #l = input("Enter length in inches:\t")
    #w = input("Enter width in inches:\t")
    area = l*w/144
    print ("The area is", area , "sf")
    return area
#
def area_circ(diameter):
    area = pi*(diameter**2/4)/144
    print ("The area is", area , "sf")
    return area
#
def area_tri(base, height):
    area = (base*height/2)/144
    print ("The area is", area , "sf")
    return area
#