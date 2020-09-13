scenes = [
    "Visiting a Grocery Store",
    "Hanging out with 2 people outdoor",
    "Attending an indoor party, wedding with 50 people for 3 hours",
    "Car ride with driver for 30 minutes with windows open",
    "Eating in a restaurant indoors with 15 people for 90 minutes",
    "Taking a plane ride with 20 people for 150 minutes"
]
distances = ["3 feet", "6 feet", "12 feet"]
masks = ["No one wearing", "You are wearing", "All are wearing"]
talks = ["Not talking at all", "Normal conversation", "Talking Loudly"]


def printOnCalled(list_of_items, input_statement):
    count = 0
    for item in list_of_items:
        count += 1
        print(str(count)+".", item)
    scene_select = input(input_statement)


printOnCalled(scenes, "Please select the scenario: ")
printOnCalled(distances, "Enter the distance maintained: ")
printOnCalled(masks, "Select how the masks are being worn: ")
printOnCalled(talks, "Are people talking?: ")
