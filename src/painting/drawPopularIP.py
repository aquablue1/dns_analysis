import math

import matplotlib.pyplot as plt

from src.popularIP.dns_popularIP_tidy import tidyPopIP


def get_labels(cookie):
    if cookie == "out_dst":
        x_label = "Sequence of distinct destination IPs"
        y_label = "Number of outbound sessions"
        title = "Destination IP popularity of Outbound Traffic"
        color = "red"
    elif cookie == "out_src":
        x_label = "Sequence of Distinct source IPs"
        y_label = "Number of outbound sessions"
        title = "Source IP popularity of Outbound Traffic"
        color = "blue"
    elif cookie == "in_dst":
        x_label = "Sequence of Distinct destination IPs"
        y_label = "Number of inbound sessions"
        title = "Destination IP popularity of Inbound Traffic"
        color = "green"
    elif cookie == "in_src":
        x_label = "Sequence of Distinct source IPs"
        y_label = "Number of inbound sessions"
        title = "Destination IP popularity of Inbound Traffic"
        color = "grey"
    else:
        return None
    return x_label, y_label, title, color

def draw_popIP(cookie):
    filename = "../data/result_popIP/%s_tidy.log" % cookie
    ips = tidyPopIP(filename)

    x_data = [math.log(x, 10) for x in ips.popIP_dict.keys()]
    y_data = [math.log(elem[0], 10) for elem in ips.popIP_dict.values()]
    ax = plt.subplot(1,1,1)

    x_label, y_label, title, color = get_labels(cookie)
    ax.scatter(x_data, y_data, color=color, label=cookie)

    plt.legend(loc="best")

    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)

    xticks_real = [0,1,2,3,4,5]
    xticks_mask = ["1", "10", "100", "10E3", "10E4", "10E5"]
    plt.xticks(xticks_real, xticks_mask)

    yticks_real = [0,1,2,3,4,5,6]
    yticks_mask = ["1", "10", "100", "10E3", "10E4", "10E5", "10E6"]
    plt.yticks(yticks_real, yticks_mask)

    ax.set_xlim([-0.2, 5])
    ax.set_ylim([-0.2, 6.5])
    plt.title(title)
    plt.show()


if __name__ == '__main__':
    cookie = "out_dst"
    draw_popIP(cookie)