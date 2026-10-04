class Recommender:
    def rank(self, providers, priority: str = "score"):
        ranked = sorted(providers, key=lambda item: item.get("score", 0), reverse=True)
        return {"priority": priority, "results": ranked}
