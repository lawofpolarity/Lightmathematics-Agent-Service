"""Experimental C10 operation-bound receipt gate; trusted callbacks are required."""
import hashlib
import json

def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(',', ':'), allow_nan=False).encode('utf-8')

def verify(request, receipt, *, authenticate, authorize, verify_signature, current):
    denied = {'decision': 'REFUSE', 'authenticated_reliance': False}
    if not isinstance(request, dict) or not isinstance(receipt, dict):
        return denied
    try:
        required = ('caller', 'operation', 'scope', 'evidence', 'dependency_token')
        if any(not request.get(k) for k in required):
            return denied
        if any(receipt.get(k) != request[k] for k in ('caller', 'operation', 'scope', 'dependency_token')):
            return denied
        if receipt.get('evidence_sha256') != hashlib.sha256(canonical(request['evidence'])).hexdigest():
            return denied
        if receipt.get('decision') != 'ALLOW' or receipt.get('canonical_admission') is not False:
            return denied
        if not authenticate(request['caller']):
            return denied
        if not authorize(request['caller'], request['operation'], request['scope']):
            return denied
        signed = {k: receipt[k] for k in ('caller', 'operation', 'scope', 'dependency_token', 'evidence_sha256', 'decision', 'canonical_admission')}
        if not verify_signature(canonical(signed), receipt.get('signature')):
            return denied
        if not current(request['dependency_token']):
            return {'decision': 'STALE', 'authenticated_reliance': False}
        return {'decision': 'ALLOW', 'authenticated_reliance': True}
    except Exception:
        return denied
