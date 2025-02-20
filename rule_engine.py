class RuleEngine:
    def __init__(self):
        self.rules = []

    def add_rule(self, rule):
        self.rules.append(rule)

    def evaluate_pose(self, keypoints):
        results = {}
        for rule in self.rules:
            result = rule(keypoints)
            results[rule.__name__] = result
        return results