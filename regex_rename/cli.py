import os
import re

from cement.core import controller, foundation, handler

class RenamerBaseController(controller.CementBaseController):
    class Meta(object):
        label = 'base'
        arguments = [
            (['--regex', '-r'], {
                'help': 'Regular expression to match.',
                'required': True}),
            (['--template', '-t'], {
                'help': ('python format string. match groups from '
                         'regex will be passed as parameters.'),
                'required': True}),
            (['--dry-run', '-n'], {
                'help': ('Print what would be done rather than '
                         'actually renaming'),
                'action': 'store_true'}),
            (['files'], {
                'help': 'Files to rename',
                'nargs': '+'}),
        ]

    @controller.expose(hide=True)
    def default(self):
        pattern = re.compile(self.app.pargs.regex)
        for file_name in self.app.pargs.files:
            if not os.path.exists(file_name):
                self.app.log.warn('File %r not found' % (file_name,))
                continue
            match = pattern.match(file_name)
            if not match:
                self.app.log.info('File %r does not match regex %r' % (
                                      file_name, self.app.pargs.regex))
                continue
            destination = self.app.pargs.template % match.groups()
            if self.app.pargs.dry_run:
                print('%r -> %r' % (file_name, destination))
            else:
                os.rename(file_name, destination)

class RenamerApp(foundation.CementApp):
    class Meta(object):
        label = 'RegexRenamer'
        handlers = [RenamerBaseController]

def main():
    with RenamerApp() as app:
        app.run()

