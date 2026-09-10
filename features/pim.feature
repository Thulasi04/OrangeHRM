Feature : PIM

  Scenario : Navigate to PIM
    Given Navigates to url
    When User logs in with valid credentials and clicks PIM
    Then Should display PIM

  Scenario : Search employee by employee ID
    Given Opens login page
    When User logs in as "Admin" and goes to PIM module
    Then Should navigate to PIM module

  Scenario : Navigate to Add Employee
    Given Opens login page
    When User logs in as "Admin", goes to PIM module, and clicks Add Employee
    Then Should display "Add Employee"

  Scenario : Add employee required field validation
    Given Opens login page
    When User logs in as "Admin", goes to PIM module, clicks Add Employee, and clicks submit
    Then Required message should be displayed

  Scenario : Reset PIM search filter
    Given Opens login page
    When User logs in as "Admin", goes to PIM module, enters employee ID "0421", and clicks reset
    Then Employee ID field should be empty