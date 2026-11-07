import hashlib
import unittest
from receipt_boundary import canonical, verify

class BoundaryTests(unittest.TestCase):
    def setUp(self):
        self.req = dict(caller='agent-1', operation='read', scope='wheel:1', evidence={'x': 1}, dependency_token='v1')
        self.receipt = dict(caller='agent-1', operation='read', scope='wheel:1', dependency_token='v1', evidence_sha256=hashlib.sha256(canonical({'x':1})).hexdigest(), decision='ALLOW', canonical_admission=False, signature='synthetic')
        self.callbacks = dict(authenticate=lambda c:c=='agent-1', authorize=lambda c,o,s:(o,s)==('read','wheel:1'), verify_signature=lambda b,s:s=='synthetic', current=lambda t:t=='v1')
    def check(self, expected='REFUSE'):
        self.assertEqual(verify(self.req,self.receipt,**self.callbacks)['decision'],expected)
    def test_valid_synthetic_callbacks(self): self.check('ALLOW')
    def test_altered_evidence(self): self.req['evidence']={'x':2}; self.check()
    def test_wrong_operation(self): self.req['operation']='write'; self.check()
    def test_wrong_scope(self): self.req['scope']='wheel:2'; self.check()
    def test_unauthorized_caller(self): self.req['caller']='intruder'; self.check()
    def test_invalid_signature(self): self.receipt['signature']='forged'; self.check()
    def test_stale(self): self.callbacks['current']=lambda t:False; self.check('STALE')
    def test_unsigned(self): self.receipt.pop('signature'); self.check()
    def test_admission_claim(self): self.receipt['canonical_admission']=True; self.check()
    def test_missing_token(self): self.req.pop('dependency_token'); self.check()
    def test_callback_exception(self): self.callbacks['authenticate']=lambda c:1/0; self.check()
    def test_nonfinite_evidence(self): self.req['evidence']={'x':float('nan')}; self.check()

    def test_missing_receipt_caller(self):
        self.receipt.pop('caller'); self.check()
    def test_cross_principal_receipt_reuse(self):
        self.req['caller']='agent-2'
        self.callbacks['authenticate']=lambda c:True
        self.callbacks['authorize']=lambda c,o,s:True
        self.check()
    def test_signed_payload_contains_caller(self):
        import json
        def check_payload(payload, signature):
            self.assertEqual(json.loads(payload)['caller'], 'agent-1')
            return True
        self.callbacks['verify_signature']=check_payload
        self.check('ALLOW')


    def test_truthy_authentication_is_not_authentication(self):
        for value in (1, 'yes', ['agent-1']):
            with self.subTest(value=value):
                self.callbacks['authenticate'] = lambda c, v=value: v
                self.check()
    def test_truthy_authorization_is_not_authorization(self):
        for value in (1, 'authorized', ['read']):
            with self.subTest(value=value):
                self.callbacks['authorize'] = lambda c, o, s, v=value: v
                self.check()
    def test_truthy_signature_result_is_not_verification(self):
        for value in (1, 'verified', ['valid']):
            with self.subTest(value=value):
                self.callbacks['verify_signature'] = lambda b, s, v=value: v
                self.check()
    def test_truthy_currentness_is_not_current(self):
        for value in (1, 'current', ['v1']):
            with self.subTest(value=value):
                self.callbacks['current'] = lambda t, v=value: v
                self.check('STALE')

if __name__=='__main__': unittest.main()
