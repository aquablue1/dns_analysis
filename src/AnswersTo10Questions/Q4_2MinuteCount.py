import matplotlib.pyplot as plt
import os

time_start = 1520834400
time_length = 24*60
count_list_in = [0] * time_length
count_list_out = [0] * time_length

data_in_folder = "../../data/result_inbound/"
data_out_folder = "../../data/result_outbound/"
output_folder = "../../result/result_q4_minSecCount/"
output_filename = "min_2018-03-12_2.log"
output_error = "min_2018-03-12_2_error.log"


def get_minuteData_byHour(filename, cookie="inbound"):
    error_filename = output_folder +"/"+ output_error
    errorF = open(error_filename, 'a')

    with open(filename, 'r') as f:
        for line in f:
            line_list = line.strip().split("\t")

            time_index = int((float(line_list[0]) - time_start)/60)

            if 0 <= time_index < time_length:
                if cookie=="inbound":
                    count_list_in[time_index] += 1
                elif cookie=="outbound":
                    count_list_out[time_index] += 1
            else:
                print("Error Detected!")
                errorF.write(line)



if __name__ == '__main__':
    cached = None
    for hourly_file in os.listdir(data_in_folder):
        if "2018-03-12" in hourly_file:
            get_minuteData_byHour(data_in_folder+"/"+hourly_file, cookie="inbound")

    for hourly_file in os.listdir(data_out_folder):
        if "2018-03-12" in hourly_file:
            get_minuteData_byHour(data_out_folder+"/"+hourly_file, cookie="outbound")

    outputF = open(output_folder + "/" + output_filename, 'a')
    outputF.write("# output minutely volume of dns traffic in 2018-03-12. hour\tin\tout.\n")

    for i in range(time_length):
        outputF.write("%d\t%d\t%d\n" % (i, count_list_in[i], count_list_out[i]))
    outputF.close()
