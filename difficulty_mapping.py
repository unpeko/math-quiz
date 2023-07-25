import easy

# difficulty_mapping.py
  # author: luka
  # date: Jun 24, 2023
  # math quiz chanlange def
  # v2.1
# Define the difficulty-to-index mapping function
def get_index(difficulty):
    if difficulty == "easy":
      
      easy.questions()
      
    elif difficulty == "medium":
        return 2
    elif difficulty == "hard":
        return 3
    else:
        raise ValueError("Invalid difficulty level. Please choose from Easy, Medium, or Hard.")
