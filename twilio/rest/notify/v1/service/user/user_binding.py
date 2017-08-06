# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from twilio.base import deserialize
from twilio.base import serialize
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.page import Page


class UserBindingList(ListResource):
    """ PLEASE NOTE that this class contains beta products that are subject to
    change. Use them with caution. """

    def __init__(self, version, service_sid, identity):
        """
        Initialize the UserBindingList

        :param Version version: Version that contains the resource
        :param service_sid: The service_sid
        :param identity: The identity

        :returns: twilio.rest.notify.v1.service.user.user_binding.UserBindingList
        :rtype: twilio.rest.notify.v1.service.user.user_binding.UserBindingList
        """
        super(UserBindingList, self).__init__(version)

        # Path Solution
        self._solution = {
            'service_sid': service_sid,
            'identity': identity,
        }
        self._uri = '/Services/{service_sid}/Users/{identity}/Bindings'.format(**self._solution)

    def create(self, binding_type, address, tag=values.unset,
               notification_protocol_version=values.unset,
               credential_sid=values.unset, endpoint=values.unset):
        """
        Create a new UserBindingInstance

        :param UserBindingInstance.BindingType binding_type: The binding_type
        :param unicode address: The address
        :param unicode tag: The tag
        :param unicode notification_protocol_version: The notification_protocol_version
        :param unicode credential_sid: The credential_sid
        :param unicode endpoint: The endpoint

        :returns: Newly created UserBindingInstance
        :rtype: twilio.rest.notify.v1.service.user.user_binding.UserBindingInstance
        """
        data = values.of({
            'BindingType': binding_type,
            'Address': address,
            'Tag': tag,
            'NotificationProtocolVersion': notification_protocol_version,
            'CredentialSid': credential_sid,
            'Endpoint': endpoint,
        })

        payload = self._version.create(
            'POST',
            self._uri,
            data=data,
        )

        return UserBindingInstance(
            self._version,
            payload,
            service_sid=self._solution['service_sid'],
            identity=self._solution['identity'],
        )

    def stream(self, start_date=values.unset, end_date=values.unset,
               tag=values.unset, limit=None, page_size=None):
        """
        Streams UserBindingInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param date start_date: The start_date
        :param date end_date: The end_date
        :param unicode tag: The tag
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.notify.v1.service.user.user_binding.UserBindingInstance]
        """
        limits = self._version.read_limits(limit, page_size)

        page = self.page(
            start_date=start_date,
            end_date=end_date,
            tag=tag,
            page_size=limits['page_size'],
        )

        return self._version.stream(page, limits['limit'], limits['page_limit'])

    def list(self, start_date=values.unset, end_date=values.unset, tag=values.unset,
             limit=None, page_size=None):
        """
        Lists UserBindingInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param date start_date: The start_date
        :param date end_date: The end_date
        :param unicode tag: The tag
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.notify.v1.service.user.user_binding.UserBindingInstance]
        """
        return list(self.stream(
            start_date=start_date,
            end_date=end_date,
            tag=tag,
            limit=limit,
            page_size=page_size,
        ))

    def page(self, start_date=values.unset, end_date=values.unset, tag=values.unset,
             page_token=values.unset, page_number=values.unset,
             page_size=values.unset):
        """
        Retrieve a single page of UserBindingInstance records from the API.
        Request is executed immediately

        :param date start_date: The start_date
        :param date end_date: The end_date
        :param unicode tag: The tag
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of UserBindingInstance
        :rtype: twilio.rest.notify.v1.service.user.user_binding.UserBindingPage
        """
        params = values.of({
            'StartDate': serialize.iso8601_date(start_date),
            'EndDate': serialize.iso8601_date(end_date),
            'Tag': tag,
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(
            'GET',
            self._uri,
            params=params,
        )

        return UserBindingPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of UserBindingInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of UserBindingInstance
        :rtype: twilio.rest.notify.v1.service.user.user_binding.UserBindingPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url,
        )

        return UserBindingPage(self._version, response, self._solution)

    def get(self, sid):
        """
        Constructs a UserBindingContext

        :param sid: The sid

        :returns: twilio.rest.notify.v1.service.user.user_binding.UserBindingContext
        :rtype: twilio.rest.notify.v1.service.user.user_binding.UserBindingContext
        """
        return UserBindingContext(
            self._version,
            service_sid=self._solution['service_sid'],
            identity=self._solution['identity'],
            sid=sid,
        )

    def __call__(self, sid):
        """
        Constructs a UserBindingContext

        :param sid: The sid

        :returns: twilio.rest.notify.v1.service.user.user_binding.UserBindingContext
        :rtype: twilio.rest.notify.v1.service.user.user_binding.UserBindingContext
        """
        return UserBindingContext(
            self._version,
            service_sid=self._solution['service_sid'],
            identity=self._solution['identity'],
            sid=sid,
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Notify.V1.UserBindingList>'


class UserBindingPage(Page):
    """ PLEASE NOTE that this class contains beta products that are subject to
    change. Use them with caution. """

    def __init__(self, version, response, solution):
        """
        Initialize the UserBindingPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API
        :param service_sid: The service_sid
        :param identity: The identity

        :returns: twilio.rest.notify.v1.service.user.user_binding.UserBindingPage
        :rtype: twilio.rest.notify.v1.service.user.user_binding.UserBindingPage
        """
        super(UserBindingPage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of UserBindingInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.notify.v1.service.user.user_binding.UserBindingInstance
        :rtype: twilio.rest.notify.v1.service.user.user_binding.UserBindingInstance
        """
        return UserBindingInstance(
            self._version,
            payload,
            service_sid=self._solution['service_sid'],
            identity=self._solution['identity'],
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Notify.V1.UserBindingPage>'


class UserBindingContext(InstanceContext):
    """ PLEASE NOTE that this class contains beta products that are subject to
    change. Use them with caution. """

    def __init__(self, version, service_sid, identity, sid):
        """
        Initialize the UserBindingContext

        :param Version version: Version that contains the resource
        :param service_sid: The service_sid
        :param identity: The identity
        :param sid: The sid

        :returns: twilio.rest.notify.v1.service.user.user_binding.UserBindingContext
        :rtype: twilio.rest.notify.v1.service.user.user_binding.UserBindingContext
        """
        super(UserBindingContext, self).__init__(version)

        # Path Solution
        self._solution = {
            'service_sid': service_sid,
            'identity': identity,
            'sid': sid,
        }
        self._uri = '/Services/{service_sid}/Users/{identity}/Bindings/{sid}'.format(**self._solution)

    def fetch(self):
        """
        Fetch a UserBindingInstance

        :returns: Fetched UserBindingInstance
        :rtype: twilio.rest.notify.v1.service.user.user_binding.UserBindingInstance
        """
        params = values.of({})

        payload = self._version.fetch(
            'GET',
            self._uri,
            params=params,
        )

        return UserBindingInstance(
            self._version,
            payload,
            service_sid=self._solution['service_sid'],
            identity=self._solution['identity'],
            sid=self._solution['sid'],
        )

    def delete(self):
        """
        Deletes the UserBindingInstance

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
        return '<Twilio.Notify.V1.UserBindingContext {}>'.format(context)


class UserBindingInstance(InstanceResource):
    """ PLEASE NOTE that this class contains beta products that are subject to
    change. Use them with caution. """

    class BindingType(object):
        APN = "apn"
        GCM = "gcm"
        SMS = "sms"
        FCM = "fcm"
        FACEBOOK_MESSENGER = "facebook-messenger"
        ALEXA = "alexa"

    def __init__(self, version, payload, service_sid, identity, sid=None):
        """
        Initialize the UserBindingInstance

        :returns: twilio.rest.notify.v1.service.user.user_binding.UserBindingInstance
        :rtype: twilio.rest.notify.v1.service.user.user_binding.UserBindingInstance
        """
        super(UserBindingInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'sid': payload['sid'],
            'account_sid': payload['account_sid'],
            'service_sid': payload['service_sid'],
            'credential_sid': payload['credential_sid'],
            'date_created': deserialize.iso8601_datetime(payload['date_created']),
            'date_updated': deserialize.iso8601_datetime(payload['date_updated']),
            'notification_protocol_version': payload['notification_protocol_version'],
            'endpoint': payload['endpoint'],
            'identity': payload['identity'],
            'binding_type': payload['binding_type'],
            'address': payload['address'],
            'tags': payload['tags'],
            'url': payload['url'],
            'links': payload['links'],
        }

        # Context
        self._context = None
        self._solution = {
            'service_sid': service_sid,
            'identity': identity,
            'sid': sid or self._properties['sid'],
        }

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context

        :returns: UserBindingContext for this UserBindingInstance
        :rtype: twilio.rest.notify.v1.service.user.user_binding.UserBindingContext
        """
        if self._context is None:
            self._context = UserBindingContext(
                self._version,
                service_sid=self._solution['service_sid'],
                identity=self._solution['identity'],
                sid=self._solution['sid'],
            )
        return self._context

    @property
    def sid(self):
        """
        :returns: The sid
        :rtype: unicode
        """
        return self._properties['sid']

    @property
    def account_sid(self):
        """
        :returns: The account_sid
        :rtype: unicode
        """
        return self._properties['account_sid']

    @property
    def service_sid(self):
        """
        :returns: The service_sid
        :rtype: unicode
        """
        return self._properties['service_sid']

    @property
    def credential_sid(self):
        """
        :returns: The credential_sid
        :rtype: unicode
        """
        return self._properties['credential_sid']

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
    def notification_protocol_version(self):
        """
        :returns: The notification_protocol_version
        :rtype: unicode
        """
        return self._properties['notification_protocol_version']

    @property
    def endpoint(self):
        """
        :returns: The endpoint
        :rtype: unicode
        """
        return self._properties['endpoint']

    @property
    def identity(self):
        """
        :returns: The identity
        :rtype: unicode
        """
        return self._properties['identity']

    @property
    def binding_type(self):
        """
        :returns: The binding_type
        :rtype: unicode
        """
        return self._properties['binding_type']

    @property
    def address(self):
        """
        :returns: The address
        :rtype: unicode
        """
        return self._properties['address']

    @property
    def tags(self):
        """
        :returns: The tags
        :rtype: unicode
        """
        return self._properties['tags']

    @property
    def url(self):
        """
        :returns: The url
        :rtype: unicode
        """
        return self._properties['url']

    @property
    def links(self):
        """
        :returns: The links
        :rtype: unicode
        """
        return self._properties['links']

    def fetch(self):
        """
        Fetch a UserBindingInstance

        :returns: Fetched UserBindingInstance
        :rtype: twilio.rest.notify.v1.service.user.user_binding.UserBindingInstance
        """
        return self._proxy.fetch()

    def delete(self):
        """
        Deletes the UserBindingInstance

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
        return '<Twilio.Notify.V1.UserBindingInstance {}>'.format(context)
