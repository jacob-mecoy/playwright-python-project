Feature: E-commerce

    Scenario: Place an order whilst logged in
        Given I navigate to the homepage
        And I navigate to the signup login page
        And I sign in
        And I add a product to my basket
        And I navigate to the cart
        When I place the order
        Then I am taken to the Payment Screen
        When I input card details and confirm the order
        Then the order has been placed
        And I can download an invoice