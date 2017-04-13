import json
import re

from submitscore_helper import SubmitScoreHelperV1


class PassLevelForEcV1:
    def __init__(self, host, level, username, level_test=True):

        self.level = level
        self.username = username
        self.level_test = level_test
        self.score_help_v1 = SubmitScoreHelperV1(host)

    def get_course_ids(self):

        levels_page = self.score_help_v1.load_student_information(self.username)
        print(levels_page)
        match_course = levels_page.split('$')
        print(match_course)
        member_information = match_course[0].split('|')
        member_id = member_information[3]
        partner = member_information[4]
        print(partner)
        level1 = member_information[5]
        match_course.pop(0)
        course_lists = []

        for list in match_course:
            matched_course = re.search(r'#(\d{3})', str(list))

            if matched_course:
                course_lists.append(matched_course.group(1))

        course_lists.insert(0, level1)
        print(course_lists)
        print("get course done")
        course_id = course_lists[self.level]
        return member_id, course_id, partner

    def get_unit_ids(self):
        member_id, course_id, partner = self.get_course_ids()
        unit_page = self.score_help_v1.load_unit_list(course_id, member_id)
        print(unit_page)
        unit_list = unit_page.split('$')
        print(unit_list)
        units = []

        for unit in unit_list:
            unit_matched = re.search(r'\d{4}', str(unit))

            if unit_matched:
                units.append(unit_matched.group(0))
            else:
                pass

        print(units)
        print("get units done")
        return units

    def pass_level_test(self):
        member_id, course_id, partner = self.get_course_ids()

        if self.level_test == True:
            searched_units = self.get_unit_ids()
        else:
            searched_units = self.get_unit_ids()[0:6]

        for unit_id in searched_units:
            progress_page = self.score_help_v1.show_unit_list_progress(member_id, course_id, unit_id)
            print(progress_page)
            progress_json = json.loads(progress_page)
            print(progress_json['Lessons'])
            lessons = str(progress_json['Lessons'])
            matched_activity = re.compile(r"'Activities':\s\[(.*?)\]")
            matched_activity_id = re.compile(r"'ID':\s(\d+),")
            activity_id = re.findall(matched_activity, lessons)
            print(activity_id)
            activity_list = []

            for id in activity_id:
                activity = re.findall(matched_activity_id, id)
                activity_list.append(activity)
                print(activity_list)

            activity_listed = str(activity_list).replace('[', '').replace(']', '')
            activity_listed = activity_listed.replace('\'', '')
            print(activity_listed)

            submit_page = self.score_help_v1.save_activity_score(member_id, course_id, unit_id,
                                                                 activity_listed,
                                                                 partner)
            print(submit_page)
            progress_page = self.score_help_v1.show_unit_list_progress(member_id, course_id, unit_id)
            print(progress_page)
            print("Done!")
