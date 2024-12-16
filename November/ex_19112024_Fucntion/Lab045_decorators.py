def ui_visiblity(func):
    def before():
        print("Connect the device to test suite")
        print("Run the test suite")
        print("go to a app and take the screenshot for varification")
        func()
        print("Compare the screenshot with ref image")
        print("Quite the test suite once done")
    return before()


@ui_visiblity
def test_ui_visiblity():
    print(" This test case for UI visiblity test cases")