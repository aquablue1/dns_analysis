from src.dns_popularIP_getTop import popIPTop
from src.dns_popularIP_tidy import tidyPopIP
import matplotlib.pyplot as plt

class topPropertyCDF(object):
    def __init__(self, filename):
        tidyIP = tidyPopIP(filename)
        self.popIP_dict = tidyIP.popIP_dict
        self.total_count = tidyIP.total_count
        self.total_IP_count = tidyIP.total_IP_count
        self.startCount = 1
        self.endCount = self.total_IP_count
        self.x_data = []
        self.y_data = []

    def topPropertyDataGen(self):
        self.x_data.append(self.startCount)
        self.y_data.append(int(self.popIP_dict[self.startCount][0]))
        for index in range(self.startCount+1, self.endCount):
            self.x_data.append(index)
            self.y_data.append(int(self.popIP_dict[index][0]) + self.y_data[-1])

    def draw_CDF(self, x_label, y_label, title=""):
        x_data = self.x_data
        y_data = [float(count)/self.total_count for count in self.y_data]
        plt.plot(x_data, y_data)
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.title(title)
        plt.show()


if __name__ == '__main__':
    cookie = "in_dst"
    timestamp = "2018-03-08_12"
    filename = "../data/result_popIP/%s/%s_tidy.log" % (timestamp, cookie)
    x_label = "Number of distinct %s IPs" % cookie
    y_label = "CDF"

    cdf = topPropertyCDF(filename)
    cdf.topPropertyDataGen()
    print(cdf.x_data)
    print(cdf.y_data)
    cdf.draw_CDF(x_label, y_label)
