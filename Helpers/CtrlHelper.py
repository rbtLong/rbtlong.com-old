from flask import Response, json


def Resp(data, mime='application/json'):
    return Response(json.dumps(data), mimetype=mime)


def Succ(data, res={}):
    res['success'] = 1
    res['content'] = data
    return Resp(res)


def Fail(reason=None, err_code=0, res=None):
    if res is None:
        res = {}

    res['success'] = err_code

    if reason is not None:
        res['reason'] = reason

    return Resp(res)
