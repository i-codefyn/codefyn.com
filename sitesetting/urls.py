from django.urls import path

from users.views import SignupPageView, StaffView, UserAcountView
from users.staff.services import StaffViewServices

from users.staff.users import (
    UsersDetail,
    UsersExportPdfAll,
    UsersExportPdfbyId,
    UsersExportCsv,
    UsersList,
    UsersExportPdfbyDate,
)
from users.staff.sites import (
    SitesList,
    SitesDetail,
    SitesCreate,
    SitesUpdate,
    SitesDelete,
)

from users.staff.faq import FaqCreate, FaqDetail, FaqList, FaqUpdate, FaqDelete

from users.staff.onlinerequests import (
    OnlineRequestsList,
    OnlineRequestDetails,
    ViewOnlineRequestsByDate,
    OnlineRequestsExportPdfAll,
    OnlineRequetsExportPdfbyDate,
    OnlineRequetsExportPdfbyId,
    OnlineRequestsExportCsv,
)

from users.staff.feedback import FeedbackList
from users.staff.messages import MessageList

urlpatterns = [
    path("staff/", StaffView.as_view(), name="staff"),
    # Alerts
    path("staff/feedback", FeedbackList.as_view(), name="feedback_list"),
    path("staff/msg", MessageList.as_view(), name="msg_list"),
    path(
        "staff/OnlineRequests",
        OnlineRequestsList.as_view(),
        name="online_requests_list",
    ),
    path(
        "staff/OnlineRequests/<uuid:pk>",
        OnlineRequestDetails.as_view(),
        name="online_requests",
    ),
    path(
        "staff/OnlineRequests/ListFiltered",
        ViewOnlineRequestsByDate.as_view(),
        name="online_requests_list_bydate",
    ),
    path(
        "staff/OnlineRequests/ExportPdfAll",
        OnlineRequestsExportPdfAll,
        name="online_requests_list_pdf_export",
    ),
    path(
        "staff/OnlineRequests/ExportPdfFiltered",
        OnlineRequetsExportPdfbyDate,
        name="online_requests_list_pdf_export_bydate",
    ),
    path(
        "staff/OnlineRequests/<uuid:pk>/pdf",
        OnlineRequetsExportPdfbyId,
        name="online_requests_list_pdf_export_by_id",
    ),
    path(
        "staff/OnlineRequests/Csv",
        OnlineRequestsExportCsv,
        name="online_requests_list_export_csv",
    ),
    # staff users section
    path("staff/users", UsersList.as_view(), name="users_list"),
    path(
        "staff/users/exportpdfbydate", UsersExportPdfbyDate, name="users_export_bydate"
    ),
    path("staff/users/pdf", UsersExportPdfAll, name="users_exportpdf_all"),
    path("staff/users/csv", UsersExportCsv, name="users_exportcsv"),
    path("staff/users/<uuid:pk>/pdf", UsersExportPdfbyId, name="users_exportpdf_byid"),
    path("staff/users/<uuid:pk>", UsersDetail.as_view(), name="users"),
    path("staff/services", StaffViewServices.as_view(), name="staff-view-services"),
    path("accounts/profile/", UserAcountView.as_view(), name="user-profile"),
]
