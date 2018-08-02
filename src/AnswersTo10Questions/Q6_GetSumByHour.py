if __name__ == '__main__':
    filepath = "../../data/result_inout/dns_InOutCount_2018-03_F.log"
    cached = 0
    with open(filepath, 'r') as f:
        for line in f:
            if("2018-03-12") in line:
                line_list = line.split("\t")
                if line_list[1][22:24]!=line_list[1][31:33]:
                    print(line_list[1])
                    print(int(line_list[3]) + int(cached))
                    print("===")
                    cached = 0
                else:
                    cached = line_list[4]

