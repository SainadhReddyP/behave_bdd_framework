Feature: Search functionality

  Scenario: Search for a valid product
    Given user navigated to Home page
    When user enter valid product say "HP" into the search box
    And user clicks on search button
    Then valid product should get displayed in search results

  Scenario: Search for an invalid product
    Given user navigated to Home page
    When user enter invalid product say "DELL" into the search box
    And user clicks on search button
    Then proper message should be displayed in search results

  Scenario: Search without entering any product
    Given user navigated to Home page
    When user dont enter anything into search box
    And user clicks on search button
    Then proper message should be displayed in search results