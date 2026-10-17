import unittest,sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from main import plan,apply_local
class IdentityTests(unittest.TestCase):
 def setUp(self):
  self.people=[dict(id='joiner',state='active',team='research'),dict(id='mover',state='active',team='operations'),dict(id='leaver',state='left')]
  self.accounts={'mover':dict(enabled=True,groups=['research']),'leaver':dict(enabled=True,groups=['research']),'external':dict(enabled=True,groups=['operations'])}
 def test_joiner(self):self.assertEqual(plan(self.people,self.accounts)['changes'][0]['action'],'create')
 def test_mover_removes_old_group(self):self.assertEqual(apply_local(plan(self.people,self.accounts,True),self.accounts)['mover']['groups'],['operations'])
 def test_leaver_disabled(self):self.assertFalse(apply_local(plan(self.people,self.accounts,True),self.accounts)['leaver']['enabled'])
 def test_no_approval(self):
  with self.assertRaises(PermissionError):apply_local(plan(self.people,self.accounts),self.accounts)
 def test_idempotent(self):
  updated=apply_local(plan(self.people,self.accounts,True),self.accounts);self.assertEqual(plan(self.people,updated)['changes'],[])
 def test_missing_person_not_deleted(self):self.assertEqual(apply_local(plan(self.people,self.accounts,True),self.accounts)['external'],self.accounts['external'])
 def test_duplicate_id(self):
  with self.assertRaises(ValueError):plan(self.people+self.people,self.accounts)
 def test_unknown_team(self):
  with self.assertRaises(ValueError):plan([dict(id='x',state='active',team='admin')],{})
 def test_unknown_state(self):
  with self.assertRaises(ValueError):plan([dict(id='x',state='pending',team='research')],{})
 def test_inputs_not_mutated(self):
  apply_local(plan(self.people,self.accounts,True),self.accounts);self.assertTrue(self.accounts['leaver']['enabled'])
if __name__=='__main__':unittest.main()
