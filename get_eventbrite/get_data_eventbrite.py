from get_eventbrite.cities import web3event_cities
from get_eventbrite.tags import web3event_tags
from get_eventbrite.get_event_list import get_event_list
from common.utils import remove_repeated_events
from get_eventbrite.event_detail_info import get_event_detailinfo

def get_from_eventbrite():
    eventbrite_url = "https://www.eventbrite.com"
    event_list = []
    for city in web3event_cities:
        for tag in web3event_tags:
            url = eventbrite_url + "/d/" + city + "/" + tag
            event_list.extend(get_event_list(url))


    filtered_event_list = remove_repeated_events(event_list, "href")

    print("count:", len(filtered_event_list))

    event_detail_list = [get_event_detailinfo(event) for event in filtered_event_list]
    # event_detail_list = [get_event_detailinfo(filtered_event_list[0])]
    return event_detail_list