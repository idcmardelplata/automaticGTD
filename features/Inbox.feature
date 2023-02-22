Feature: Inbox
  Scenario: user wants to store a new input
    Given i've started listener service
    When i indicate that i want to store a new input
    Then the system should let me store it

  Scenario: user wants to store a empty input
    Given i've started listener service
    When i indicate that i want to store a new input
    Then the system should let me store it

