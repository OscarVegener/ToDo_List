from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import sessionmaker
from datetime import datetime

Base = declarative_base()


class Table(Base):
    __tablename__ = 'task'
    id = Column(Integer, primary_key=True, autoincrement=True)
    task = Column(String, default='default_value')
    deadline = Column(Date, default=datetime.today())

    def __repr__(self):
        return self.task

    def __str__(self):
        return str(self.id) + ". " + self.task


def add_task():
    print("Enter task")
    task = input()
    new_row = Table(task=task)
    session.add(new_row)
    session.commit()


def tasks():
    print()
    print("Today:")
    rows = session.query(Table).all()
    if len(rows) > 0:
        for row in rows:
            print(row)
        print()
    else:
        print("Nothing to do!")
        print()


def delete_tasks():
    pass


def main_menu():
    while True:
        print("1) Today's tasks")
        print("2) Add task")
        print("0) Exit")
        usr_input = int(input())
        if usr_input == 0:
            break
        elif usr_input == 1:
            tasks()
        elif usr_input == 2:
            add_task()


engine = create_engine('sqlite:///todo.db?check_same_thread=False')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
main_menu()