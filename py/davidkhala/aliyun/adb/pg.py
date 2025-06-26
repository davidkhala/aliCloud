import alibabacloud_credentials.client
from alibabacloud_gpdb20160503.client import Client as PGClient
from alibabacloud_gpdb20160503.models import DescribeDBInstancesRequest
from alibabacloud_tea_openapi.models import Config
from alibabacloud_tea_util.models import RuntimeOptions


class Client:
    def __init__(self, credential: alibabacloud_credentials.client):
        config = Config(
            credential=credential,
            endpoint='gpdb.aliyuncs.com'
        )

        self.client = PGClient(config)
        self.region_id = 'cn-hongkong'

    def list(self):
        return self.client.describe_dbinstances_with_options(DescribeDBInstancesRequest(
            region_id=self.region_id,
        ), RuntimeOptions())
