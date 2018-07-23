"""
Classify the original outbound traffic data based on the source IP.
Choose a list of popular IP and store them in a specific file.
To Use:
"""

import os

class DNSOutbound(object):
    """
    A class used to describe all the outbound traffic in a folder (usually contains one hour of the data.
    """
    def __init__(self, filename):
        """
        Constructor
        :param filename: The name of file where outbound traffic data is stored
        """
        self.sourceLocation = filename
        self.sourceFile = open(self.sourceLocation, 'r')

        self.uniq_IPList = []
        self.popularList = []
        self.lessPopularList = []

    def __del__(self):
        """
        Destory the file handler in destroctor.
        :return:
        """
        self.sourceFile.close()

    def get_uniq_IPList(self):
        self.sourceFile = open(self.sourceLocation, 'r')
        for line in self.sourceFile.readlines():
            line_list = line.split("\t")
            sourceIP = line_list[4]
            if sourceIP not in self.uniq_IPList:
                self.uniq_IPList.append(sourceIP)

    def set_pop_list(self, popList, lessPopList=None):
        self.popularList = popList
        if lessPopList is None:
            self.lessPopularList = []
        else:
            self.lessPopularList = lessPopList

    def do_list_classify(self, output_folder):
        # Store the IP and its file handler in file_handler_dict.
        # In this method, only the IP in popularList or lessPopularList are classified.
        output_file_handler_dict = {}
        # use a dict to store all file handler of popular IPs.
        # These handler will then be used to output the result of IP classification.
        for ip in (self.popularList + self.lessPopularList):
            output_file_handler_dict[ip] = open(output_folder+"/%s.log" % ip, 'a')
            output_file_handler_dict["others"] = open(output_folder+"/others.log", 'a')

        self.sourceFile = open(self.sourceLocation, 'r')
        for line in self.sourceFile.readlines():
            line_list = line.split("\t")
            destIP = line_list[4]
            if destIP in self.popularList or destIP in self.lessPopularList:
                output_file_handler_dict[destIP].write(line)
            else:
                output_file_handler_dict["others"].write(line)

        for handler in output_file_handler_dict.values():
            handler.close()

    def do_global_classify(self, output_folder):
        # This method is different from do_list_classify since all the IP appeared are classified.
        #
        # Store the IP and its file handler in file_handler_dict.
        output_file_handler_dict = {}
        # use a dict to store all file handler of popular IPs.
        # These handler will then be used to output the result of IP classification.
        for ip in (self.uniq_IPList):
            output_file_handler_dict[ip] = open(output_folder+"/%s.log" % ip, 'a')
            output_file_handler_dict["others"] = open(output_folder+"/others.log", 'a')

        self.sourceFile = open(self.sourceLocation, 'r')
        for line in self.sourceFile.readlines():
            line_list = line.split("\t")
            destIP = line_list[4]
            try:
                output_file_handler_dict[destIP].write(line)
            except KeyError:
                print("source IP %s not found in the uniq_IPList" % destIP)

        for handler in output_file_handler_dict.values():
            handler.close()


if __name__ == '__main__':
    timestamp = "2018-03-08_12"
    filename = "../../data/result_inbound/%s.log" % timestamp
    listoutputfolder = "../../result/result_inbound_classify"

    outbound = DNSOutbound(filename)

    popList = ["136.159.1.21",
               "136.159.34.201",
               "136.159.2.4",
               "136.159.2.1"]

    """
    lessPopList = ["136.159.5.75",
                   "136.159.222.244",
                   "136.159.160.157",
                   "136.159.160.156",
                   "136.159.160.155",
                   "136.159.160.154",
                   "136.159.117.235",
                   "136.159.160.153",
                   "136.159.160.110"]
    """

    outbound.set_pop_list(popList)

    outbound.do_list_classify(listoutputfolder)

    # globaloutputfolder = "../../result/result_inbound_global_classify"
    # outbound.get_uniq_IPList()
    # outbound.do_global_classify(globaloutputfolder)