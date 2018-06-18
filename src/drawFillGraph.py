from src.continuousFill import ContinuousFill
from src.dataGenToDraw import DataGenToDraw

from matplotlib import colors as mcolors


def drawInOutFill():
    file_path = "../data/result_io/dns_InOutCount_2018-03.log"
    file_list = [file_path]

    data_factory = DataGenToDraw()
    global_label = ["Inbound", "Outbound", "Odd"]
    draw_label = ["Inbound", "Outbound", "Odd"]
    color_list = ["red", "green", "blue"]
    data_factory.set_label_list(global_label, draw_label)
    data_factory.set_data_dict(file_list)
    data_factory.set_color_dict(color_list)

    x_data = data_factory.get_x_label()
    draw_master = ContinuousFill(draw_label, data_factory.data_dict, x_data,
                                 color_dict=data_factory.color_dict)
    draw_master.organize_draw_data()

    x_label = "Time (hour)"
    y_label = "# of Sessions Per Hour"
    graph_handle = draw_master.gen_continuous_fill(x_label, y_label)


    date_range = range(1,20)
    x_ticks = ["2018-03-%02d"%date for date in date_range]
    x_mask = []
    for seq in x_data:
        if seq % 24 == 0:
            x_mask.append(seq)
    print(x_ticks)

    graph_handle.xticks(x_mask, x_ticks, rotation=45)
    graph_handle.show()


def drawOverallFill():
    file_path = "../data/result_overall/dns_overall_hourlyCount_dns_2018-03.log"
    file_list = [file_path]

    data_factory = DataGenToDraw()
    global_label = ["All", "A", "AAAA", "STAR", "DASH", "NS", "DNSKEY", "PTR", "TXT", "MX", "SOA",
                   "SRV", "DS", "CNAME", "NAPTR", "NBSTAT", "SPF", "OTHER"]
    draw_label = ["A", "AAAA", "STAR", "DASH", "NS", "DNSKEY", "PTR", "TXT", "MX", "SOA",
                   "SRV", "DS", "CNAME", "NAPTR", "NBSTAT", "SPF", "OTHER"]
    color_list = []
    data_factory.set_label_list(global_label, draw_label)
    data_factory.set_data_dict(file_list)
    data_factory.set_color_dict(color_list)

    x_data = data_factory.get_x_label()
    draw_master = ContinuousFill(draw_label, data_factory.data_dict, x_data,
                                 color_dict=data_factory.color_dict)
    draw_master.organize_draw_data()

    x_label = "Time (hour)"
    y_label = "# of Sessions Per Hour"
    graph_handle = draw_master.gen_continuous_fill(x_label, y_label)


    date_range = range(1,20)
    x_ticks = ["2018-03-%02d"%date for date in date_range]
    x_mask = []
    for seq in x_data:
        if seq % 24 == 0:
            x_mask.append(seq)
    print(x_ticks)

    graph_handle.xticks(x_mask, x_ticks, rotation=45)
    graph_handle.show()


if __name__ == '__main__':
    # drawInOutFill()
    drawOverallFill()