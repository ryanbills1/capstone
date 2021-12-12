# About me

Hello, my name is Ryan Bills and I have been studying computer science while working as a data engineer over the last four years. I am planning to continue my growth in my area of expertise, which includes ETL, data warehousing, and analytical applications. 

Throughout the computer science program at SNHU, I worked on many projects that provided me with skills that are transferrable to my work as a data engineer. While working through course projects, I learned how to collaborate with other developers while working on the same code simultaneously by utilizing git repositories and advanced git practices. I've also worked through the entire SDLC, through requirements gathering, development, testing, and implementation for data-centric projects involving data cleaning and analysis. While working in an Agile development environment as a data engineer, I was able to apply certain Agile concepts learned through coursework at SNHU to help my team and I better follow best practices such as writing out more defined and descriptive acceptance criteria in user stories and providing iterative value to stakeholders and end-users.

## Capstone Project
For my capstone project at SNHU, I decided to create a data pipeline for retrieving data from eBay's API and creating a report based off of the data. 
As a part of this project, some existing code for connecting to and manipulating a MongoDB database was reused from a prior project. The enhancements and new code exemplifies my skills in three categories: software engineering, databases, and data structures. Below are the artifacts showcased and described in detail.

Here is a link to the informal code review which was conducted prior to the enhancements being done:                          
https://vimeo.com/655928715

## Enhancement 1: Software Engineering Category
The artifact I have selected to fulfill the software design / engineering requirement is to create an eBay application using modular development, in order to be able to expand the program in the future. This code includes a main file (controller), a .env file for holding the API key, a file for connecting to and handling eBay API requests, a file for interacting with the MongoDB database, and a file for interacting with Excel file input / output. All of these files are new code development, except for the MongoDB file which will be edited / enhanced / reused from a previous project.

This artifact was included in my ePortfolio because it showcases being able to modify existing code in order to fit it into a brand new project. Completing this artifact also demonstrates the ability to structure new code while following best practices to ensure better code maintainability and expandability. I am utilizing the Model View Controller design pattern for this, which is the most widely used framework for scalable projects.

The process of enhancing the application to connect and retrieve data from the eBay API was a learning experience. Ebay includes some code examples with their API documentation; however a lot of trial and error was required when working with the data object that is returned by the API call. Separately, I decided to go with using a Pandas dataframe rather than a Python dictionary for storing Excel input, due to compatibility issues, and overall because Pandas has a lot of support on operations on DataFrames. 



## Enhancement 2: Data Structures Category
The artifact that was used to satisfy the data structures / algorithms encompasses the data operations throughout the application. This is all new code being created. This includes retrieving data from eBay’s API, which involves iterating through the results and appending the data to a Pandas dataframe. This was done for database efficiency; instead of executing many queries to insert each product search result into the database, I am now able to execute one insert statement to insert the Pandas dataframe into the MongoDB database.                    

This artifact was included in this project and the ePortfolio because it showcases being able to identify what kind of data is being returned, and how to access / manipulate that data. These specific data structures (Pandas dataframe, Python dictionary) were selected due to their efficiency and extensive collection of useful functions to operate on them. For the requirements of this project, these data structures made the most sense to use. Overall, the course objectives for this enhancement were met, as I was able to retrieve the data from the API and access/store the fields in preparation for the database portion of the project.

In terms of reflecting on the enhancement of this artifact, I did run into a few separate contemplations regarding what API call to use due to the kinds of data they return, and how well they work when searching for products. (For example, a certain method call would return multiple products with multiple listings in a single data objet, whereas the method call I chose to use returns the listings for one product at a time in each data object.) I learned how to access nested data fields within the eBay data object; this skill is great to have for API’s in general, as many times it’s up to the developer to find efficient ways to retrieve and store data from an API.



## Enhancement 3: Database Category
The database artifact being enhanced during this project is a Python module which was created during a previous project at SNHU. The module is used to connect, and perform CRUD operations on a MongoDB server. In the previous project, it was used to connect to a sample MongoDB collection for Animal Shelter data. 

This artifact is included in my ePortfolio because it is required for the application’s functionality and value it provides, and the artifact also showcases my skills in database development, and modifying/reusing existing code. I selected this particular database module because it was already existing and mostly reusable; the required changes involved changing the connection details, adding comments to help with code readability, and add an exception statement for connecting to the database, in case there was an issue with connecting. 

In addition to these changes, I used this module to insert and read data to the ‘products’ collection in MongoDB. This module will allow the application to filter document results based on specified criteria, which is useful for outputting the data to an Excel; the end user will not have to filter on such criteria. Making changes and additions to an application with the end user in mind is a useful skill that this demonstrates. 
