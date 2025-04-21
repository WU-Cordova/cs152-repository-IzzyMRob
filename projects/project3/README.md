## Class Implementations
**Menu**
- A list of strings
- Looping through any structure has a linear complexity, so any choice here would have been the same in that regard. Indexing a list has a constant complexity. A list is relatively small in computer storage, and we don't need access to any operations besides iterating and indexing. This makes a list a simple and compact choice.

**Customer Order**
- A custom class
- Contains `cust_name`, a string representing the name of the customer who ordered it.
- Contains `order`, an `Array` of `Drink` objects representing the items ordered.
- Again we need to iterate through the drinks in the order, as well as be able to add new ones to it. Iterating still has linear complexity, while appending has constant complexity. Because Arrays support fast appending and can grow dynamically it was the best choice for this.

**Open Orders Queue**
- A `CircularQueue` of `CustomerOrder` objects
- The orders made follow the First-In-First-Out principle, which is built into the `CircularQueue` with `enqueue` and `dequeue`. Both methods are constant time, and iterating is linear. 

**Completed Orders**
- An `Array` of `CustomerOrder` objects
- Again, we need to be able to iterate (linear) and append (constant) to this structure, so an Array was the best choice.

## How to Run
1. Hit the button you told us to hit.

## Sample Runs


## Issues to be aware of
- The in_progress_orders Queue is initialized with a max size of 10 objects, meaning if there are more than 9 open orders at a time no new ones can be added.

## Future Aspirations
- I would love to add more fluidity in ordering, like a way to go back and edit/cancel orders that haven't been completed yet.