import get_data_functions as func
import time
import matplotlib.pyplot as plt


    
def plot_data(function,max_entries,title):
    x_data=[]
    y_data=[]


    plt.show()
    fig=plt.figure()
    fig.suptitle(title)
    axes=plt.gca()
    lines,=axes.plot(x_data,y_data,'r-')

    i=len(x_data)

    while 1:
        y_data.append(int(function()))
        if (len(y_data)>max_entries):
            y_data.pop(0)
        else:
            x_data.append(i)
            i=i+1
        lines.set_ydata(y_data)
        lines.set_xdata(x_data)
        axes.relim()
        axes.autoscale_view()
        plt.draw()
        plt.pause(1e-17)
        time.sleep(0.5)

#uncomment to see usage
plot_data(func.get_cpu_usage,50,"CPU Usage %")
