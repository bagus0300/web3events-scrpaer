from get_eventbrite.cities import web3event_cities
from get_eventbrite.tags import web3event_tags
from get_eventbrite.get_event_list import get_event_list

def get_from_brite():
    eventbrite_url = "https://www.eventbrite.com"
    event_list = []
    for city in web3event_cities:
        for tag in web3event_tags:
            url = eventbrite_url + "/d/" + city + "/%23" + tag
            event_list.extend(get_event_list(url))

    print(event_list)
    return event_list