Feature : Admin

  Scenario : Navigate to admin
    Given   Navigates to url
    When    Clicks the login with valid credentials
    Then    Should display admin

  Scenario : Search a User in admin
    Given    Opens login page
    When     user logs in as "Admin", goes to Admin module, enters username "Admin", and clicks search
    Then     results should show "(1) Record Found"