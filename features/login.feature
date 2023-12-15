Feature: Login functionality

  Scenario: Login with valid credentials
    Given user navigated to Login page
    When user entered valid credentials "sainadhreddy@gmail.com" and "sainadh@123"
    And clicks on Login button
    Then user should get logged in

  Scenario: Login with invalid credentials
    Given user navigated to Login page
    When user entered invalid credentials
    And clicks on Login button
    Then user should get a proper warning message

  Scenario: Login with valid email and invalid password
    Given user navigated to Login page
    When user enter valid email and invalid password
    And clicks on Login button
    Then user should get a proper warning message

  Scenario: Login with valid email and invalid password
    Given user navigated to Login page
    When user enter valid email and invalid password
    And clicks on Login button
    Then user should get a proper warning message

  Scenario: Login with invalid email and valid password
    Given user navigated to Login page
    When user enter invalid email and valid password
    And clicks on Login button
    Then user should get a proper warning message

  Scenario: Login without entering any credentials
    Given user navigated to Login page
    When user dont enter anything in email and password fields
    And clicks on Login button
    Then user should get a proper warning message
