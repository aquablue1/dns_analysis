import os


def get_Potential_IPList(cookie1, cookie2):
    IPList = []
    source_folder = "../../data/result_q7_popIPs/"
    source_file = source_folder + "/%s_%s.log" % (cookie1, cookie2)
    with open(source_folder, 'r') as f:
        for line in f:
            if line[0] == "#":
                continue
            line = line.strip()
            IPList.append(line)
    return IPList


def get_trafficVolume_byHour(cookie1, cookie2, filename, IPDict):
    IPList = IPDict.keys()
    if cookie2 == "Source":
        search_IP_field = 2
        search_volume_field = 9
    elif cookie2 == "Destination":
        search_IP_field = 4
        search_volume_field = 10
    else:
        raise ValueError("Invaild cookie2 value")

    with open(filename, 'r') as f:
        for line in f:
            if line[0] == "#":
                continue
            line_list = line.strip().split("\t")

            this_IP = line_list[search_IP_field]
            if line_list[search_volume_field] != "-":
                this_volume = int(line_list[search_volume_field])
            else:
                this_volume = 0

            if this_IP in IPList:
                IPDict[this_IP] += this_volume

    return IPDict


if __name__ == '__main__':
    cookie1 = "Inbound"
    cookie2 = "Source"
    search_folder = "../../data/"

    IPList = get_Potential_IPList(cookie1, cookie2)
    IPDict = {}
    for ip in IPList:
        IPDict[ip] = 0
    for filename in os.listdir(search_folder):
        if "conn." in filename:
            IPDict = get_trafficVolume_byHour(cookie1, cookie2, search_folder+"/"+filename, IPDict)

