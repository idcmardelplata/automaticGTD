class Dependency(object):

    __instance = None

    def __new__(cls):
        if Dependency.__instance is None:
            Dependency.__instance = object.__new__

        return Dependency.__instance

if __name__ == "__main__":

    print("this's a singleton class mate whoa there")

