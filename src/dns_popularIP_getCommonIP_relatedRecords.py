"""
Generatere related records from original records, print full records.
"""
import gzip
import os
from datetime import datetime

input_timestamp = "2018-03-08_12"

def get_IPList(timestamp, cookie):
    filename = "../data/commonIP/%s/%s_CommonTopIP.log" % (timestamp, cookie)
    ret_ip_list = []
    with open(filename) as f:
        for line in f:
            line.strip()
            ret_ip_list.append(line)
    return ret_ip_list

in_src_topIP_list = get_IPList(input_timestamp, "in_src")
in_dst_topIP_list = get_IPList(input_timestamp, "in_dst")
out_src_topIP_list = get_IPList(input_timestamp, "out_src")
out_dst_topIP_list = get_IPList(input_timestamp, "out_dst")


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

def output_IP_list(record_list, output_filename):
    with open(output_filename, 'a') as f:
        for record in record_list:
            f.write(record + "\n")


def doRelatedRecordCollect(filename):
    def is_private(ip):
        if ip.startswith("10.") or ip.startswith("192.168.") or ip.startswith("172.16."):
            return True
        else:
            return False

    inbound_record_list = []
    outbound_record_list = []

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
                if(is_top_out(line_list[2], line_list[4])):
                    # do save this record to outbound CommonTopRelated records
                    outbound_record_list.append(line)

            elif line_list[4].startswith("136.159."):
                # field4 equals $5, If $5 start with 136.159, this indicates an inbound session
                if(is_top_in(line_list[2], line_list[4])):
                    # do save this record to inbound CommonTopRelated records
                    inbound_record_list.append(line)
            else:
                # else this is defined as an odd session.
                continue
    # print(in_dst_list)
    return inbound_record_list, outbound_record_list

def is_top_out(srcIP, dstIP):
    if srcIP in out_src_topIP_list and dstIP in out_dst_topIP_list:
        return True
    else:
        return False

def is_top_in(srcIP, dstIP):
    if srcIP in in_src_topIP_list and dstIP in in_dst_topIP_list:
        return True
    else:
        return False


if __name__ == '__main__':
    data_folder = "/data3/"
    date_format = '%Y-%M-%d'
    search_key = "2018-03-08"

    log_file = "../runtime_info_popularIP_CommonIPRecord_%s.log" % search_key

    inbound_record_list = []
    outbound_record_list = []

    for daily_folder in os.listdir(data_folder):
        if os.path.isdir(data_folder + daily_folder) and search_key in daily_folder:
            date = daily_folder

            write_to_log(log_file, "Now Inside: %s" %daily_folder)
            yyyymm = year_month = date[0:7]
            for trace_filename in os.listdir(data_folder + daily_folder + "/"):
                if "dns.12" in trace_filename:
                    write_to_log(log_file, "Start searching in DNS file --> %s" % trace_filename)
                    inbound_record_list_tmp, outbound_record_list_tmp = \
                        doRelatedRecordCollect(data_folder + daily_folder + "/" + trace_filename)
                    inbound_record_list = inbound_record_list + inbound_record_list_tmp
                    outbound_record_list = outbound_record_list + outbound_record_list_tmp

    # tidy_IP_list(in_src_list)
    # tidy_IP_list(in_dst_list)

    inbound_record_filename = "../result_popIP_RelatedRecord/inbound_commonIP_relatedRecord.log"
    output_IP_list(inbound_record_list, inbound_record_filename)

    outbound_record_filename = "../result_popIP_RelatedRecord/outbound_commonIP_relatedRecord.log"
    output_IP_list(outbound_record_list, outbound_record_filename)