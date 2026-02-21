from atf.ui import *

from pages.AuthPages import AuthPage
from pages.MilestoneCard import MilestoneCard
from atf import *


class Test(TestCaseUI):

    mil_c = None
    auth = None

    @classmethod
    def setUpClass(cls):

        cls.mil_c = MilestoneCard(cls.driver)

    # def test_1(self):
    #     MilestoneCard(self.driver).add_task_btn.print_locator()
    #     MilestoneCard(self.driver).search_task_cs.print_locator()
    #     MilestoneCard(self.driver).task_grid_tgv.print_locator()

    def test_2(self):
        auth = AuthPage(self.driver)
        self.mil_c.add_task_btn.print_locator()
        self.mil_c.add_task_btn.add_parent(auth.login)
        self.mil_c.add_task_btn.print_locator()
        self.mil_c.add_task_btn.set_absolute_position()
        self.mil_c.add_task_btn.print_locator()
        self.mil_c.add_task_btn.add_child(auth.login)
        auth.login.print_locator()

    def test_3(self):

        self.mil_c.add_task_btn.print_locator()
