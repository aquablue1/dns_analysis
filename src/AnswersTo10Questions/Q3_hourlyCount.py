import matplotlib.pyplot as plt
import os


def get_hourlyData(filename):
    in_traffic_total = 0
    out_traffic_total = 0
    with open(filename, 'r') as f:
        for line in f:
            line_list = line.strip().split("\t")
            direction = line_list[1]

            if line_list[2] != "-":
                in_traffic = int(line_list[2])
            else:
                in_traffic = 0

            if line_list[3] != "-":
                out_traffic = int(line_list[3])
            else:
                out_traffic = 0

            in_traffic_total += in_traffic
            out_traffic_total += out_traffic
    return in_traffic_total, out_traffic_total


if __name__ == '__main__':
    data_folder = "../../data/result_q3Data/2018-03-12/"
    output_folder = "../../result/result_q3_hourlyCount/"
    output_filename = "2018-03-12.log"
    cached = None
    outputF = open(output_folder + "/" + output_filename, 'a')
    try:
        outputF.write("# output hourly volume of dns traffic in 2018-03-12. hour\tin\tout.\n")
        for hourly_file in os.listdir(data_folder):
            if "conn." in hourly_file:
                in_traffic, out_traffic = get_hourlyData(data_folder+"/"+hourly_file)

                if hourly_file[5:7] == hourly_file[14:16]:
                    cached = [in_traffic, out_traffic]
                else:
                    if cached is not None:
                        in_traffic += cached[0]
                        out_traffic += cached[1]
                        cached = None
                    print(hourly_file[14:16]+"=="+hourly_file[5:7])
                    print(in_traffic, out_traffic)
                    outputF.write("%s\t%s\t%s\n" %(hourly_file[5:7], in_traffic, out_traffic))
                    print("====")
    finally:
        outputF.close()
