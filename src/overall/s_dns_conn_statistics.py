import os
import gzip
from datetime import datetime


def doHourlyAnalysis(filename):
    session_in_count = 0
    session_out_count = 0

    session_out_sizein = 0
    session_out_sizeout = 0
    session_out_size_lost = 0
    # session_out_sizein_min = 1000
    # session_out_sizeout_max = 0
    session_in_sizein = 0
    session_in_sizeout = 0
    session_in_size_lost = 0
    # session_in_sizein_min = 1000
    # session_in_sizeout_max = 0


    session_duration = 0
    # session_duration_min = 0
    # session_duration_max = 0
    session_duration_lost = 0

    session_tcpBased = 0
    session_udpBased = 0

    session_SF = 0

    with gzip.open(filename, 'rb') as f:
        for line in f:
            if line[0] == '#':
                continue
            line_list = line.split("\t")
            if line_list[7] != "dns":
                continue
            # all the traffic should be DNS Related.

            if line_list[8] == "-":
                # Does not have a valid duration section
                session_duration_lost += 1
            else:
                session_duration += float(line_list[8])

            if line_list[12] == "T" and line_list[13] == "F":
                # Should be outbound traffic
                session_out_count += 1
                if line_list[9] == '-' or line_list[10] == '-':
                    session_out_size_lost += 1
                else:
                    session_out_sizeout += int(line_list[9])
                    session_out_sizein += int(line_list[10])

            elif line_list[12] == "F" and line_list[13] == "T":
                # Should be inbound traffic
                session_in_count += 1
                if line_list[9] == '-' or line_list[10] == '-':
                    session_in_size_lost += 1
                else:
                    session_in_sizein += int(line_list[9])
                    session_in_sizeout += int(line_list[10])

            if line_list[11] == "SF":
                # Count all the normal-ended sessions
                session_SF += 1

            # Count TCP/UDP based sessions
            if line_list[6] == "udp":
                session_udpBased += 1
            elif line_list[6] == "tcp":
                session_tcpBased += 1
    record = "%s\t%s\t%s\t%s\t%s\t" \
             "%s\t%s\t%s\t%s\t%s\t%s\t" \
             "%s\t%s\t%s\n" % \
             (filename, session_out_count, session_out_sizein, session_out_sizeout, session_out_size_lost,
              session_in_count, session_in_sizein, session_in_sizeout, session_in_size_lost, session_duration, session_duration_lost,
              session_tcpBased, session_udpBased, session_SF)

    return record

def writeToFile(outputFile, string):
    with open(outputFile, 'a') as f:
        f.write(str(string))



if __name__ == '__main__':
    data_folder = "/data3/"
    output_folder = "../result/"
    search_key = "2018-04-01"


    for daily_folder in os.listdir(data_folder):
        if os.path.isdir(data_folder + daily_folder) and daily_folder.startswith(search_key):
            print("Current in %s." % daily_folder)
            date = daily_folder
            outputFile = output_folder + "%s.log" % date
            for trace_filename in os.listdir(data_folder + daily_folder + "/"):
                if "conn.00" in trace_filename:
                    print(" ===>now analysing %s, Time: %s" % (trace_filename, datetime.now()))
                    full_path = data_folder + daily_folder + "/" + trace_filename
                    hourly_statistics = doHourlyAnalysis(full_path)
                    writeToFile(outputFile, hourly_statistics)
