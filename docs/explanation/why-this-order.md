# Why the phases are in this order

Which skill to use is answered by the `development-lifecycle` router, or by [reference/catalog.md](../reference/catalog.md).
This page answers a different question: why the phases run in the order they do.

The rule is that a decision costs less to change the earlier it is written down.
Each phase is a point where one class of mistake is still cheap to correct.

## What each phase settles

| Phase | Settles | Cost of skipping it |
|---|---|---|
| Orientation | How this project works and where the change belongs | The change fights existing conventions, or duplicates code that already exists |
| Requirements | What "done" means, in writing | The dispute arrives at review time, and nothing written down settles it |
| Architecture and design | Structure, interfaces, data model, anything touching auth, secrets, personal data, money or untrusted input | The next person cannot tell a deliberate trade-off from an accident, and reverses it |
| Planning | Task order, and what will be tested at which level | Test level gets decided under implementation pressure, where the fastest test to write wins |
| Implementation | The code | — |
| Debugging and performance | Why something is wrong, measured before it is changed | A fix aimed at the wrong cause |
| Verification | That the commands were run and the output read | A review cycle, or a release, spent on something that does not work |
| Review | What the change exposes, and what any new dependency brings | — |
| Release | Instrumentation, then the gate, then confirmation in production | Instrumentation cannot be added during an incident, and whatever was emitted before the failure is all the information there will be |
| Operations | Service restored first, understood second | Diagnosis while users are affected turns a five-minute problem into an hour-long one |

Two items are worth stating plainly.

The decision record is what carries reasoning forward, and reasoning is the part that decays fastest.
It belongs to design but is read during review, months later.

The postmortem is how an incident's cost buys something.
Skipping it when everyone is tired is how the same incident happens twice, and how the first postmortem's action items are discovered to have never been done.

## Where the order does not hold

A failed check returns to implementation, not forward.
A reviewer asking "why is it built this way?" usually means a decision record is missing.
Postmortem action items are requirements and belong in the same backlog as features.
"We could not tell what was happening" is the most common postmortem finding, and its fix ships with the next change.
