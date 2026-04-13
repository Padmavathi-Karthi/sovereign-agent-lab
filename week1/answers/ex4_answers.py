"""
Exercise 4 — Answers
====================
Fill this in after running exercise4_mcp_client.py.
"""

# ── Basic results ──────────────────────────────────────────────────────────

# Tool names as shown in "Discovered N tools" output.
TOOLS_DISCOVERED = ["search_venues", "get_venue_details"]

QUERY_1_VENUE_NAME    = "none"
QUERY_1_VENUE_ADDRESS = "none"
QUERY_2_FINAL_ANSWER  = "The agent did not produce a final natural-language answer in my run. It only emitted a search_venues function call for a venue for 300 people with vegan options."

# ── The experiment ─────────────────────────────────────────────────────────
# Required: modify venue_server.py, rerun, revert.

EX4_EXPERIMENT_DONE = True   # True or False

# What changed, and which files did or didn't need updating? Min 30 words.
EX4_EXPERIMENT_RESULT = """

I changed The Albanach's status from available to full, reran the Exercise 4 client, and then reverted the change.
In my run, I did not see a visible difference in the terminal output. The discovered tools stayed the same, and
the printed trace still only showed the search_venues tool call rather than a full final answer. This still showed
the key MCP idea: I changed shared server-side data without changing the client agent code.

"""

# ── MCP vs hardcoded ───────────────────────────────────────────────────────

LINES_OF_TOOL_CODE_EX2 = 4   # count in exercise2_langgraph.py
LINES_OF_TOOL_CODE_EX4 = 0   # count in exercise4_mcp_client.py

# What does MCP buy you beyond "the tools are in a separate file"? Min 30 words.
MCP_VALUE_PROPOSITION = """

MCP gives a shared tool interface, not just a separate file. The client can discover tools dynamically from the
server, so the agent code does not need hardcoded venue logic. That makes it easier to reuse the same tools across
multiple systems and update the server in one place instead of editing every agent that depends on it.

"""

# ── Week 5 architecture ────────────────────────────────────────────────────
# Describe your full sovereign agent at Week 5 scale.
# At least 5 bullet points. Each bullet must be a complete sentence
# naming a component and explaining why that component does that job.

WEEK_5_ARCHITECTURE = """

- A front-door router should classify whether the request is exploratory research or a tightly controlled operational task.
- A LangGraph research agent should handle open-ended work like venue comparison, weather checks, cost estimation, and planning because it can loop through tools flexibly.
- A structured digital employee should handle booking confirmation, escalation, and policy checks because those decisions need deterministic business rules.
- A shared MCP server should expose venue search and venue detail tools so both agent types can use the same operational capabilities.
- A common data and policy layer should store venue status, constraints, and limits so updates happen in one place and stay consistent across the whole system.

"""

# ── The guiding question ───────────────────────────────────────────────────
# Which agent for the research? Which for the call? Why does swapping feel wrong?
# Must reference specific things you observed in your runs. Min 60 words.

GUIDING_QUESTION_ANSWER = """

The research work fits the LangGraph agent better, and the phone-call confirmation fits the structured employee better.
In my runs, LangGraph was better suited to searching and coordinating multiple tools, even though some outputs were messy
or incomplete. In contrast, the Exercise 3 assistant was narrow, consistent, and good at enforcing rules like the GBP300
deposit limit and the cutoff guard. Swapping them feels wrong because the research task needs flexibility and tool-driven
exploration, while the call-handling task needs predictability, auditability, and strict control over what can be said
or confirmed.

"""
