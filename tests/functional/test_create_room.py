import re
from functools import partial
from pytest_bdd import scenario as scen, when, then

scenario = partial(scen, 'create_room.feature')


test_create_room = scenario('Create a room')


@when(re.compile("I create a new room called (?P<room_name>[\w\d]+)"))
def create_new_room_called_x(browser, room_name):
    browser.fill("name", room_name)


@then(re.compile("I should see the room (?P<room_name>[\w\d]+)"))
def i_should_see_the_new_room(browser, room_name):
    assert browser.find_by_xpath(
        '//div[@class="room"]/h1/a[@href="/{0}"]'.format(
            room_name
        )
    )
