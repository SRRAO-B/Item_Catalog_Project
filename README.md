# Item Catalog

> Sundar Bairavarasu

## About

The Item Catalog project consists of developing an application that provides a list of items within a variety of categories, as well as provide a user registration and authentication system. This project uses persistent data storage to create a RESTful web application that allows users to perform Create, Read, Update, and Delete operations.
The user needs to be logged in to perform update and delete operations and can read the categories or items of the catalog application. Authentication and Authorization for login is implemented by third party OAuth services like Google and Facebook.

Some of the technologies used to build this application include Flask, Bootsrap, Jinja2, and SQLite.


## Skills used for this project
- Python
- HTML
- CSS
- Bootstrap
- Flask
- Jinja2
- SQLAchemy
- OAuth
- Facebook / Google Login

## Project Setup and getting started
### Prerequisites
* Python 2.7
* Vagrant
* VirtualBox
* [Vagrant](https://vagrantup.com)
* [Udacity Vagrantfile](https://github.com/udacity/fullstack-nanodegree-vm)
* [VirtualBox](https://www.virtualbox.org/wiki/Downloads)


### How to Run
1. Install VirtualBox and Vagrant
3. Unzip and place the Item Catalog folder in your Vagrant directory
4. Launch Vagrant
```
$ Vagrant up
```
5. Login to Vagrant
```
$ Vagrant ssh
```
6. Change directory to `/vagrant`
```
$ Cd /vagrant
```
7. Initialize the database
```
$ Python database_setup.py
```
8. Populate the database with some initial data
```
$ Python lotsofmenus.py
```
9. Launch application
```
$ Python application.py
```
10. Open the browser and go to http://localhost:8000



## JSON Endpoints

`/catalog.json/` - Returns JSON of all items in catalog

`/category/<int:category_id>/JSON` - Generates and displays JSON for all items in 1 category

`/category/<int:category_id>/<int:item_id>/JSON/` - Generates and displays JSON for 1 item

## REST Endpoints

#### --------------------------------------
#### CRUD for categories
#### --------------------------------------

`/` or `/category` - Returns catalog page with all categories and recently added items

`/category/new` - Allows user to create new category

`/category/<int:category_id>/edit/` - Allows user to edit an existing category

`/category/<int:category_id>/delete/` - Allows user to delete an existing category

#### --------------------------------------
#### CRUD for category items
#### --------------------------------------

`/category/<int:category_id>/` - returns items in category

`/category/<int:category_id>/<int:item_id>/`  - returns specific item

`/category/<int:category_id>/new/` - Creating a new item in category

`/category/<int:category_id>/<int:item_id>/edit/` - Edit an existing Item

`/category/<int:category_id>/<int:item_id>/delete/` - Delete an existing Item


#### --------------------------------------
#### Login
#### --------------------------------------

`/login` - login page
