from agents.base_agent import BaseAgent
from agents.project_agent import DATA

class CareerAgent(BaseAgent):
    def __init__(self):
        super().__init__("Career guide", "Uses only the confirmed public profile")
    def get_skills_summary(self):
        return DATA["focus"] + ". Portfolio tools demonstrate lab work; they are not certifications or a proficiency ranking."
    def get_experience_summary(self):
        return DATA["experience_summary"] + " " + DATA["study"]
    def assess_job_fit(self, job_description):
        return "Compare this role with the linked project evidence and verified CV. The public demo has insufficient employment evidence for a complete fit assessment. " + DATA["focus"]
