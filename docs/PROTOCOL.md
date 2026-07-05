## Memory Rule

The CLI always stores complete execution data.

The AI never receives complete execution data by default.

The AI explicitly requests any additional information
(stdout, stderr, files, or previous outputs) when required.

The CLI retrieves the requested data from session memory
without re-executing commands.


"""
Defines the communication protocol
between the CLI and the AI.
"""
