# Request Flow
User
↓
CLI
↓
Parser
↓
If Built-in Command
    Execute locally
Else
↓
Collect Context
↓
Cloud
↓
Display Response


# AI Communication Protocol

## Overview

The Terminal Agent communicates with the AI in iterative rounds.

Each round follows this flow:

User Request
      ↓
Collect Context
      ↓
Send Request to AI
      ↓
Receive Execution Plan
      ↓
Execute Commands
      ↓
Collect Results
      ↓
Send Results Back to AI
      ↓
Repeat until AI returns the final response.

---

## Execution Plan

The AI does not execute commands.

It only generates an execution plan.

The CLI is responsible for executing commands.

Each command contains:

- Reason
- Command
- Execution Policy

Example:

Step 1
Reason:
Check project directory.

Command:
pwd

---

Step 2
Reason:
Install missing dependencies.

Command:
npm install

---

## Command Results

By default, the CLI sends only:

- Command
- Exit Code

Example:

pwd
Exit Code: 0

npm install
Exit Code: 1

No stdout or stderr is sent unless explicitly requested by the AI.

---

## Additional Information Request

If the AI requires more information, it must explicitly request it.

Example:

Request stderr:
- npm install

Request stdout:
- git status

Request files:
- package.json

The CLI only returns the requested data.

---

## Session Memory

The CLI maintains session memory during the entire task.

Memory includes:

- Original user request
- Commands executed
- Exit codes
- Requested outputs
- AI reasoning history (internal)
- Current execution state

The AI should continue from the existing session instead of starting over.

---

## Completion

The AI completes the task by returning:

Step: 0

Message:
<Task completed successfully>

No further commands are executed after Step 0.