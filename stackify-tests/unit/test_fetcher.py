from unittest import mock

import pytest

import fetcher


@pytest.mark.parametrize("current_time", [0, 1, 2, 3, 4, 5])
@mock.patch("config.set_value", autospec=True)
def test_save_start_time_to_config(config, current_time):
    with mock.patch("time.time", return_value=current_time):
        fetcher.fetch(sites=[], from_time=0)

    config.assert_called_with("last-sync", current_time)



