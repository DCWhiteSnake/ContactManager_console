#![ID Keeper](icon.png)
A console contact-manager application implementing some datastructures and oop concepts. It can load contacts from a csv file and supports undo actions too. Enjoy!

## Tech Stack

- **Core Python** - python 3.6+

## Main Files: Project Structure


```sh
ContactManager
│   __main__.py  *** Entry point
│   icon.png
│   log1.txt
│   readme.md
│   repl.py 
│   utils.py *** miscellanous functions

├───Commands
│   │   command.py
│   │   command_factory.py *** factory methods for generating commands
│
├───DataStructures
│   │   doublylinkedlist.py
│   │   sortedlist.py

├───Models
│   │   contact.py
│   │   contactstore.py 

```

## Demo

![list and add](demo_1.gif)

## Local Running

─ Make sure you have the correct version of python(3.6+)
─ run app.py

## Commands

─ load filename=filename.csv; = loads the file from csv
─ l, list = list all available contacts
─ a,add [fn=firstname;ln=lastname;etc] = adds a contact manually
─ exit = closes the app.
─ undo = cancels the last action.