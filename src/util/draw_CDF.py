"""
" This is a General Method Used to draw Single CDF graph
" The single CDF graph indicates that original graph only contains one line. Only has one "SubGraph"
" Typically accept a (sorted) integer list, with each number represent the occurrence of a certain object.
" This method will check all the input values to make sure they are nature numbers or zero.
" This method can either return the plt used to generate the graph or show the graphs directly.
" By default there is no label/tick/title/colors. TBut they can be specified by calling corresponding methods.
"
"""
import matplotlib.pyplot as plt
import math

class CDF_Single(object):
    def __init__(self):
        # Original Data used to generate graph
        self.plt = plt
        self.data = None

        # color
        self.color = None

        # label_list, first elem represents xlabel and second elem represents ylabel
        self.labels = None

        # legend
        self.legend = None

        # Title
        self.title = None

        # x- and y-axis mapping
        # first elem is real data
        # second elem is to show data
        self.xtick_map = None
        self.ytick_map = None

    def set_data(self, data):
        self.data = data
        self.data.sort(reverse=True)

    def set_color(self, color):
        self.color = color

    def set_labels(self, label_list):
        try:
            self.labels = label_list[0:2]
        except IndexError as e:
            print("Input label_list does not long enough")

    def set_legend(self, legend):
        self.legend = legend
        plt.legend(loc="upper left")

    def set_title(self, title):
        self.title = title
        plt.title(self.title)

    def set_tick_map(self, axis_str, real_data, tick_data):
        if axis_str.lower() == "x":
            self.xtick_map = [real_data, tick_data]
        elif axis_str.lower() == "y":
            self.ytick_map = [real_data, tick_data]


    def gen_toDraw_data(self):
        if self.data is None:
            raise ValueError("No Input data has been specified")
        sum_count = sum(self.data)
        property_list = [0]*(len(self.data)+1)
        for i in range(1, len(self.data)+1):
            property_list[i] = property_list[i-1] + self.data[i-1]/sum_count
        return property_list

    def do_draw(self, is_log = False):
        y_orig_data = self.gen_toDraw_data()
        print(y_orig_data)
        x_orig_data = [i+1 for i in range(len(y_orig_data))]

        y_data = y_orig_data
        if is_log:
            x_data = [math.log10(i) for i in x_orig_data]
        else:
            x_data = x_orig_data

        self.plt.plot(x_data, y_data, color=self.color, label=self.legend)
        self.plt.ylim([0,1.1])
        if self.labels is not None:
            plt.xlabel(self.labels[0])
            plt.ylabel(self.labels[1])
        if self.legend is not None:
            plt.legend(loc="best")
        if self.title is not None:
            plt.title(self.title)
        if self.xtick_map is not None:
            plt.xticks(self.xtick_map[0], self.xtick_map[1])
        if self.ytick_map is not None:
            plt.yticks(self.ytick_map[0], self.ytick_map[1])
        return self.plt

    def do_show(self, is_log = False):
        self.do_draw(is_log)
        self.plt.show()

if __name__ == '__main__':

    # Sample usage
    list = [1,2,3,4,7,53,6,4,1,1]
    cdf = CDF_Single()
    cdf.set_data(list)
    cdf.set_color("red")
    cdf.set_legend("A")
    cdf.set_tick_map("x", [1, 5, 7], ["A", "B", "C"])
    cdf.set_labels(["Number of Distinct URLs.", "CDF"])
    cdf.do_show()
