# Created by nhousllc at 3/31/25
Feature: Cart Page Feature
  # Enter feature description here

  Scenario: Verify cart is empty
    Given Open target.com
    When Click on cart icon
    Then Verify "Your Cart is empty" message is shown


