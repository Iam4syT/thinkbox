import json
from pathlib import Path
from agents.base_agent import BaseAgent
DATA = json.loads((Path(__file__).resolve().parents[2] / "portfolio.json").read_text())

class ProjectAgent(BaseAgent):
    def __init__(self):
        super().__init__("Project guide", "Describes only the checked project catalogue")
        self.projects = {p["id"]: p for p in DATA["projects"]}
    def get_project_list(self):
        return "\n\n".join(self.get_project_details(key) for key in self.projects)
    def get_project_details(self, project_id):
        project = self.projects.get(project_id)
        if not project: return "Project not in the checked catalogue."
        return f"### {project['name']}\n{project['description']}\nTools: {', '.join(project['stack'])}\n[Source and evidence]({project['url']})"
    def answer_technical_question(self, project_id, question):
        return self.get_project_details(project_id) + "\nFurther implementation details must be checked in the linked source; this catalogue does not invent them."
