import matplotlib.pyplot as __plt__
import seaborn as __sea__
__plt__.rcParams['figure.figsize'] = (14.0,8.0) # change figure size

def histogram_cool(X,label,path):
    """
    Customize histogram.
    ___
    X: variable (array-like)
    label: string
    path: string, path to save the picture
    """
    __plt__.figure()
    __plt__.hist(X)
    __plt__.xlabel(label)
    __plt__.savefig(path)

def histogram_cool_limit(X,label,path, xmin, xmax):
    """
    Customize histogram.
    ___

    X: variable (array-like)
    label: string
    path: string, path to save the picture
    xmin, xmax: limites of the variable

    """
    __plt__.figure()
    __plt__.hist(X)
    __plt__.xlabel(label)
    __plt__.xlim(xmin,xmax)
    __plt__.savefig(path)
