"""
Generate all the outbound traffic from original data folders.
To Use: set search_key and search_hour to change the target search folder.
"""
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

    outbound_list = []

    with gzip.open(filename, 'rb') as f:
        for line in f:
            if line[0] == "#":
                continue
            line_list = line.split("\t")
            if is_private(line_list[2]) or is_private(line_list[4]):
                continue
            elif line_list[2].startswith("136.159.") and line_list[4].startswith("136.159."):
                continue
            elif line_list[2].startswith("136.159."):
                # field2 equals $3, If $3 start with 136.159, this indicates an outbound session
                outbound_list.append(line)

            elif line_list[4].startswith("136.159."):
                continue
            else:
                # else this is defined as an odd session.
                continue
    # print(in_dst_list)
    return outbound_list


def output_IP_list(session_list, output_filename):
    with open(output_filename, 'a') as f:
        for ip in session_list:
            f.write(ip)



if __name__ == '__main__':
    data_folder = "/data3/"
    date_format = '%Y-%M-%d'
    search_key = "2018-03-08"
    search_hour = "12"

    log_file = "../runtime_info_outbound_%s.log" % search_key

    outbound_list = []

    for daily_folder in os.listdir(data_folder):
        if os.path.isdir(data_folder + daily_folder) and search_key in daily_folder:
            date = daily_folder

            write_to_log(log_file, "Now Inside: %s" %daily_folder)
            yyyymm = year_month = date[0:7]
            for trace_filename in os.listdir(data_folder + daily_folder + "/"):
                if "dns.%s" % search_hour in trace_filename:
                    outbound_list_tmp = []
                    write_to_log(log_file, "Start searching in DNS file --> %s" % trace_filename)
                    outbound_list_tmp = doIPCollect(data_folder + daily_folder + "/" + trace_filename)
                    outbound_list = outbound_list + outbound_list_tmp

    output_filename = "../result/result_outbound/%s_%s.log" % (search_key, search_hour)
    output_IP_list(outbound_list, output_filename)