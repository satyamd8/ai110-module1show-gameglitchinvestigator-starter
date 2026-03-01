# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").

The first bug I noticed had to do with submitting a guess. When typing a number in the input box, it said "Press Enter to apply". If I pressed the Enter button instead of clicking the submit button, it would log the guess in the Dev Debug Info but not count it as a guess. 

Another bug I noticed was with the hints. With each guess, it's meant to give a hint whether your guess was too high or too low. However, after the first guess, the hint always remained the same and seemed like it didn't reflect the current guess. For example, if I guessed 10 and the hint said "Go lower", even if I guessed 1 which is the lower bound, it would still say to go lower.

A third bug had to do with creating a new game after winning. After correctly guessing the number on one game, it prompted me to start a new game which I tried to do. The button was unresponsive and would not create a new game.

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

The first AI suggestion I received (GPT-4.1) was for fixing the check_guess logic. I pointed out how the game seemed to give the wrong hint when guessing. It pointed out how the input guess was being cast as a string before being checked by the check_guess function, leading to wonky results. After fixing it by removing the string casting, I tried testing it by playing the game again and it still wasn't working properly. After asking AI why it still wasn't working, it pointed out the return statements themselves were inversed, so if you guessed too high it would say to guess higher. After fixing it, I tested the game again and the hints worked properly. 

The second AI suggestion I received was for the new game button not working after winning a game. It stated that the issue came from how the game state variables were being reset when calling the new_game function. It said that we were resetting attempts to 0 instead of 1 which was the default start. We also didn't factor in difficulty ranges when resetting the secret number, and other variables of score, history, and status weren't reset. After correcting how new_game was called, I tested it by winning a game and clicking the new game button, which worked. 

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

After each specific bug fix that the Copilot agent did, I ran the streamlit app and manually tried to recreate the bug to see if it was resolved. By doing this, I was able to see that the first fix for the wrong hints didn't work properly, so I was able to go back and fix it again. After fixing both bugs and refactoring the core logic to logic_utils.py, I followed the instructions to have Copilot generate test cases in test_game_logic.py. These tests tested different edge cases regarding both the hints and resetting game states. 

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

The number might have changed because it was being regenerated as the Streamlit app was refreshing. When interacting with certain elements, Streamlit reruns the entire script, which would rerun the function that generates the secret number. This was fixed by using a session state variable to store the number, which only regenerates when starting a new game. 

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

One habit/strategy I'd continue to use is the manual testing of certain bugs. Obviously it's hard to do for certain tests, but when minimal, manually testing allows me to see if I'm able to encounter the bug from the perspective of a user, therefore verifying if the bug is truly resolved. One thing I'd do differently is to check the corrected functions more deeply. Going back to the wrong hints bug, if I were to look at the check_guess function a bit more closely, I would have identified the wrong return statements myself rather than having to ask Copilot to check the logic again. My initial thoughts on AI generated code definietely haven't changed, since I've always believed that you have to be a close observer of any generated code due to how often it may mess up.