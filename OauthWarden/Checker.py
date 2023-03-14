from OauthWarden import warden

def test_check_token():
    # create a test token file
    with open("tokens.txt", "w") as f:
        f.write("this is a test")

    # call the function to check the test file
    warden.checktoken("tokens.txt")

    # delete the test file after the check is complete
    os.remove("tokens.txt")
