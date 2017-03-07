Feature: Search Sorted Sets For A Specified Value

  Scenario: Empty sets result in a -1
    Given an empty set is passed in
    When I attempt to find the specified value
    Then I should get a -1 response