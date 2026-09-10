Feature : Recruitment

  Scenario : Navigate to recruitment
    Given Navigates to url
    When User logs in with valid credentials and clicks Recruitment
    Then Should display Recruitment

  Scenario : Navigate to vacancies
    Given Opens login page
    When User logs in as "Admin", goes to Recruitment module, and clicks Vacancies
    Then Should display "Vacancies"

  Scenario : Open add candidate form
    Given Opens login page
    When User logs in as "Admin", goes to Recruitment module, and clicks Add
    Then Should display "Add Candidate"

  Scenario : Add candidate required field validation
    Given Opens login page
    When User logs in as "Admin", goes to Recruitment module, clicks Add, and clicks submit
    Then Required message should be displayed

  Scenario : Reset Recruitment filter
    Given Opens login page
    When User logs in as "Admin", goes to Recruitment module, selects a Job Title, and clicks reset
    Then Job Title should display "-- Select --"