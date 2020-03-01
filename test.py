from vultr import Vultr
import json
api_key = 'KYDEEGRW34BFTPY4W6ZE7OWDOGJT5HSCJSRA' 
vultr = Vultr(api_key) 
#plans_json = vultr.plans.list()
#print(plans_json)

server_list = vultr.server.list()
server_list_json = json.dumps(server_list, sort_keys=True, indent=4, separators=(', ', ':' ))
#print(server_list_json)

server_list_json_dict = json.loads(server_list_json)

d_key, = server_list_json_dict
# print(d_key)

# d_id = server_list_json_dict[d_key]
# s_id = d_id['SUBID']

bandwidth = vultr.server.bandwidth(d_key)
bandwidth_json = json.dumps(bandwidth, sort_keys=True, indent=4, separators=(', ', ':' ))
print(bandwidth_json)