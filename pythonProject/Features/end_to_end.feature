Feature: Test end to end MittiCool flow
  Scenario: User should be able to login
        Given User is on the signin page
        When  User enters valid username and password
        Then  User will be able to navigate to homepage
        Then  Close browser

    Scenario: Add an item to cart and checkout
        Given User is on the product listing page
        When User selects a product
        And User clicks add to cart button
        Then Cart should display the selected product
        Then User clicks proceed to checkout
        Then Place order on checkout page
        Then  Close browser