import os
import gzip
from datetime import datetime

def is_private(ip):
    if ip.startswith("10.") or ip.startswith("192.168.") or ip.startswith("172.16."):
        return True
    else:
        return False

def doSearch(filename, outputFile, targetIP):
    outputF = open(outputFile, 'a')
    with gzip.open(filename, 'r') as f:
        for line in f:
            if line[0] == "#":
                continue
            line_list = line.split("\t")
            if not is_private(line_list[4]) and line_list[2] == targetIP:
                # Make sure this is an outbound traffic
                    outputF.write(line)
    outputF.close()


if __name__ == '__main__':
    data_folder = "/data3/"
    output_folder = "../result/"
    search_key = "2018-04-01"


    for daily_folder in os.listdir(data_folder):
        if os.path.isdir(data_folder + daily_folder) and daily_folder.startswith(search_key):
            print("Current in %s." % daily_folder)
            date = daily_folder
            try:
                os.stat(output_folder + date)
            except:
                os.mkdir(output_folder + date)
            for trace_filename in os.listdir(data_folder + daily_folder + "/"):
                if "dns.00" in trace_filename:
                    print(" ===>now analysing %s, Time: %s" % (trace_filename, datetime.now()))
                    full_path = data_folder + daily_folder + "/" + trace_filename
                    outputFile = output_folder + date + "/%s.log" % trace_filename[:-7]
                    targetIP = "136.159.1.21"
                    doSearch(full_path, outputFile, targetIP)