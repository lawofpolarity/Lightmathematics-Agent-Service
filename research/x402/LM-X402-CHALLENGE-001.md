# LM-X402-CHALLENGE-001

**Status:** Observed production/testnet experiment  
**Date:** 2026-10-02  
**Environment:** Production service boundary; Base Sepolia settlement network  
**Scope:** Challenge issuance only; no payment executed

## Purpose

This report records the first observed production issuance of an x402 payment challenge by the LightMathematics agent-facing service. It documents protocol-level behavior and the semantic-governance boundary without disclosing private credentials, protected runtime configuration, proprietary population-generation methods, or security-sensitive implementation details.

## Observation

An unsigned request to the production semantic verification resource returned:

- HTTP status: `402 Payment Required`
- x402 version: `2`
- scheme: `exact`
- network: Base Sepolia (`eip155:84532`)
- asset: USDC
- required amount: 10,000 atomic units ($0.01 USDC)
- validity window: 300 seconds
- nonce: none supplied

The response stated that payment was required before semantic eligibility would be evaluated.

The eligibility receipt reported:

- `payment.required = true`
- `payment.verified = false`
- `payment.testnetOnly = true`
- `payment.serviceEligibility = false`

No `PAYMENT-SIGNATURE` was supplied. No payer credential was used. No facilitator verification, settlement, blockchain transaction, persistent payment receipt, or semantic evaluation occurred.

## Observed invariant: pre-settlement semantic isolation

In the tested production configuration, issuance of an economic challenge did not constitute semantic authorization. Before payment verification, semantic service eligibility remained false and semantic evaluation was not performed.

The observed transition was:

`REQUEST -> PAYMENT_REQUIRED -> [authorization not exercised]`

The intended subsequent experimental path is:

`PAYMENT_REQUIRED -> AUTHORIZED -> VERIFIED -> SETTLED -> SEMANTIC_EVALUATION -> RECEIPT`

The subsequent path is **not established by this report** and requires a separate end-to-end experiment.

## Governance interpretation

The experiment supports a separation between two distinct layers:

1. **Economic/service authorization** — whether the requester has satisfied the terms required to invoke a service.
2. **Semantic authority** — what the evidence, provenance, dependencies, currentness, unresolved obligations, and applicable governance rules permit the service to conclude.

Payment is therefore not evidence and does not itself increase semantic authority. A future successful payment may establish eligibility to execute an evaluation; it must not determine the semantic result.

## What this experiment establishes

This experiment establishes that the production service can expose machine-readable economic terms before semantic execution and can withhold semantic service eligibility while payment remains unverified.

It does **not** establish successful payment authorization, facilitator verification, settlement, paid semantic execution, commercial readiness, or superiority over other systems.

## Disclosure boundary

This public record intentionally omits:

- private keys and private JWK material;
- protected environment values and authentication credentials;
- payer credentials and unnecessary payer-identifying operational detail;
- internal deployment/security topology;
- security-sensitive middleware and gate implementation details;
- unpublished semantic-population construction methods;
- proprietary transformation/scoring machinery;
- private corpus structure.

Public blockchain/protocol identifiers may be disclosed separately when needed for independent verification of a completed end-to-end experiment.

## Next experiment

A separate record, provisionally **LM-X402-E2E-001**, should be created only after an independently authorized testnet payment completes the sequence from challenge through verification and settlement to governed semantic execution.

The principal invariant to test is:

> Economic authorization may change service eligibility; it must not change semantic authority.

That experiment should preserve sufficient private evidence to audit the transaction while publishing only the minimum protocol and semantic evidence required to support its conclusions.
