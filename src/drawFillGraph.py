"""
Using dataGenToDraw and continuousFill to generate continuous graphs.
"""
from src.continuousFill import ContinuousFill
from src.dataGenToDraw import DataGenToDraw

from matplotlib import colors as mcolors


def drawInOutFill():
    file_path = "../data/result_inout/dns_InOutCount_2018-03_F.log"
    file_list = [file_path]

    data_factory = DataGenToDraw()
    global_label = ["Internal", "Inbound", "Outbound", "External"]
    # draw_label = ["Exchange", "Internal", "External"]
    draw_label = ["Outbound", "Inbound"]
    color_list = ["red", "green", "blue", "yellow"]
    data_factory.set_label_list(global_label, draw_label)

    data_factory.set_data_dict(file_list)

    # exchange_list = [sum(x) for x in zip(data_factory.data_dict["Inbound"], data_factory.data_dict["Outbound"])]
    # data_factory.set_specified_data("Exchange", exchange_list)

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
    graph_handle.ylim([0, 17500000])
    graph_handle.xticks(x_mask, x_ticks, rotation=45)
    graph_handle.show()


def drawOverallFill():
    file_path = "../data/result_overall/dns_overall_hourlyCount_dns_2018-03.log"
    file_list = [file_path]

    data_factory = DataGenToDraw()
    # length = 18
    global_label = ["All", "A", "AAAA", "STAR", "DASH", "NS", "DNSKEY", "PTR", "TXT", "MX", "SOA",
                   "SRV", "DS", "CNAME", "NAPTR", "NBSTAT", "SPF", "OTHER"]

    # length = 17
    # draw_label = ["A", "AAAA", "STAR", "DASH", "NS", "DNSKEY", "PTR", "TXT", "MX", "SOA",
                   # "SRV", "DS", "CNAME", "NAPTR", "NBSTAT", "SPF", "OTHER"]

    draw_label = ["STAR", "NS", "DNSKEY", "PTR", "TXT", "MX", "SOA",
                    "SRV", "DS", "CNAME", "NAPTR", "NBSTAT", "SPF", "OTHER"]

    # length = 17
    color_list = ["black", "b", "g", "r", "m", "y",
                  "r", "pink", "goldenrod", "aqua", "teal",
                  "olive", "chartreuse", "plum", "darkslategray", "indigo",
                  "crimson", "teal"]
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
    # graph_handle.ylim([0, 17500000])
    graph_handle.xticks(x_mask, x_ticks, rotation=45)
    graph_handle.show()


def drawEndStatusFill():
    status = "Odd"
    file_path = "../data/result_endstatus/dns_EndStatus%s_2018-03.log" % status
    file_list = [file_path]

    data_factory = DataGenToDraw()
    # length = 12
    global_label = ["NOERROR", "FORMERR", "SERVFAIL", "NXDOMAIN", "NOTIMP", "REFUSED",
                    "YXDOMAIN", "YXRRSET", "XRRSET", "NOTAUTH", "NOTZONE",
                    "OTHERS", "DASH"]

    # length =
    draw_label = ["NOERROR", "FORMERR", "SERVFAIL", "NXDOMAIN", "REFUSED",
                    "OTHERS", "DASH"]


    # draw_label = ["STAR", "NS", "DNSKEY", "PTR", "TXT", "MX", "SOA",
                   # "SRV", "DS", "CNAME", "NAPTR", "NBSTAT", "SPF", "OTHER"]

    # length = 16
    color_list = ["b", "g", "teal", "m", "y",
                  "r", "pink", "goldenrod", "aqua", "teal",
                  "olive", "chartreuse", "plum", "darkslategray", "indigo",
                  "crimson"]
    data_factory.set_label_list(global_label, draw_label)
    data_factory.set_data_dict(file_list)
    data_factory.set_color_dict(color_list)

    x_data = data_factory.get_x_label()
    draw_master = ContinuousFill(draw_label, data_factory.data_dict, x_data,
                                 color_dict=data_factory.color_dict)
    draw_master.organize_draw_data()

    x_label = "Time (hour)"
    y_label = "# of %s Sessions Per Hour" % status
    graph_handle = draw_master.gen_continuous_fill(x_label, y_label)


    date_range = range(1,20)
    x_ticks = ["2018-03-%02d"%date for date in date_range]
    x_mask = []
    for seq in x_data:
        if seq % 24 == 0:
            x_mask.append(seq)
    print(x_ticks)
    # graph_handle.ylim([0, 17500000])
    graph_handle.xticks(x_mask, x_ticks, rotation=45)
    graph_handle.show()


def drawEndFlagFill():
    file_path = "../data/result_overall/dns_overall_hourlyCount_conn_2018-03.log"
    file_list = [file_path]

    data_factory = DataGenToDraw()
    # length = 18
    global_label = ["All", "SF", "S0", "SHR", "S2", "S3", "S1", "SH", "RSTR", "OTH", "RSTO", "OTHER"]

    # length = 17

    draw_label = ["SF", "S0", "SHR", "S2", "S3", "S1", "SH", "RSTR", "OTH", "RSTO", "OTHER"]

    # length = 17
    color_list = ["black", "b", "g", "r", "m", "y",
                  "r", "pink", "goldenrod", "aqua", "teal",
                  "olive", "chartreuse", "plum", "darkslategray", "indigo",
                  "crimson", "teal"]
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
    graph_handle.ylim([0, 17500000])
    graph_handle.xticks(x_mask, x_ticks, rotation=45)
    graph_handle.show()


if __name__ == '__main__':
    drawInOutFill()
    # drawOverallFill()
    # drawEndStatusFill()
    # drawEndFlagFill()