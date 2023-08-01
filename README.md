# software-recruitment
Technical exercises for software engineering recruitment

## Task 1

You have been given a data set as in the file `exercise_1.xlsx`.
This data set simulates the information we collect from potential users who wish to sign up to our web applications. It contains the following fields:

* `id` (int): A unique identifier for each individual
* `firstname` (str): Individual's first name
* `surname` (bool): Individual's family name
* `email` (str): Individual's email address
* `primary_trust` (str): The trust or NHS organisaton to which an individual is affiliated
* `start_date` (date %d/%m/%Y): The first date on which they may access our applications
* `end_date` (date %d/%m/%Y): The last date on which they may access our applications

You have been asked to create the functionality required by a REST-ful API to perform basic CRUD operations on this data set, assuming an appropriate data persistence of your choice.
You are provided with a main method and a utility function to extract data from an excel file.

Furthermore, you are presented with the following requirements by internal stakeholders:
 * Users (and collections thereof) will need to be retrieved variously by unique ID and by trust.
 * Only 'active' users should be retrieved. A user is considered 'active' during the time period between their start and end dates.
 * Before user data is stored, it must be validated to ensure that users only register with an '@nhs.' email address. Other email addresses are not permitted.

You may use tools, packages and testing as you feel appropriate and be prepared to discuss your technical solution, methodology, design decisions and any assumptions you have made.

Please fork the software-recruitment repository and work on a new branch. 
Throughout development, you should commit your code with appropriate messaging as you see fit and at the end of the test, please push the completed exercise to the repo to enable us to assess it.