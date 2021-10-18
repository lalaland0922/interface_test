import requests
import pytest
import allure
from utils.get_event_yaml import get_yaml
from common.bases.get_config import cf

case_names, parameters = get_yaml(cf.get_event_list_path)
params = list(parameters)


@allure.feature('查询发布会接口测试')
class TestGetEvent:
    @allure.story('验证发布会查询接口')
    @pytest.mark.parametrize('case_name, http_request, expected_results', params, ids=case_names)
    def test_get_event(self, case_name, http_request, expected_results):
        res = requests.request(http_request['method'], url='http://' + cf.address + http_request['path'], params=http_request['params'])
        if res.content:
            actual_response = res.json()
            expected_status = expected_results['response']['status']
            actual_status = actual_response['status']
            expected_message = expected_results['response']['message']
            actual_message = actual_response['message']
            assert actual_status == expected_status
            assert actual_message == expected_message


