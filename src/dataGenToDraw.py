"""
Generate data to draw continuous fill graphs
"""

class DataGenToDraw(object):
    def __init__(self):
        self.global_label_list = None
        self.draw_label = None

        self.data_dict = {}
        self.color_dict = {}
        # self.data_list_length = 0
        print("Create Parameter Container")

    def set_label_list(self, global_label_list, draw_label_list):
        """
        Accept two lists
        :param global_label_list: list used to store all label info
        :param draw_label_list: list used to specify labels to show on graph
        :return:
        """
        # If global_label_list is empty, raise error
        if global_label_list is None or global_label_list == []:
            raise RuntimeError("Input global label list is empty.")
        self.global_label_list = global_label_list

        # If draw label list is empty, also raise error
        if draw_label_list is None or draw_label_list == []:
            raise RuntimeError("Input draw label list is empty.")
        self.draw_label_list = draw_label_list

    def set_data_dict(self, location_list=None):
        """
        Init the data_dict with the merge of global_list and draw_list
        and insert original data to data_dict.
        :param location_list:
        :return:
        """
        if location_list is None:
            raise RuntimeError("No input data file specified.")

        # First loop add all labels for original data
        # Second loop add all new labels in draw_label_list
        for key in self.global_label_list:
            self.data_dict[key] = []
        for key in self.draw_label_list:
            if key in self.global_label_list:
                continue
            else:
                self.data_dict[key] = []

        for location in location_list:
            with open(location) as f:
                last_hour = "-10"
                for line in f:
                    line = line.strip()
                    line_list = line.split("\t")
                    insert_pointer = 2
                    cur_hour = line_list[1].split("/")[-1].split(".")[-3][0:2]
                    for key in self.global_label_list:
                        if cur_hour == last_hour:
                            self.data_dict[key][-1] += int(line_list[insert_pointer])
                        else:
                            self.data_dict[key].append(int(line_list[insert_pointer]))
                        insert_pointer += 1
                    last_hour = cur_hour
        print(self.data_dict)

    def set_specified_data(self, key, new_list):
        if key not in self.data_dict.keys():
            raise KeyError("Key not found in pre-defined key list")
        self.data_dict[key] = new_list
        print(self.data_dict)

    def set_color_dict(self, color_list):
        for key in self.data_dict.keys():
            self.color_dict[key] = None
        for key, color in zip(self.data_dict.keys(), color_list):
            if color == "":
                color = "black"
            self.color_dict[key] = color
        print(self.color_dict)

    def get_x_label(self):
        return list(range(len(self.data_dict[self.global_label_list[0]])))

if __name__ == '__main__':
    file_path = "../data/insert_sample.txt"
    file_path_list = [file_path]
    data_factory = DataGenToDraw()

    global_list = ["Inbound", "Outbound", "Odd"]
    draw_list = ["Inbound", "Outbound", "Sum"]
    data_factory.set_label_list(global_list, draw_list)
    data_factory.set_data_dict(file_path_list)

    sum_list = [sum(x) for x in zip(data_factory.data_dict["Inbound"], data_factory.data_dict["Outbound"])]
    data_factory.set_specified_data("Sum", sum_list)

    color_list = ["red", "green", "blue", ""]
    data_factory.set_color_dict(color_list)
    print(data_factory.get_x_label())