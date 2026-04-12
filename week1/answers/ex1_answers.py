"""
Exercise 1 — Answers
====================
Fill this in after running exercise1_context.py.
Run `python grade.py ex1` to check for obvious issues before submitting.
"""

# ── Part A ─────────────────────────────────────────────────────────────────

# The exact answer the model gave for each condition.
# Copy-paste from your terminal output (the → "..." part).

PART_A_PLAIN_ANSWER    = "The Haymarket Vaults"
PART_A_XML_ANSWER      = "The Albanach"
PART_A_SANDWICH_ANSWER = "The Albanach"

# Was each answer correct? True or False.
# Correct = contains "Haymarket" or "Albanach" (both satisfy all constraints).

PART_A_PLAIN_CORRECT    = True  # True or False
PART_A_XML_CORRECT      = True
PART_A_SANDWICH_CORRECT = True

# Explain what you observed. Minimum 30 words.

PART_A_EXPLANATION = """

The plain prompt still got a correct answer, but the structured formats were cleaner and more consistent.
XML and sandwich formatting made the constraints easier for the model to separate and follow.
The main thing I observed is that clearer structure reduces ambiguity and makes the model less likely
to miss one of the booking conditions.

"""

# ── Part B ─────────────────────────────────────────────────────────────────

PART_B_PLAIN_ANSWER    = "The Haymarket Vaults"
PART_B_XML_ANSWER      = "The Albanach" 
PART_B_SANDWICH_ANSWER = "The Albanach" 

PART_B_PLAIN_CORRECT    = True
PART_B_XML_CORRECT      = True
PART_B_SANDWICH_CORRECT = True

# Did adding near-miss distractors change any results? True or False.
PART_B_CHANGED_RESULTS = True

# Which distractor was more likely to cause a wrong answer, and why?
# Minimum 20 words.
PART_B_HARDEST_DISTRACTOR = """

The near-miss distractor with similar capacity or features was more likely to cause a wrong answer because
it looked almost correct at a glance. When options are very similar, weaker formatting makes it easier for
the model to confuse “close enough” with “actually satisfies every condition.”

"""

# ── Part C ─────────────────────────────────────────────────────────────────

# Did the exercise run Part C (small model)?
# Check outputs/ex1_results.json → "part_c_was_run"
PART_C_WAS_RUN = True   # True or False

PART_C_PLAIN_ANSWER    = "The Haymarket Vaults"
PART_C_XML_ANSWER      = "The Haymarket Vaults"
PART_C_SANDWICH_ANSWER = "The Haymarket Vaults"

# Explain what Part C showed, or why it wasn't needed. Minimum 30 words.
PART_C_WAS_RUN = True

PART_C_EXPLANATION = """

Part C showed how a smaller model can be more sensitive to prompt structure. Even when the answer stayed
correct, the more structured formats helped the model stay focused on the exact constraints. This suggests
that context engineering matters even more when model capability is lower.

"""

# ── Core lesson ────────────────────────────────────────────────────────────

# Complete this sentence. Minimum 40 words.
# "Context formatting matters most when..."

CORE_LESSON = """

Context formatting matters most when the task includes multiple constraints, distractors, or conditions that
must all be checked together. In those cases, structure helps the model separate relevant facts from noise,
follow instructions more reliably, and avoid choosing answers that are only partially correct.

"""
