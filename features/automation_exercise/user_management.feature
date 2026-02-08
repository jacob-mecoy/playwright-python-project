Feature: User management

    Background: 
        Given I navigate to the homepage

    Scenario: Navigate to homepage
        Then the homepage loads successfully
    
    Scenario: Register a user
        Given I navigate to the signup login page
        And I enter initial signup info
        And I enter the remaining signup information
        When I create the user account
        Then I expect a confirmation message to be displayed
        When I choose to continue
        Then I am returned to the homepage

    Scenario: Login as existing user
        Given I navigate to the signup login page
        When I sign in
        Then I am returned to the homepage
        And the homepage shows I am logged in
