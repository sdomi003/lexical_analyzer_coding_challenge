# written by u/jiri-n on reddit. 
# this is a condensed version of the FSM implementation.


def advanced_state_machinery(txt: str):
    state = 0
    for i, ch in enumerate(txt):
        next_state = 2 if state == 2 else 0
        fn_check = str.isalpha if state in (0, 1, 5, 6) else str.isdigit
        state = state + 1 if fn_check(ch) else next_state
        if state > 6:
            state = 2
            yield (i - 6, txt[i - 6:i + 1]) 
s = "AB123CD123EF123GHAB120BZ"
i = None
for i in advanced_state_machinery(s):
	print(i)


