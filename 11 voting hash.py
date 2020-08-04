# Голосование, используя хеш-таблицы (словари).
# Используя словарь, здесь мы отслеживаем проголосовавших избирателей и не позволяем им голосовать,
# а также заносим в словарь тех избирателей, кто еще не проголосовал и позволяем им голосовать.
# ----------
# Voting using hash table (dictionaries).
# Using the dictionary, here we track the voters who voted and do not allow them to vote,
# and we also enter into the dictionary those voters who have not yet voted and allow them to vote.


# Создаем словарь (это хеш-таблица в Python) "voted", который хранит список проголосовавших избирателей.
# Хеш-таблица это тип структуры данных, который представляет из себя массив,
# элементы которога содержат пары "ключ : значение".
# При помощи хеш-функции можно получить доступ к значению, обратившись к его ключу.
# ----------
# Create the dictionary (this is a hash table in Python) "voted", that stores the list of voters who voted.
# A hash table is a type of data structure, that is an array whose elements contain pairs "key : value".
# Using a hash function, you can access a value by referring to its key.
voted = {}


# Создаем функцию "check_voter", которая принимает один входной параметр:
# переменная "voter_name", которая содержит ключ, обозначающий имя избирателя.
# ----------
# Create the function "check_voter" that accepts one parameter:
# the variable "voter_name" that contains a key representing the voter's name.
def check_voter(voter_name):
    # При помощи функции "get" пытаемся получить значение, обращаясь к указанному ключу "voter_name".
    # Если указанный ключ "voter_name" есть в словаре "voted", то это означает,
    # что избиратель уже проголосовал и нам необходимо не позволить ему голосовать.
    # Функция "print()" выводит некую указанную информацию на экран или на какое-либо другое устройство вывода.
    # ----------
    # Using the function "get", we try to get the value by referring to the specified key "voter_name".
    # If the specified key "voter_name" is in the dictionary "voted",
    # then it means that the voter has already voted and we need to not allow him to vote.
    # The function "print()" prints the specified message to the screen, or other standard output device.
    if voted.get(voter_name):
        print("Get out!")
    # Если указанный ключ "voter_name" отсутствует в словаре "voted", то функция "get" возвращает "None".
    # Это означает, что избиратель голосует первый раз, поэтому
    # нам необходимо позволить ему проголосовать и занести имя этого избирателя в словарь "voted",
    # внеся значение "True" путем обращения к ключу "voter_name".
    # ----------
    # If the specified key "voter_name" is not in the dictionary "voted", then the function "get" returns "None".
    # This means that the voter votes for the first time, so we need to allow him to vote
    # and add the name of this voter to the dictionary "voted",
    # adding the value "True" by referring to the key "voter_name".
    else:
        voted[voter_name] = True
        print("You can vote!")


# Пользователь Shepard пытается проголосовать первый раз.
# ----------
# User Shepard tries to vote the first time.
print("User Shepard tries to vote the first time:")
check_voter("Shepard")

# Пользователь Wrex пытается проголосовать первый раз.
# ----------
# User Wrex tries to vote the first time.
print("User Wrex tries to vote the first time:")
check_voter("Wrex")

# Пользователь Wrex пытается проголосовать снова.
# ----------
# User Wrex tries to vote again.
print("User Wrex tries to vote again:")
check_voter("Wrex")

# Пользователь Grunt пытается проголосовать первый раз.
# ----------
# User Grunt tries to vote the first time.
print("User Grunt tries to vote the first time:")
check_voter("Grunt")

# Пользователь Shepard пытается проголосовать снова.
# ----------
# User Shepard tries to vote again.
print("User Shepard tries to vote again:")
check_voter("Shepard")
