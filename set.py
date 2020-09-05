from faker import Faker

set_1 = {"s", "a", "c", "h", "h", "a", "s"}
set_1.add("s")

print(set_1)

fake = Faker()

print("Name - {}".format(fake.name()))

list_ = list()

for _ in range(100):
    list_.append(fake.name())

print("Count of fake names in the list :- {}".format(len(list_)))

set_2 = set(list_)

print("Count of fake names in the set :- {}".format(len(set_2)))
