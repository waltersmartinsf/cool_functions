import matplotlib.pyplot as __plt__
import seaborn as __sns__
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
    __plt__.xlabel(label, fontsize=20)
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
    __plt__.xlabel(label,fontsize=20)
    __plt__.xlim(xmin,xmax)
    __plt__.savefig(path)

def scatter_cool(X,Y,labelx,labely,label_data,path):
    """
    Scatter plot
    ___
    X: x-variable (array-like)
    Y: y-variable (array-like)
    labelx: label of the x-axis (string)
    labely: label of the y-axis (string)
    label_data: legend of the data in the plot
    path: string, ath to save the picture
    ___


    """
    __plt__.figure()
    __plt__.grid(color='white')
    __plt__.scatter(X,Y, color='blue', label=label_data)
    __plt__.legend()
    __plt__.xlabel(labelx, fontsize=20)
    __plt__.ylabel(labely, fontsize=20)
    __plt__.savefig(path)

def multi_scatter_cool(X1,X2,Y1,Y2,labelx,labely,label_data1,label_data2,path):
    """
    Create in a same plot two scatters plots: (X,Y) and (X,Z)
    ___
    X1: x1-variable (array-like)
    X2: x2-variable (array-like)
    Y1: y1-variable (array-like)
    Y2: y2-variable (array-like)
    labelx: label of the x-axis (string)
    labely: label of the y-axis (string)
    label_data1: legend of the data1 in the plot
    label_data2: legend of the data2 in the plot
    path: string, ath to save the picture
    ___
    """
    __plt__.figure()
    __plt__.grid(color='white')
    __plt__.scatter(X1,Y1, color='blue', label=label_data1)
    __plt__.scatter(X2,Y2, color='red', label=label_data2)
    __plt__.legend()
    __plt__.xlabel(labelx, fontsize=20)
    __plt__.ylabel(labely, fontsize=20)
    __plt__.savefig(path)

def multi_scatter_cool_ylimit(X1,X2,Y1,Y2,labelx,labely,label_data1,label_data2, ymin, ymax, path):
    """
    Create in a same plot two scatters plots: (X,Y) and (X,Z)
    ___
    X1: x1-variable (array-like)
    X2: x2-variable (array-like)
    Y1: y1-variable (array-like)
    Y2: y2-variable (array-like)
    labelx: label of the x-axis (string)
    labely: label of the y-axis (string)
    label_data1: legend of the data1 in the plot
    label_data2: legend of the data2 in the plot
    ymin: minimum in the y-axis
    ymax: maximus in the y-axis
    path: string, ath to save the picture
    ___
    """
    __plt__.figure()
    __plt__.grid(color='white')
    __plt__.scatter(X1,Y1, color='blue', label=label_data1)
    __plt__.scatter(X2,Y2, color='red', label=label_data2)
    __plt__.legend()
    __plt__.xlabel(labelx, fontsize=20)
    __plt__.ylabel(labely, fontsize=20)
    __plt__.ylim(ymin,ymax)
    __plt__.savefig(path)

def multi_scatter_cool_xlimit(X1,X2,Y1,Y2,labelx,labely,label_data1,label_data2, xmin, xmax, path):
    """
    Create in a same plot two scatters plots: (X,Y) and (X,Z)
    ___
    X1: x1-variable (array-like)
    X2: x2-variable (array-like)
    Y1: y1-variable (array-like)
    Y2: y2-variable (array-like)
    labelx: label of the x-axis (string)
    labely: label of the y-axis (string)
    label_data1: legend of the data1 in the plot
    label_data2: legend of the data2 in the plot
    xmin: minimum in the x-axis
    xmax: maximus in the x-axis
    path: string, ath to save the picture
    ___
    """
    __plt__.figure()
    __plt__.grid(color='white')
    __plt__.scatter(X1,Y1, color='blue', label=label_data1)
    __plt__.scatter(X2,Y2, color='red', label=label_data2)
    __plt__.legend()
    __plt__.xlabel(labelx, fontsize=20)
    __plt__.ylabel(labely, fontsize=20)
    __plt__.xlim(xmin,xmax)
    __plt__.savefig(path)

def multi_scatter_cool_xylimit(X1,X2,Y1,Y2,labelx,labely,label_data1,label_data2, xmin, xmax, ymin, ymax, path):
    """
    Create in a same plot two scatters plots: (X1,Y1) and (X2,Y2)
    ___
    X1: x1-variable (array-like)
    X2: x2-variable (array-like)
    Y1: y1-variable (array-like)
    Y2: y2-variable (array-like)
    labelx: label of the x-axis (string)
    labely: label of the y-axis (string)
    label_data1: legend of the data1 in the plot
    label_data2: legend of the data2 in the plot
    xmin: minimum in the x-axis
    xmax: maximus in the x-axis
    ymin: minimum in the y-axis
    ymax: maximus in the y-axis
    path: string, ath to save the picture
    ___
    """
    __plt__.figure()
    __plt__.grid(color='white')
    __plt__.scatter(X1,Y1, color='blue', label=label_data1)
    __plt__.scatter(X2,Y2, color='red', label=label_data2)
    __plt__.legend()
    __plt__.xlabel(labelx, fontsize=20)
    __plt__.ylabel(labely, fontsize=20)
    __plt__.ylim(ymin,ymax)
    __plt__.xlim(xmin,xmax)
    __plt__.savefig(path)
