import matplotlib.pyplot as plt


class Plot_Perodical(object):
    def __init__(self, data):
        self.data = data

        self.labels = None
        self.title = None

    def set_labels(self, labels):
        self.labels = [None, None]
        self.labels[0] = labels[0]
        self.labels[1] = labels[1]

    def set_title(self, title):
        self.title = title

    def do_draw(self, y_min=0, y_max=1):
        y_list = [y_min, y_max]
        for x_data in self.data:
            x_list = [x_data, x_data]
            plt.plot(x_list, y_list, color='black')
        if self.labels is not None:
            plt.xlabel(self.labels[0])
            plt.ylabel(self.labels[1])
        if self.title is not None:
            plt.title(self.title)
        plt.show()




if __name__ == '__main__':
    sample_data = [1.1,2,3,4,5]
    p_test = Plot_Perodical(sample_data)
    p_test.do_draw(0, 1)
