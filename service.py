import os
import win32service
import win32serviceutil
import win32event
import servicemanager
from waitress import serve
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cedossa.settings')

class DjangoService(win32serviceutil.ServiceFramework):
    _svc_name_ = "DjangoService"
    _svc_display_name_ = "Django Web Service"
    _svc_description_ = "Runs Django as a Windows service"

    def __init__(self, args):
        super().__init__(args)
        self.stop_event = win32event.CreateEvent(None, 0, 0, None)

    def SvcStop(self):
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        win32event.SetEvent(self.stop_event)

    def SvcDoRun(self):
        servicemanager.LogMsg(
            servicemanager.EVENTLOG_INFORMATION_TYPE,
            servicemanager.PYS_SERVICE_STARTED,
            (self._svc_name_, "")
        )
        application = get_wsgi_application()
        serve(application, host='127.0.0.1', port=8000)

if __name__ == '__main__':
    win32serviceutil.HandleCommandLine(DjangoService)
