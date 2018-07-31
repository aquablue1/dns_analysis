from src.util.draw_Perodical import Plot_Perodical

def data_generate(path):
    ts_list = []
    with open(path, 'r') as f:
        for line in f:
            line_list = line.split("\t")
            if line_list[9] == "www.google.com" and line_list[4]=="8.8.4.4":
                ts_list.append(float(line_list[0]))

    return ts_list

if __name__ == '__main__':
    path = "../../result/result_outbound_global_classify/136.159.160.157.log"
    x_label = "Time (in second)."
    y_label = "Meaningless at Present."
    title = "136.159.160.157's Queries to Google."
    ts_list = data_generate(path)
    ts_list.sort()

    start = min(ts_list)
    sort_ts_list = [ts-start for ts in ts_list]
    plot = Plot_Perodical(sort_ts_list[100:200])
    plot.set_labels([x_label,y_label])
    plot.set_title(title)
    plot.do_draw(0, 100)