# User stories and planning

Submit form for users per machine. One machine can have multiple users and user can use multiple machines. Machine should have the basics data.

User can be a students or a teacher with some kind of adming right in this case.

User story: Students goes to the machine. Opens a camera to Qr Code which opens up a login page
User story: Students logs in using what kind of credentials? Open or do you need to create one?
User story: Students fill in the data from the machine manually to the form that contains the machine details.
User story: Students send the data from the form by pressing submit and all the data has to be filled int.
User story: Student interupts the process for some reason and needs to be able to continue the filling in
User story: Student closes the form after submissions.
User story: In theory there could be students who would update the data in short intervales so there needs to be checks for this.

User story: Teachers and maintenance responsibles need to be able to login to adming page of some kind.
User story: Teachers and maintenance responsible people need to be able to see all the machines and their data.
User story: This data needs to be updated daily or instant update is also reasonalbe
User story: Teacher could also use the camera and with admin login be able to see the machine data.
User story: Teachers need to get message when maintenance is close for example if the machine has beed running for 6900 hours and maintenance is needed at 7000 hours there should be email or some kind of notification.

# System design

Flask and python + some kind of frontend for web that needs a webserver to be able to show the content and deploy place for the app (Heroku or some other). Database needs to be designed from the user stories. Sqlalchemy can be used as an ORM if needed for the crud operations.

Database could be SQLLite.

# Unit testing
