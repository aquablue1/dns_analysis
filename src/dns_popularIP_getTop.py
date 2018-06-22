from src.dns_popular_IP_tidy import tidyPopIP


class popIPTop(object):
    def __init__(self, percent, tidyIPDict):
        if percent < 0 or percent > 100:
            raise ValueError("input percent not between 0 and 100")
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
        print(self.popIPList)
        print(len(self.popIPList))


if __name__ == '__main__':
    timestamp = "2018-03-07_12"
    percent = 80
    cookie = "out_src"

    filename = "../data/result_popIP/%s/%s_tidy.log" % (timestamp, cookie)
    ipTop = popIPTop(percent, tidyPopIP(filename))
    ipTop.get_pop_list()