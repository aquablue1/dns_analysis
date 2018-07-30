import matplotlib.pyplot as plt


class Plot_Perodical(object):
    def __init__(self, data):
        self.data = data


    def do_draw(self, y_min=0, y_max=1):
        y_list = [y_min, y_max]
        for x_data in self.data:
            x_list = [x_data, x_data]
            plt.plot(x_list, y_list, color='b')
        plt.show()


if __name__ == '__main__':
    sample_data = [1,2,3,4,5]
    p_test = Plot_Perodical(sample_data)
    p_test.do_draw(0, 1)
