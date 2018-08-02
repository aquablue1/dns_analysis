import os

from datetime import datetime


def writeToFile(outputFile, string):
    with open(outputFile, 'a') as f:
        f.write(str(string))


def do_domainNameCount(filename):

    name_count = set()

    with open(filename, 'r') as f:
        for line in f:
            if line[0] == '#':
                continue
            line_list = line.strip().split("\t")

            name_count.add(line_list[9])

    return len(name_count)


if __name__ == '__main__':
    cookie = "outbound"
    data_folder = "../../data/result_%s/" % cookie
    output_folder = "../../result/result_q9_domainNameCount/"
    search_key = "2018-03-12"
    date = "2018-03-12"
    outputFile = "%s_%s.log" % (date, cookie)

    for filename in os.listdir(data_folder):
        if search_key in filename:
            name_count = do_domainNameCount(data_folder+"/"+filename)
            hourly_statistics = "%s\t%d\n" % (filename, name_count)
            writeToFile(output_folder+"/"+outputFile, hourly_statistics)


