Beatles = []
Beatles.append("John Lennon")
Beatles.append("Paul Mcartney")
Beatles.append("George Harrison")
print(Beatles)

for new_member in ["Stu Sutcliffe", "Pete Best"]:
    user_input = input(f"Add the member {new_member} to the list (y/n)? ")
    if user_input.lower() == 'y':
        Beatles.append(new_member)
        print(Beatles)

Beatles.remove('Stu Sutcliffe')
Beatles.remove('Pete Best')
print(Beatles)
Beatles.insert(0, 'Ringo Star')

print(Beatles)