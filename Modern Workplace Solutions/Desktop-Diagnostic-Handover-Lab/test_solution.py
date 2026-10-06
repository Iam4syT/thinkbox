import unittest
from diagnose import diagnose
class Tests(unittest.TestCase):
    def setUp(self):self.s={'asset_alias':'TEST','adapter_up':True,'dns_ok':True,'tcp_443_ok':True,'app_ok':True,'disk_free_percent':30}
    def test_clear_does_not_close(self):self.assertEqual(diagnose(self.s)['state'],'checks_clear');self.assertIn('confirm user task',diagnose(self.s)['checks'][0])
    def test_network_failure(self):self.assertIn('no firewall change',diagnose({**self.s,'tcp_443_ok':False})['checks'][0])
    def test_low_space(self):self.assertIn('do not delete',diagnose({**self.s,'disk_free_percent':5})['checks'][0])
    def test_missing_not_success(self):self.assertEqual(diagnose({'asset_alias':'TEST'})['state'],'needs_review');self.assertEqual(len(diagnose({'asset_alias':'TEST'})['missing']),5)
    def test_bad_boolean(self):
        with self.assertRaises(ValueError):diagnose({**self.s,'dns_ok':'false'})
    def test_bad_percent(self):
        for val in [-1,101,True]:
            with self.assertRaises(ValueError):diagnose({**self.s,'disk_free_percent':val})
    def test_app_failure(self):self.assertIn('reproduction',diagnose({**self.s,'app_ok':False})['checks'][0])
if __name__=='__main__':unittest.main()
