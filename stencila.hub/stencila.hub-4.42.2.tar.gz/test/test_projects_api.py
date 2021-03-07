# coding: utf-8

"""
    Stencila Hub API

    # Authentication  Many endpoints in the Stencila Hub API require an authentication token. These tokens carry many privileges, so be sure to keep them secure. Do not place your tokens in publicly accessible areas such as client-side code. The API is only served over HTTPS to avoid exposing tokens and other data on the network.  To obtain a token, [`POST /api/tokens`](#operations-tokens-tokens_create) with either a `username` and `password` pair, or an [OpenID Connect](https://openid.net/connect/) token. Then use the token in the `Authorization` header of subsequent requests with the prefix `Token` e.g.      curl -H \"Authorization: Token 48866b1e38a2e9db0baada2140b2327937f4a3636dd5f2dfd8c212341c88d34\" https://hub.stenci.la/api/projects/  Alternatively, you can use `Basic` authentication with the token used as the username and no password. This can be more convenient when using command line tools such as [cURL](https://curl.haxx.se/) e.g.      curl -u 48866b1e38a2e9db0baada2140b2327937f4a3636dd5f2dfd8c212341c88d34: https://hub.stenci.la/api/projects/  Or, the less ubiquitous, but more accessible [httpie](https://httpie.org/):      http --auth 48866b1e38a2e9db0baada2140b2327937f4a3636dd5f2dfd8c212341c88d34: https://hub.stenci.la/api/projects/  In both examples above, the trailing colon is not required but avoids being asked for a password.  # Versioning  The Stencila Hub is released using semantic versioning. The current version is available from the [`GET /api/status`](/api/status) endpoint. Please see the [Github release page](https://github.com/stencila/hub/releases) and the [changelog](https://github.com/stencila/hub/blob/master/CHANGELOG.md) for details on each release. We currently do not provide versioning of the API but plan to do so soon (probably by using a `Accept: application/vnd.stencila.hub+json;version=1.0` request header). If you are using, or interested in using, the API please contact us and we may be able to expedite this.   # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import stencila.hub
from stencila.hub.api.projects_api import ProjectsApi  # noqa: E501
from stencila.hub.rest import ApiException


class TestProjectsApi(unittest.TestCase):
    """ProjectsApi unit test stubs"""

    def setUp(self):
        self.api = stencila.hub.api.projects_api.ProjectsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_projects_agents_create(self):
        """Test case for projects_agents_create

        Create an object.  # noqa: E501
        """
        pass

    def test_projects_agents_delete(self):
        """Test case for projects_agents_delete

        Destroy an object.  # noqa: E501
        """
        pass

    def test_projects_agents_list(self):
        """Test case for projects_agents_list

        List objects.  # noqa: E501
        """
        pass

    def test_projects_agents_partial_update(self):
        """Test case for projects_agents_partial_update

        Update an object.  # noqa: E501
        """
        pass

    def test_projects_agents_read(self):
        """Test case for projects_agents_read

        Retrieve an object.  # noqa: E501
        """
        pass

    def test_projects_convert(self):
        """Test case for projects_convert

        Convert a file to another format.  # noqa: E501
        """
        pass

    def test_projects_create(self):
        """Test case for projects_create

        Create a project.  # noqa: E501
        """
        pass

    def test_projects_delete(self):
        """Test case for projects_delete

        Destroy a project.  # noqa: E501
        """
        pass

    def test_projects_files_delete(self):
        """Test case for projects_files_delete

        Destroy an object.  # noqa: E501
        """
        pass

    def test_projects_files_list(self):
        """Test case for projects_files_list

        List objects.  # noqa: E501
        """
        pass

    def test_projects_files_read(self):
        """Test case for projects_files_read

        Retrieve an object.  # noqa: E501
        """
        pass

    def test_projects_history(self):
        """Test case for projects_history

        Get the a file's history.  # noqa: E501
        """
        pass

    def test_projects_jobs_cancel(self):
        """Test case for projects_jobs_cancel

        Cancel a job.  # noqa: E501
        """
        pass

    def test_projects_jobs_connect_create(self):
        """Test case for projects_jobs_connect_create

        Connect to a job.  # noqa: E501
        """
        pass

    def test_projects_jobs_connect_read(self):
        """Test case for projects_jobs_connect_read

        Connect to a job.  # noqa: E501
        """
        pass

    def test_projects_jobs_create(self):
        """Test case for projects_jobs_create

        Create an object.  # noqa: E501
        """
        pass

    def test_projects_jobs_execute(self):
        """Test case for projects_jobs_execute

        Create an execute job.  # noqa: E501
        """
        pass

    def test_projects_jobs_list(self):
        """Test case for projects_jobs_list

        List objects.  # noqa: E501
        """
        pass

    def test_projects_jobs_partial_update(self):
        """Test case for projects_jobs_partial_update

        Update an object.  # noqa: E501
        """
        pass

    def test_projects_jobs_read(self):
        """Test case for projects_jobs_read

        Retrieve an object.  # noqa: E501
        """
        pass

    def test_projects_list(self):
        """Test case for projects_list

        List projects.  # noqa: E501
        """
        pass

    def test_projects_partial_update(self):
        """Test case for projects_partial_update

        Update a project.  # noqa: E501
        """
        pass

    def test_projects_pull(self):
        """Test case for projects_pull

        Pull the project.  # noqa: E501
        """
        pass

    def test_projects_read(self):
        """Test case for projects_read

        Retrieve a project.  # noqa: E501
        """
        pass

    def test_projects_snapshots_archive(self):
        """Test case for projects_snapshots_archive

        Retrieve an archive for a project snapshot.  # noqa: E501
        """
        pass

    def test_projects_snapshots_create(self):
        """Test case for projects_snapshots_create

        Create an object.  # noqa: E501
        """
        pass

    def test_projects_snapshots_delete(self):
        """Test case for projects_snapshots_delete

        Destroy an object.  # noqa: E501
        """
        pass

    def test_projects_snapshots_files(self):
        """Test case for projects_snapshots_files

        Retrieve a file within a snapshot of the project.  # noqa: E501
        """
        pass

    def test_projects_snapshots_list(self):
        """Test case for projects_snapshots_list

        List objects.  # noqa: E501
        """
        pass

    def test_projects_snapshots_read(self):
        """Test case for projects_snapshots_read

        Retrieve an object.  # noqa: E501
        """
        pass

    def test_projects_snapshots_session(self):
        """Test case for projects_snapshots_session

        Get a session with the snapshot as the working directory.  # noqa: E501
        """
        pass

    def test_projects_sources_create(self):
        """Test case for projects_sources_create

        Create a project source.  # noqa: E501
        """
        pass

    def test_projects_sources_delete(self):
        """Test case for projects_sources_delete

        Destroy a project source.  # noqa: E501
        """
        pass

    def test_projects_sources_list(self):
        """Test case for projects_sources_list

        List a project's sources.  # noqa: E501
        """
        pass

    def test_projects_sources_open(self):
        """Test case for projects_sources_open

        Open a project source, or a file within it.  # noqa: E501
        """
        pass

    def test_projects_sources_partial_update(self):
        """Test case for projects_sources_partial_update

        Update a project source.  # noqa: E501
        """
        pass

    def test_projects_sources_pull(self):
        """Test case for projects_sources_pull

        Pull a project source.  # noqa: E501
        """
        pass

    def test_projects_sources_read(self):
        """Test case for projects_sources_read

        Retrieve a project source.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
