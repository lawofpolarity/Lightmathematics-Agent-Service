# Trust Stack integration cases

1. Unknown artifact + operation -> NOT_EVALUATED or not-found; never ALLOW.
2. Σ152 research.reference -> NOT_EVALUATED.
3. Successful payment + NOT_EVALUATED semantic state -> NOT_EVALUATED.
4. Agent identity present + NOT_EVALUATED semantic state -> NOT_EVALUATED.
5. Missing Trust credential -> fail closed.
6. Trust API unavailable -> fail closed; no cached ALLOW.
7. Transition dropping unresolved obligation without discharge -> invalid.
8. Runtime response includes Trust Stack/schema version.
