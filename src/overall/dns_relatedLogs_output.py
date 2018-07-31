import os

if __name__ == '__main__':
    data_folder = "/data3/"
    search_key = "2018-04"

    for daily_folder in os.listdir(data_folder):
        if os.path.isdir(data_folder + daily_folder) and daily_folder.startswith(search_key):
            print(data_folder)
            date = daily_folder
            for trace_filename in os.listdir(data_folder + daily_folder + "/"):
                if "dns" in trace_filename:
                    print(trace_filename)

