# default is uat

def set_env(env):
    admin = {
        "uat": "SMobile",
        "qa": "SMobile1",
        "staging": "SMobile",
    }[env]

    host = {
        "uat": "mobilefirst",
        "qa": "qa",
        "staging": "staging"
    }[env]

    return host,admin


class Teacher():
    def current_teacher(self, env,teacherid):
        if env =="uat":
            teacher = {
                "A": "23788715,AMobile4",
                "B": "23788716,BMobile",
                "C": "23788717,CMobile1",
                "D": "23788718,DMobile1"
            }[teacherid]


        elif env =="qa":
            teacher = {
                "A": "10708789,AMobile1",
                "B": "10708791,BMobile",
                "C": "10708792,CMobile"
            }[teacherid]


        elif env == "staging":
            teacher = {
                "A": "14830955,AMobile1",
                "B": "14830956,BMobile",
                "C": "14830957,CMobile1"
            }[teacherid]
        return teacher
