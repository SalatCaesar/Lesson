from controls import *


@templatename("Addressee/popup:Stack")
class StaffSelector(CatalogTemplateList):
    """Выбор сотрудника"""

    list_grid = ControlsListView(SabyBy.DATA_QA, "msg-addressee-selector__plain-list-view")
