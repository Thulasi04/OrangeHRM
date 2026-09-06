Feature: Login

 Scenario : User successfully logs in with valid credentials
    Given     go to url
    When      enter username "Admin"
    And       enter password "admin123"
    Then      header should display "Dashboard"

 Scenario : User attempts login with invalid username
    Given go to url
    When enter username "InvalidUser"
    And enter password "admin123"
    Then error message should display "Invalid credentials"

  Scenario: User attempts login with invalid password
    Given go to url
    When enter username "Admin"
    And enter password "WrongPassword123"
    Then error message should display "Invalid credentials"

  Scenario: User submits empty credentials
    Given go to url
    When click login button
    Then validation error should display "Required"

  Scenario: User navigates to reset password page
    Given go to url
    When click forgot password link
    Then header should display "Reset Password"

2.Feature : Admin

Scenario : Navigate to admin
Given    : Navigates to url
When     : Clicks the login with valid credentials
Then     : Should display admin

Scenario : Search a User in admin
Given    : Opens login page
When     : user logs in as "Admin", goes to Admin module, enters username "Admin", and clicks search
Then     : results should show "(1) Record Found"


