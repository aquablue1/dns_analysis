"""
" Note: This is a duplicated work which has already been done in Q7
" The result of this script is correct. however, the ticks and y_lim are not set properly.

"""
import os
from src.painting.continuousFill import ContinuousFill
import numpy as np


def file_len(filename):
    i = 0
    with open(filename, 'r') as f:
        for i, l in enumerate(f):
            pass
    return i + 1


def gen_dailyData(file_folder):
    daily_data = {}
    for filename in os.listdir(file_folder):
        if "2018-03-12" in filename:
            time = filename[11:13]
            session_count = file_len(file_folder + "/" + filename)
            daily_data[time] = session_count

    return daily_data


def gen_output():
    folder_in = "../../data/result_inbound"
    folder_out = "../../data/result_outbound"
    output_filename ="../../result/result_q3_hourlyCount/2018-03-12_q3.2.log"

    in_daily_dict = gen_dailyData(folder_in)
    out_daily_dict = gen_dailyData(folder_out)

    outputF = open(output_filename, 'a')
    outputF.write("# Number of session per hour, time\tinCount\toutCount\n")
    for time in ["%02d"%time for time in range(0, 24)]:
        line_log = "%s\t%d\t%d\n" % (time, in_daily_dict[time], out_daily_dict[time])
        outputF.write(line_log)
    outputF.close()


def get_statistics(filename):
    label_list = ["inbound", "outbound"]
    data_dict = {}
    x_data = []
    for label in label_list:
        data_dict[label] = []
    with open(filename, 'r') as f:
        for line in f:
            if line[0] == "#":
                continue
            line_list = line.strip().split("\t")
            x_data.append(line_list[0])
            data_dict[label_list[0]].append(int(line_list[1]))
            data_dict[label_list[1]].append(int(line_list[2]))
    return label_list, data_dict, x_data

def draw_hourly(filename):

    label_list, data_dict, x_data = get_statistics(filename)
    color_dict = {"inbound":"blue",
                  "outbound":"red"}

    draw_label = ["outbound", "inbound"]
    draw_master = ContinuousFill(draw_label, data_dict, x_data,
                                 color_dict=color_dict)
    draw_master.organize_draw_data()

    x_label = "time (hour)"
    y_label = "volume of data per hour"
    graph_handle = draw_master.gen_continuous_fill(x_label, y_label, fontsize=20)

    x_ticks = [hour for hour in x_data]

    y_ticks = ["%.2f GB"%size for size in np.arange(0, 10, 2)]
    print(x_data)
    graph_handle.ylim([0, 1000000])
    graph_handle.xticks(x_data, x_ticks, rotation=35, fontsize=15)
    graph_handle.yticks(range(0, 10000000, 2000000), y_ticks, fontsize=15)
    graph_handle.title("Volume of DNS Traffic on 2018-03-12", fontsize=30)
    graph_handle.show()


if __name__ == '__main__':
    # gen_output()
    statistics_filename = "../../result/result_q3_hourlyCount/2018-03-12_q3.2.log"
    draw_hourly(statistics_filename)

