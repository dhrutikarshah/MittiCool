Feature: Mitticool logo
    Scenario: Logo present
        Given Launch web browser
        When  View mitticool home page
        Then  Check logo is present on homepage
        And   Close browser
