from src.painting.continuousFill import ContinuousFill
import numpy as np
from src.painting.dataGenToDraw import DataGenToDraw

def draw_hourly():
    print("")


def data_gen():
    filename = "../../result/result_q3_hourlyCount/2018-03-12.log"
    label_list = ["inbound", "outbound"]
    x_data = []
    data_dict = {}
    for label in label_list:
        data_dict[label] = []

    with open(filename, 'r') as f:
        for line in f:
            if line[0] == "#":
                continue
            line_list = line.strip().split("\t")
            x_data.append(int(line_list[0]))
            data_dict[label_list[0]].append(int(line_list[1]))
            data_dict[label_list[1]].append(int(line_list[2]))

    return label_list, data_dict, x_data


if __name__ == '__main__':
    label_list, data_dict, x_data = data_gen()
    color_dict = {"inbound":"blue",
                  "outbound":"red"}

    draw_label = ["outbound", "inbound"]
    draw_master = ContinuousFill(draw_label, data_dict, x_data,
                                 color_dict=color_dict)
    draw_master.organize_draw_data()

    x_label = "time (hour)"
    y_label = "volume of data per hour"
    graph_handle = draw_master.gen_continuous_fill(x_label, y_label, fontsize=20)

    x_ticks = ["%02d:00"%hour for hour in x_data]

    y_ticks = ["%.2f GB"%size for size in np.arange(0, 10, 2)]
    print(x_data)
    graph_handle.ylim([0, 10000000000])
    graph_handle.xticks(x_data, x_ticks, rotation=35, fontsize=15)
    graph_handle.yticks(range(0, 10000000000, 2000000000), y_ticks, fontsize=15)
    graph_handle.title("Volume of DNS Traffic on 2018-03-12", fontsize=30)
    graph_handle.show()
