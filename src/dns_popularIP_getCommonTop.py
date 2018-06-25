from src.dns_popularIP_tidy import tidyPopIP
from src.dns_popularIP_getTop import popIPTop

def get_common_list(ip_list1, ip_list2):
    """
    return a list of common elements of two different lists.
    :param ip_list1:
    :param ip_list2:
    :return:
    """
    return [element for element in ip_list1 if element in ip_list2]
    # return list(set(ip_list1) - (set(ip_list1) - set(ip_list2)))


def get_common_IPList(cookie, ts1,ts2, percent):
        filename1 = "../data/result_popIP/%s/%s_tidy.log" % (ts1, cookie)
        ipTop1 = popIPTop(ts1, cookie, percent, tidyPopIP(filename1))
        ip_list1 = ipTop1.get_pop_list()

        filename2 = "../data/result_popIP/%s/%s_tidy.log" % (ts2, cookie)
        ipTop2 = popIPTop(ts2, cookie, percent, tidyPopIP(filename2))
        ip_list2 = ipTop2.get_pop_list()

        common_list = get_common_list(ip_list1, ip_list2)
        return common_list


def output_IPList(ip_list, output_filename):
    with open(output_filename, 'a') as f:
        for ip in ip_list:
            f.write(ip + "\n")

if __name__ == '__main__':
    timestamp_list = ["2018-03-01_12", "2018-03-08_10", "2018-03-08_12",
                      "2018-03-08_16", "2018-03-07_12", "2018-03-16_12"]

    cookie_list = ["in_src", "in_dst", "out_src", "out_dst"]
    cookie_index = 2

    percent = 90

    common_list = get_common_IPList(cookie_list[cookie_index], timestamp_list[0], timestamp_list[1], percent)

    for timestamp in timestamp_list[2:]:
        filename = "../data/result_popIP/%s/%s_tidy.log" % (timestamp, cookie_list[cookie_index])
        ipTop = popIPTop(timestamp, cookie_list[cookie_index], percent, tidyPopIP(filename))
        ip_list = ipTop.get_pop_list()

        common_list = get_common_list(common_list, ip_list)

    output_filename = "../result/result_commonIP/%s/%s_CommonTopIP.log" % ("2018-03-08_12", cookie_list[cookie_index])
    output_IPList(common_list, output_filename)



