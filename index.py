from components.scrab import Scrab


class MainApp:

    def searchSomething(self):
        xexist = Scrab()
        xexist.validateFileDriver()
        print(xexist)

    


if __name__ == '__main__':
    execdef = MainApp()
    execdef.searchSomething()
