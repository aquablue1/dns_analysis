import matplotlib.pyplot as plt


class ContinuousPie(object):
    def __init__(self, label_list, data_dict, color_dict=None,):
        self.label_list = label_list
        self.data_dict = data_dict

        # Check whether all labels exist in data_dict
        for key in label_list:
            if key not in self.data_dict.keys():
                raise KeyError("Label Name not exist in data_dict")

        # Generate an empty draw_data dict to store the data used to generate graph
        self.draw_data = {}
        for key in label_list:
            self.draw_data[key] = 0

        # Check the color dict if it is defined by user
        if color_dict is not None:
            for key in label_list:
                if key not in color_dict.keys():
                    raise KeyError("Label Name not exist in color_dict")
            self.color_dict = color_dict
        else:
            self.color_dict = color_dict

    def organize_draw_data(self):
        for key in self.label_list:
            self.draw_data[key] = sum(self.data_dict[key])
        print(self.draw_data)

    def generate_continuous_fill(self, title):
        """
        Generate plt object for Pie chart and return it
        :param title: Title for this pie chart
        :return: plt which stores the pie chart
        """
        plt.pie([self.draw_data[key] for key in self.label_list],
                labels=self.label_list,
                colors=[self.color_dict[key] for key in self.label_list],
                autopct = '%.0f%%',
                radius=0.8
                )
        plt.title(title)
        plt.legend(loc="best")

        return plt

    def draw_continuous_fill(self, title):
        draw_handle = self.generate_continuous_fill(title)
        draw_handle.show()


if __name__ == '__main__':
    label_list = ["a", "b"]
    data_dict = {"a": [1,2,3],
                 "b": [4,5,6]}

    color_dict = {"a": "r",
                  "b": "b"}
    c = ContinuousPie(label_list, data_dict, color_dict=color_dict)
    c.organize_draw_data()

    title = "Pie Chart"
    c.draw_continuous_fill(title)
    # do_draw.show()