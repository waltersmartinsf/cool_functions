import matplotlib.pyplot as plt
import seaborn
plt.rcParams['figure.figsize'] = (14.0,8.0) # change figure size

def histogram_cool(X,label,path):
    """
    Customize histogram.
    ___
    X: variable (array-like)
    label: string
    path: string, path to save the picture
    """
    plt.figure()
    plt.hist(X)
    plt.xlabel(label)
    plt.savefig(path)

def histogram_cool_limit(X,label,path, xmin, xmax):
    """
    Customize histogram.
    ___

    X: variable (array-like)
    label: string
    path: string, path to save the picture
    xmin, xmax: limites of the variable

    """
    plt.figure()
    plt.hist(X)
    plt.xlabel(label)
    plt.xlim(xmin,xmax)
    plt.savefig(path)
