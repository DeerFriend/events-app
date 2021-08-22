from unittest import TestCase
from app import TICKETMASTER_API_EVENTDISCOVERY_URL, build_searchevents_url, perform_event_ticketmaster_api_call
from datetime import datetime
import responses


class TestBuildUrls(TestCase):

    def test_build_searchevents_url(self):
        expected_result = TICKETMASTER_API_EVENTDISCOVERY_URL + "&size=100&countryCode=GB&city=London&segmentId=KZFzniwnSyZfZ7v7nn&startDateTime=2021-09-24T15:30:00Z&endDateTime=2021-09-30T23:59:59Z"
        actual_result = build_searchevents_url("Film", "London", datetime(2021, 9, 24, 15, 30, 0), 7)
        self.assertEqual(expected_result, actual_result)

    def test_build_singleeventretrieval_url(self):
        # TODO
        pass


class TestTicketmasterApiCall(TestCase):
    FAKE_URL = "http://fakeurl"

    @responses.activate
    def test_ticketmastercall_no_event(self):
        # set up the mock (not calling the real API)
        no_event_api_response_body = {'_embedded': {'events': []}}
        responses.add(responses.GET, TestTicketmasterApiCall.FAKE_URL, json=no_event_api_response_body, status=200)

        # make the call and check if we get the expected events
        expected_result = []
        actual_result = perform_event_ticketmaster_api_call(TestTicketmasterApiCall.FAKE_URL)
        assert expected_result == actual_result

    @responses.activate
    def test_ticketmastercall_many_event(self):
        # TODO
        pass
