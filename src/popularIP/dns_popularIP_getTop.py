from src.popularIP.dns_popularIP_tidy import tidyPopIP


class popIPTop(object):
    def __init__(self, timestamp, cookie, percent, tidyIPDict):
        if percent < 0 or percent > 100:
            raise ValueError("input percent not between 0 and 100")
        self.timestamp = timestamp
        self.cookie = cookie
        self.percent = percent
        self.tidyIPDict = tidyIPDict

        self.popIPList = []
        self.target_count = int(self.tidyIPDict.total_count * self.percent / 100)

    def get_pop_list(self):
        count_remain = self.target_count
        index = 1
        while count_remain > 0:
            self.popIPList.append(self.tidyIPDict.popIP_dict[index][1])
            count_remain -= self.tidyIPDict.popIP_dict[index][0]
            index += 1
        # print(self.popIPList)
        # print(len(self.popIPList))
        return self.popIPList

    def store_pop_list(self):
        output_file = "../result/result_topIP/%s/%s_top_%d.log" % (self.timestamp, self.cookie, self.percent)
        with open(output_file, 'a') as f:
            for ip in self.popIPList:
                f.write(ip + "\n")


if __name__ == '__main__':
    # timestamp = "2018-03-01_12"

    # cookie = "out_src"

    timestamp_list = ["2018-03-01_12", "2018-03-08_10", "2018-03-08_12",
                      "2018-03-08_16", "2018-03-07_12", "2018-03-16_12"]

    cookie_list = ["in_src", "in_dst", "out_src", "out_dst"]

    percent = 90

    for timestamp in timestamp_list:
        for cookie in cookie_list:
            filename = "../data/result_popIP/%s/%s_tidy.log" % (timestamp, cookie)
            ipTop = popIPTop(timestamp, cookie, percent, tidyPopIP(filename))
            ipTop.get_pop_list()
            ipTop.store_pop_list()
