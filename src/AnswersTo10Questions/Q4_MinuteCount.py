import matplotlib.pyplot as plt
import os

time_start = 1520834400
time_length = 24*60
count_list_in = [0] * time_length
count_list_out = [0] * time_length

data_folder = "../../data/result_q3Data/2018-03-12/"
output_folder = "../../result/result_q4_minSecCount/"
output_filename = "min_2018-03-12.log"
output_error = "min_2018-03-12_error.log"

def get_minuteData_byHour(filename):
    error_filename = output_folder +"/"+ output_error
    errorF = open(error_filename, 'a')

    with open(filename, 'r') as f:
        for line in f:
            line_list = line.strip().split("\t")
            direction = line_list[1]
            time_index = int((float(line_list[0]) - time_start)/60)

            if line_list[2] != "-":
                in_traffic = int(line_list[2])
            else:
                in_traffic = 0

            if line_list[3] != "-":
                out_traffic = int(line_list[3])
            else:
                out_traffic = 0

            if 0 <= time_index < time_length:
                count_list_in[time_index] += in_traffic
                count_list_out[time_index] += out_traffic
            else:
                print("Error Detected!")
                errorF.write(line)


if __name__ == '__main__':
    cached = None
    for hourly_file in os.listdir(data_folder):
        if "conn." in hourly_file:
            get_minuteData_byHour(data_folder+"/"+hourly_file)

    outputF = open(output_folder + "/" + output_filename, 'a')
    outputF.write("# output minutely volume of dns traffic in 2018-03-12. hour\tin\tout.\n")

    for i in range(time_length):
        outputF.write("%d\t%d\t%d\n" % (i, count_list_in[i], count_list_out[i]))
    outputF.close()
