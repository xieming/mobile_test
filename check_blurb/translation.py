import langid
import numpy as np
import pandas as pd
import requests

LANGUAGES = ['ar', 'de', 'en', 'es', 'fr', 'it', 'ja-JP', 'ko-KR', 'pt-BR', 'ru', 'th', 'tr-TR', 'zh-cn', 'zh-HK',
             'zh-TW']
ID = ['699126', '699124', '669751', '647306', '697256', '647306']
host = "mobilefirst"
url = "http://{}.englishtown.com/services/school/query?q=blurb!{}&c=culturecode={}"

<<<<<<< HEAD
list_obj = {}
=======
list_obj = []
>>>>>>> ba04dda4cf91056bd49e265afc7e7491ae6c8242


class Translate():
    def get_translated_string(self, blurb_id, language_code):
        response = requests.post(url.format(host, blurb_id, language_code))
        value = (response.json())[0]['translation'].strip()
        # print(value)
        return value

    def check_language(self, target, language):
        lineTuple = langid.classify(target)  # 调用langid来对该行进行语言检测
        if "-" in language:
            language = language.split("-")[0]
        if lineTuple[0] != language:
            return False
        else:
            return True


<<<<<<< HEAD
    def get_final_check(self,ids=ID):

        translated = (self.get_translated_string(x, y) for x in ids for y in LANGUAGES)

        translated_list = np.array(list(translated)).reshape(len(ids), len(LANGUAGES))

        translated_dataframe = pd.DataFrame(translated_list, index=ids, columns=LANGUAGES)

        check_dataframe = translated_dataframe.copy()

        # print(translated_dataframe)
        writer = pd.ExcelWriter('translated_blurbs.xlsx')
        translated_dataframe.to_excel(writer, 'all_translated')



        for ix, row in check_dataframe.iterrows():
            for col_name in check_dataframe.columns:
                # print("\n")
                # print (row[col_name])
                if not self.check_language(row[col_name], col_name):
                    list_obj[ix]= col_name


        translate_not = pd.Series(list_obj)
        print(translate_not)
        translate_not.to_csv("blurb_not_translation.csv")



# def main():
#     # translate = get_translated_string(ID[1], LANGUAGES[7])
#     # check_language(translate, LANGUAGES[7])
#     # #check_language(translate, LANGUAGES[1].split("-")[0])
#     # # translate_list = list(translate)
#     # # translate_array = np.array(translate)
#     # # print(translate_array.data)
#     # # # translate_frame = pd.DataFrame(translate_array,index=ID, columns=LANGUAGES)
#     # # # print(translate_frame)
#     translate = Translate()
#     translated = (translate.get_translated_string(x, y) for x in ID for y in LANGUAGES)
#
#     translated_list = np.array(list(translated)).reshape(len(ID), len(LANGUAGES))
#
#     translated_dataframe = pd.DataFrame(translated_list, index=ID, columns=LANGUAGES)
#
#     check_dataframe = translated_dataframe.copy()
#
#     # print(translated_dataframe)
#     writer = pd.ExcelWriter('translated_blurbs.xlsx')
#     translated_dataframe.to_excel(writer, 'all_translated')
#
#
#
#     for ix, row in check_dataframe.iterrows():
#         for col_name in check_dataframe.columns:
#             # print("\n")
#             # print (row[col_name])
#             if not translate.check_language(row[col_name], col_name):
#                 list_obj.append(ix + ":" + col_name)
#
#
#     translate_not = pd.Series(list_obj)
#     print(translate_not)
#     translate_not.to_csv("blurb_not_translation.csv")
#
#
#
#
# if __name__ == "__main__":
#     main()
=======
def main():
    # translate = get_translated_string(ID[1], LANGUAGES[7])
    # check_language(translate, LANGUAGES[7])
    # #check_language(translate, LANGUAGES[1].split("-")[0])
    # # translate_list = list(translate)
    # # translate_array = np.array(translate)
    # # print(translate_array.data)
    # # # translate_frame = pd.DataFrame(translate_array,index=ID, columns=LANGUAGES)
    # # # print(translate_frame)
    translate = Translate()
    translated = (translate.get_translated_string(x, y) for x in ID for y in LANGUAGES)

    translated_list = np.array(list(translated)).reshape(len(ID), len(LANGUAGES))

    translated_dataframe = pd.DataFrame(translated_list, index=ID, columns=LANGUAGES)

    check_dataframe = translated_dataframe.copy()

    # print(translated_dataframe)
    writer = pd.ExcelWriter('translated_blurbs.xlsx')
    translated_dataframe.to_excel(writer, 'all_translated')



    for ix, row in check_dataframe.iterrows():
        for col_name in check_dataframe.columns:
            # print("\n")
            # print (row[col_name])
            if not translate.check_language(row[col_name], col_name):
                list_obj.append(ix + ":" + col_name)


    translate_not = pd.Series(list_obj)
    print(translate_not)
    translate_not.to_csv("blurb_not_translation.csv")




if __name__ == "__main__":
    main()
>>>>>>> ba04dda4cf91056bd49e265afc7e7491ae6c8242
