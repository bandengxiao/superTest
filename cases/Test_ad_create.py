import json
import allure
import pytest
import requests
from ac.base import BaseTest
from ac import requests
from ac.dataGet import dataGet
from ac.logger import loggerConfig, log

@allure.feature('创建计划测试')
class Test_ad_create(BaseTest):
    # dataGet.getYamlData('Test_ad_create.yaml', 'normal')

    # API='http://192.168.0.102:9999/V3/ad/create.json'
    @pytest.mark.parametrize("caseName,inputData2,expectResult,expectDB",dataGet.getYamlData('Test_ad_create.yaml', 'normal'))
    @allure.title('{caseName}')
    @allure.severity("normal")
    def test_ad_create_normal(self,caseName,inputData2,expectResult,expectDB):
       #   response=requests.post(url='http://192.168.0.105:9999/V3/ad/create.json',datas=inputData,'')
       # data="""{"caller_source": 1, "campaign_id": 3340071, "fe_version": "2.0.1", "fe_is_edit": true, "fe_is_copy": false, "fe_is_self_obj_url": false, "fe_is_ghost": false, "mid_source": 0, "objective": 88030003, "fe_app_type": null, "fe_app_id": null, "optimization_goal": 86006001, "target_explicit_content_targeting": 0, "target_template_id": null, "fe_daily_budget_type": 1, "billing_type": 1, "schedule_delivery_type": 2, "schedule_start_time": "2021-02-28 00:00:00", "schedule_stop_time": "2021-03-28 00:00:00", "schedule_daily_delivery_type": 3, "name": "create_first_test_ad", "deliver_scope": 2, "convert_goal": [89001001], "subject_obj_type": 1, "subject_obj_url": {"url": "https://lingdong.biz.weibo.com/a/2608812381/2186382339027965/index.html", "site_id": "2186382339027965", "type": 2}, "fe_age_type": 0, "target_genders": 401, "fe_locations_label": 0, "target_user_os": [], "target_user_network": [3], "fe_audience_list": 0, "fe_account_list": 0, "fe_interests_list": 0, "target_exp_convert_account": 0, "target_login_frequency": [210001], "fe_user_device": 0, "target_mobile_price": [90201000], "target_new_account_type": [220001], "daily_budget": "999.00", "ocpx_bid_amount": "32.00", "fe_schedule_range": ["2021-02-28 00:00:00", "2021-03-28 00:00:00"], "schedule_hourly_per_week": [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23], [], [], [], [], [], []], "target_is_enlarge": false, "fe_auto_message": false, "transform_goal": 86005001}"""
       #  response = requests.post(url='http://192.168.0.105:9999/V3/ad/create.json', datas=data)
       #  print(response.status_code)
       # data1 = dataGet.convertInputData(data=inputData)
       # print(dataGet.getYamlData('Test_ad_create.yaml','normal'))
       # requests.post(url=self.API,datas=inputData2)
       # header = {
       #     "Cookie": globalConf.COOKIE,
       #     "Content-Type": "application/x-www-form-urlencoded"
       # }
       # response = requests.post(url='http://192.168.225.107:9999/V3/ad/create.json', data=inputData2,headers=header)
       response=requests.post(url=self.API,datas=inputData2)
       # log.info('测试输入数据 ：', json.dumps(inputData2,ensure_ascii=False))
       log.info(self.API)
       log.info('输入数据:%s' % (json.dumps(inputData2))) #直接写log.info(‘输入数据’，json.dumps(inputData2))会报错，要写成这种形式






    @pytest.mark.parametrize("caseName,inputData2,expectResult,expectDB",dataGet.getYamlData('Test_ad_create.yaml', 'normal'))
    @allure.title('{caseName}')
    @allure.severity("normal")
    def test_ad_create_normal2(self, caseName, inputData2, expectResult, expectDB):
        #   response=requests.post(url='http://192.168.0.105:9999/V3/ad/create.json',datas=inputData,'')
        # data="""{"caller_source": 1, "campaign_id": 3340071, "fe_version": "2.0.1", "fe_is_edit": true, "fe_is_copy": false, "fe_is_self_obj_url": false, "fe_is_ghost": false, "mid_source": 0, "objective": 88030003, "fe_app_type": null, "fe_app_id": null, "optimization_goal": 86006001, "target_explicit_content_targeting": 0, "target_template_id": null, "fe_daily_budget_type": 1, "billing_type": 1, "schedule_delivery_type": 2, "schedule_start_time": "2021-02-28 00:00:00", "schedule_stop_time": "2021-03-28 00:00:00", "schedule_daily_delivery_type": 3, "name": "create_first_test_ad", "deliver_scope": 2, "convert_goal": [89001001], "subject_obj_type": 1, "subject_obj_url": {"url": "https://lingdong.biz.weibo.com/a/2608812381/2186382339027965/index.html", "site_id": "2186382339027965", "type": 2}, "fe_age_type": 0, "target_genders": 401, "fe_locations_label": 0, "target_user_os": [], "target_user_network": [3], "fe_audience_list": 0, "fe_account_list": 0, "fe_interests_list": 0, "target_exp_convert_account": 0, "target_login_frequency": [210001], "fe_user_device": 0, "target_mobile_price": [90201000], "target_new_account_type": [220001], "daily_budget": "999.00", "ocpx_bid_amount": "32.00", "fe_schedule_range": ["2021-02-28 00:00:00", "2021-03-28 00:00:00"], "schedule_hourly_per_week": [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23], [], [], [], [], [], []], "target_is_enlarge": false, "fe_auto_message": false, "transform_goal": 86005001}"""
        #  response = requests.post(url='http://192.168.0.105:9999/V3/ad/create.json', datas=data)
        #  print(response.status_code)
        # data1 = dataGet.convertInputData(data=inputData)
        # print(dataGet.getYamlData('Test_ad_create.yaml','normal'))
        # requests.post(url=self.API,datas=inputData2)
        # header = {
        #     "Cookie": globalConf.COOKIE,
        #     "Content-Type": "application/x-www-form-urlencoded"
        # }
        # response = requests.post(url='http://192.168.225.107:9999/V3/ad/create.json', data=inputData2,headers=header)
        response = requests.post(url=self.API, datas=inputData2)
        assert 1==1









if __name__ == '__main__':
    t=Test_ad_create()
    t.test_ad_create_normal