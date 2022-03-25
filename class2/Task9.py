import scipy

from scipy.integrate import simps



MEAN = 0

SIGMA = 2



x_axis = np.round(np.arange(MEAN - 3*SIGMA, MEAN + 3*SIGMA, 0.01), 2)

normal = scipy.stats.norm.pdf(x_axis, MEAN, SIGMA)



startSigma = int(np.where(x == MEAN - SIGMA)[0])

endSigma = int(np.where(x == MEAN + SIGMA)[0])

startSigmaDouble = int(np.where(x == MEAN - 2*SIGMA)[0])

endSigmaDouble = int(np.where(x == MEAN + 2*SIGMA)[0])



areas = (

    np.trapz(normal[startSigma:endSigma], x=x[startSigma:endSigma]),

    np.trapz(normal[startSigmaDouble:endSigmaDouble], x=x[startSigmaDouble:endSigmaDouble]),

    np.trapz(normal, x=x[:]))

print(areas)

plt.plot(x_axis, normal)

plt.text(0, 0, "Area: " + str(np.trapz(normal, x=x[:])), bbox={'facecolor':'white'})

plt.fill_between(x_axis, normal)

plt.show()
