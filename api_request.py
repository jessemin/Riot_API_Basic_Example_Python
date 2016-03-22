import requests
import pickle


dev_key_filename = "RiotDevKey"
api_list_picklename = "ApiListPickle"


def retrieve_key():
    f = open(dev_key_filename)
    api_key = f.readlines()[0]
    f.close()
    return api_key


def get_basic_api_request(api_name):
    f = open(api_list_picklename)
    api_dict = pickle.load(open(api_list_picklename, "rb"))
    f.close()
    return api_dict[api_name]


def summoner_by_name_request(summoner_name):
    api_request = get_basic_api_request("summoner_by_name")
    api_request = api_request[:api_request.rfind("/")+1] + summoner_name
    api_request += "?api_key=" + retrieve_key()
    return api_request


def matchlist_request(summoner_id):
    api_request = get_basic_api_request("matchlist")
    api_request = api_request[:api_request.rfind("/")+1] + str(summoner_id)
    api_request += "?api_key=" + retrieve_key()
    return api_request


def get_user_info(summoner_name):
    r = requests.get(summoner_by_name_request(summoner_name))
    return r.json()


def get_matchlist(summoner_name):
    summoner_id = get_user_info(summoner_name)[summoner_name]["id"]
    r = requests.get(matchlist_request(summoner_id))
    print r.text
    return r.json()

