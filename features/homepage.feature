Feature: Actions on Parabank home page. Demonstrating some assertion and scooping methods

  Scenario: User observes Parabank logo on home page
    Given User has navigated to the home page website
    When User has loaded home page
    Then User observes logo


  Scenario: User navigates to home page, clicks on header products category button and is redirected to the products page
    Given User has navigated to the home page website
    When User clicks on products category button in the header
    Then User is redirected to the products page URL and observes products page content

  Scenario: User clicks on news article link on main page in the latest news and is redirected to the corresponding news page
    Given User has navigated to the home page website
    When User clicks on "Parabank is now re-opened" button
    Then User is redirected to the "Parabank is now re-opened" and observes news content

  Scenario: User logs into user account
    Given User has navigated to the home page website
    When User enters login details
    Then User is redirected to the Account overview page