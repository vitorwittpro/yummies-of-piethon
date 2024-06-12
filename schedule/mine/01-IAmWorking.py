import schedule
import time

def job(word):
    time_ = time.strftime("%H:%M:%S")
    print(f"I'm working... {time_}, {word}")

def test():
    print("china")

schedule.every(1).minutes.do(job, "here")
schedule.every().second.do(job, "some time hein....")

current_task = lambda task_name : print(f"running at {task_name}")
schedule.every().minutes.at(":30").do(current_task, time.strftime("%H:%M:%S"))
schedule.every().tuesday.at("21:16:05").do(test)
schedule.every().day.at("08:22:00", "Asia/Shanghai").do(test)



current_time = lambda : time.strftime("%H:%M:%S")

while True:
    schedule.run_pending()
    time.sleep(1)
