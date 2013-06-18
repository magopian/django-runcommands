# -*- coding: utf-8 -*-

from __future__ import unicode_literals, absolute_import, division

from subprocess import check_output, STDOUT

from django.core.exceptions import ImproperlyConfigured
from django.views.generic import TemplateView


def run_command(command):
    """Run a system command, and return the output."""
    args = command.split()
    output = check_output(args, stderr=STDOUT)
    return output.decode()


class RunCommandView(TemplateView):
    """Add a new article."""
    command = None
    command_runner = None
    template_name = 'runcommands/command.html'

    def get_command(self):
        """Return the command."""
        if self.command is None:
            raise ImproperlyConfigured(
                "RunCommandView requires either a definition of 'command' or "
                "an implementation of 'get_command()'")
        else:
            return self.command

    def get_context_data(self, **kwargs):
        """Set the command output in the context."""
        context = super(RunCommandView, self).get_context_data(**kwargs)
        command = self.get_command()
        runner = self.command_runner or run_command
        context['command_output'] = runner(command)
        return context
