from agsadmin._endpoint_base import _EndpointBase
from agsadmin._utils import send_session_request
from ._permissions_mixin import _PermissionsMixin
from ._utils import _get_service_class

class _Folder(_PermissionsMixin, _EndpointBase):

    def __init__(self, requests_session, server_url, name):
        super(_Folder, self).__init__(requests_session, server_url)
        self._name = name

    def __str__(self):
        return self.name

    @property
    def name(self):
        return self._name

    @property
    def _url_full(self):
        return "{0}/services/{1}".format(self._url_base, self.name)
    
    def get_services(self):
        """
        Gets a list of service proxy objects for services in this folder.
        """
        response = send_session_request(
            self._session,
            self._create_operation_request(self._url_full, method = "GET")).json()
            
        services = []
        for s in response["services"]:
            service_class = _get_service_class(s["type"])
            if service_class != None:
                services.append(service_class(self._session, self._url_base, s["serviceName"], s["folderName"]))
        
        return services