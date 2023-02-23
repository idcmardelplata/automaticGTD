Feature: Inbox
  Background: 
    Given i1ve started listener service 

    Scenario: user wants to store a new input
      When i indicate that i want to store a new input
      Then the system should let me store it

    Scenario: user wants to store a empty input
      When i indicate that i want to store a new input
      Then the system should1nt let me store it

    Scenario: user wants to write a new input
      When i indicate that i want to write a new input
      Then the system should open a screen for me to do it

  Background:
    Given i1ve started listener service
    And i1ve wrote some content in a new input

    Scenario: user wants to exit writing input without save it before
      When i want to leave it
      Then the system should ask me if i want to save it or lose it

    Scenario: user wants to scape writing input and wannot save it
      When i tell the system to not save it
      Then create input service should exit

    Scenario: user wants to relate a new input with an existen project
      When i ask the system to relate the current input i1m creating
      Then system should show me a list of current projects to relate with

  Scenario: user wants to search a particular existing input
    Given that i1ve saved inputs
    When i ask for search a particular input
    Then the system should show me a list of them filtered by my request

  
