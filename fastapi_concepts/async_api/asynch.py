from fastapi import FastAPI
import asyncio
import time

app = FastAPI()

@app.get('/')
def home():
    return {'message':"API to demonstrate the difference between Async and Sync."}

@app.get('/asynchroute')
def asy():
    async def task1():
        print("message:Task 1 Started.")
        await asyncio.sleep(2)
        print("message:Task 1 Completed.")

    async def task2():
        print("message:Task 2 Started.")
        await asyncio.sleep(2)
        print("message:Task 2 Completed.")

    async def main():
        await asyncio.gather(task1(),task2())

    start_time = time.time()
    asyncio.run(main())
    return {"Message":f"Total Time Taken {time.time() - start_time}"}

@app.get('/synchroute')
def sy():
    def task1():
        print("message : Task 1 Started.")
        time.sleep(2)
        print("message : Task 1 Completed.")
    
    def task2():
        print("message : Task 2 Started.")
        time.sleep(2)
        print("message : Task 2 Completed.")

    start_time = time.time()
    task1()
    task2()
    return {"message":f"Total Time Taken: {time.time() - start_time}"}

    