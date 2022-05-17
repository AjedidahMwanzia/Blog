# Blog
## Author

[AjedidahMwanzia](https://github.com/AjedidahMwanzia)

# Description
A flask application that allows writers to post , edit and delete blogs. It also allows users who have signed up to comment on the blogs that hav been posted . 

## Live Link
[View Site]()

## Screenshot


## User Story

* Comment on the different blogs posted by other writers.
* See the blogs posted by other writers.
* Register to be allowed to log in to the application
* Submit a pitch to a specific category of their choice.

## BDD
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| Load the page | **On page load** | Get all posts, Select between signup and login|
| Select SignUp| **Email**,**Username**,**Password** | Redirect to login|
| Select Login | **Username** and **password** | Redirect to page with app blogsand commenting section|
| Select comment button | **Comment** | Form that you input your comment|
| Click on submit |  | Redirect to all comments template with your comment and other comments|





## Development Installation
To get the code..

1. Cloning the repository:
  ```bash
 https://github.com/AjedidahMwanzia/Blog.git
  ```
2. Move to the folder and install requirements
  ```bash
  cd Blog
  pipenv install requests
  ```
3. Exporting Configurations
  ```bash
  export SQLALCHEMY_DATABASE_URI=postgresql+psycopg2://{User Name}:{password}@localhost/{database name}
  ```
4. Running the application
  ```bash
  python3.8 manage.py server
  ```
5. Testing the application
  ```bash
  python3.8 manage.py test
  ```
Open the application on your browser `127.0.0.1:5000`.


## Technology used

* [Python3.8](https://www.python.org/)
* [Flask](http://flask.pocoo.org/)
* [Heroku](https://heroku.com)


## Known Bugs
* There are no known bugs currently but pull requests are allowed incase you spot a bug

## Contact Information 


-   Email- [Ajedidah Mwanzia](mailto:ajedidah.mwanzia@student.moringaschool.com)
-   Linkedin - [Ajedidah Mwanzia](https://www.linkedin.com/in/ajedidah-mwanzia/)
-   Portfolio - [Ajedidah Mwanzia](https://ajedidahmwanzia.github.io/portfolio/)


## License
* *MIT License:*
* Copyright (c) 2022 **Ajedidah Mwanzia**

[Go Back to the top](#blog)