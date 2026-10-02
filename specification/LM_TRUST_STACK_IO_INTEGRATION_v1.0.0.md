# LM Trust Stack .io Integration v1.0.0

Status: implementation contract

Lightmathematics-Agent-Service is currently a specification/research repository,
not a deployable web runtime. This contract therefore defines the machine-facing
adapter without claiming that lightmathematics.io has been deployed from this
repository.

## Upstream

Trust API base: configured server-side.
Authentication: bearer/JWT supplied server-side.

## Mapping

Agent Service capability discovery -> GET /v1/capabilities
Artifact inspection -> GET /v1/artifacts/{id}/status
History -> GET /v1/artifacts/{id}/history
Reliance request -> POST /v1/reliance/qualify
Transition validation -> POST /v1/transitions/verify
Receipt lookup -> GET /v1/receipts/{id}

## Invariants

Payment authorization does not change semantic authority.
Agent identity does not change semantic authority.
External attestation does not change semantic authority.
NOT_EVALUATED is preserved and MUST NOT be mapped to ALLOW.

## Deployment requirement

Before .io activation, create a runtime that:
1. keeps Trust credentials server-side;
2. validates request/response schemas;
3. exposes version/capability metadata;
4. preserves x402 pre-settlement semantic isolation;
5. logs safe OpenTelemetry identifiers only.
