# RestApiProject
Create a fully functioning user dataase app to build a REST API
Allows users to authenticate with username & password
Manage user profile feed items

Learned:
 -how to create a working local development server, 
 -how to use Django Models to create database, 
 -enable and use Django Admin
 -use Django dev server to run and test the code
 -deploy the app to AWS

 - api/ - you can check the API main view using api/
 - api/login/ - to login with the user and generate a Token / 
              can use Mode header from Google Chrome with name Authorization Token 33f5c3afc06a45360aa2d0ab21d642621991628b as example
              https://prnt.sc/wkveyf
 - api/profiles/ to see the current profiles and to create a new one
 - api/profiles/1 - where 1 is the id number of your profile - will  not allow you to modify it if is not your own and logged in
 - api/feed/ to see the feeds - can create and edit feeds for own profiles only.
