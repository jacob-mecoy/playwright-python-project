Feature: Rick And Morty API

# Characters API: /api/character - Test filters and individual character retrieval
# Location API: /api/location - Test location schema and individual location retrieval
# Episode API: /api/episode - Test episode schema and that there is at least 1 character present

    Scenario: Character API returns 826 characters
        Given I get all characters using the character API
        Then the response is ok
        And the response contains 826 characters

    Scenario: user can use the Character API to get a character by id
        Given I get a single character via id
        Then the response is ok
        And the response contains only 1 character 

    Scenario: user can use the Character API to get a character using filters
        Given I get characters that match specific filters
        Then the response is ok
        And the response contains 29 characters
