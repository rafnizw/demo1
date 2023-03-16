from __future__ import absolute_import, division, print_function
__metaclass__ = type

from ansible.plugins.callback import CallbackBase

class CallbackModule(CallbackBase):
    CALLBACK_VERSION = 2.0
    CALLBACK_NAME = 'numbered_tasks'
    CALLBACK_NEEDS_WHITELIST = True

    def __init__(self):
        super(CallbackModule, self).__init__()
        self.task_count = 0

    def v2_playbook_on_task_start(self, task, is_conditional):
        self.task_count += 1
        self._display.display("Task {}: {}".format(self.task_count, task.get_name()), color='bright_blue')
