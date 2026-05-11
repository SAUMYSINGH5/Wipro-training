Feature: Signup Functionality

  Scenario: Successful Signup

    Given User launches Demoblaze application
    When User clicks on Sign up menu
    And User enters signup username "user"
    And User enters signup password "pwdaaaaa"
    And User clicks Signup button
    Then User should see signup success message