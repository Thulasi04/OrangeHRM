Feature : Leave

  Scenario : Navigate to leave
    Given Navigates to url
    When User logs in with valid credentials and clicks Leave
    Then Should display Leave

  Scenario : Navigate to Apply Leave
    Given Opens login page
    When User logs in as "Admin", goes to Leave module, and clicks Apply
    Then Should display "Apply Leave"

  Scenario : Apply Leave required field validation
    Given Opens login page
    When User logs in as "Admin", goes to Leave module, clicks Apply, and clicks submit
    Then Required message should be displayed

  Scenario : Navigate to My Leave
    Given Opens login page
    When User logs in as "Admin", goes to Leave module, and clicks My Leave
    Then Should display "My Leave List"

  Scenario : Reset Leave search filter
    Given Opens login page
    When User logs in as "Admin", goes to Leave module, selects Sub Unit "Engineering", and clicks reset
    Then Sub Unit should display "-- Select --"