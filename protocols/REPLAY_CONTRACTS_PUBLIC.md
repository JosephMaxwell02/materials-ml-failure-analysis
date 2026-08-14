# Public Replay Contracts

Replay is judged through separable contracts: raw byte identity, semantic metadata
identity and frozen numerical equivalence. A route may pass numerical replay while
failing byte identity, and adverse differences remain visible. Resume preserves an
interrupted execution identity; replay uses a separately identified execution and is
not interchangeable with resume.
