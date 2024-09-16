Feature: User API. Verify the GET PUT POST DELETE methods of User API

  Scenario: Get Account ID for single user
    Given a request url https://parabank.parasoft.com/parabank/services/bank
    When User sends Account ID "15231"
    Then User verifies the status code is "200"
    And User verifies "Get Account ID" response contains following information




