from src.painting.continuousFill import ContinuousFill


def data_gen():
    filename = "../../result/result_q4_minSecCount/sec_2018-03-12.log"
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

    """
    # This gives a micro version with only 100 points ahead.
    label_list = label_list[0:100]
    data_dict["inbound"] = data_dict["inbound"][0:100]
    data_dict["outbound"] = data_dict["outbound"][0:100]
    x_data = x_data[0:100]
    """
    draw_label = ["outbound", "inbound"]
    draw_master = ContinuousFill(draw_label, data_dict, x_data,
                                 color_dict=color_dict)
    draw_master.organize_draw_data()

    x_label = "time"
    y_label = "volume of data per second"
    graph_handle = draw_master.gen_continuous_fill(x_label, y_label, fontsize=20)

    x_ticks = ["%02d:00"%hour for hour in range(0, 24)]
    x_real_selection = range(0, 86400, 3600)
    y_ticks = ["%d KB"%size for size in range(0, 800, 160)]
    # print(x_ticks)
    graph_handle.ylim([0, 800000])
    graph_handle.xticks(x_real_selection, x_ticks, rotation=35, fontsize=15)
    graph_handle.yticks(range(0, 800000, 160000), y_ticks, fontsize=15)
    graph_handle.title("Volume of DNS Traffic per second on 2018-03-12", fontsize=30)
    graph_handle.show()
