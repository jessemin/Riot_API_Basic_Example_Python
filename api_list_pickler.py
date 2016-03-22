import pickle


api_list_filename = "ApiList"
api_list_picklename = "ApiListPickle"


def generate_api_dict():
    f = open(api_list_filename)
    api_dict = dict()
    line = f.readline()
    while line:
        api_name, api_request = line.split(" ")[0], line.split(" ")[1]
        api_dict[api_name] = api_request
        line = f.readline()
    f. close()
    return api_dict


def dump_dict(api_dict):
    pickle.dump(api_dict, open(api_list_picklename, "wb"))


dump_dict(generate_api_dict())
