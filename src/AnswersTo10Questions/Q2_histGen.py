import matplotlib.pyplot as plt
import numpy as np


def data_collect(filaname, date_list):
    data_in = {}
    data_out = {}
    for date in date_list:
        data_in[date] = 0
        data_out[date] = 0
    with open(filaname, 'r') as f:
        for line in f:
            line_list = line.strip().split("\t")
            descp = line_list[1]
            date = descp[7:17]
            if date in date_list:
                data_in[date] += int(line_list[3])
                data_out[date] += int(line_list[4])
    return data_in, data_out


def do_hist_gen(daily_count_in_dict, daily_count_out_dict):
    x_location = range(len(daily_count_in_dict))

    ax = plt.subplot(1, 1, 1)

    ax.bar(x_location, list(daily_count_in_dict.values()),[0.6]*len(daily_count_in_dict),
             label="inbound", color="blue")

    ax.bar(x_location, list(daily_count_out_dict.values()), [0.6]*len(daily_count_out_dict),
            list(daily_count_in_dict.values()), label="outbound", color="red")

    plt.xlabel("date", fontsize=14)
    plt.ylabel("number of DNS sessions per day", fontsize=14)
    x_toshow = list(daily_count_in_dict.keys())
    plt.ylim([0, 80000000])
    plt.xticks(x_location, x_toshow, rotation=20, fontsize=14)
    handles, labels = ax.get_legend_handles_labels()
    plt.legend(handles[::-1], labels[::-1], loc="upper left")
    plt.show()


if __name__ == '__main__':
    source = "../../data/result_inout/dns_InOutCount_2018-03_F.log"
    date_list = ["2018-03-11", "2018-03-12", "2018-03-13",
                 "2018-03-14", "2018-03-15", "2018-03-16", "2018-03-17"]
    daily_count_in_dict, daily_count_out_dict = data_collect(source, date_list)
    print(daily_count_in_dict)
    print(daily_count_out_dict)
    do_hist_gen(daily_count_in_dict, daily_count_out_dict)