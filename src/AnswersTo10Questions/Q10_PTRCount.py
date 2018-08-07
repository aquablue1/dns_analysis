import os


def get_hourlyCount(filename):
    ptr_count = 0
    sd_count = 0
    with open(filename, 'r') as f:
        for line in f:
            if line[0] == "#":
                continue
            line_list = line.strip().split("\t")
            if line_list[13] != "PTR":
                continue
            if "dns-sd" in line_list[9]:
                sd_count += 1
            else:
                ptr_count += 1

    return ptr_count, sd_count


def get_dailyStatistics(daily_folder, date, cookie):
    output_filename = "../../result/result_q10_ptr/%s_%s.log" % (date, cookie)
    outputF = open(output_filename, 'a')
    for filename in os.listdir(daily_folder):
        if date in filename:
            ptr_count, sd_count = get_hourlyCount(daily_folder + "/" + filename)
            output_string = "%s\t%d\t%d\n" % (filename[11:13], ptr_count, sd_count)
            outputF.write(output_string)
    outputF.close()


if __name__ == '__main__':
    cookie = "outbound"
    daily_folder = "../../data/result_%s" % cookie
    date = "2018-03-12"
    get_dailyStatistics(daily_folder, date, cookie)