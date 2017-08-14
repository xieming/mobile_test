import re
import requests
from globals import ENV


token_page_url = '{}/services/oboe2/Areas/ServiceTest/MemberSiteSetting.aspx'
url = "http://" + ENV +".englishtown.com"


def get_token():
    page_url = token_page_url.format(url)
    result = requests.get(page_url)
    pattern = '.*token">(.*)</span>.*'
    for line in result.text.split():
        m = re.match(pattern, line)
        if m:
            return m.group(1)

    else:
        raise EnvironmentError("Cannot get token!")


def score_helper_load_student(student_name_or_id):
    """Get student info via S15 submit score helper."""
    token = get_token()
    data = {'cmd': 'loadStudentInfo',
            'member_id': student_name_or_id,
            'token': token}
    target_url = "/services/school/_tools/progress/SubmitScoreHelper.aspx"
    response = requests.post(url + target_url, data=data)
    match_char = u'★'
    result = {}

    if response.status_code == 200 and '|' in response.text:
        raw = response.text.split('|')
        result = {'username': raw[1], 'member_id': int(raw[3]), 'partner': raw[4]}
        levels = raw[5].split('#')
        units = raw[6].split('#')

        current_level = [l for l in levels if match_char in l][0]  # e.g. '378$★GE2013 Level3'
        current_unit = [l for l in units if match_char in l][0]  # e.g. '1803$★Level 1 - Unit 6'
        if 'Level' not in current_level:
            result['current_level'] = current_level[current_level.index(match_char) + 1:]
            result['current_level_name'] = result['current_level_code']
            result['current_unit'] = current_unit[current_unit.index(match_char) + 1:]

        else:
            result['current_level'] = int(re.findall(r'Level([\d ]+)', current_level)[0].strip())  # 1~16
            result['current_level_name'] = re.findall(r'Level(.+)-', current_unit)[0].strip()  # A, B, 1~14
            result['current_unit'] = int(re.findall(r'Unit([\d ]+)', current_unit)[0].strip())  # 1~6

    return result


if __name__ == '__main__':
    result = score_helper_load_student('tauto4327')
    print("result is: {}".format(result))
    print("current level is: {}".format(result['current_level']))