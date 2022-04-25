from pprint import pprint
import inquirer

questions = [
    inquirer.List(
        "size",
        message="What size do you need?",
        choices=[None, "Jumbo", "Large", "Standard", "Medium", "Small", "Micro"],
    ),
    inquirer.List(
        "type",
        message="What size do you need?",
        choices=["Jumbo", "Large", "Standard", "Medium", "Small", "Micro"],
    ),
]

answers = inquirer.prompt(questions)
pprint(answers)
