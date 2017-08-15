import pandas as pd
import requests
import matplotlib.pyplot   as plt

# result = pd.read_html("https://confluence.englishtown.com/display/SCHUX/Live+Test+Account+-+EFEC")

# print(result)
s = requests.Session()
username = "ming.xiesh"
password = "Good_Luck888"
CONFLUENCE_LOGIN_URL = "https://confluence.englishtown.com/login.action?os_destination=%2Findex.action&permissionViolation=true"

CONFLUENCE_DEVICE_TRACKING_URL = "https://confluence.englishtown.com/pages/viewpage.action?pageId=673644924"

s.post(CONFLUENCE_LOGIN_URL, data={"os_username": username, "os_password": password}, verify=False)

result = s.get(CONFLUENCE_DEVICE_TRACKING_URL, verify=False).content
table = pd.read_html(result)
android_device = table[0]



# print(android_device)

phone_device = android_device[android_device[4] == 'Tablet']

phone_device.to_csv("devices_tablet.csv")

print(phone_device)
print(phone_device.groupby(5).size())
print(phone_device.groupby(1).size())
sum_df = phone_device.groupby(5).size()

#sum_df.plot(kind='pie', subplots=True, figsize=(6, 6), legend = True, x = 'numbers')
sum_df.plot(kind='pie', subplots=True, autopct='%.2f', figsize=(8, 8), title = "Versions", legend = True,y="fuck")  # 显示百分比
plt.show()

# phone_device.groupby(5).size().plot.pie()

# pie = sum_df.plot(kind="pie", figsize=(6,6), legend = False, use_index=False, subplots=True, colormap="Pastel1")
# fig = pie[0].get_figure()
# fig.show()
# fig.savefig("./fuck.png")
