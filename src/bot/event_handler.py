# 3rd
from linebot.models import (MessageEvent, TextMessage, FollowEvent,
                            UnfollowEvent)

# our
from .message_event.text_message import text_message_dispatcher


def event_broker(events):
    ''' event_broker is responsible for dispatching different kinds of
        events to specific event handler

        @params:
            events: Line Webhook event types
    '''
    for event in events:
        # Handle Text Message
        if isinstance(event, MessageEvent) and isinstance(
                event.message, TextMessage):
            text_message_dispatcher(event)
        elif isinstance(event, FollowEvent):  # Handle Follow Event
            pass
        elif isinstance(event, UnfollowEvent):  # Handle Unfollow Event
            pass
