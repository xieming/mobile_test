# coding:utf-8
import itchat
import numpy as np
import pandas as pd
  
# 先登录  
itchat.auto_login(hotReload=True)  
  
  
def getFriends():  
    return itchat.get_friends(update=True)[0:]  
  
  
def getUserNameList():
    userNameList = set()

    # 得到我的所有好友列表  
    for friend in getFriends():  
        userNameList.add(friend['UserName'])

    return userNameList

    # for i in userNameList:
    #     #print( itchat.search_friends(userName=i))
    #     list.append(itchat.update_friend(i))
    # print(list)
    # dd = pd.DataFrame(list)
    # # dd.to_csv("friends.csv")
    # # ff = pd.read_csv("friends.csv")
    # print(dd)
    # dd.drop("HeadImgUrl").drop("HeadImgUrl").drop("WebWxPluginSwitch").drop("VerifyFlag").drop("MemberList")
    # print(dd)



  
  
# 得到指定的 微信群，获得他们的所有的昵称放到一个list中。这个指定的微信群名称包含某个关键字
def getGroupAllNicknameList():  
    for chatRoom in itchat.get_chatrooms():  
        groupNameList = set()  
        if chatRoom['NickName'].__contains__("Badminton"):
            androidGroupName = chatRoom['UserName']  
            memberListDiction = itchat.update_chatroom(androidGroupName)  
            androidGroupContactlist = memberListDiction['MemberList']
            print(androidGroupContactlist)
            for contact in androidGroupContactlist:
                print(contact['NickName'])
                groupNameList.add(contact['NickName'])
            return groupNameList

  
  
if __name__ == '__main__':
    result = getFriends()

    dd = pd.DataFrame(list(result))
    dd.dropna(axis=1,inplace=True)
    #print(dd)
    dd.drop('Alias',1, inplace=True)
    print(dd)
    #result = list(getGroupAllNicknameList())




    #groupAllNicknameList = list(getGroupAllNicknameList())
    # print(len(groupAllNicknameList))
    # # print(type(groupAllNicknameList))
    # # #
    # with open("d.txt",'w') as f:
    #     for i in sorted(groupAllNicknameList):
    #         f.write(i)
    #         f.write("\n")



    # for i in groupAllNicknameList:
    #     #print(i['UserName'])
    #     print(i)
        #print(i['RemarkName'])
