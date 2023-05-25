# constructor_AFN
Small application that allows building automata over a language.

# Context:

The automaton that utilizes epsilon transitions is known as an epsilon-NFA (Nondeterministic Finite Automaton) or NFA with epsilon moves. In this type of automaton, in addition to regular transitions based on input symbols, special transitions called epsilon transitions (ε) are allowed.

An epsilon transition allows the automaton to change state without consuming any input symbol. In other words, the automaton can make an epsilon transition even if there is no input symbol present at that moment. This provides an additional capability for the automaton to "jump" between states without necessarily consuming an input symbol.
