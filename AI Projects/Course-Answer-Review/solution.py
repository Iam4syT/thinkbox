CATALOGUE = {'sample-course': {'duration': 'one year', 'mode': 'full time'}}

def review(course, answer):
    source = CATALOGUE.get(course)
    if source is None or not isinstance(answer, dict) or not answer:
        return 'human review'
    if answer != source:
        return 'human review'
    return 'ready for reviewer'
