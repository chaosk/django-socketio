Scenario: Create a room
    Given I open the example project

    When I create a new room called test
    And I submit the form
    And I go to the homepage

    Then I should see the room test in the rooms list
