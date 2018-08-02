import os
import gzip
from datetime import datetime

def extract_data(filename, outputFile):
    output_f = open(outputFile)
    direction = None
    traffic_in = None
    traffic_out = None
    valid = False
    with gzip.open(filename, 'r') as f:
        for line in f:
            if line[0] == "#":
                continue
            line_list = line.split("\t")
            if line_list[7] != "dns":
                continue

            ts = line_list[0]
            if line_list[12] == "T" and line_list[13] == "F":
                # Should be outbound traffic
                valid = True
                direction = "out"
                traffic_in = line_list[10]
                traffic_out = line_list[9]


            elif line_list[12] == "F" and line_list[13] == "T":
                # Should be inbound traffic
                valid = True
                direction = "in"
                traffic_in = line_list[9]
                traffic_out = line_list[10]
            if valid:
                output_f.write("%s\t%s\t%s\t%s\n" %(ts, direction, traffic_in, traffic_out))
                valid = False
    output_f.close()


if __name__ == '__main__':
    data_folder = "/data3/"
    output_folder = "../result/result_q3Data/"
    search_key = "2018-03-12"


    for daily_folder in os.listdir(data_folder):
        if os.path.isdir(data_folder + daily_folder) and daily_folder.startswith(search_key):
            print("Current in %s." % daily_folder)
            date = daily_folder
            try:
                os.stat(output_folder + date)
            except:
                os.mkdir(output_folder + date)


            for trace_filename in os.listdir(data_folder + daily_folder + "/"):
                if "conn.00" in trace_filename:
                    print(" ===>now analysing %s, Time: %s" % (trace_filename, datetime.now()))
                    full_path = data_folder + daily_folder + "/" + trace_filename
                    outputFile = output_folder + date + "/%s.log" % trace_filename[:-7]
                    extract_data(full_path, outputFile)
