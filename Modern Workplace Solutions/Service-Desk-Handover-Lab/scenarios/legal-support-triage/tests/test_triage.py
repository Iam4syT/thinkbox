import sys, unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"scripts"))
from triage import triage
BASE=dict(id="X",kind="document",suspected_exposure="no",service_wide="no",urgent_event="no",minutes_open="10",target_minutes="30",user_retested="no")
class Triage(unittest.TestCase):
    def test_normal(self):self.assertEqual(triage(BASE)["route"],"FIRST LINE")
    def test_security_first(self):self.assertEqual(triage({**BASE,"suspected_exposure":"yes","service_wide":"yes","minutes_open":"40"})["route"],"SECURITY")
    def test_outage(self):self.assertEqual(triage({**BASE,"service_wide":"yes"})["route"],"INCIDENT")
    def test_boundary(self):self.assertEqual(triage({**BASE,"minutes_open":"30"})["route"],"ESCALATE")
    def test_urgent(self):self.assertEqual(triage({**BASE,"urgent_event":"yes"})["route"],"URGENT REVIEW")
    def test_unknown(self):self.assertEqual(triage({**BASE,"kind":"other"})["route"],"REVIEW")
    def test_invalid(self):self.assertEqual(triage({**BASE,"minutes_open":"-1"})["route"],"REVIEW")
    def test_no_auto_close(self):self.assertEqual(triage(BASE)["closure"],"KEEP OPEN")
if __name__=="__main__":unittest.main()
