# Testing
## Testing Features
#### Header - General User
| Feature | Expectation | Action | Result |
| ---| ---| ---| ---|
| Logo | Clicking the logo takes the user back to the home page. | Started on All Products page. Then clicked the logo. | Taken back to the home page. |
| Home link | Text italicises when hovered over. Takes user back to Home Page. | Started on the All Products page. Hovered over the link. Then clicked the link. | Text italicised when hovered over. Taken back to Home Page when clicked. |
| All link | Text italicises when hovered over. Clicking it shows a dropdown menu with 'By Price', 'By Category' and 'All Products'. Clicking 'By Price' displays all of the products in increasing price order. Clicking 'By Category' shows all of the products in alphabetical order of their categories. Clicking 'All Products' shows all of the items. | Hovered over the link. Then clicked the 'By Price', 'By Category' and 'All Products' links. | Text italicised when hovered over. Clicking 'By Price' displayed all of the products in increasing price order. Clicking 'By Category' showed all of the products in alphabetical order of their categories. Clicking 'All Products' showed all of the items. |
| Earrings, Bracelets, Necklaces and Rings links | Text italicises when hovered over. Clicking each of these links displays a dropdown menu with Gold '*item name*', Silver '*item name*', and All '*item name*'. Clicking on Gold '*item name*' displays all of the gold items of that type. Clicking on Silver '*item name*' displays all of the silver items of that type. Clicking All '*item name*' displays all of the items of that type. | Hovered over the link. Then clicked the Gold '*item name*', Silver '*item name*', and All '*item name*' links. | Text italicised when hovered over. Clicking on Gold '*item name*' displayed all of the gold items of that type. Clicking on Silver '*item name*' displayed all of the silver items of that type. Clicking All '*item name*' displayed all of the items of that type. |
| Profile icon | Clicking the icon displays a dropdown menu with 'Register' and 'Login' links. Clicking 'Register' takes the user to the sign up page. Clicking login takes the user to the login page. | Clicked the 'Register' link, then clicked the 'Login' link. | Taken to the sign up page after clicking 'Register'. Taken to the login page after clicking 'login'. |
| Search icon | Displays a search bar when clicked. If a product is found matching the searched word it will be displayed, alongside the number of products matching the searched word. If not, no products will be displayed. If a blank search is entered, an error message will appear and the user will be taken to the All Products page. | Clicked the icon. Then entered the word 'gold'. Then entered the word 'test'. Then entered a blank search. | Search bar appeared. 26 products were found for 'gold' and these were displayed. 0 products were found for 'test'. Entereing a blank search resulted in an error message appearing stating 'You didn't enter an search criteria'. Taken to the All Products page. |
| Wishlist icon | Clicking the icon takes the unregistered user to the login page. | Clicked the icon. | Taken to the login page. |
| Bag icon | Clicking the icon takes the user to the bag page. | Clicked the icon. | Taken to the bag page. |
| Mobile view | All links apart from the search, wishlist and bag icons appear in a hamburger menu. Clicking this menu displays all the other links which function as above. | Clicked the mobile hamburger menu. | The menu appeared with all of the other links. Clicking each of these links displayed the same dropdown menus as above. |

#### Header - Signed in User
| Feature | Expectation | Action | Result |
| ---| ---| ---| ---|
| Profile icon | User's profile name appears next to this icon. Clicking the icon displays the 'My Profile' and 'Logout' links. Clicking 'My Profile' takes the user to their profile page. Clicking 'Logout' takes the user to the logout page. | Signed in as Jim1. Clicked the icon. Clicked each of the links. | 'Jim1 appeared next to the profile icon'. Clicking the icon displayed the 'My Profile' and 'Logout' links. Taken to the profile page after clicking the 'My Profile' link. Taken to the logout page after clicking 'Logout'. |
| Wishlist icon | Clicking the icon takes the user to their wishlist page. | Clicked the icon. | Taken to the wishlist page. |

#### Header - Admin Member
| Feature | Expectation | Action | Result |
| ---| ---| ---| ---|
| Profile icon | Clicking the icon displays the 'Product Management' and 'Logout' links. Clicking 'Product Management' takes the user to the Add a product page. | Clicked 'Product Management'. | Taken to the Add product page. |

#### Footer
| Feature | Expectation | Action | Result |
| ---| ---| ---| ---|
| Home link | Text italicises when hovered over. Takes user back to Home Page. | Started on the All Products page. Hovered over the link. Then clicked the link. | Text italicised when hovered over. Taken back to Home Page when clicked. |
| Contact link | Text italicises when hovered over. Takes user back to Contact Us page. | Hovered over the link. Then clicked the link. | Text italicised when hovered over. Taken Contact Us Page when clicked. |
| Privacy Policy link | Text italicises when hovered over. Takes user to external privacy policy page. | Hovered over the link. Then clicked the link. | Taken to external privacy policy page in a new tab. |
| Subscribe link - correct inputs | When a valid email address that hasn't been used before is entered, a success message appears below the input box thanking the user for subscribing. | Entered a valid email address and pressed subscribe. | A success message appeared below the input box thanking the user for subscribing. |
| Subscribe link - already used email address | When a email address is used to subscribe again, a message appears below the input box informing the user that they are already subscribed. | Entered the same email address and pressed subscribe. | A message appeared below the input box informing the user that they are already subscribed. |
| Subscribe link - no inputs | Clicking subscribe will show an error message that the email field is required. | Clicked subscribe with no input. | Error message appeared below the input box that this field is required. |
| Subscribe link - invalid email address | Clicking subscribe will show an error message to enter a valid email address. | Clicked subscribe with just 'test' as the input. | Error message appeared below the input box to enter a valid email address. |
| Social media icons | Clicking each of the icons will open them to their respective websites (Facebook, Instagram or Twitter) in new tabs. | Clicked each of the icons. | Each social media website opened up in a new tab. |

#### Home page
| Feature | Expectation | Action | Result |
| ---| ---| ---| ---|
| Shop Now button | Button changes colour when hovered over. Clicking it takes the user to the Products page. | Hovered over button then clicked it. | Button changed colour when hovered over. Clicking it took the user to the Products page. |

#### Products page - General User
| Feature | Expectation | Action | Result |
| ---| ---| ---| ---|
| Product image link | Clicking on a product image link takes the user to the product detail page for that product. | Clicked the product image. | Taken to the product detail page for that product. |
| Category link | Link underlines when hovered over. Clicking on the category link displays all of the items within that category. | Hovered over the category 'Gold Rings' link. Clicked the link. | Link underlined when hovered over. Taken to the page displaying all of the 'Gold Rings'. |
| Wishlist icon | Clicking the icon takes the user to the sign in page. After signing in the user is taken to the wishlist page where their added item will appear with a success message. | Clicked the icon. | Taken to the sign in page. Taken to the wishlist page after signing in where the added item appeared with a success message. |
| Back to top arrow | Button changes colour when hovered over. Clicking the button takes the user to the top of the page. | Hovered over button then clicked it. | Button changed colour when hovered over. Clicking the button takes the user to the top of the page. |
| Sorting - price low to high | Products are displayed in increasing price order. | Sorted the products from lowest price to highest. | Products displayed from lowest price to highest. |
| Sorting - price high to low | Products are displayed in decreasing price order. | Sorted the products from highest price to lowest. | Products displayed from highest price to lowest. |
| Sorting - name (A-Z) | Products are displayed in alphabetical order. | Sorted the products alphabetically by name. | Products displayed in alphabetical order. |
| Sorting - name (Z-A) | Products are displayed in reverse alphabetical order. | Sorted the products in reverse alphabetical order by name. | Products displayed in reverse alphabetical order. |
| Sorting - category (A-Z) | Products are displayed alphabetically by category. | Sorted the products alphabetically by category. | Products displayed in alphabetical order of category. |
| Sorting - cateory (Z-A) | Products are displayed in reverse alphabetical order by category. | Sorted the products in reverse alphabetical order by category. | Products displayed in reverse alphabetical order of category. |

#### Products page - Signed in User
| Feature | Expectation | Action | Result |
| ---| ---| ---| ---|
| Wishlist icon | Clicking the icon adds the item to their wishlist and takes them to the wishlist page. | Clicked the icon. | Item added to the wishlist and taken to the wishlist page. Success message appears informing the user that the item has been successfully added. |
| Solid wishlist icon | Clicking the icon removes the item from their wishlist and takes them to the wishlist page. | Clicked the icon. | Item removed from the wishlist and taken to the wishlist page. Success message appears informing the user that the item has been successfully removed. |

#### Products page - Admin member
| Feature | Expectation | Action | Result |
| ---| ---| ---| ---|
| Edit and delete buttons | Shown on each of the product cards. Buttons change colour when hovered over. | Hovered over buttons. | Buttons shown on each product card. Buttons changed colour when hovered over. |
| Edit product | Alert message appears informing the user that they are editing a product. Takes user to Edit a Product page. Clicking update will post the updated product and show its product detail page. Success message appears. | Clicked 'Edit'. Changed the price of the product. Clicked 'Update' | Alert message appeared. Taken to the Edit a Product page. Edited the price, then clicked 'Update'. Updated product product detail page was shown. Success message appeared. |
| Delete product | Confirm deletion modal appears. Clicking 'Delete' deletes the product. Success message appears. | Clicked 'Delete'. | Confirm deletion modal appeared. Product was deleted after clicking 'Delete'. Success message appeared. | 

#### Product detail page - General User
| Feature | Expectation | Action | Result |
| ---| ---| ---| ---|
| Wishlist icon | Clicking the icon takes the user to the sign in page. After signing in the user is taken to the wishlist page where their added item will appear with a success message. | Clicked the icon. | Taken to the sign in page. Taken to the wishlist page after signing in where the added item appeared with a success message. |
| Category link | Link underlines when hovered over. Clicking on the category link displays all of the items within that category. | Hovered over the category 'Gold Bracelets' link. Clicked the link. | Link underlined when hovered over. Taken to the page displaying all of the 'Gold Bracelets'. |
| Quantity (1-99) | Increment and decrement buttons change colour when hovered over. Decrement button is disabled when the quantity is one and the increment button is disabled when the quantity is 99. Clicking the + or - buttons either increases or decreases the quantity. | Hovered over buttons then clicked them. | Quantity increased when clicking + and decreased when clicking -. Decrement button was disabled when the quantity was one and the increment button was disabled when the quantity was 99. |
| Quantity (outside the range) | Inputting a quantity below 1 and then clicking Add to Bag results in a message informing that the value must be greater than or equal to 1. Inputting a quantity greater than 99 and then clicking Add to Bag results in a message informing that the value must be less than or equal to 99 | Inputted -5 then clicked Add to Bag. Then inputted 105 and clicked Add to Bag. | Received an error message that the value must be greater than or equal to or and then that the value must be less than or equal to 99. |
| Keep Shopping button | Button changes colour when hovered over. Clicking it takes the user to the Products page. | Hovered over button then clicked it. | Button changed colour when hovered over. Clicking it took the user to the Products page.
| Add to Bag button | Button changes colour when hovered over. Clicking it adds the item to the basket. A success message appears stating that the item was added to the bag. The success message also shows what is in the basket, how much more the user could spend to get free delivery and what the total excluding delivery is. There is also an icon to go straight to the checkout. The bag icon in the header shows the grand total beneath it and the counter shows how many items are in the basket. | Hovered over button then clicked it. | Button changed colour when hovered over. Clicking it added the item to the bag. The quantity on the bag icon in the header increased and the total price below the icon updated as well. A success message appeared stating that the item was added to the bag. The success message also showed what is in the basket, how much more to spend to get free delivery and what the total excluding delivery is. There was also a button to go straight to the checkout. |
| Reviews accordion | Clicking the reviews section reveals the reviews left below. If there are no reviews there is a message stating this. If there are reviews these are displayed below. | Clicked the reviews section. | The accordion opened up revealing either the reviews where there were some, or the message that there aren't any yet. |
| Sign in to leave a review link | Link size increases when hovered over. Clicking the link takes the user to the sign in page. After signing in the user is taken back to the product detail page. | Hovered over the link then clicked it. | Link size increased when hovered over. Taken to the sign in page after clicking the link. Taken back to the product detail page after signing in. |

#### Product detail page - Signed in User
| Feature | Expectation | Action | Result |
| ---| ---| ---| ---|
| Wishlist icon | Regular and solid icons function the same as on the products page. | Clicked the icon. | Regular and solid icons functioned the same as on the products page. |
| Leave a review button | Button changes colour when hovered over. Clicking it opens up the Leave a review modal. | Hovered over button then clicked it. | Button changed colour when hovered over. Clicking it opened up the Leave a review modal. |
| Leave a review modal | Button changes colour when hovered over. Clicking it opens up the Leave a review modal. Modal is fixed so clicking outside the box will not close the modal. Cancel and submit buttons change colour when hovered over. Clicking cancel or the cross takes the user back to the reviews. Clicking submit after writing a review posts the review with the current date. Success message appears after posting the review. | Hovered over button then clicked it. Hovered over the cancel and submit buttons. Clicked cancel. Clicked the cross. Clicked submit after writing a review. | Button changed colour when hovered over. Clicking it opened up the Leave a review modal. Modal was fixed so clicking outside the box will not close the modal. Cancel and submit buttons changed colour when hovered over. Taken back to the reviews after clicking cancel. Taken back to the reviews after clicking the cross. Review posted in the accordion with the current date after typing 'Great!' and pressing submit. Success message appeared after posting the review. |
| Leave a review - no input | Clicking submit with no content written will show a message to fill in the field. | Clicked submit with no content written. | Message shown to fill in the field. | 
| Edit and delete buttons | Only shown to the author of the review. Buttons change colour when hovered over. | Hovered over buttons. | Buttons only shown below the reviews that the author wrote. Buttons changed colour when hovered over. |
| Edit review | Modal appears again with the current review written. Clicking update will post the updated review with the reviews. Success message appears. | Clicked 'Edit'. Changed the text in the review. Clicked 'Update' | Current review was initially written in the text box. Edited the text, then clicked 'Update'. Updated review was posted with the reviews. Success message appeared. |
| Delete review | Confirm deletion modal appears. Clicking 'Delete' deletes the review. Success message appears. | Clicked 'Delete'. | Confirm deletion modal appeared. Review was deleted after clicking 'Delete'. Success message appeared. | 

#### Product detail page - Admin member
| Feature | Expectation | Action | Result |
| ---| ---| ---| ---|
| Edit and delete buttons | Buttons appear on all product detail pages. Function the same as on the Products page. | Clicked on a product to view its product detail page. | Buttons appear below details. Buttons function the same as on the Products page. |
| Delete review | Delete buttons appear on all reviews. Confirm deletion modal appears. Clicking 'Delete' deletes the review. Success message appears. | Clicked 'Delete'. | Delete buttons appeared on all reviews. Confirm deletion modal appeared. Review was deleted after clicking 'Delete'. Success message appeared. |

#### Basket
| Feature | Expectation | Action | Result |
| ---| ---| ---| ---|
| Empty basket | Message informing the user their basket is empty. Keep shopping buttons changes colour when hovered over. Takes the user to the Products page. | Went to the basket. Hovered over Keep Shopping button then clicked it. | 'Your basket is empty' message. Keep shopping button changed colour when hovered over. Taken to the Products page when button was clicked. |
| Increment and decrement quantity buttons | Function the same as on the product detail page. | Increased and decreased the quantity (both within the allowed range and outside of the range). | Functioned the same as on the product detail page. |
| Update and Remove links | Links underline when hovered over. Changing the quantity of the product then clicking Update changes the totals displayed in the basket page, changes the bag icon values and displays a success message. Clicking Remove removes the product from the basket, updates the bag icon values and displays a success message. | Hovered over the links then clicked them. Updated the quantity of the item in the basket. Then removed the item from the basket. | Links underlined when hovered over. Changing the quantity of the product then clicking Update changed the totals displayed in the basket page, changed the bag icon values and displayed a success message. Clicking Remove removed the product from the basket, updated the bag icon values and displayed a success message. |
| Keep shopping and Secure Checkout buttons | Buttons change colour when hovered over. Clicking the Keep shopping button takes the user to the Products page. Clicking Secure Checkout takes the user to the checkout page. | Hovered over buttons then clicked them. | Buttons changed colour when hovered over. Clicking the Keep shopping button took the user to the Products page. Clicking the Secure Checkout button took the user to the checkout page. |

#### Checkout - General User
| Feature | Expectation | Action | Result |
| ---| ---| ---| ---|
| Go to checkout button on added to bag success message | Button changes colour when hovered over. Clicking button takes the user to the checkout page. | Hovered over the button then clicked it. | Button changed colour when hovered over. Taken to the checkout page when clicked. |
| Adjust basket and complete order buttons | Buttons change colour when hovered over. Clicking the Adjust basket button takes the user to the basket page. Clicking Complete order completes the order if there are correct inputs displays a loading screen and then takes the user to the checkout success page. A success message appears and a confirmation email is sent. | Hovered over the buttons then clicked Adjust basket. Then [completed the form](docs/testing/checkout-form.png) with all correct inputs and no missing fields and clicked complete order. | Buttons changed colour when hovered over. Taken back to the basket page after clicking the Adjust basket button. [Loading screen](docs/testing/loading-screen.png) displays then taken to the checkout success page after clicking Complete order. Success message appeared and a [confirmation email](docs/testing/confirmation-email.png) was received. |
| Checkout success page | All the correct details from the purchase are present. Back to store button changes colour when hovered over. Takes the user back to the Products page when clicked. | Completed purchase to reach the checkout success page. Hovered over the Back to store button then clicked it. | All the [correct details](docs/testing/checkout-success.png) from the purchase were present. Back to store button changed colour when hovered over. Taken back to the Products page when clicked. |
| Checkout form - missing required inputs | For every field marked with an asterisk that is left blank, a message stating to fill in the field appears when clicking Complete Order, starting with the first required field. | Clicked Complete Order without filling in any fields. Then filled in the next required field but left the rest blank and repeated with all of the other required fields. | A message appeared to fill in the blank field for every field that was not completed, therefore preventing the user from submitting a blank or incomplete form. |
| Checkout form - incorrectly inputted email address | Clicking Complete Order will result in a message informing the user to correctly input their email address. | Inputted the email address 'test. | Message appeared informing the user to input their email address correctly with the @ symbol. |
| Checkout form - no card details | Clicking Complete Order will result in a message informing the user that their card number is incomplete. | Inputted all details except the payment details. | Message appeared stating that the card number is incomplete. |
| Checkout form - invalid card details | Clicking Complete Order will result in a message informing the user that their card number is invalid. | Inputted the card number 1111 1111 1111 1111. | Message appeared stating that the card number is incomplete and the card number goes red. |
| Checkout form - no card expiry date | Clicking Complete Order will result in a message informing the user that their card's expiry date is incomplete. | Inputted the card number 4242 4242 4242 4242 but no expiry date. | Message appeared stating that the card number's expiry date is incomplete. |
| Checkout form - card expiry date in the past | Clicking Complete Order will result in a message informing the user that their card's expiry date is in the past. | Inputted the card number 4242 4242 4242 4242 and the expiry date 11/01. | Message appeared stating that the card number's expiry date is in the past and the dat goes red. |
| Checkout form - no card security code | Clicking Complete Order will result in a message informing the user that their card's security code is incomplete. | Inputted the card number 4242 4242 4242 4242, the expiry date 11/31 but no security code. | Message appeared stating that the card's security code is incomplete. |
| Create an account and login links | Link size increases when hovered over. Clicking create an account takes the user to the sign up page. Clicking login takes the user to the login page. After logging in, the user is redirected back to the checkout page. | Clicked create an account and created an account. Then clicked login. | Link size increased when hovered over. Taken to the sign up page after clicking create an account. Taken to the login page after clicking login. Then redirected back to the checkout page after logging in. |
| Trying to access the checkout page with an empty basket | User is redirected to the products page and receives an error message that their basket is empty. | Added the '/checkout' to the end of the home page url. | Taken to the products page and presented with an error that the basket is empty. |

#### Checkout - Signed in User
| Feature | Expectation | Action | Result |
| ---| ---| ---| ---|
| No profile information already saved | User's email address will automatically appear in the email address field. All other fields are empty but once the fields are completed, selecting the save delivery information checkbox will add these details to the user's profile page once they complete their order. | Completed all of the fields, ensured the checkbox was selected and clicked Complete Order. | Emaill address was already completed. After completing the order, the delivery details were saved to the My Profile page. |
| Profile information already saved | All the user's details that are saved in their profile will appear in the checkout form when the user goes to the checkout. | Saved delivery details in the profile. Then added an item to the bag and went to the checkout page. | Details were prefilled in the checkout form. |

#### Wishlist page - Signed in User
| Feature | Expectation | Action | Result |
| ---| ---| ---| ---|
| Empty wishlist | Message states that there are no items in the wishlist. There is a button to Keep Shopping which changes colour when hovered over and takes the user to the Products page. | Clicked on the wishlist icon. | Message stated that there were no items in the wishlist. There was a button to Keep Shopping which changed colour when hovered over and took the user to the Products page. |
| Items in the wishlist | Clicking the product image displays the product detail page. Clicking the solid heart icon removes the item from the wishlist and a success message appears. | Added an item to the wishlist. Clicked the product image. Then returned to the wishlist and clicked the solid heart icon. | Taken to the product detail page. Then clicking the heart icon removed the item from the wishlist and displayed a success message. |

#### Sign in page
| Feature | Expectation | Action | Result |
| ---| ---| ---| ---|
| Correct inputs for a valid user | Sign in button changes colour when hovered over. Clicking it takes the user to the home page after clicking it. | Entered the username and password for a valid user. | Sign in button changed colour when hovered over. Taken to the home page after clicking it. |
| No inputs | Clicking Sign in will result in a message informing the user to fill in the username field. | Clicked Sign in. | Message appeared informing the user to fill in the username field. |
| No password | Clicking Sign in will result in a message informing the user to fill in the password field. | Inputted a username but no password. | Message appeared informing the user to fill in the password field. |
| Incorrect password | Clicking Sign in will result in a message informing the user that the username and/or password is not correct. | Inputted the incorrect password. | Message appeared informing the user that the username and/or password was not incorrect. |
| Sign up link | Link size increases when hovered over. Clicking the link takes the user to the sign up page. | Hovered over the link then clicked it. | Link size increased when hovered over. Taken to the sign up page when clicked. |
| Reset password link | Link size increases when hovered over. Takes the user to the password reset page. | Hovered over the link then clicked it. | Link size increased when hovered over. Taken to the password reset page. |

#### Sign up page
| Feature | Expectation | Action | Result |
| ---| ---| ---| ---|
| No inputs | Clicking Sign up will result in a message informing the user to fill in the email field. | Clicked Sign up. | Message appeared informing the user to fill in the email field. |
| Incorrectly inputted email address | Clicking Sign up will result in a message informing the user to correctly input their email address. | Inputted the email of bob. | Message appeared informing the user to input their email address correctly with the @ symbol. |
| Username less than 3 characters long | Clicking sign up with a username of less than 3 characters results in a message informing the user to enter a longer username. | Entered the username bob. | Message appeared informing the user to input a longer username. |
| No password | Clicking Sign up will result in a message informing the user to fill in the password field. | Inputted a username and email address but no password. | Message appeared informing the user to fill in the password field. |
| Insufficient password | Clicking Sign up will result in a message informing the user that their password needs to be changed to meet the specified requirements. | Inputted the password 123. | Message appeared informing the user that the password was too short, was too common and only had numeric values.|
| Non-matching passwords | Clicking Sign up will result in a message informing the user that they must type the same password each time. | Inputted the password Password975 then the password Password987. | Message appeared informing the user that they must type the same password each time. |
| Successful Sign Up | Clicking Sign up will take the user to the verify your email address page. After following the link provided, they are asked to confirm their email address. Clicking the confirm button takes them to the sign in page. | Clicked Sign up. | Taken to the verify your email address page. Confirmed email address after following the [link provided in the email](docs/testing/confirm-email.png). Taken to the sign in page after clicking the [confirm button](docs/testing/email-confirmation.png). |
| Sign in link | Link size increases when hovered over. Clicking the link takes the user to the sign in page. | Hovered over the link then clicked it. | Link size increased when hovered over. Taken to the sign in page when clicked. |

#### Logout page
| Feature | Expectation | Action | Result |
| ---| ---| ---| ---|
| Sign out button | Button changes colour when hovered over. Clicking it signs the user out, takes them to the home page and a success message appears. | Hovered over button then clicked it. | Button changed colour when hovered over. Clicking it signed the user out and took them to the home page. A success message appeared. |

#### My Profile page - Signed in User
| Feature | Expectation | Action | Result |
| ---| ---| ---| ---|
| Update information button | Button changes colour when hovered over. If the details fields are edited, clicking this button updates the profile details to show the newly saved details and a success message appears. | Updated the profile details then clicked the button. | Button changed colour when hovered over. Default delivery details were updated with the newly saved details. Success message appeared. |
| Order history | All previous orders appear here. If there are no orders a message will state that there have been no orders made yet. The order number link increases in size when hovered over. Clicking the link takes the user to the order confirmation for that order and an alert message appears. | Clicked the order number link. | The order number link increased in size when hovered over. Clicking the link took the user to the order confirmation for that order and an alert message appeared. For a user who has no orders, the message that there are no orders yet was present. |

#### Product Management page - Admin Member
| Feature | Expectation | Action | Result |
| ---| ---| ---| ---|
| Adding a product - correct inputs | The product will be added to the products page when the Add Product button is clicked and the user is taken to that item's product detail page. | Added a product with all of the required fields completed. | The product was added to the products page and the user was taken to the product detail page. |
| Adding a product - no inputs | Clicking Add Product results in a message below the first required field informing the user to fill in that field. | Clicked Add Product without filling in any of the required fields. | Instructed to fill in the first required field. |
| Incorrect price - price too large | Adding a price outside the range results in an error message that the form is not valid and to ensure there are no more than 6 digits in total. | Added the price 123456789. | Error message appeared informing that the form was not valid and to ensure that there are no more than 6 digits in total. |
| Incorrect price - more than 4 digits before the decimal point | An error message appears that the form is not valid and to ensure there are no more than 4 digits before the decimal point. | Added the price 123456 | An error message appeared that the form is not valid and to ensure there are no more than 4 digits before the decimal point. |

## Testing User Stories
EPIC: Navigating through the website
- As a shopper, I want to be greeted with a clearly structured interface, so that I can navigate through the website with ease
    - Result: Shoppers can navigate easily through all of the navbar links to find what they are looking for
- As a shopper, I want the website to be responsive, so that I can access it on a range of devices
    - Result: The website is responsive and so can be accessed on mobile devices, tablets, laptops and desktops
- As a shopper, I want to view a list of products, so that I can browse the store to know what to buy
    - Result: The Products page displays all of the products that can be purchased on the site
- As a shopper, I want to view details about an individual product, so that I can see the product description, price, image, reviews, and be able to purchase the item
    - Result: Clicking on the image of any product will display that item's product detail page, which shows the name, description, price, image, materials and reviews for the item, along with the functionality to purchase the item
- As a shopper, I want to see how many items have been added to my basket, so that I can be aware of what I have selected
    - Result: The bag icon in the navbar (which is visible on both desktop and mobile view) shows the number of items in the basket, as well as the total price

EPIC: Registration and User Accounts
- As a new user, I want to navigate to the sign up page, so that I can create an account
    - Result: General users can create an account through the sign up page
- As a registered user, I want to login to my account, so that I can make purchases
    - Result: Registered users can login to their accounts
- As a registered user, I want to log out of my account, so that I can protect my information from being accessed by others
     - Result: Signed in users can log out of their accounts
- As a registered user, I want to be able to edit my account details, so that I can make changes if needed
    - Result: Signed in users can navigate to the My Profile page where they can update their delivery details
- As a registered user, I want to have a personalised user profile, so that I can view my account details and any previous purchases I have made
    - Result: The My Profile page displays the user's default delivery information, as well as all of their previous purchases
- As a new user, I want to receive an email confirmation after signing up, so that I can confirm that my account is set up successfully
    - Result: An email verifying the account is automatically sent out to users signing up to the site

EPIC: Sorting and searching for products
- As a shopper, I want to sort the list of available products, so that I can easily view the items alphabetically or by price
    - Result: The products can be sorted alphabetically or by price (in both directions) through the sort selector on the Products page
- As a shopper, I want to sort items by category, so that I can view just the items I am interested in buying
    - Result: The products can be sorted in alphabetical category order through the sort selector on the Products page or directly through the navbar where users can choose which item, and whether they would rather gold or silver, they want to purchase
- As a shopper, I want to search for a product, so that I can find exactly what I am looking for
    - Result: The magnifying glass icon in the navbar makes it easy to search for any product, and if the searched term appears in either the name or the description of the product, it will be displayed
- As a shopper, I want to view what I have searched for and the number of items I have searched for, so that I can see whether the product I want is available
    - Result: When a shopper searches for an item, the searched term appears in bold at the top of the page along with the number of items that were found

EPIC: Purchasing and checkout
- As a shopper, I want to be able to add an item to my basket and choose how many of an item I want to buy, so that I can select the quantity I desire in case I want more than one of the item
    - Result: Shoppers can choose the quantity of the item they want, either by using the +/- buttons or by directly typing in the quantity they want. They can do this directly from the product detail page or from the basket
- As a shopper, I want to view the items in my basket, so that I can see what items I have chosen and the total cost
    - Result: The basket can be viewed by clicking on the bag icon in the navbar, and this shows all of the items that have been added, along with the bag total, the delivery cost, the grand total and how much more could be spent to receive free delivery
- As a shopper, I want to adjust the quantity of an item from the basket page, so that I can easily edit my purchase before the checkout
    - Result: The quantity of an item can be adjusted from the basket page
- As a shopper, I want to be able to remove an item from my basket, if I no longer want it
    - Result: Clicking the Remove link on the basket page will remove the item from the basket
- As a shopper, I want to receive feedback when adding, editing or deleting a product, so that I can clearly see what I have done
    - Result: The user is always presented with feedback messages for actions that they carry out. These messages are colour coded whether they are success messages, error messages or alert messages
- As a shopper, I want to view any delivery costs on the checkout page, so that I can see how much I am paying for delivery and if I'd rather purchase something extra to avoid this cost
    - Result: The delivery cost is clearly stated on both the basket page and the checkout page under the order summary
- As a registered user, I want to see my delivery details automatically filled in on the checkout page, so that I can save time when it comes to checking out
    - Result: Signed in users who have updated their profile page with their delivery details will see these automatically completed on the checkout page if they are logged in
- As a shopper, I want to receive an email confirmation after completing my payment, so that I can see exactly what I have purchased and the cost for future records
    - Result: Confirmation emails are automatically sent out to shoppers after they complete a purchase
- As a shopper, I want to be able to put in my card details, so that I can make a purchase
    - Result: The payment details input field requires a card number, expiry date and security code. Error messages will be presented for any invalid inputs

EPIC: Reviewing products
- As a registered user, I want to be able to review a product, so that I can give feedback
    - Result: Signed in users can leave reviews underneath products
- As a shopper, I want to be able to see reviews for the products, so that I can see which are rated highly
    - Result: All shoppers can see any reviews that have been left on the product detail page for the product
- As a registered user, I want to be able to edit my reviews, so that I can make adjustments if needed
    - Result: Signed in users who are the author of the written review can edit it
- As a registered user, I want to be able to delete my reviews, if I no longer want to leave that review
    - Result: Signed in users who are the author of the written review can delete it

EPIC: Adding items to a wishlist
- As a registered user, I want to be able to add a product that I like to a wishlist, so that I can save the item without having to add it to the checkout
    - Result: Signed in users can add products to their wishlist by clicking on the blank heart icon next to each product
- As a registered user, I want to be able to view my favourited items in my wishlist, so that I can see all of the items that I like before I buy them
    - Result: Signed in users can click on the heart icon in the navbar to go to their wishlist where they can see all of the items they have favourited

EPIC: Contacting the store
- As a shopper, I want to be able to contact Hidden Gems directly, so that I can let them know about any queries I have
    - Result: All shoppers can navigate to the Contact link in the footer to send a message directly to Hidden Gems

EPIC: Frequently asked questions
- *As a shopper, I want to see a list of FAQs, so that I can see common queries that other people have - **could have***
    - Result: This user story has not been completed due to time constraints, however, it does not affect the usability of the website and has been added to the list of future features
- *As a registered user, I want to be able to submit a question on the FAQ page, so that I can enquire about any general concerns - **could have***
    - Result: This user story has not been completed due to time constraints, however, it does not affect the usability of the website and has been added to the list of future features

EPIC: Administrative managing of the store
- As a store owner, I want to be able to add new products to the store, so that I can update the items we sell
    - Result: Store owners can navigate to the product management page where they can add new products to the store
- As a store owner, I want to be able to edit items, so that I can update the price/description/image
    - Result: Store owners can edit any item directly from the products page
- As a store owner, I want to be able to delete items, so that I can remove items that are no longer on sale
    - Result: Store owners can delete any item directly from the products page

## Responsiveness
## Browser Compatibility
## Accessiblity
## Lighthouse Testing
### Desktop
### Mobile
## Unit Tests
## Code Validation
### HTML
### CSS
### JavaScript
### Python
## Bugs
### Solved Bugs
### Unsolved Bugs
