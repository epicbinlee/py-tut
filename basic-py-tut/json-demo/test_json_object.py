import json


class JSONObject:
    def __init__(self, d):
        self.__dict__ = d


def json2obj(s):
    return json.loads(s, object_hook=JSONObject)


def obj2json(a):
    return json.dumps(a, default=lambda obj: obj.__dict__, sort_keys=True)  # indent=4,这个参数用来更好的展示json


a = {"status": 1, "info": "发布成功", "data": {"id": "52", "feed_id": "70"}}
b = json2obj(json.dumps(a))
print(b.info)

print(obj2json(a))

# out-put : 发布成功
# out-put :  {"data": {"feed_id": "70", "id": "52"}, "info": "\u53d1\u5e03\u6210\u529f", "status": 1}
