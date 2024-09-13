import numpy as np
import math
#from chisla import b, xo, kappa, alpham, chi, ao
import matplotlib as mpl
import matplotlib.pyplot as plt

c = 30_000_000_000
G = 0.000_000_0667
Mo = 2 * 10**33

xo = 100.
mclass = 30.
kappa = 1.0
chi = 0.04
def counting (m, alpham, ao):
    name = f'm={m}, a={ao}, alpham={alpham}.png'
    Rg = 2 * G * m * Mo / (c * c)
    b = mclass / m
    tau = 0
    xs= []
    phis = []
    taus = []
    Ls = []
    aes = []
    x = xo
    a = ao
    v = 0
    metka = 0
    data = []
    while x > 1.05 and tau < 1000:
        h = x / 50.
        tau = tau + h
        f = (x * x - 2. * a * math.sqrt(x) + a * a)**2 / (x * x * x * (math.sqrt(x) * (x - 2) + a * a)**2)
        phi = xo * xo / (x * x) * (1. / xo + 0.5 / (xo * xo) + math.log(1 - 1./xo)) / (1. / x + 0.5 / (x * x) + math.log(1 - 1./x))
        g = 6.25 * a * a / (x * x * x * x) - f + (math.sqrt(1. + b**(4. / 3.)/(x * x)) - 1) / (x) - 2.5 * a * v / (2 * math.pi * chi * x * x)
        gamma = - 0.729 * kappa * alpham * a * a * a * xo * xo * phi * phi / (x * x * x * x * x * x)
        v = v + g * h
        x = x + v * h
        a = a + gamma * h
        #if a > 0.99 * ao: 
        Lo = 1.25 * a * v * v / (2 * math.pi * chi * x * x)
        L1 = 35 * xo * xo * a * a * a * a * alpham * kappa * phi / (x**8)
        #else:
        L = (Lo + L1) * (x * x + a * a - 2 * x) / (x * x + a * a)
        #if x < 0.1 * xo:
        #    if metka == 0:
        #        to=tau
        #        metka = 1
        xs.append(x)
        phis.append(v*v)
        taus.append(tau)
        Ls.append(Lo)
        aes.append(L1)
        data.append([round (tau, 2), round (math.log10(L), 2)])
    return data

