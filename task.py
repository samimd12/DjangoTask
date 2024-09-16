# Question 1: By default are django signals executed synchronously or asynchronously? Please support your answer with a code snippet that conclusively proves your stance. The code does not need to be elegant and production ready, we just need to understand your logic.

import time
from django.dispatch import Signal, receiver

# Define a custom signal
my_signal = Signal()

# Receiver function for the signal
@receiver(my_signal)
def my_receiver(sender, **kwargs):
    print("Signal received.")
    time.sleep(5)  # Introduce a delay to simulate synchronous execution
    print("Receiver processing complete.")

def trigger_signal():
    print("Triggering signal...")
    my_signal.send(sender=None)  # Trigger the signal
    print("Signal sent.")

if name == "main":
    trigger_signal()


# Question 2: Do django signals run in the same thread as the caller? Please support your answer with a code snippet that conclusively proves your stance. The code does not need to be elegant and production ready, we just need to understand your logic

import threading
from django.dispatch import Signal, receiver

# Define a custom signal
my_signal = Signal()

# Receiver function for the signal
@receiver(my_signal)
def my_receiver(sender, **kwargs):
    print(f"Receiver is running in thread: {threading.current_thread().name}")

def trigger_signal():
    print(f"Caller is running in thread: {threading.current_thread().name}")
    my_signal.send(sender=None)  # Trigger the signal

if name == "main":
    trigger_signal()


# Question 3: By default do django signals run in the same database transaction as the caller? Please support your answer with a code snippet that conclusively proves your stance. The code does not need to be elegant and production ready, we just need to understand your logic.

from django.db import transaction
from django.db.models.signals import post_save
from django.dispatch import receiver
from myapp.models import MyModel

@receiver(post_save, sender=MyModel)
def my_signal_handler(sender, instance, **kwargs):
    print("Signal handler executed")

def create_instance():
    with transaction.atomic():
        instance = MyModel(name="Test")
        instance.save()
        # Simulate an error that causes a rollback
        raise ValueError("Forcing rollback")

try:
    create_instance()
except ValueError:
    print("Transaction rolled back")

# Check if signal was executed


# Topic: Custom Classes in Python
# Description: You are tasked with creating a Rectangle class with the following requirements:

class Rectangle:
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width

    def __iter__(self):
        yield {'length': self.length}
        yield {'width': self.width}

# Example usage:
rect = Rectangle(10, 5)

for item in rect:
    print(item)

# Output:
# {'length': 10}
# {'width': 5}
