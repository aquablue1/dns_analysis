import os


def get_hourlyCount(filename):
    noerror_count = 0
    null_count = 0
    nxdomain_count = 0
    serverfail_count = 0
    refuse_count = 0
    formerr_count = 0
    notauth_count = 0

    with open(filename, 'r') as f:
        for line in f:
            if line[0] == "#":
                continue
            line_list = line.strip().split("\t")
            # Error information stores at field $16, [15]
            if line_list[15] == "NOERROR":
                noerror_count += 1
            elif line_list[15] == "NXDOMAIN":
                nxdomain_count += 1
            elif line_list[15] ==  "SERVFAIL":
                serverfail_count += 1
            elif line_list[15] == "REFUSED":
                refuse_count += 1
            elif line_list[15] == "FORMERR":
                formerr_count += 1
            elif line_list[15] == "NOTAUTH":
                notauth_count += 1
            else:
                null_count += 1
        return noerror_count, nxdomain_count, serverfail_count, refuse_count, \
               formerr_count, notauth_count, null_count


def get_dailyStatistics(daily_folder, date, cookie):
    output_filename = "../../result/result_q12_error/%s_%s.log" % (date, cookie)
    outputF = open(output_filename, 'a')
    for filename in os.listdir(daily_folder):
        if date in filename:
            noerror_count, nxdomain_count, serverfail_count, refuse_count, \
            formerr_count, notauth_count, null_count = \
                get_hourlyCount(daily_folder + "/" + filename)
            output_string = "%s\t%d\t%d\t%d\t%d\t%d\t%d\t%d\n" % (filename[11:13], noerror_count, nxdomain_count,
                                                                  serverfail_count, refuse_count, formerr_count,
                                                                  notauth_count, null_count)
            outputF.write(output_string)
    outputF.close()


if __name__ == '__main__':
    cookie = "outbound"
    daily_folder = "../../data/result_%s" % cookie
    date = "2018-03-12"
    get_dailyStatistics(daily_folder, date, cookie)