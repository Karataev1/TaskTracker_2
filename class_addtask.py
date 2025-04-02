from user_interface import Ui_AddTask
from PySide6.QtCore import QDate

class AddTaskUI:
    def __init__(self,ui,task,parent_form):
        self.super_ui = ui
        self.parent_form = parent_form
        self.task = task

        self.ui_form = Ui_AddTask(self.parent_form.ui_form)
        self.ui_form.ui.setModal(True)

        self.button_binding()
        self.install_settings()

        today = QDate.currentDate()
        self.ui_form.ui.input_date_task_box.setDate(today)

    def button_binding(self):
        self.ui_form.ui.button_add_task.clicked.connect(self.add_task_button)

    def install_settings(self):  # установка подсказок для lineEdit и прочее
        self.ui_form.ui.input_taskname_line.setPlaceholderText('enter a new task')
        self.ui_form.ui.input_addinfo_textline.setPlaceholderText('enter additional information')
        self.ui_form.ui.input_date_task_box.setCalendarPopup(True)
        self.ui_form.setFixedSize(270, 205)

    def add_task_button(self):

        input_name_task, input_text, type_task, date = self.get_data_from_form()
        if input_name_task:

            type_task = self.task.type_task_names[type_task]
            self.task.add(task_name=input_name_task,
                          type_task=type_task,
                          text=input_text,
                          date=date)
            self.clear_input_forms()
            self.parent_form.update_list()
            self.ui_form.hide()


    def get_data_from_form(self):
        input_name_task = self.ui_form.ui.input_taskname_line.text()
        input_text = self.ui_form.ui.input_addinfo_textline.toPlainText()
        type_task = self.ui_form.ui.input_type_task_box.currentIndex()
        date = self.ui_form.ui.input_date_task_box.date()
        date = date.toString("yyyy-MM-dd")

        return input_name_task, input_text, type_task, date

    def clear_input_forms(self):
        self.ui_form.ui.input_taskname_line.clear()
        self.ui_form.ui.input_addinfo_textline.clear()