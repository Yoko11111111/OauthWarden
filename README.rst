####################
    OauthWarden V1
####################

**********
 Overview
**********

This is an twitch api wrapper and scraper written in python that u can use to build simple scripts fast.

*******
 Usage
*******

Requirements
============

-  Python: Version 3.9, 3.10, 3.11
-  Python Package: Requests, Colorama

Installation
============

There will be an package on the pypi page. But you can also
install it from source code, but also like any other
Python program it can be installed via the normal ``pip install OauthWarden`` routine.

*******
Examples
*******

Token Checker
============

.. code:: python

    from OauthWarden import warden

    def test_check_token():
        # create a test token file
        with open("tokens.txt", "w") as f:
            f.write("this is a test")

        # call the function to check the test file
        warden.checktoken("tokens.txt")

        # delete the test file after the check is complete
        os.remove("tokens.txt")
    
Bio Changer
============

soon

*******
Updates
*******

We will try our best to release new versions and fixes as soon as possible please stay patient..
If you want to support our Project please give our repo an star
