"""
Draw continuous fill graphs.
"""
import matplotlib.pyplot as plt


class ContinuousFill(object):
    def __init__(self, label_list, data_dict, x_data, color_dict=None,):
        self.label_list = label_list
        self.data_dict = data_dict
        self.x_data = x_data

        # Check whether all labels exist in data_dict
        for key in label_list:
            if key not in self.data_dict.keys():
                raise KeyError("Label Name not exist in data_dict")

        # Generate an empty draw_data dict to store the data used to generate graph
        self.draw_data = {}
        for key in label_list:
            self.draw_data[key] = []

        # Check whether all values in data_dict has the same length.
        self.data_length = len(self.x_data)
        for key in label_list:
            if self.data_length != len(self.data_dict[key]):
                raise RuntimeError("Not all the value lists have the same length")

        # Check the color dict if it is defined by user
        if color_dict is not None:
            for key in label_list:
                if key not in color_dict.keys():
                    raise KeyError("Label Name not exist in color_dict")
            self.color_dict = color_dict
        else:
            self.color_dict = color_dict

    def organize_draw_data(self):
        cur_peak_list = [0] * self.data_length
        for key in self.label_list:
            cur_peak_list = [a+b for a,b in zip(cur_peak_list, self.data_dict[key])]
            self.draw_data[key] = cur_peak_list
        print(self.draw_data)

    def gen_continuous_fill(self, x_label, y_label, fontsize=10):
        """
        Accept two string parameters as the label for x and y axis respectively. Then draw continuous fill graph
        :param x_label: label for x axis
        :param y_label: label for y axis
        :return: graph
        """
        cur_bottom_list = [0] * self.data_length
        ax = plt.subplot(1, 1, 1)
        for key in self.label_list:
            ax.fill_between(self.x_data, cur_bottom_list, self.draw_data[key], label=key, color=self.color_dict[key])
            cur_bottom_list = self.draw_data[key]
        handles, labels = ax.get_legend_handles_labels()
        plt.legend(handles[::-1], labels[::-1], loc="upper left")
        plt.xlabel(x_label, fontsize=fontsize)
        plt.ylabel(y_label, fontsize=fontsize)
        return plt

    def draw_continuous_fill(self, x_label, y_label):
        graph_handle = self.gen_continuous_fill(x_label, y_label)
        graph_handle.show()



if __name__ == '__main__':
    label_list = ["a", "b"]
    data_dict = {"a": [1,2,3],
                 "b": [4,5,6]}
    x_data = [1,3,5]
    color_dict = {"a": "r",
                  "b": "b"}
    c = ContinuousFill(label_list, data_dict, x_data, color_dict=color_dict)
    c.organize_draw_data()

    x_label = "Time (hour)"
    y_label = "# of Sessions Per Hour"
    do_draw = c.draw_continuous_fill(x_label, y_label)
    do_draw.show()