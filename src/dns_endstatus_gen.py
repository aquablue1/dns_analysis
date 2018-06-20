"""
Generate End Status information of DNS traffic
By Zhengping in June, 2018
"""
import gzip
import os
from datetime import datetime

key_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 99]


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


def get_empty_dict():
    """
    Init an empty dict with all keys as specified above and values equals 0
    :return:
    """
    new_dict = {}
    for key in key_list:
        new_dict[key] = 0
    return new_dict


def process_rcode(code):
    """
    Accept a String return code as input, process it to the rcode we use

    :param code:
    :return: real rcode number.
    """
    if code == "-":
        return 99
    code = int(code)
    if code <= 10:
        return code
    else:
        return 11


def doInOutCount(filename):
    def is_private(ip):
        if ip.startswith("10.") or ip.startswith("192.168.") or ip.startswith("172.16."):
            return True
        else:
            return False
    inter_dict = get_empty_dict()
    in_dict = get_empty_dict()
    out_dict = get_empty_dict()
    exter_dict = get_empty_dict()

    with gzip.open(filename, 'rb') as f:
        for line in f:
            if line[0] == "#":
                continue
            line_list = line.split("\t")
            rcode = process_rcode(line_list[14])
            if is_private(line_list[2]) or is_private(line_list[4]):
                inter_dict[rcode] += 1
            elif line_list[4].startswith("136.159.") and line_list[4].startswith("136.159."):
                inter_dict[rcode] += 1
            elif line_list[2].startswith("136.159."):
                # field2 equals $3, If $3 start with 136.159, this indicates an outbound session
                out_dict[rcode] += 1

            elif line_list[4].startswith("136.159."):
                # field4 equals $5, If $5 start with 136.159, this indicates an inbound session
                in_dict[rcode] += 1
            else:
                # else this is defined as an odd session.
                exter_dict[rcode] += 1

    return inter_dict, in_dict, out_dict, odd_dict


def print_dict_as_str(dict):
    ret_str = ""
    for key in key_list:
        ret_str = ret_str + str(dict[key])
    return ret_str


if __name__ == '__main__':
    data_folder = "/data3/"
    date_format = '%Y-%M-%d'
    search_key = "2018-03-16"
    output_rcode_inter_gen = "../result_endStatus/dns_EndStatusInter_***.log"
    output_rcode_in_gen = "../result_endStatus/dns_EndStatusIn_***.log"
    output_rcode_out_gen = "../result_endStatus/dns_EndStatusOut_***.log"
    output_rcode_exter_gen = "../result_endStatus/dns_EndStatusExter_***.log"

    log_file = "../runtime_info_endStatus_%s_F.log" % search_key

    for daily_folder in os.listdir(data_folder):
        if os.path.isdir(data_folder + daily_folder) and search_key in daily_folder:
            date = daily_folder

            write_to_log(log_file, "Now Inside: %s" %daily_folder)
            yyyymm = year_month = date[0:7]
            for trace_filename in os.listdir(data_folder + daily_folder + "/"):
                if "dns" in trace_filename:
                    in_dict = {}
                    out_dict = {}
                    exter_dict = {}
                    inter_dict = {}
                    write_to_log(log_file, "Start searching in DNS file --> %s" % trace_filename)
                    inter_dict, in_dict, out_dict, odd_dict = doInOutCount(data_folder + daily_folder + "/" + trace_filename)

                    ## Write inbound information to inbound file
                    f_out = open(output_rcode_inter_gen.replace("***", yyyymm), 'a')
                    f_out.write("DNS\t" + data_folder + daily_folder + "/" + trace_filename + "\t%s\n"
                                % (print_dict_as_str(inter_dict)))
                    f_out.close()

                    f_out = open(output_rcode_in_gen.replace("***", yyyymm), 'a')
                    f_out.write("DNS\t" + data_folder + daily_folder + "/" + trace_filename + "\t%s\n"
                                % (print_dict_as_str(in_dict)))
                    f_out.close()

                    ## Write outbound info to outbound file
                    f_out = open(output_rcode_out_gen.replace("***", yyyymm), 'a')
                    f_out.write("DNS\t" + data_folder + daily_folder + "/" + trace_filename + "\t%s\n"
                                % (print_dict_as_str(out_dict)))
                    f_out.close()

                    ## Write odd info to odd file
                    f_out = open(output_rcode_exter_gen.replace("***", yyyymm), 'a')
                    f_out.write("DNS\t" + data_folder + daily_folder + "/" + trace_filename + "\t%s\n"
                                % (print_dict_as_str(exter_dict)))
                    f_out.close()