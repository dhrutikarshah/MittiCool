Feature: Add to Cart & Checkout feature
    Scenario: Add an item to cart and checkout

        Given User is on the product listing page
        When User selects a product
        And User clicks add to cart button
        Then Cart should display the selected product
        Then User clicks proceed to checkout
        Then Place order on checkout page




