Feature: Login to MittiCool feature
    Scenario: User should be able to login
        Given User is on the signin page
        When  User enters valid username and password
        Then  User will be able to navigate to homepage
        Then  Close browser