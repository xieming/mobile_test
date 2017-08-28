import requests
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

url = 'http://www.lagou.com/jobs/positionAjax.json?city={}&yx={}&needAddtionalResult=false'
cities = np.array(['北京', '上海', '广州', '深圳'])
salaries = np.array(['2k-5k', '5k-10k', '10k-15k', '15k-25k', '25k-50k'])


def get_page(url, page_num, keyword):  # 模仿浏览器post需求信息，并读取返回后的页面信息
    headers = {
        "User-Agent": "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Referer": "https://www.lagou.com/jobs/list_%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90%E5%B8%88?px=default&city=%E6%B7%B1%E5%9C%B3&district=%E5%8D%97%E5%B1%B1%E5%8C%BA",
        "X-Requested-With": "XMLHttpRequest",
        "Host": "www.lagou.com",
        "Connection": "keep-alive",
        "Cookie": "user_trace_token=20160214102121-0be42521e365477ba08bd330fd2c9c72; LGUID=20160214102122-a3b749ae-d2c1-11e5-8a48-525400f775ce; tencentSig=9579373568; pgv_pvi=3712577536; index_location_city=%E5%85%A8%E5%9B%BD; SEARCH_ID=c684c55390a84fe5bd7b62bf1754b900; JSESSIONID=8C779B1311176D4D6B74AF3CE40CE5F2; TG-TRACK-CODE=index_hotjob; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1485318435,1485338972,1485393674,1485423558; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1485423598; _ga=GA1.2.1996921784.1455416480; LGRID=20170126174002-691cb0a5-e3ab-11e6-bdc0-525400f775ce",
        "Origin": "https://www.lagou.com",
        "Upgrade-Insecure-Requests": "1",
        "X-Anit-Forge-Code": "0",
        "X-Anit-Forge-Token": "None",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.8"
    }
    if page_num == 1:
        boo = 'true'
    else:
        boo = 'false'

    page_data = {
        'first': boo,
        'pn': page_num,
        'kd': keyword
    }
    page = requests.post(url=url, headers=headers, data=page_data)
    return page.json()

if __name__ == '__main__':
    keyword = "测试"
    final_result = []
    for city in cities:
        total_count = []
        for salary in salaries:
            result = get_page(url.format(city, salary), 1, keyword)['content']['positionResult']['totalCount']
            total_count.append(result)
        final_result.append(total_count)
    count_array = np.array(final_result)
    count_frame= pd.DataFrame(count_array, index=cities, columns=salaries)
    print(count_frame)

    font = FontProperties(fname='/Library/Fonts/华文仿宋.ttf', size=14)
    # 创建柱状图，设置颜色，透明度和外边框颜色
    plt.bar(np.arange(len(cities)), count_array.sum(axis=1), color='b', alpha=0.8, align='center', edgecolor='white')
    # 设置x轴标签
    plt.xlabel('城市', fontproperties=font)
    # 设置y周标签
    plt.ylabel('工作机会', fontproperties=font)
    # 设置图表标题
    plt.title('一线城市软件测试工作分布', fontproperties=font)
    # 设置图例的文字和在图表中的位置
    plt.legend(['数量'], loc='upper right', prop=font)
    # 设置背景网格线的颜色，样式，尺寸和透明度
    plt.grid(color='#95a5a6', linestyle='--', linewidth=1, axis='y', alpha=0.4)
    # 设置数据分类名称
    plt.xticks(np.arange(len(cities)), cities, fontproperties=font)
    # 显示图表
    plt.savefig('result1.png')

    # 单独显示
    plt.style.use('ggplot')
    logistic_regression = count_array

    engines = cities
    colors = 'rgbcy'

    fig, ax1 = plt.subplots(ncols=1)

    idx = np.arange(len(logistic_regression[0]))
    n = len(logistic_regression)
    width = 1.0 / (n + 1)
    for i in range(n):
        ax1.bar(idx + i * width, logistic_regression[i], width, color=colors[i], alpha=0.5)
        xpos = idx + (i + 0.5) * width
        ypos = logistic_regression[i]
        for j in range(len(ypos)):
            ax1.text(xpos[j], ypos[j], str(ypos[j]), ha='center', va='bottom', rotation=90)
    ax1.legend(engines, prop=font)
    ax1.set_xticks(idx + 0.5, [25, 50, 100, 200, 400])
    ax1.set_xticklabels(['', '2k-5k', '5k-10k', '10k-15k', '15k-25k', '25k-50k'])
    ax1.set_xlabel("薪水", fontproperties=font)
    ax1.set_ylabel('职位数', fontproperties=font)
    ax1.set_title('城市和薪水分布图', fontproperties=font)
    plt.tight_layout()
    plt.savefig("result3.png")

    number = count_frame.loc[cities[1], '15k-25k']
    page_number = int(number / 15)
    tags = np.array(['companyFullName', 'companyLabelList', 'companySize', 'district', 'financeStage', 'industryField','positionAdvantage', 'positionLables', 'positionName', 'workYear'])
    # np.savetxt('haha.csv',tag.reshape(1,10),delimiter=',',fmt='%s')
    for page_index in range(1, 3):
        page = get_page(url.format('上海', '15k-25k'), page_index, keyword)
        page_result = page['content']['positionResult']['result']
        jobs = (page_result[index][tag] for index in range(0, 15) for tag in tags)
        job_list = list(jobs)
        #print(job_list)
        tag_array = np.array(job_list, dtype=object)
        #print(tag_array.reshape(15, 10))
        tag_frame = pd.DataFrame(tag_array.reshape(15,10))
        if page_index ==1:
            tag_frame.to_csv(path_or_buf="tageframe.csv", header=tags)
        else:
            tag_frame.to_csv(path_or_buf="tageframe.csv", header=False, mode='a+')