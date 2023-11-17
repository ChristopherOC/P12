from rest_framework import routers
from Events.views import EventViewSet, EventUpdate, SupportOfTheEvent

router = routers.DefaultRouter()
router.register('events', EventViewSet, basename='events')
router.register('events_update', EventUpdate)
router.register('support_of_the_event', SupportOfTheEvent)
