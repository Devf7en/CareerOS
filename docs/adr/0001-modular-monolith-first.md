# ADR-0001: Start CareerOS as a Modular Monolith
**Status:** Accepted for initial foundation  
**Date:** 2026-10-31

## Context
CareerOS spans connected domains, but the product is at foundation stage. Premature distribution adds deployment, observability, consistency and security overhead before boundaries and workloads are validated.

## Decision
Start with a modular monolith using explicit domain boundaries, stable interfaces, versioned schemas and independently testable application services. Keep AI/analytics workloads and workflow orchestration separable behind interfaces where useful.

## Consequences
**Positive:** faster end-to-end delivery, simpler local development and easier transactional consistency.

**Trade-offs:** module boundaries require discipline; independent scaling is not an initial capability; background workloads may need separate workers as demand grows.

## Revisit when
A module demonstrates independent scaling, deployment, security or reliability requirements that outweigh distributed-system complexity.
