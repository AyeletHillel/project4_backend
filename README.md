# Bookmark App - Backend

This app is dedicated to helping people learn data science and software engineering. Built using Python and Django for the backend, and React for the frontend, this app provides users with the ability to add reccomendations for helpul resources and manage them with all CRUD functionality. 
Through this platform, users can access carefully curated content such as articles, books, YouTube videos and more. 

# Technologies Used

* Python
* Django
* Postgres
* render.com

## Backend Route Table

| Route Name | URL |	HTTP Verb | Description	
| --- | --- | --- | --- | 
| Index | /bookmark/ | GET | Loads a list of all bookmarks 
| Show | /bookmark/:id | GET | Loads one bookmark 
| Create | /bookmark/ | POST | Creates one bookmark 
| Update| /bookmark/:id | PUT | Updates one bookmark
| Delete| /bookmark/:id | DELETE | Deletes one bookmark

## Models

<img width="452" alt="Screen Shot 2023-02-21 at 10 00 18 PM" src="https://user-images.githubusercontent.com/91492759/220510258-1ec743e9-abe1-402d-aa01-25b5388dc074.png">


## Links to project

* [Deployed Backend](https://project4-backend.onrender.com)
* [Deployed Frontend](https://project4-frontend.onrender.com)
