import os
import matplotlib.pyplot as plt
import math

def get_countData(filename):
    count_list = []
    with open(filename, 'r') as f:
        for line in f:
            if line[0] == "#":
                continue
            line_list = line.strip().split(" ")
            # print(line_list)
            count_list.append(int(line_list[0]))
    return count_list


if __name__ == '__main__':
    filename = "../../data/result_q8_popIP/top1000_out_domainName.log"
    label = "Outgoing Domain Names"
    count_list = get_countData(filename)
    x_log_data = [math.log10(i) for i in range(1, 1+len(count_list))]
    y_log_data = [math.log10(i) for i in count_list]
    plt.plot(x_log_data, y_log_data, label=label, color="black")
    plt.legend(loc="upper right")

    x_ticks = ["1", "10", "100", "1000"]
    plt.xticks([0,1,2, 3], x_ticks, fontsize=15)
    y_ticks = ["1", "10", "100", "1000", "10E4", "10E5", "10E6", "10E7"]
    plt.yticks([0,1,2,3,4,5,6,7], y_ticks, fontsize=15)

    plt.xlabel("Rank of Domain Name", fontsize=20)
    plt.ylabel("Number of Corresponding Sessions on 2018-03-12", fontsize=20)
    plt.show()