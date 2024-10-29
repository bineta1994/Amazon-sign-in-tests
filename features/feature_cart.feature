Feature: Verify cart functionality on Target.com

  Scenario: User clicks on the cart icon and sees an empty cart message
    Given I open "https://www.target.com"
    When I click on the cart icon
    Then I should see the message "Your cart is empty"


Feature: Verify Sign In functionality on Target.com

  Scenario: Logged out user navigates to Sign In page
    Given I open "https://www.target.com"
    When I click on "Sign In"
    And I click on the "Sign In" option from the right-side navigation menu
    Then the Sign In form should be displayed


