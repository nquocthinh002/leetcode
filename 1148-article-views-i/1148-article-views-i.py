import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    ids = views[views.author_id == views.viewer_id].author_id.unique()
    ids = sorted(ids)
    ans = pd.DataFrame({'id': ids})
    return ans