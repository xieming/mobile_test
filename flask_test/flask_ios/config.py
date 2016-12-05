class Environment:
    def get_host(self, current_host):
        host = {
            "UAT":"mobilefirst.englishtown.com",
            "QA": "qa.englishtown.com",
            "STAG": "staging.englishtown.com",
        }[current_host]
        return host


