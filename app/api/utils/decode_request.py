import json

def decode_request(req):
    raw_request_data = req.get_data()
    charset = req.mimetype_params.get('charset') or 'UTF-8'
    request_dic = json.loads(raw_request_data.decode(charset, 'replace'))

    return request_dic
