from collections import Counter
from src.util.draw_CDF import CDF_Single
import math

class TargetDomainSet(object):
    def __init__(self, path):
        self.source_path = path
        self.f = open(path, 'r')

        # Core data structure. Used to store domain count dict.
        # keys are the unique URLs and values are their occurrence.
        self.domain_counter = None

    def __del__(self):
        self.f.close()

    def gen_domain_dict(self):
        lines = self.f.readlines()
        domain_list = []
        for line in lines:
            domain = line.split("\t")[9]
            if domain != "-":
                domain_list.append(line.split("\t")[9])

        self.domain_counter = Counter(domain_list)

    def get_domain_dict(self):
        """
        Return domain_dict as a dict
        :return:
        """
        if self.domain_counter is None:
            raise ValueError("domain_counter not Initialized.")
        else:
            return dict(self.domain_counter)

    def get_count_data(self):
        """
        Return pure count data, i.e. a list with pure counting based on dict_count
        :return:
        """
        if self.domain_counter is None:
            raise ValueError("domain_counter not Initialized.")
        else:
            return list(dict(self.domain_counter).values())


if __name__ == '__main__':

    ts = "136.159.190.37"
    cookie = "out"
    log_file = "../../result/result_%sbound_global_classify/%s.log" % (cookie,ts)

    domainSet = TargetDomainSet(log_file)
    domainSet.gen_domain_dict()


    cdf = CDF_Single()
    cdf.set_data(domainSet.get_count_data())
    cdf.set_labels(["Number of Distinct URLs.", "CDF"])
    cdf.set_legend("%s"%(ts))
    x_real = [math.log10(1), math.log10(10), math.log10(100), math.log10(1000),
                math.log10(10000), math.log10(100000), math.log10(1000000)]
    x_tick = ["0", "10", "100", "1000", "10E4", "10E5", "10E6"]
    cdf.set_tick_map("x", x_real, x_tick)
    cdf.set_color("black")
    cdf.do_show(is_log=True)