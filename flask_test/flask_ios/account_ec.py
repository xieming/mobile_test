import re
import time
import urllib
import urllib2

# config all types

txt_file_path = r'EC_accounts.txt'
start_time_stamp = time.strftime("%Y%m%d%H%M%S")


class AccountHelper():
    def __init__(self):
        self.headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
        }
        self.host = "mobilefirst.englishtown.com"
        self.url = r"http://{0}/services/oboe2/salesforce/test/creatememberfore14hz?v=2".format(self.host)
        self.load_url = r"http://{0}/services/oboe2/salesforce/test/ActivateV2".format(
            self.host)

    def get_page(self, url, parameters, headers):
        post_data = urllib.urlencode(parameters)
        request = urllib2.Request(url, post_data, headers=headers)
        response = urllib2.urlopen(request)
        page = response.read()
        return page

    def set_values(self, memberId, mainRedemptionCode, freeRedemptionCode, divisionCode, productId, mainRedemptionQty=3,
                   startLevel="0A", freeRedemptionQty=3, securityverified="on", includesenroll="on"):
        score_json = {
            "memberId": memberId,
            "startLevel": startLevel,
            "mainRedemptionCode": mainRedemptionCode,
            "mainRedemptionQty": mainRedemptionQty,
            "freeRedemptionCode": freeRedemptionCode,
            "freeRedemptionQty": freeRedemptionQty,
            "divisionCode": divisionCode,
            "productId": productId,
            "securityverified": securityverified,
            "includesenroll": includesenroll

        }
        response = self.get_page(self.load_url, score_json, self.headers)

        return response

        # memberid, username

    def create_member(self):
        page = urllib2.urlopen(self.url)
        html = page.read()
        url2 = re.search("memberid=(\d+)'", html)
        memberid = url2.group(1)
        return memberid

    #

    def write_log(self, file_name, content):
        file_object = open(file_name, 'a+')
        file_object.write(content)
        file_object.close()


# def main():
#     new = AccountHelper()
#     memberId= new.create_member()
#     mainRedemptionCode = "S15SCHOOLMAIN"
#     freeRedemptionCode = "S15SCHOOLF1D"
#     divisionCode = "SSCNTE2"
#     productId = 63
#
#     result = new.set_values(memberId, mainRedemptionCode, freeRedemptionCode, divisionCode, productId)
#     print result
#
#
# if __name__ == '__main__':
#     main()
