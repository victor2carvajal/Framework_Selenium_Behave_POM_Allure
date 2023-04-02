Feature: add and delete products to the cart

  Scenario: add and delete products from Amazon page to the cart
    Given the user is at home page
    When user search a new product
    And sort by decent order the list
    And add the product
    Then delete de product