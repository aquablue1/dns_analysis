import csv

class INDEX:
    index = 0


def output_node_data(node_list, filename):
    with open(filename, "a") as f:
        f.write("Id, Label\n")
        for node in node_list:
            f.write("%d, %s\n" % (INDEX.index, node))
            INDEX.index += 1


def output_link_data(link_list, filename):
    with open(filename, "a") as f:
        f.write("Source, Target\n")
        for link in link_list:
            f.write("%s, %s\n" %(link[0], link[1]))


def input_node_data(filename):
    node_list = []
    with open(filename) as f:
        for line in f:
            line = line.strip()
            node_list.append(line)
    return node_list


def input_link_data(filename):
    link_list = []
    with open(filename) as f:
        for line in f:
            line = line.strip()
            line_list = line.split()
            link_list.append([line_list[2], line_list[4]])
    return link_list


if __name__ == '__main__':
    cookie_list = ["out_src", "out_dst"]
    output_fname_cookie = "Outbound"
    timestamp = "2018-03-08_12"

    for cookie in cookie_list:
        input_node_fname = "../data/result_commonIP/%s/%s_CommonTopIP.log" % (timestamp, cookie)
        output_node_fname = "../result/Gephi_Input/%s_node.csv" % output_fname_cookie

        # node_list = input_node_data(input_node_fname)
        # print(node_list)
        # output_node_data(node_list, output_node_fname)

    cookie = "Outbound"
    input_link_fname = "../data/result_popIP_RelatedRecord/%s_commonIP_relatedRecord.log" % cookie
    output_link_fname = "../result/Gephi_Input/%s_link.csv" % output_fname_cookie

    link_list = input_link_data(input_link_fname)
    print(link_list)
    output_link_data(link_list, output_link_fname)


















