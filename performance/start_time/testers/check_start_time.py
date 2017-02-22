from ptest.decorator import TestClass, Test, BeforeMethod
from ptest.plogger import preporter
from testhelpers.adb_helper import *
from testhelpers.jenkins_helper import Build_jenkins
from enumeration import *
from globals import *
from datastruct import *
from testhelpers.graph import *

MAX_TIME=2
cold_start={}
hot_start={}

@TestClass(run_mode='singleline')
class ANDROIDSTARTTIME:

    @Test()
    def check_android_start_time(self):
        if find_devices():
            print(get_device_state().decode().strip())

            if get_device_state().decode().strip() == "device":
                device_information = """
                device id: {}
                device model: {}
                android version: {}
                sdk version: {}
                """.format(get_device_id().decode().strip(), get_device_model().decode().strip(),
                           get_android_version().decode().strip(), get_sdk_version().decode().strip())
                print(device_information)

                # Download apk
                Build_jenkins().download_build()

                build_information = """
                product:{}
                env:{}
                type:{}
                build_url:{}
                """.format(Product.to_name(current_app_info.app_product), current_app_info.app_env,
                           current_app_info.app_type, Build_jenkins().get_build_info())

                print(build_information)

                # install apk
                url, apk_name = Build_jenkins().get_build_info()
                print(apk_path + apk_name)
                if find_apks(apk_path + apk_name):
                    print("prepare to install {}".format(apk_path + apk_name))
                    install_apks(apk_path + apk_name)
                else:
                    print("please check your folder")

            else:
                print("status is wrong!")


        else:
            print("please connect device!")

        colde_test = check_start_time(Product.to_start_page(current_app_info.app_product))
        hot_test = check_start_time(Product.to_start_page(current_app_info.app_product))
        uninstall_apks(Product.to_package(current_app_info.app_product))

        print(colde_test.decode().strip())
        print(hot_test.decode().strip())
        return colde_test,hot_test




    @Test()
    def check_android_start_time_and_draw(self):
        for i in range(MAX_TIME):
            colde_test, hot_test=self.check_android_start_time()
            cold_start[i] = colde_test.decode().strip()
            hot_start[i] = hot_test.decode().strip()

        draw_bar(cold_start, "cold start time")
        draw_bar(hot_start, "hot start time")



