from datetime import datetime, timedelta

class Task:

    def __init__(self):
        self.database = None
        self.type_task_names = {0: 'everyday',
                                1:'home',
                                2:'job',
                                3:'all'}
        self.type_task_names_reverse = {v: k for k, v in self.type_task_names.items()}

        self.filter_timeframe_name = {0: 'today',
                                      1:'week',
                                      2:'month',
                                      3:'all'}

    def get(self, type_task=0, timeframes=0, where=None) -> dict:

        if where is None:
            tasks: dict[str, list] = {"Tasks": []}

            type_select = self.type_task_names[type_task]
            timeframe = self.filter_timeframe_name[timeframes]
            end_date = self.filter_timeframe(timeframe)
            today_start, today_end, now = self.set_start_and_end_today()

            task_list = self.database.get_task_data()

            for idd, item in enumerate(task_list['TaskList']):
                is_task_type_valid = (type_select == 'all' or item['type'] == type_select)
                is_due_date_valid = (end_date is None or
                                     datetime.combine(item['date'], datetime.min.time()) <= end_date)
                is_timeframe_valid = (timeframe != 'today' or
                                      (today_start.date() <= item['date'] <= today_end.date()))

                if is_task_type_valid and is_due_date_valid and is_timeframe_valid:
                    tasks['Tasks'].append(item)

            return tasks
        task = self.database.get_task_data(selection=where)
        return task


    def add(self,task_name,text,type_task,date):

        self.database.insert(
            task_name=task_name,
            text=text,
            type_task=type_task,
            date=date
        )

    def update(self,task_id,name,text,date,type_task):

        self.database.update(
            task_id=task_id,
            name=name,
            text=text,
            date=date,
            type_task=type_task
        )

    def delete(self,task_id):
        self.database.delete(task_id)

    def filter_timeframe(self,timeframe:str):

        n, today_end, now = self.set_start_and_end_today()
        if timeframe == 'week':
            end_date = now + timedelta(weeks=1)
        elif timeframe == 'month':
            end_date = now + timedelta(weeks=4)
        elif timeframe == 'today':
            end_date = today_end
        elif timeframe == 'all':
            end_date = None

        return end_date

    def set_start_and_end_today(self):
        now = datetime.now()
        today_start = now.replace(hour=0, minute=0, second=0, microsecond=0)
        today_end = now.replace(hour=23, minute=59, second=59, microsecond=999999)

        return today_start, today_end, now