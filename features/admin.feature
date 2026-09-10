Feature : Admin

  Scenario : Navigate to admin
    Given Navigates to url
    When Clicks the login with valid credentials
    Then Should display admin

  Scenario : Search a User in admin
    Given Opens login page
    When User logs in as "Admin", goes to Admin module, enters username "Admin", and clicks search
    Then Results should show "(1) Record Found"

  Scenario : Add user role
    Given Opens login page
    When User logs in as "Admin", goes to Admin module, selects User Role "ESS", and clicks search
    Then Results should show "ESS"

  Scenario : Reset user role filter
    Given Opens login page
    When User logs in as "Admin", goes to Admin module, selects User Role "ESS", and clicks reset
    Then User Role should display "-- Select --"

  Scenario : Search invalid username in admin
    Given Opens login page
    When User logs in as "Admin", goes to Admin module, enters invalid username "InvalidUser99999", and clicks search
    Then Results should show "No Records Found"