from modules.translate_myanmar import translate_myanmar_to_english
from extras.expansion import FooocusExpansion
import random

def expand_myanmar_prompt(user_prompt):
    """
    1. Translate Myanmar prompt to English
    2. Use FooocusExpansion to expand the prompt
    3. Return expanded prompt (English)
    """
    # Step 1: Translate
    en_prompt = translate_myanmar_to_english(user_prompt)
    # Step 2: Expand
    expander = FooocusExpansion()
    seed = random.randint(0, 999999)
    expanded = expander(en_prompt, seed)
    return expanded
