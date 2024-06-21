"""
Given a list of structs, a struct have the following fields type, name, quantity, cost.
The type can be either Fizz or Buzz, for Fizz there is integer cost and for Buzz the cost is always 0. A transcation happens from Fizz to Buzz.
Print all the transactions that can happen with minimum cost.

Note:

We need to did the transaction in a first come first serve basis assuming streamed inputs.
The output should be "FizzBuzz! quantity From(name)
(name) cost" where no duplicates are allowed.
There won't be any negative cost values.
example:
Input:
[
{
type : "Fizz",
name: "Alice",
quantity: 2,
cost: 10
},
{
type : "Fizz",
name: "Catherine",
quantity: 3,
cost: 5
},
{
type : "Buzz",
name: "Bob",
quantity: 7,
cost: 0
},
{
type : "Fizz",
name: "Alice",
quantity: 5,
cost: 8
}
]

Output:
FizzBuzz! 3 Catherine 15
FizzBuzz! 4 Alice 36

Explanation:
First transaction from Catherine to Bob! quantity -> 3, cost -> (3 x 5) = 15
Second transaction from Alice to Bob! quantity -> 2, cost -> (2 x 10) = 20
Third transaction from Alice to Bob! quantity -> 2, cost -> (2 x 8) = 16

"""
#import deque
from collections import deque

def transaction(transactions):
    fizz = deque() #(name, quantity, cost)
    buzz = deque() #(name, quantity)
    processed = {}
    prev_cost = 0
    result = []
    for transaction in transactions:
        # add fizz, and buzz queue
        t_type= transaction["type"]
        name = transaction["name"]
        quantity = transaction["quantity"]
        cost = transaction["cost"]
        if t_type == "Fizz":
            fizz.append((name, quantity, cost))
        elif t_type == "Buzz":
            buzz.append((name, quantity))
        
        while fizz and buzz:
            print(fizz, buzz)
            fizz_name, fizz_q, fizz_cost = fizz[0]
            buzz_name, buzz_q = buzz[0]
            #if visited delete it
            if (fizz_name, buzz_name) in processed:
                print(processed)
                prev_cost = processed[(fizz_name, buzz_name)]
                result = result[1:]

            #calutale transaction quantity
            trans_q = min(fizz_q, buzz_q)
            trans_cost = (trans_q * fizz_cost) + prev_cost #transcation cost = min quantity * cost
            result.append([f"FizzBuzz! {trans_q} From({fizz_name}):To({buzz_name}) {trans_cost}"])

            # calculate current 
            fizz_q -= trans_q
            buzz_q -= trans_q

            if fizz_q == 0 : fizz.popleft()
            else: fizz[0] = (fizz_name, fizz_q, fizz_cost)

            if buzz_q == 0 : buzz.popleft()
            else: buzz[0] = (buzz_name, buzz_q)
            processed[(fizz_name, buzz_name)] = trans_cost
    return result







transactions = [
{ "type" : "Fizz", "name": "Alice", "quantity": 2, "cost": 10},
{ "type" : "Fizz", "name": "Catherine", "quantity": 3, "cost": 5},
{ "type" : "Buzz", "name": "Bob", "quantity": 7, "cost": 0},
{ "type" : "Fizz", "name": "Alice", "quantity": 5, "cost": 8}
]

print(transaction(transactions))