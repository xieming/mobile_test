from ptest.decorator import TestClass, Test, BeforeClass
from ptest.plogger import preporter
from get_blurbs import REQUEST, get_ids
from translation import LANGUAGES, Translate

@TestClass()
class Content:
    @BeforeClass()
    def setup_data(self):
        self.levels = [20000507, 20000524, 20000525, 20000526, 20000527, 20000547, 20000548, 20000549, 20000550, 20000585, 20000599, 20000600, 20000608, 20000609, 20000610, 20000611]


    @Test()
    def check_tranlstaltes(self):
        study_context_id = get_ids(REQUEST().get_response("studycontext"))
        course_structure_id = []
        for level in self.levels:
            course_structure_id.append(get_ids(REQUEST().get_response("coursestructure",level=level)))

        Translate().get_final_check(ids=study_context_id)
        Translate().get_final_check(ids=course_structure_id)


