from src.util.draw_Perodical import Plot_Perodical


def data_collect(file_path):
    ts_list = []
    with open(file_path, 'r') as f:
        for line in f:
            line_list = line.split("\t")
            ts = line_list[0]
            # if line_list[4] == "136.159.142.7":
            if line_list[2] == "88.99.62.159":
                ts_list.append(float(ts))
    return ts_list


if __name__ == '__main__':
    path = "../../data/auroral/ns_auroral.log"
    x_label = "Time (in second)."
    y_label = "Meaningless at Present."
    title = "Queries to Auroral NSes (100 counts)"
    ts_list = data_collect(path)
    ts_list.sort()
    start = min(ts_list)
    sort_ts_list = [ts-start for ts in ts_list]

    plot = Plot_Perodical(sort_ts_list)
    plot.set_title(title)
    plot.set_labels([x_label, y_label])
    plot.do_draw(0,100)