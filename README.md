# ADA2022_Group10
ADA2022 Group 10 Project Repository


Hey, you!
Let me tell you how to start this stuff:

- First, cd to the directory (ADA2022_Group10)
- Run "docker-compose build", this will build the images
- Run "docker-compose up -d", this will start all the services (store_service, product_service & inventory_service AND the 2 DBs)
- Open docker desktop (or look up the commands to enter the bash of a container) and enter "store_service" and "product_service", then run "alembic upgrade head" in both
- Next up, navigate to the endpoints that are in the main.py files (I don't remember them but I think localhost:5001/stores/seed and localhost:5002/products/seed) to seed the database with fake data
- ??????
- Profit