Feature: add and delete products to the cart

  Scenario Outline: add and delete products from Amazon page to the cart
    Given the user is at "<home_page>"
    When user search a new "<product>"
    And sort by "<index>" order the list
    And add the product
    Then delete de product
    Examples: data
    |product        |index|home_page                   |
    |iphone 14 pro  |  1  |https://www.amazon.com/-/es/|
    |washing machine|  2  |https://www.amazon.com/-/es/|