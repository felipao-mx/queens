# queens
### Api for N queens problem.
how to run:
1. Checkout the repository
1. Create `.env` file and [declare environment variables](https://docs.docker.com/compose/env-file/):
    1. `DATABASE_NAME` 
    1. `DATABASE_USER` 
    1. `DATABASE_USER_PWD`
1. Execute command `docker-compose up`
1. Make `GET` request to `http://localhost:8888/queens/{queenNum}/solutions`, where `{queenNum}` refers to chessboard size and queens
