class Base(object):
    def __repr__(self):
        return '%r' % self.__dict__

    def __eq__(self, other):
        """
        override __eq__ to support == operator for object comparison
        :param other:
        :return:
        """
        if not isinstance(other, self.__class__):
            return False

        for key, value in self.__dict__.items():
            if value != other.__getattribute__(key):
                return False

        return True

    def __ne__(self, other):
        """
        override __ne__ to support != operator for object comparison
        :param other:
        :return:
        """
        return not self == other


class Container(Base):
    """Class to contain runtime attributes"""
    pass


class AppInfo(Base):
    app_env = None
    app_product = None
    app_platform = None
    app_job = None
