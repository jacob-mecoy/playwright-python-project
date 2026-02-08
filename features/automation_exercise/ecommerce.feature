Feature: E-commerce

    Background: Sign in
        Given I navigate to the homepage
        And I navigate to the signup login page
        And I sign in

    Scenario: Place an order whilst logged in
        Given I add a product to my basket
        And I navigate to the cart
        When I place the order
        Then I am taken to the Payment Screen
        When I input card details and confirm the order
        Then the order has been placed
        And I can download an invoice

    Scenario: Search for and add products to basket from products page
        Given I navigate to the products page
        And I search for product 'Blue Top'
        And I open the product details page for the only available product
        And I add 10 of the current product to my basket
        When I navigate to the cart via the modal
        Then there are 10 of 'Blue Top' in my basket