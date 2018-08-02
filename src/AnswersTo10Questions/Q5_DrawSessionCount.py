import os


def file_len(filename):
    i=0
    with open(filename, 'r') as f:
        for i, l in enumerate(f):
            pass
    return i + 1

def get_Statistics_byHour(folder_name):
    session_count_list = []
    for filename in os.listdir(folder_name):
        if "2018-03-12" in filename:
            session_count = file_len(folder_name + "/" + filename)
            session_count_list.append(session_count)
    return session_count_list


if __name__ == '__main__':
    folder_name_in = "../../data/result_inbound"
    folder_name_out = "../../data/result_outbound"

    session_count_in = get_Statistics_byHour(folder_name_in)
    session_count_out = get_Statistics_byHour(folder_name_out)

    output_folder = "../../result/result_q5_sessionCount/"
    output_filename = "2018-03-12.log"
    outputF = open(output_folder + output_filename, 'a')

    for inbound, outbound in zip(session_count_in, session_count_out):
        outputF.write("%d\t%d\n" % (inbound, outbound))

    outputF.close()