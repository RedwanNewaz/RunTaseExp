import matplotlib
import matplotlib.pyplot as plt
import numpy as np



class PlotResult(object):
    
    def __init__(self, labels, legends):
        self.fig, self.ax = plt.subplots()
        self.labels = labels
        self.legends = legends

    def autolabel(self, rects, xpos='center'):
        """
        Attach a text label above each bar in *rects*, displaying its height.
    
        *xpos* indicates which side to place the text w.r.t. the center of
        the bar. It can be one of the following {'center', 'right', 'left'}.
        """

        ha = {'center': 'center', 'right': 'left', 'left': 'right'}
        offset = {'center': 0, 'right': 1, 'left': -1}
    
        for rect in rects:
            height = rect.get_height()
            self.ax .annotate('{:.3f}'.format(height),
                        xy=(rect.get_x() + rect.get_width() / 2, height),
                        xytext=(offset[xpos]*3, 3),  # use 3 points offset
                        textcoords="offset points",  # in both directions
                        ha=ha[xpos], va='bottom')
            
    def __call__(self, *args, **kwargs):
        assert len(args)==4 ,"4 arguments needed"
        self.dp_means, self.dp_std = args[0], args[1]
        self.recur_means, self.recur_std = args[2], args[3]
        
            
    
    def plot(self):
        ind = np.arange(len(self.dp_means))  # the x locations for the groups
        width = 0.35  # the width of the bars
        
        rects1 = self.ax .bar(ind - width/2, self.dp_means, width, yerr=self.dp_std,
                        label=self.legends[0])
        rects2 = self.ax .bar(ind + width/2, self.recur_means, width, yerr=self.recur_std,
                        label=self.legends[1])
        
        # Add some text for labels, title and custom x-axis tick labels, etc.
        self.ax.set_ylabel('Time in log sec')
        self.ax.set_title('Performance Comparison')
        self.ax.set_xticks(ind)
        self.ax.set_xticklabels(self.labels)
        self.ax.legend(loc=2)
        
        self.autolabel(rects1, "left")
        self.autolabel(rects2, "right")
        
        self.fig.tight_layout()        
        plt.show()
    






if __name__ == '__main__':
    labels = ('G1', 'G2', 'G3', 'G4', 'G5')
    legends = ("DP", "RECURSION")
    disp = PlotResult(labels,legends)
    dp_mean, dp_std = (20, 35, 30, 35, 27), (2, 3, 4, 1, 2)
    recur_mean, recur_std = (25, 32, 34, 20, 25), (3, 5, 2, 3, 3)
    disp(dp_mean, dp_std, recur_mean, recur_std)
    disp.plot()

