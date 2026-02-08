Feature: Rick and Morty UI

    Background:
        Given I navigate to the homepage
    
    Scenario: Navigate to homepage
        Then the homepage is loaded

    Scenario: Unique characters show on homepage
        Then there are 6 characters shown
        And the characters are all unique

    Scenario: Navigate to documents page
        Given I navigate to the documents page
        Then the documents page is loaded

    Scenario: Navigate to about page
        Given I navigate to the about page
        Then the about page is loaded