from user_interface import Ui_TaskList
from PySide6.QtCore import (QCoreApplication, Qt)
from PySide6.QtWidgets import QListWidgetItem

class TaskListUI:
    def __init__(self,ui,task):
        self.super_ui = ui
        self.task = task

        self.ui_form = Ui_TaskList()

        self.button_binding()
        self.install_settings()

    def button_binding(self):
        self.ui_form.ui.button_add_new_task.clicked.connect(lambda: self.super_ui.show_form(form='add_task'))
        self.ui_form.ui.del_button.clicked.connect(self.del_task_button)
        self.ui_form.ui.comboBox.currentIndexChanged.connect(lambda: self.update_list())
        self.ui_form.ui.comboBox_2.currentIndexChanged.connect(lambda: self.update_list())

    def install_settings(self):
        self.ui_form.ui.comboBox.setCurrentText('Все')
        self.ui_form.ui.comboBox_2.setCurrentText('Все')
        self.ui_form.setFixedSize(330, 260)

    def del_task_button(self):
        select_item = self.get_data_from_form()
        if select_item is not None:

            task_id = self.super_ui.task_ids_from_the_database['ItemTaskId'][select_item]['id']
            self.task.delete(task_id=task_id)
            self.update_list()


    def get_data_from_form(self):
        current_item = self.ui_form.ui.listWidget.currentItem()
        if current_item is not None:
            return self.ui_form.ui.listWidget.row(current_item)
        return None

    def update_list(self):

        get_type_select, get_timeframe_select = self.get_data_from_comboBox()
        tasks = self.task.get(type_task=get_type_select, timeframes=get_timeframe_select)

        self.ui_form.ui.listWidget.clear()
        self.super_ui.task_ids_from_the_database['ItemTaskId'] = list('')

        for idd,item in enumerate(tasks['Tasks']):
            task_id = dict()
            task_id['id'] = item['id']
            self.super_ui.task_ids_from_the_database['ItemTaskId'].append(task_id)
            newtask_item = QListWidgetItem(self.ui_form.ui.listWidget)
            newtask_item.setCheckState(Qt.Unchecked)
            newtask_item.setText(QCoreApplication.translate("MainWindow", f"{item['name']}", None))


    def get_data_from_comboBox(self):
        selected = self.ui_form.ui.comboBox.currentIndex()
        selected_2 = self.ui_form.ui.comboBox_2.currentIndex()

        return selected, selected_2
