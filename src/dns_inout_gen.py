import gzip
import os
from datetime import datetime



def write_to_log(log_filename, info):
    f = open(log_filename, "a")
    f.write("== Time: %s ==\n" % datetime.now())
    f.write(str(info)+"\n")
    f.close()


def doInOutCount(filename):
    def is_private(ip):
        if ip.startswith("10.") or ip.startswith("192.168.") or ip.startswith("172.16."):
            return True
        else:
            return False
    interCount = 0
    inCount = 0
    outCount = 0
    exterCount = 0

    with gzip.open(filename, 'rb') as f:
        for line in f:
            if line[0] == "#":
                continue
            line_list = line.split("\t")

            if is_private(line_list[2]) or is_private(line_list[4]):
                # if one of the IP is private,
                interCount += 1
            elif line_list[2].startswith("136.159") and line_list[4].startswith("136.159"):
                interCount += 1
            elif line_list[2].startswith("136.159"):
                # field2 equals $3, If $3 start with 136.159, this indicates an outbound session
                outCount += 1
            elif line_list[4].startswith("136.159"):
                # field4 equals $5, If $5 start with 136.159, this indicates an inbound session
                inCount += 1
            else:
                # else this is defined as an odd session.
                exterCount += 1

    return interCount, inCount, outCount, oddCount



if __name__ == '__main__':
    data_folder = "/data3/"
    date_format = '%Y-%M-%d'
    search_key = "2018-03"
    output_inout_gen = "./result/dns_InOutCount_***.log"

    log_file = "./runtime_info_%s.log" % search_key

    for daily_folder in os.listdir(data_folder):
        if os.path.isdir(data_folder + daily_folder) and search_key in daily_folder:
            date = daily_folder

            write_to_log(log_file, "Now Inside: %s" %daily_folder)
            yyyymm = year_month = date[0:7]
            for trace_filename in os.listdir(data_folder + daily_folder + "/"):
                if "dns" in trace_filename:
                    inCount = 0
                    outCount = 0
                    oddCount = 0
                    interCount = 0
                    write_to_log(log_file, "Start searching in DNS file --> %s" % trace_filename)
                    interCount, inCount, outCount, oddCount = doInOutCount(data_folder + daily_folder + "/" + trace_filename)
                    f_out = open(output_inout_gen.replace("***", yyyymm), 'a')
                    f_out.write("DNS\t" + data_folder + daily_folder + "/" + trace_filename + "\t%d\t%d\t%d\t%d\n"
                                % (interCount, inCount, outCount, oddCount))
                    f_out.close()