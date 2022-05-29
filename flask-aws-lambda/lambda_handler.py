import re
from helper.lambda_proxy import LambdaProxy


location_details = re.compile(r'')
location_pre_list = re.compile(r'')


def handler(event, context):
    request = LambdaProxy.from_request(event=event)
    print(request)

    try:
        if location_pre_list.match(request.path):
            pass
        elif location_details.match(request.path):
            pass
        else:
            raise Exception()
        return LambdaProxy.to_response(200, {"name": "tanaka", "age": 100})
    except NotImplemented as e:
        print(e)
        return LambdaProxy.to_response(404, {"message": "error"})
    except Exception as e:
        print(e)
        return LambdaProxy.to_response(500, {"message": "error"})


def get_locations(imei: str):
    print(imei)


if __name__ == "__main__":
    _event = {
        "resource": "/xxx/{foo}/{bar}",
        "path": "/xxx/foofoo/barbar",
        "httpMethod": "GET",
        "headers": {},
        "multiValueHeaders": {},
        "queryStringParameters": {
            "fuga": "fugaga",
            "hoge": "hogege"
        },
        "multiValueQueryStringParameters": {...},
        "pathParameters": {
            "bar": "barbar",
            "foo": "foofoo"
        },
        "stageVariables": None,
        "requestContext": {...},
        "body": None,
        "isBase64Encoded": False
    }

    handler(_event, None)
