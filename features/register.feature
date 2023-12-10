Feature: Register account functionality

  Scenario: Register with mandatory fields
    Given user navigated to Register page
    When user enter mandatory fields
    And clicks on continue button
    Then account should get created

  Scenario: Register with all fields
    Given user navigated to Register page
    When user enter all fields
    And clicks on continue button
    Then account should get created

  Scenario: Register with a duplicate email address
    Given user navigated to Register page
    When user enter all fields except email field
    And user enter existing accounts email into email field
    And clicks on continue button
    Then proper warning message informing about duplicate account should be displayed

  Scenario: Register without providing any details
    Given user navigated to Register page
    When user dont enter anything into all fields
    And clicks on continue button
    Then proper warning message for every mandatory fields should be displayed
