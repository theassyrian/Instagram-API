from InstagramAPI.src.http.Response.Objects.Item import Item
from InstagramAPI.src.http.Response.Response import Response


class PopularFeedResponse(Response):
    def __init__(self):
        self._types = {}

        self._types["next_max_id"] = str
        self.next_max_id = None
        self.more_available = None
        self.auto_load_more_enabled = None
        self._types["items"] = [Item]
        self.items = None
        self.num_results = None
        self._types["max_id"] = str
        self.max_id = None