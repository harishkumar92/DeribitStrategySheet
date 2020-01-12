# -----------------------------------------------------------------------
# blackscholes.py
# -----------------------------------------------------------------------

import sys
import math


# -----------------------------------------------------------------------

# Return the value of the Gaussian probability function with mean 0.0
# and standard deviation 1.0 at the given x value.

def phi(x):
    return math.exp(-x * x / 2.0) / math.sqrt(2.0 * math.pi)


# -----------------------------------------------------------------------

# Return the value of the Gaussian probability function with mean mu
# and standard deviation sigma at the given x value.

def pdf(x, mu=0.0, sigma=1.0):
    return phi((x - mu) / sigma) / sigma


# -----------------------------------------------------------------------

# Return the value of the cumulative Gaussian distribution function
# with mean 0.0 and standard deviation 1.0 at the given z value.

def Phi(z):
    if z < -8.0: return 0.0
    if z > 8.0: return 1.0
    total = 0.0
    term = z
    i = 3
    while total != total + term:
        total += term
        term *= z * z / float(i)
        i += 2
    return 0.5 + total * phi(z)


# -----------------------------------------------------------------------

# Return standard Gaussian cdf with mean mu and stddev sigma.
# Use Taylor approximation.

def cdf(z, mu=0.0, sigma=1.0):
    return Phi((z - mu) / sigma)


# -----------------------------------------------------------------------

# Black-Scholes formula.

def callPrice(s, x, r, sigma, t):
    a = (math.log(s / x) + (r + sigma * sigma / 2.0) * t) / (sigma * math.sqrt(t))
    b = a - sigma * math.sqrt(t)

    return s * cdf(a) - x * math.exp(-r * t) * cdf(b)


def putPrice(s, x, r, sigma, t):
    a = (math.log(s / x) + (r + sigma * sigma / 2.0) * t) / (sigma * math.sqrt(t))
    b = a - sigma * math.sqrt(t)

    return (x * math.exp(-r * t) * cdf(-b)) - (s * cdf(-a))


def straddlePrice(s, x, r, sigma, t):
    return callPriceUsd(s, x, r, sigma, t) + putPrice(s, x, r, sigma, t)


def stranglePrice(s, x1, x2, r, sigma, t):
    """
	x1 : strike price of OTM Call
	x2 : strike price of OTM Put
	"""
    callPriceUsd = callPrice(s, x1, r, sigma, t)
    putPriceUsd = putPrice(s, x2, r, sigma, t)
    return callPriceUsd + putPriceUsd


if __name__ == '__main__':
    x1 = 4250
    x2 = 3750
    r = 0
    sigma = float(.5)
    t = float(7 / 365.0)

    print (callPrice(s=7350, x=7250, r=0, sigma=0.55, t=7/365.0)/7350)

    # strangleUSD = round(stranglePrice(s, x1, x2, r, sigma, t), 2)
    # strangleBTC = round(strangleUSD / s, 4)

    #print("Spot={0}, strangleUSD={1}, strangleBTC={2}".format(s, strangleUSD, strangleBTC))

# print ("SPOT=${0}, CallPriceUSD=${1}, CallPriceBtc={2}, PutPriceUSD=${3}, PutPriceBtc={4}"\
#	.format(s, round(callPriceUsd, 3), round(callPriceBtc, 3), round(putPriceUsd, 3), round(putPriceBtc, 3)))
