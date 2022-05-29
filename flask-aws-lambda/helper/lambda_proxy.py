import json


class LambdaProxy:
    """ APIGatewayとLambda間のリクエスト/レスポンスを変換するクラス。
    """
    class Request:
        """ Lambdaのイベントから、リクエストに必要な情報を保持するクラス。
        :param dict event: Lambdaのイベント情報
        """
        def __init__(self, event: dict):
            self.path = event['path']
            self.path_params = event['pathParameters']
            self.query_params = event['queryStringParameters']

        def __str__(self):
            return f'{self.path=}, {self.path_params=}, {self.query_params=}'

    @staticmethod
    def from_request(event: dict) -> Request:
        """ Lambdaのイベントから、APIのリクエスト情報を生成する。
        :param dict event: Lambdaのイベント情報
        :return Request: APIのリクエスト情報
        """
        return LambdaProxy.Request(event)

    @staticmethod
    def to_response(status_code: int, body: dict) -> dict:
        """ レスポンス情報を、APIのレスポンス仕様に合わせて変換する。
        :param int status_code: HTTPステータス
        :param dict body: レスポンスのBody
        :return dict: APIのレスポンス
        """
        return {
            'isBase64Encoded': False,
            'statusCode': status_code,
            'headers': {},
            'body': json.dumps(body)
        }
