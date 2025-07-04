# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

import pytest
import requests

TIMEOUT = 60


def pytest_generate_tests(metafunc):
    if "not headless" in metafunc.config.option.markexpr:
        return  # test deslected by mark expression
    base_url = metafunc.config.option.base_url
    if not base_url:
        pytest.skip("This test requires a base URL to be specified on the command line or in a configuration file.")
    paths = (
        "/firefox/115.16.1/releasenotes/",
        "/firefox/135.0beta/releasenotes/",
        "/firefox/140.0a1/releasenotes/",
        "/firefox/android/115.0/releasenotes/",
        "/firefox/android/115.0/system-requirements/",
        "/firefox/ios/128.0/releasenotes/",
        "/firefox/ios/128.0/system-requirements/",
    )
    metafunc.parametrize("url", [base_url + path for path in paths])


@pytest.mark.headless
@pytest.mark.nondestructive
def test_generated_pages(url):
    r = requests.head(url, allow_redirects=True, timeout=TIMEOUT, headers={"accept-language": "en"})
    assert requests.codes.ok == r.status_code
