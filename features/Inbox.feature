Feature: Inbox
  Background: 
    Given i've started listener service 

  Scenario: user wants to store a new input
    When i indicate that i want to store a new input
    Then the system should let me store it

  Scenario: user wants to store a empty input
    When i indicate that i want to store a new input
    Then the system should let me store it

