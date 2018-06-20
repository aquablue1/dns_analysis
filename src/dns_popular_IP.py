import gzip
import os
from datetime import datetime


def write_to_log(log_filename, info):
    """
    write runtime log.
    :param log_filename:
    :param info:
    :return:
    """
    f = open(log_filename, "a")
    f.write("== Time: %s ==\n" % datetime.now())
    f.write(str(info)+"\n")
    f.close()


def doIPCollect(filename):
    def is_private(ip):
        if ip.startswith("10.") or ip.startswith("192.168.") or ip.startswith("172.16."):
            return True
        else:
            return False
    in_src_list = []
    in_dst_list = []

    out_src_list = []
    out_dst_list = []

    with gzip.open(filename, 'rb') as f:
        for line in f:
            if line[0] == "#":
                continue
            line_list = line.split("\t")
            if is_private(line_list[2]) or is_private(line_list[4]):
                continue
            elif line_list[4].startswith("136.159.") and line_list[4].startswith("136.159."):
                continue
            elif line_list[2].startswith("136.159."):
                # field2 equals $3, If $3 start with 136.159, this indicates an outbound session
                out_src_list.append(line_list[2])
                out_dst_list.append(line_list[4])

            elif line_list[4].startswith("136.159."):
                # field4 equals $5, If $5 start with 136.159, this indicates an inbound session
                in_src_list.append(line_list[2])
                in_dst_list.append(line_list[4])
            else:
                # else this is defined as an odd session.
                continue

    return inter_dict, in_dict, out_dict, odd_dict


if __name__ == '__main__':
    data_folder = "/data3/"
    date_format = '%Y-%M-%d'
    search_key = "2018-03-01"

    log_file = "../runtime_info_popularIP_%s.log" % search_key

    for daily_folder in os.listdir(data_folder):
        if os.path.isdir(data_folder + daily_folder) and search_key in daily_folder:
            date = daily_folder

            write_to_log(log_file, "Now Inside: %s" %daily_folder)
            yyyymm = year_month = date[0:7]
            for trace_filename in os.listdir(data_folder + daily_folder + "/"):
                if "dns.12" in trace_filename:
                    in_dict = {}
                    out_dict = {}
                    exter_dict = {}
                    inter_dict = {}
                    write_to_log(log_file, "Start searching in DNS file --> %s" % trace_filename)
                    inter_dict, in_dict, out_dict, odd_dict = doIPCollect(data_folder + daily_folder + "/" + trace_filename)
