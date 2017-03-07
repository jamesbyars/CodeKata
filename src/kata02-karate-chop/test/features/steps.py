from lettuce import step, world, before
from nose.tools import assert_equals
from app.application import chop, app

import logging
logging.basicConfig(level=logging.DEBUG)


@before.all
def before_all():
    world.app = app.test_client()


@step(u'Given an empty set is passed in')
def given_an_empty_set_is_passed_in(step):
    world.set_to_pass = []
    world.value_to_find = 1


@step(u'When I attempt to find the specified value')
def when_i_attempt_to_find_the_specified_value(step):
    world.response = chop(world.value_to_find, world.set_to_pass)


@step(u'Then I should get a -1 response')
def then_i_should_get_a_1_response(step):
    assert world.response == -1