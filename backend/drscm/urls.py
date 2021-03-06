from django.urls import path
from drscm.views import InvoiceReportView
from drscm.views import ListUsersView
from drscm.views import CreateAndListClientsView, ClientDetailsView
from drscm.views import ProjectDetailsView, CreateAndListProjectsView
from drscm.views import WorkSessionDetailsView, CreateAndListWorkSessionView
from drscm.views import (
    HourlyTravelDetailsView,
    CreateAndListHourlyTravelsView,
    CreateAndListFixedTravelsView,
    FixedTravelDetailsView,
)
from drscm.views import InvoiceDetailsView, CreateAndListInvoicesView


urlpatterns = [
    path(
        "clients/",
        CreateAndListClientsView.as_view(),
        name=CreateAndListClientsView.view_name,
    ),
    path(
        "clients/<uuid:pk>",
        ClientDetailsView.as_view(),
        name=ClientDetailsView.view_name,
    ),
    path(
        "worksession/",
        CreateAndListWorkSessionView.as_view(),
        name=CreateAndListWorkSessionView.view_name,
    ),
    path(
        "worksession/<uuid:pk>",
        WorkSessionDetailsView.as_view(),
        name=WorkSessionDetailsView.view_name,
    ),
    path(
        "projects/",
        CreateAndListProjectsView.as_view(),
        name=CreateAndListProjectsView.view_name,
    ),
    path(
        "projects/<uuid:pk>",
        ProjectDetailsView.as_view(),
        name=ProjectDetailsView.view_name,
    ),
    path("users", ListUsersView.as_view(), name=ListUsersView.view_name),
    path(
        "travel/fixed",
        CreateAndListFixedTravelsView.as_view(),
        name=CreateAndListFixedTravelsView.view_name,
    ),
    path(
        "travel/fixed/<uuid:pk>",
        FixedTravelDetailsView.as_view(),
        name=FixedTravelDetailsView.view_name,
    ),
    path(
        "travel/hourly",
        CreateAndListHourlyTravelsView.as_view(),
        name=CreateAndListHourlyTravelsView.view_name,
    ),
    path(
        "travel/hourly/<uuid:pk>",
        HourlyTravelDetailsView.as_view(),
        name=HourlyTravelDetailsView.view_name,
    ),
    path(
        "invoices",
        CreateAndListInvoicesView.as_view(),
        name=CreateAndListInvoicesView.view_name,
    ),
    path(
        "invoices/<uuid:pk>",
        InvoiceDetailsView.as_view(),
        name=InvoiceDetailsView.view_name,
    ),
    path(
        "invoices/report/<uuid:pk>",
        InvoiceReportView.as_view(),
        name=InvoiceReportView.view_name,
    ),
]
