import os
import sys
import json
import nexmo


class NumberInsightWrapper:
    def __init__(self):
        self.number = sys.argv[1]
        self.client = nexmo.Client(
            key=os.environ["NEXMO_API_KEY"], secret=os.environ["NEXMO_API_SECRET"]
        )

    def print_json(self, insight_object):
        print(json.dumps(insight_object))


class NumberInsightBasic(NumberInsightWrapper):
    def get(cls):
        response = cls.client.get_basic_number_insight(number=cls.number)
        cls.print_json(response)


class NumberInsightStandard(NumberInsightWrapper):
    def get(cls):
        response = cls.client.get_standard_number_insight(number=cls.number)
        cls.print_json(response)


class NumberInsightAdvanced(NumberInsightWrapper):
    def get(cls):
        response = cls.client.get_advanced_number_insight(number=cls.number, cnam=True)
        cls.print_json(response)


class NumberInsightIP(NumberInsightWrapper):
    def get(cls):
        ip = sys.argv[2]
        response = cls.client.get_advanced_number_insight(number=cls.number, ip=ip)
        cls.print_json(response)
