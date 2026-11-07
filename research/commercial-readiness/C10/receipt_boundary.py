"""Experimental C10 operation-bound receipt gate; trusted callbacks are required."""
import hashlib
import json

def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(',', ':'), allow_nan=False).encode('utf-8')

def _identifier(value):
    """Reject ambiguous/non-text identifiers before invoking trusted callbacks."""
    return (type(value) is str and 0 < len(value) <= 512
            and not any(ord(char) < 32 or ord(char) == 127 for char in value))

def verify(request, receipt, *, authenticate, authorize, verify_signature, current):
    denied = {'decision': 'REFUSE', 'authenticated_reliance': False}
    if not isinstance(request, dict) or not isinstance(receipt, dict):
        return denied
    try:
        required = ('caller', 'operation', 'scope', 'evidence', 'dependency_token')
        if any(not _identifier(request.get(k)) for k in ('caller', 'operation', 'scope', 'dependency_token')) or 'evidence' not in request:
            return denied
        if any(not _identifier(receipt.get(k)) or receipt[k] != request[k] for k in ('caller', 'operation', 'scope', 'dependency_token')):
            return denied
        if receipt.get('evidence_sha256') != hashlib.sha256(canonical(request['evidence'])).hexdigest():
            return denied
        if (receipt.get('decision') != 'ALLOW' or receipt.get('canonical_admission') is not False
                or not _identifier(receipt.get('signature'))):
            return denied
        if authenticate(request['caller']) is not True:
            return denied
        if authorize(request['caller'], request['operation'], request['scope']) is not True:
            return denied
        signed = {k: receipt[k] for k in ('caller', 'operation', 'scope', 'dependency_token', 'evidence_sha256', 'decision', 'canonical_admission')}
        if verify_signature(canonical(signed), receipt.get('signature')) is not True:
            return denied
        if current(request['dependency_token']) is not True:
            return {'decision': 'STALE', 'authenticated_reliance': False}
        return {'decision': 'ALLOW', 'authenticated_reliance': True}
    except Exception:
        return denied
