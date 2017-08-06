# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from twilio.base import deserialize
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.page import Page


class CredentialListMappingList(ListResource):
    """  """

    def __init__(self, version, account_sid, domain_sid):
        """
        Initialize the CredentialListMappingList

        :param Version version: Version that contains the resource
        :param account_sid: The account_sid
        :param domain_sid: A string that uniquely identifies the SIP Domain

        :returns: twilio.rest.api.v2010.account.sip.domain.credential_list_mapping.CredentialListMappingList
        :rtype: twilio.rest.api.v2010.account.sip.domain.credential_list_mapping.CredentialListMappingList
        """
        super(CredentialListMappingList, self).__init__(version)

        # Path Solution
        self._solution = {
            'account_sid': account_sid,
            'domain_sid': domain_sid,
        }
        self._uri = '/Accounts/{account_sid}/SIP/Domains/{domain_sid}/CredentialListMappings.json'.format(**self._solution)

    def create(self, credential_list_sid):
        """
        Create a new CredentialListMappingInstance

        :param unicode credential_list_sid: The credential_list_sid

        :returns: Newly created CredentialListMappingInstance
        :rtype: twilio.rest.api.v2010.account.sip.domain.credential_list_mapping.CredentialListMappingInstance
        """
        data = values.of({
            'CredentialListSid': credential_list_sid,
        })

        payload = self._version.create(
            'POST',
            self._uri,
            data=data,
        )

        return CredentialListMappingInstance(
            self._version,
            payload,
            account_sid=self._solution['account_sid'],
            domain_sid=self._solution['domain_sid'],
        )

    def stream(self, limit=None, page_size=None):
        """
        Streams CredentialListMappingInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.api.v2010.account.sip.domain.credential_list_mapping.CredentialListMappingInstance]
        """
        limits = self._version.read_limits(limit, page_size)

        page = self.page(
            page_size=limits['page_size'],
        )

        return self._version.stream(page, limits['limit'], limits['page_limit'])

    def list(self, limit=None, page_size=None):
        """
        Lists CredentialListMappingInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.api.v2010.account.sip.domain.credential_list_mapping.CredentialListMappingInstance]
        """
        return list(self.stream(
            limit=limit,
            page_size=page_size,
        ))

    def page(self, page_token=values.unset, page_number=values.unset,
             page_size=values.unset):
        """
        Retrieve a single page of CredentialListMappingInstance records from the API.
        Request is executed immediately

        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of CredentialListMappingInstance
        :rtype: twilio.rest.api.v2010.account.sip.domain.credential_list_mapping.CredentialListMappingPage
        """
        params = values.of({
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(
            'GET',
            self._uri,
            params=params,
        )

        return CredentialListMappingPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of CredentialListMappingInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of CredentialListMappingInstance
        :rtype: twilio.rest.api.v2010.account.sip.domain.credential_list_mapping.CredentialListMappingPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url,
        )

        return CredentialListMappingPage(self._version, response, self._solution)

    def get(self, sid):
        """
        Constructs a CredentialListMappingContext

        :param sid: The sid

        :returns: twilio.rest.api.v2010.account.sip.domain.credential_list_mapping.CredentialListMappingContext
        :rtype: twilio.rest.api.v2010.account.sip.domain.credential_list_mapping.CredentialListMappingContext
        """
        return CredentialListMappingContext(
            self._version,
            account_sid=self._solution['account_sid'],
            domain_sid=self._solution['domain_sid'],
            sid=sid,
        )

    def __call__(self, sid):
        """
        Constructs a CredentialListMappingContext

        :param sid: The sid

        :returns: twilio.rest.api.v2010.account.sip.domain.credential_list_mapping.CredentialListMappingContext
        :rtype: twilio.rest.api.v2010.account.sip.domain.credential_list_mapping.CredentialListMappingContext
        """
        return CredentialListMappingContext(
            self._version,
            account_sid=self._solution['account_sid'],
            domain_sid=self._solution['domain_sid'],
            sid=sid,
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.CredentialListMappingList>'


class CredentialListMappingPage(Page):
    """  """

    def __init__(self, version, response, solution):
        """
        Initialize the CredentialListMappingPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API
        :param account_sid: The account_sid
        :param domain_sid: A string that uniquely identifies the SIP Domain

        :returns: twilio.rest.api.v2010.account.sip.domain.credential_list_mapping.CredentialListMappingPage
        :rtype: twilio.rest.api.v2010.account.sip.domain.credential_list_mapping.CredentialListMappingPage
        """
        super(CredentialListMappingPage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of CredentialListMappingInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.api.v2010.account.sip.domain.credential_list_mapping.CredentialListMappingInstance
        :rtype: twilio.rest.api.v2010.account.sip.domain.credential_list_mapping.CredentialListMappingInstance
        """
        return CredentialListMappingInstance(
            self._version,
            payload,
            account_sid=self._solution['account_sid'],
            domain_sid=self._solution['domain_sid'],
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.CredentialListMappingPage>'


class CredentialListMappingContext(InstanceContext):
    """  """

    def __init__(self, version, account_sid, domain_sid, sid):
        """
        Initialize the CredentialListMappingContext

        :param Version version: Version that contains the resource
        :param account_sid: The account_sid
        :param domain_sid: The domain_sid
        :param sid: The sid

        :returns: twilio.rest.api.v2010.account.sip.domain.credential_list_mapping.CredentialListMappingContext
        :rtype: twilio.rest.api.v2010.account.sip.domain.credential_list_mapping.CredentialListMappingContext
        """
        super(CredentialListMappingContext, self).__init__(version)

        # Path Solution
        self._solution = {
            'account_sid': account_sid,
            'domain_sid': domain_sid,
            'sid': sid,
        }
        self._uri = '/Accounts/{account_sid}/SIP/Domains/{domain_sid}/CredentialListMappings/{sid}.json'.format(**self._solution)

    def fetch(self):
        """
        Fetch a CredentialListMappingInstance

        :returns: Fetched CredentialListMappingInstance
        :rtype: twilio.rest.api.v2010.account.sip.domain.credential_list_mapping.CredentialListMappingInstance
        """
        params = values.of({})

        payload = self._version.fetch(
            'GET',
            self._uri,
            params=params,
        )

        return CredentialListMappingInstance(
            self._version,
            payload,
            account_sid=self._solution['account_sid'],
            domain_sid=self._solution['domain_sid'],
            sid=self._solution['sid'],
        )

    def delete(self):
        """
        Deletes the CredentialListMappingInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete('delete', self._uri)

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Api.V2010.CredentialListMappingContext {}>'.format(context)


class CredentialListMappingInstance(InstanceResource):
    """  """

    def __init__(self, version, payload, account_sid, domain_sid, sid=None):
        """
        Initialize the CredentialListMappingInstance

        :returns: twilio.rest.api.v2010.account.sip.domain.credential_list_mapping.CredentialListMappingInstance
        :rtype: twilio.rest.api.v2010.account.sip.domain.credential_list_mapping.CredentialListMappingInstance
        """
        super(CredentialListMappingInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'account_sid': payload['account_sid'],
            'date_created': deserialize.rfc2822_datetime(payload['date_created']),
            'date_updated': deserialize.rfc2822_datetime(payload['date_updated']),
            'friendly_name': payload['friendly_name'],
            'sid': payload['sid'],
            'uri': payload['uri'],
            'subresource_uris': payload['subresource_uris'],
        }

        # Context
        self._context = None
        self._solution = {
            'account_sid': account_sid,
            'domain_sid': domain_sid,
            'sid': sid or self._properties['sid'],
        }

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context

        :returns: CredentialListMappingContext for this CredentialListMappingInstance
        :rtype: twilio.rest.api.v2010.account.sip.domain.credential_list_mapping.CredentialListMappingContext
        """
        if self._context is None:
            self._context = CredentialListMappingContext(
                self._version,
                account_sid=self._solution['account_sid'],
                domain_sid=self._solution['domain_sid'],
                sid=self._solution['sid'],
            )
        return self._context

    @property
    def account_sid(self):
        """
        :returns: The account_sid
        :rtype: unicode
        """
        return self._properties['account_sid']

    @property
    def date_created(self):
        """
        :returns: The date_created
        :rtype: datetime
        """
        return self._properties['date_created']

    @property
    def date_updated(self):
        """
        :returns: The date_updated
        :rtype: datetime
        """
        return self._properties['date_updated']

    @property
    def friendly_name(self):
        """
        :returns: The friendly_name
        :rtype: unicode
        """
        return self._properties['friendly_name']

    @property
    def sid(self):
        """
        :returns: The sid
        :rtype: unicode
        """
        return self._properties['sid']

    @property
    def uri(self):
        """
        :returns: The uri
        :rtype: unicode
        """
        return self._properties['uri']

    @property
    def subresource_uris(self):
        """
        :returns: The subresource_uris
        :rtype: unicode
        """
        return self._properties['subresource_uris']

    def fetch(self):
        """
        Fetch a CredentialListMappingInstance

        :returns: Fetched CredentialListMappingInstance
        :rtype: twilio.rest.api.v2010.account.sip.domain.credential_list_mapping.CredentialListMappingInstance
        """
        return self._proxy.fetch()

    def delete(self):
        """
        Deletes the CredentialListMappingInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete()

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Api.V2010.CredentialListMappingInstance {}>'.format(context)