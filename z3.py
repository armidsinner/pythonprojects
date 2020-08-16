import uuid
import random
from copy import copy


class LinkedListItem():
    def __init__(self, address, data, next_pointer, next_random):
        self.address = address
        self.data = data
        self.next = next_pointer
        self.next_random = next_random


class LinkedList():
    def __init__(self):
        self.initial_id = uuid.uuid4()
        self.currentElem = LinkedListItem(
            self.initial_id, "Initial", None, None)
        self.linked_list = dict()
        self.linked_list[self.initial_id] = self.currentElem

    def add(self, data):
        new_id = uuid.uuid4()
        self.currentElem.next = new_id
        self.linked_list[new_id] = (LinkedListItem(new_id,
                                                   data, None, None))
        self.currentElem = self.linked_list[new_id]

    def add_random(self):
        tmp = list(self.linked_list.keys())
        tmp.remove(self.initial_id)
        if (self.currentElem.address in tmp):
            tmp.remove(self.currentElem.address)
        self.currentElem.next_random = random.choice(tmp)

    def set_random(self, address):
        self.currentElem.next_random = address

    def randomize(self):
        self.add_random()
        if self.next():
            self.randomize()
        else:
            return

    def toStart(self):
        self.currentElem = self.linked_list[self.initial_id]

    def next(self):
        if (self.currentElem.next):
            self.currentElem = self.linked_list[self.currentElem.next]
            return True
        else:
            return False

    def get_random(self):
        if (self.currentElem.next_random):
            self.currentElem = self.linked_list[self.currentElem.next_random]
        else:
            raise (Exception("No random element"))

    def show(self):
        tmp = self.currentElem.address
        self.toStart()
        while True:
            print("Current element: {} \nCurrent data: {} \nCurrent random elem: {} \n".format(
                self.currentElem.address, self.currentElem.data, self.currentElem.next_random))
            if not self.next():
                break
        self.toStart()
        while self.currentElem.address != tmp:
            self.next()


some_map = LinkedList()

some_map.add("Some random")
some_map.add("data")
some_map.add("spreaded across")
some_map.add("this linked")
some_map.add("list")

some_map.toStart()
some_map.randomize()
some_map.toStart()


def insert_next(linked_list, data):
    tmp = {"next": linked_list.currentElem.next, "cur": linked_list.currentElem.address}
    linked_list.add(data)
    linked_list.currentElem.next = tmp['next']
    linked_list.toStart()
    while linked_list.currentElem.address != tmp["cur"]:
        linked_list.next()
    linked_list.next()


def deep_clone(origList, newCopy):
    tmp = {"next": origList.currentElem.next, "cur": origList.currentElem.address}
    origList.get_random()
    if (origList.currentElem.data):
        connect_random(newCopy, origList.currentElem.data)
    origList.toStart()
    while origList.currentElem.address != tmp["cur"]:
        origList.next()


def connect_random(linked_list, data):
    tmp = {"next": linked_list.currentElem.next, "cur": linked_list.currentElem.address}
    linked_list.toStart()
    while linked_list.currentElem.data != data:
        linked_list.next()
    tmp["random_found_uuid"] = linked_list.currentElem.address
    linked_list.toStart()
    while linked_list.currentElem.address != tmp["cur"]:
        linked_list.next()
    linked_list.set_random(tmp["random_found_uuid"])
    linked_list.next()


def deep_copy(linked_list):
    new_copy = LinkedList()
    while linked_list.next():
        insert_next(new_copy, linked_list.currentElem.data)
    linked_list.toStart()
    new_copy.toStart()
    new_copy.next()
    while linked_list.next():
        deep_clone(linked_list, new_copy)

    return new_copy

def validate(a,b):
    while True:
        if (a.next() and b.next()):
            res_a = a.linked_list[a.currentElem.next_random]
            res_b = b.linked_list[b.currentElem.next_random]
            if (a.currentElem.data == b.currentElem.data) and res_a and res_b and (res_a.data == res_b.data):
                print("Item \nData: {}\nRandom: {}\ncopied successfully".format(a.currentElem.data, res_a.data))
        else:
            break

some_map.toStart()

new_map = deep_copy(some_map)

some_map.toStart()
new_map.toStart()


some_map.show()
print("\n")
new_map.show()


validate(some_map, new_map)