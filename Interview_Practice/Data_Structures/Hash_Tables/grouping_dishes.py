"""Grouping dishes.

Given a list dishes, where each element consists of a list of
strings beginning with the name of the dish, followed by all
the ingredients used in preparing it. Group the dishes by ingredients,
so that for each ingredient you'll be able to find all the dishes that
contain it (if there are at least 2 such dishes).

Return an array where each element is a list beginning with the ingredient
name, followed by the names of all the dishes that contain this ingredient.
The dishes inside each list should be sorted lexicographically, and the result
array should be sorted lexicographically by the names of the ingredients.
"""


def groupingDishes(dishes):
    """Return the array conatining the grouped dishes."""
    # Dictionary ingredients as keys and dishes as values.
    answer = dict()
    for dish in dishes:
        for item in dish[1:]:
            answer.setdefault(item, []).append(dish[0])

    # Sort each value (dishes) in lexicographic order and
    # prepend key (ingredient) to the value (dishes).
    for key, values in answer.items():
        answer[key] = sorted(answer[key])
        answer[key].insert(0, key)

    # Get a list of values from the hash table, and sort it.
    # It should sort by the first element (i.e. the ingredient) first.
    answer = sorted(list(answer.values()))

    # Ignore the ingredient if it is in less than two dishes.
    tmp = []
    for sub_list in answer:
        if len(sub_list) > 2:
            tmp.append(sub_list)
    return tmp


def tests():
    """Sample Tests."""
    samples = [([["Salad", "Tomato", "Cucumber", "Salad", "Sauce"],
                ["Pizza", "Tomato", "Sausage", "Sauce", "Dough"],
                 ["Quesadilla", "Chicken", "Cheese", "Sauce"],
                 ["Sandwich", "Salad", "Bread", "Tomato", "Cheese"]],
                [["Cheese", "Quesadilla", "Sandwich"],
                 ["Salad", "Salad", "Sandwich"],
                 ["Sauce", "Pizza", "Quesadilla", "Salad"],
                 ["Tomato", "Pizza", "Salad", "Sandwich"]])]
    for dishes, expected_output in samples:
        if groupingDishes(dishes) != expected_output:
            print(dishes)


if __name__ == "__main__":
    tests()
