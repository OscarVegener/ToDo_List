from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import sessionmaker
from datetime import datetime, timedelta

Base = declarative_base()


class Table(Base):
    __tablename__ = 'task'
    id = Column(Integer, primary_key=True, autoincrement=True)
    task = Column(String, default='default_value')
    deadline = Column(Date, default=datetime.today())

    def __repr__(self):
        return self.task

    def __str__(self):
        return self.task

    def str_deadline(self):
        return ". " + self.deadline.strftime("%d %b")


def add_task():
    print("Enter task")
    task = input()
    print("Enter deadline")
    deadline = input()
    new_row = Table(task=task, deadline=datetime.strptime(deadline, "%Y-%m-%d"))
    session.add(new_row)
    session.commit()


def today_tasks():
    print()
    print(datetime.today().strftime("Today %b %d:"))
    rows = session.query(Table).filter(Table.deadline == datetime.today().date()).all()
    if len(rows) > 0:
        j = 0
        for row in rows:
            j += 1
            print(str(j) + ". ", end="")
            print(row)
        print()
    else:
        print("Nothing to do!")
        print()


def week_tasks():
    for i in range(7):
        current_day = datetime.today() + timedelta(i)
        print(datetime.strftime(current_day, "%A %d %b:"))
        rows = session.query(Table).filter(Table.deadline == current_day.date()).all()
        if len(rows) > 0:
            j = 0
            for row in rows:
                j += 1
                print(str(j) + ". " , end="")
                print(row)
            print()
        else:
            print("Nothing to do!")
            print()


def all_tasks():
    print()
    print("All tasks:")
    rows = session.query(Table).order_by(Table.deadline).all()
    if len(rows) > 0:
        j = 0
        for row in rows:
            j += 1
            print(str(j) + ". ", end="")
            print(row, end="")
            print(Table.str_deadline(row))
        print()
    else:
        print("Nothing to do!")
        print()


def delete_tasks():
    pass


def main_menu():
    while True:
        print("1) Today's tasks")
        print("2) Week's tasks")
        print("3) All tasks")
        print("4) Add task")
        print("0) Exit")
        usr_input = int(input())
        if usr_input == 0:
            break
        elif usr_input == 1:
            today_tasks()
        elif usr_input == 2:
            week_tasks()
        elif usr_input == 3:
            all_tasks()
        elif usr_input == 4:
            add_task()


engine = create_engine('sqlite:///todo.db?check_same_thread=False')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
main_menu()
