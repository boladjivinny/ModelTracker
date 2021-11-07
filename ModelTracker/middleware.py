from ModelTracker.Tracker import ModelTracker
class ModelTrackerMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response
    def process_request(self, request):
        ModelTracker.thread.request = request



