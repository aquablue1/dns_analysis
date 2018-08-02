import os
import gzip
from datetime import datetime


def writeToFile(outputFile, string):
    with open(outputFile, 'a') as f:
        f.write(str(string))


def do_IPCount(filename):
    def is_private(ip):
        if ip.startswith("10.") or ip.startswith("192.168.") or ip.startswith("172.16."):
            return True
        else:
            return False

    in_src = set()
    in_dst = set()
    out_src = set()
    out_dst = set()

    with gzip.open(filename, 'rb') as f:
        for line in f:
            if line[0] == '#':
                continue
            line_list = line.split("\t")
            # all the traffic should be DNS Related.
            if is_private(line_list[2]) or is_private(line_list[4]):
                # if one of the IP is private,
                continue
            elif line_list[2].startswith("136.159") and line_list[4].startswith("136.159"):
                continue
            elif line_list[2].startswith("136.159"):
                # field2 equals $3, If $3 start with 136.159, this indicates an outbound session
                out_src.add(line_list[2])
                out_dst.add(line_list[4])
            elif line_list[4].startswith("136.159"):
                # field4 equals $5, If $5 start with 136.159, this indicates an inbound session
                in_src.add(line_list[2])
                in_dst.add(line_list[4])
            else:
                # else this is defined as an odd session.
                continue

    return len(in_src), len(in_dst), len(out_src), len(out_dst)


if __name__ == '__main__':
    data_folder = "/data3/"
    output_folder = "../result/"
    search_key = "2018-03-12"

    for daily_folder in os.listdir(data_folder):
        if os.path.isdir(data_folder + daily_folder) and daily_folder.startswith(search_key):
            print("Current in %s." % daily_folder)
            date = daily_folder
            outputFile = output_folder + "%s.log" % date
            for trace_filename in os.listdir(data_folder + daily_folder + "/"):
                if "dns.00" in trace_filename:
                    print(" ===>now analysing %s, Time: %s" % (trace_filename, datetime.now()))
                    full_path = data_folder + daily_folder + "/" + trace_filename
                    in_src_count, in_dst_count, out_src_count, out_dst_count = do_IPCount(full_path)
                    hourly_statistics = "%s\t%d\t%d\t%d\t%d\n" % (full_path, in_src_count, in_dst_count,
                                                                  out_src_count, out_dst_count)
                    writeToFile(outputFile, hourly_statistics)

