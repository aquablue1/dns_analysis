import matplotlib.pyplot as plt

def get_dataToDraw(filename):
    date_list = []
    in_traffic_list = []
    out_traffic_list = []
    with open(filename, 'r') as f:
        for line in f:
            if line[0] == "#":
                continue
            line_list = line.strip().split("\t")
            in_traffic_list.append(int(line_list[1]))
            out_traffic_list.append(int(line_list[2]))
            date_list.append(line_list[0])

    return date_list, in_traffic_list, out_traffic_list

def do_drawBar(date_list, in_traffic_list, out_traffic_list):
    x_location = range(len(in_traffic_list))

    ax = plt.subplot(1, 1, 1)

    ax.bar(x_location, out_traffic_list,[0.5] * len(out_traffic_list), label="outbound", color="red")
    ax.bar(x_location, in_traffic_list, [0.5] * len(out_traffic_list), out_traffic_list, label="inbound", color="blue")

    plt.xticks(x_location, date_list, rotation=0, fontsize=15)
    y_ticks = ["%d GB" % i for i in range(0, 50, 10)]
    plt.yticks(range(0, 50000000000, 10000000000), y_ticks, fontsize=15)
    plt.ylabel("volume of traffic per day", fontsize=20)

    handles, labels = ax.get_legend_handles_labels()

    plt.title("Daily Volume of DNS Traffic in a week of 2018-03.", fontsize=30)
    plt.legend(handles[::-1], labels[::-1], loc="upper left")
    plt.show()

if __name__ == '__main__':
    filename = "../../result/Conn_WeeklySummary_2018-03.log"
    date_list, in_traffic_list, out_traffic_list = get_dataToDraw(filename)

    do_drawBar(date_list, in_traffic_list, out_traffic_list)
