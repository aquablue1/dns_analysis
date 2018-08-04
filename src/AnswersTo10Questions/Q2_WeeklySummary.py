import os


def get_dailySummary(filename):
    total_traffic_in = 0
    total_traffic_out = 0
    with open(filename, 'r') as f:
        for line in f:
            if line[0] == "#":
                continue
            line_list = line.strip().split("\t")
            outgoing_inTraffic = int(line_list[2])
            outgoing_outTraffic = int(line_list[3])
            incoming_inTraffic = int(line_list[6])
            incoming_outTraffic = int(line_list[7])

            total_traffic_in += incoming_inTraffic
            total_traffic_in += outgoing_inTraffic
            total_traffic_out += incoming_outTraffic
            total_traffic_out += outgoing_outTraffic

    return total_traffic_in, total_traffic_out


if __name__ == '__main__':
    data_folder = "../../data/result_conn_summary/"
    output_filename = "../../result/Conn_WeeklySummary_2018-03.log"

    weeklyTraffic_dict = {}
    for filename in os.listdir(data_folder):
        if "2018-03-" in filename:
            date = filename[0:10]
            traffic_in, traffic_out = get_dailySummary(data_folder+"/"+filename)
            weeklyTraffic_dict[date] = [traffic_in, traffic_out]

    with open(output_filename, 'a') as f:
        f.write("# Traffic Volume Summary of a random week in 2018-03: date\tintraffic\touttraffic.\n")
        for date in weeklyTraffic_dict.keys():
            dailySummary_string = "%s\t%d\t%d\n" % (date,
                                                    weeklyTraffic_dict[date][0],
                                                    weeklyTraffic_dict[date][1])
            f.write(dailySummary_string)


