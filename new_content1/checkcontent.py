import json
from multiprocessing import Pool

import pandas as pd
import requests
from ptest.decorator import TestClass, Test, BeforeClass, AfterMethod

from getcontent import LevelActivityStructure, ActivityJsonStructure
from getcontent import media_url_list, THREAD_COUNT_FOR_CHECK_URL, check_resource, write_result_report, \
    fail_media_url_list, asr_error
from globals import *


@TestClass()
class Content:
    @BeforeClass()
    def setup_data(self):
        # get sessionid and token
        login_post = requests.session().post(url=HOST + LOGIN_PATH, json=LOGIN_PARAMS)
        result = login_post.json()
        self.session_id = result["serviceResponse"]["sessionId"]
        self.token = result["serviceResponse"]["token"]

        print("start to get levels, please wait for a moment-------")

        if SPIN == 'True':
            type = "be"

        else:
            type = "ge"

        level_http = LevelActivityStructure(self.session_id, self.token, type)
        level = level_http.get_levels()
        print(level)

        if not os.path.exists('%s_activity.xlsx' % (PRODUCT)):

            writer = pd.ExcelWriter('%s_activity.xlsx' % (PRODUCT))
            for i in range(len(level)):
                result = level_http.get_activity(level[i])
                get_ids = pd.DataFrame(result)
                get_ids.to_excel(writer, "%d" % (i))

        else:
            pass

    @Test()
    def check_content(self):
        if os.path.exists("%s_activity.xlsx" % (PRODUCT)):
            for i in range(16):
                id_reader = pd.read_excel("%s_activity.xlsx" % (PRODUCT), sheetname=[i], index_col=None)

                level_table = id_reader[i]

                def get_activity(x):
                    for i in range(4):
                        activity_string = x.get(i).replace("[", "").replace("]", "").replace(" ", "")

                        jsonfile = ActivityJsonStructure(self.session_id, self.token).get_json(
                            activity_string.split(","))
                        ActivityJsonStructure(self.session_id, self.token).get_url(json.dumps(jsonfile))

                        if ASR == 'True':
                            ActivityJsonStructure(self.session_id, self.token).get_asr(activity_string.split(","),
                                                                                       json.dumps(jsonfile))

                level_table.apply(get_activity, axis=1)

            print(len(media_url_list))
            pool = Pool(THREAD_COUNT_FOR_CHECK_URL)
            pool.map(check_resource, list(media_url_list))
            pool.close()
            pool.join()

            write_result_report(fail_media_url_list)

            print("-----------scan finished-----------")

            if (len(fail_media_url_list) + len(asr_error)) > 0:
                print("Finished! total error number is: %s" % (len(fail_media_url_list) + len(asr_error)))

            else:
                print("no error found!")

        else:
            print("no file exist, please check!")

    @AfterMethod()
    def clear_files(self):

        try:
            os.remove(current_dir + "/" + '%s_activity.xlsx' % (PRODUCT))

        except Exception as e:
            print("Error occur: {}".format(e))
