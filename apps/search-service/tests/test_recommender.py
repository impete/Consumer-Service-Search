from app.recommender import Recommender


def test_rank_orders_by_score_descending():
    providers = [{"name": "a", "score": 1}, {"name": "b", "score": 9}]
    result = Recommender().rank(providers)
    assert [p["name"] for p in result["results"]] == ["b", "a"]
