# Eight Queens 👑👑:crown:

Solution of the famous [Eight Queen Problem](https://en.wikipedia.org/wiki/Eight_queens_puzzle) using bitsets with a touch of Postgres and SQLAlchemy.

## Prerequisites

- Docker Compose

## Running the code

For running the source code, use the docker image.

```bash
$ docker-compose run app
```


### Sample

##### Example 1
```
$ docker-compose run app
1. Run n-queens for a given value of n
2. Store the solutions upto a given value in a database
3. View the database table
4. Clear the database table
5. Run tests
0. Quit

> 1
Enter the value of n
> 8
92
```
##### Example 2
```
$ docker-compose run app
1. Run n-queens for a given value of n
2. Store the solutions upto a given value in a database
3. View the database table
4. Clear the database table
5. Run tests
0. Quit

> 2
Enter the value of n
> 10
Successfully inserted the values
> 3
[(1, 1), (2, 0), (3, 0), (4, 2), (5, 10), (6, 4), (7, 40), (8, 92), (9, 352), (10, 724)]

```

## Project Structure

```

├── db
│   ├── create_answer_table.py       # Initialises the table and DB connections     
│   ├── main.py                      # Contains main logic for the DB
│   └── secrets.py                   # Contains secrets. Should be encrypted or not put in Version Control
├── tests                              
│   └── core_test.py                 # Contains unit test cases for core logic
├── helpers                               
│   └── bit_operations.py            # Helper class to deal with bit operations    
├── core.py                          # Contains the logic to solve the problem 
├── main.py                          # Startup script
├── docker-compose.yml               # File to compose app and DB
├── Dockerfile                       # Dockerfile to build app
├── README
├── requirments.txt                  # Specify requirements for the project
└── .gitignore                       # Files to ignore for Version Control
```

## Algorithm

The core algorithm follows the use of bitsets. While checking if it is safe to put the queen at a particular spot, we check whether there is queen in the same column, diagonal 1 or diagonal 2. To check this in O(1) time complexity, we use a number (representing a bitset). 

If it was safe to place the queen, we set the appropriate bits in column, diagonal 1, diagonal 2, marking them as occupied and then we go to the next row. If we were able to reach the end of the board, we found 1 solution otherwise we backtrack and unplace the queen means setting off those bits.

## Built With

* [Postgres](https://www.postgresql.org/) - Database
* [SQLAlchemy](https://www.sqlalchemy.org/) - ORM
* [Pytest](https://docs.pytest.org/en/latest/) - Testing