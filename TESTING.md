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

#### Header - Sigend in User
| Feature | Expectation | Action | Result |
| ---| ---| ---| ---|
| Profile icon | User's profile name appears next to this icon. Clicking the icon displays the 'My Profile' and 'Logout' links. Clicking 'My Profile' takes the user to their profile page. Clicking 'Logout' takes the user to the logout page. | Signed in as Jim1. Clicked the icon. Clicked each of the links. | 'Jim1 appeared next to the profile icon'. Clicking the icon displayed the 'My Profile' and 'Logout' links. Taken to the profile page after clicking the 'My Profile' link. Taken to the logout page after clicking 'Logout'. |
| Wishlist icon | Clicking the icon takes the user to their wishlist page. | Clicked the icon. | Taken to the wishlist page. |

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
| Shop Now button | Button changes colour when hovered over. Clicking it takes the user to the Products page. | Hovered over button then clicked it. | Button changed colour when hovered over. Clicking it took the user to the Products page.

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

## Testing User Stories
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
