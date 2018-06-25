"""
Generate dict to store popular IPs and its popularity, using nature numbers as index
By Zhengping in June, 2018
"""

class tidyPopIP(object):
    def __init__(self, filename):
        """
        Gen an tidy_popIP filename as input.
        :param filename:
        """

        with open(filename) as f:
            self.total_count = 0
            index = 1
            self.popIP_dict = {}
            for line in f:
                line = line.strip()
                line_list = line.split(" ")
                self.popIP_dict[index] = (int(line_list[0]), line_list[1])
                self.total_count += int(line_list[0])
                index += 1
        print(self.popIP_dict)


if __name__ == '__main__':
    filename = "../data/result_popIP/out_src_tidy.log"
    ips = tidyPopIP(filename)