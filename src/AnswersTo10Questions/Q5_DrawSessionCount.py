import os
import numpy as np
from src.painting.continuousFill import ContinuousFill

def file_len(filename):
    i=0
    with open(filename, 'r') as f:
        for i, l in enumerate(f):
            pass
    return i + 1

def get_Statistics_byHour(folder_name):
    session_count_list = []
    for filename in os.listdir(folder_name):
        if "2018-03-12" in filename:
            session_count = file_len(folder_name + "/" + filename)
            session_count_list.append(session_count)
    return session_count_list

def get_readyData(filename):
    session_in = []
    session_out = []
    with open(filename, 'r') as f:
        for line in f:
            if line[0] == "#":
                continue
            line_list = line.strip().split("\t")
            session_in.append(int(line_list[0]))
            session_out.append(int(line_list[1]))
    return session_in, session_out


if __name__ == '__main__':
    folder_name_in = "../../data/result_inbound"
    folder_name_out = "../../data/result_outbound"

    # session_count_in = get_Statistics_byHour(folder_name_in)
    # session_count_out = get_Statistics_byHour(folder_name_out)

    # output_folder = "../../result/result_q5_sessionCount/"
    # output_filename = "2018-03-12.log"
    # outputF = open(output_folder + output_filename, 'a')

    # for inbound, outbound in zip(session_count_in, session_count_out):
        # outputF.write("%d\t%d\n" % (inbound, outbound))

    # outputF.close()
    session_count_in, session_count_out = get_readyData("../../result/result_q5_sessionCount/2018-03-12.log")
    label_list = ["inbound", "outbound"]
    data_dict = {"inbound":session_count_in,
                 "outbound":session_count_out}
    color_dict = {"inbound": "blue",
                  "outbound": "red"}
    x_data = ["%02d" % i for i in range(0, 24)]

    draw_label = ["outbound", "inbound"]
    draw_master = ContinuousFill(draw_label, data_dict, x_data,
                                 color_dict=color_dict)
    draw_master.organize_draw_data()

    x_label = "time (hour)"
    y_label = "Number of Requests per hour"
    graph_handle = draw_master.gen_continuous_fill(x_label, y_label, fontsize=20)

    x_ticks = ["%02d:00" % int(hour)for hour in x_data]
    y_ticks = ["%.2f M" % i for i in np.arange(0, 4, 0.5)]

    graph_handle.xticks(x_data, x_ticks, rotation=35, fontsize=15)
    graph_handle.yticks(range(0, 4000000, 500000), y_ticks, fontsize=15)
    graph_handle.title("Count of DNS Traffic on 2018-03-12", fontsize=30)
    graph_handle.show()
