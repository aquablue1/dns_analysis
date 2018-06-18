import gzip
import os
from datetime import datetime
from collections import OrderedDict

ONLY_DNS = False
ONLY_CONN = False
SEP_LOC = -1


def write_to_log(filename, info):
    f = open(filename, "a")
    f.write(str(info)+"\n")
    f.close()


def do_dns_count(filename, sep_loc):
    overall_count = 0
    # a_count =0
    # aaaa_count = 0
    # cname_count = 0
    # mx_count = 0
    # prt_count = 0
    # ns_count = 0
    # soa_count = 0
    # srv_count = 0
    # txt_count = 0
    # naptr_count = 0
    # star_count = 0
    # blind_count = 0
    # other_count = 0

    # A list of status codes of DNS traffic.
    status_list = ["A", "AAAA", "STAR", "DASH", "NS", "DNSKEY", "PTR", "TXT", "MX", "SOA",
                   "SRV", "DS", "CNAME", "NAPTR", "NBSTAT", "SPF", "OTHER"]
    status_dict = OrderedDict()
    for key in status_list:
        status_dict[key] = 0
    with gzip.open(filename, 'rb') as f:
        for line in f:
            if line[0] == "#":
                continue
            else:
                overall_count += 1
                status = str(line.split("\t")[sep_loc])
                if status == "*":
                    status = "STAR"
                elif status == "-":
                    status = "DASH"
                try:
                    status_dict[status] += 1
                except KeyError:
                    status_dict["OTHER"] += 1
    return overall_count, status_dict


def do_conn_count(filename):
    overall_count = 0
    # A list of status codes of session ending methods.
    status_list = ["SF", "S0", "SHR", "S2", "S3", "S1", "SH", "RSTR", "OTH", "RSTO", "OTHER"]
    status_dict = OrderedDict()
    for key in status_list:
        status_dict[key] = 0
    with gzip.open(filename, 'rb') as f:
        for line in f:
            if line[0] == "#":
                continue
            elif line.split("\t")[7]=="dns":
                overall_count += 1
                status = line.split("\t")[11]
                try:
                    status_dict[status] += 1
                except KeyError:
                    status_dict["OTHER"] += 1
    return overall_count, status_dict

def dict_to_str(dct):
    ret = ""
    for key in dct.keys():
        ret += (str(dct[key]) + "\t")
    return ret


if __name__ == '__main__':
    data_folder = "/data3/"
    date_format = '%Y-%M-%d'
    thresh_date = "2017-03-24"
    search_key = "2018-02-01"
    output_dns_file = "./result/dns_overall_hourlyCount_dns_***.log"
    output_conn_file = "./result/dns_overall_hourlyCount_conn_***.log"
    log_file = "./runtime_info_%s.log" % search_key

    for daily_folder in os.listdir(data_folder):
        if os.path.isdir(data_folder + daily_folder) and search_key in daily_folder:
            date = daily_folder
            if datetime.strptime(date, date_format) > datetime.strptime(thresh_date, date_format):
                SEP_LOC = 13
            else:
                SEP_LOC = 12
            write_to_log(log_file, "Now Inside: "+daily_folder)
            yyyymm = year_month = date[0:7]
            for trace_filename in os.listdir(data_folder + daily_folder + "/"):
                dns_count_dict = -1
                conn_count_dict = -1

                if "dns" in trace_filename and not ONLY_CONN:
                    write_to_log(log_file, "Start searching in DNS --> "+ trace_filename)
                    dns_count, dns_dict = do_dns_count(data_folder + daily_folder + "/" + trace_filename, SEP_LOC)
                    f_out = open(output_dns_file.replace("***", yyyymm), 'a')
                    f_out.write("DNS\t" + data_folder + daily_folder + "/" + trace_filename + "\t%d\t%s\n"
                                % (dns_count, dict_to_str(dns_dict)))
                    f_out.close()
                elif "conn" in trace_filename and not ONLY_DNS:
                    write_to_log(log_file, "Start searching in CONN --> " + trace_filename)
                    conn_count, conn_dict = do_conn_count(data_folder + daily_folder + "/" + trace_filename)
                    f_out = open(output_conn_file.replace("***", yyyymm), 'a')
                    f_out.write("CONN\t" + data_folder + daily_folder + "/" + trace_filename + "\t%d\t%s\n"
                                % (conn_count, dict_to_str(conn_dict)))
                    f_out.close()
