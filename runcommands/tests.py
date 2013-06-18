# -*- coding: utf-8 -*-

from __future__ import unicode_literals, absolute_import, division

from django.core.exceptions import ImproperlyConfigured
from django.utils.unittest import TestCase

from .views import RunCommandView, run_command


class RunCommandTest(TestCase):

    def test_run_command(self):
        """run_command runs the command and returns the output."""
        output = run_command('echo Hello World')
        self.assertEqual(output.strip(), 'Hello World')


class RunCommandViewTest(TestCase):

    def test_get_command(self):
        """RunCommand.get_command() returns the command set for this slug."""
        view = RunCommandView(command='foo')
        command = view.get_command()
        self.assertEqual(command, 'foo')

    def test_get_command_not_set(self):
        """RunCommand.get_command() raises ImproperlyConfigured if no command
        has been set."""
        view = RunCommandView()
        with self.assertRaises(ImproperlyConfigured):
            view.get_command()

    def test_get_context_data(self):
        """RunCommand.get_context_data() sets the command output."""
        view = RunCommandView(command='foo')
        view.command_runner = lambda command: command  # return argument
        view.get_command = lambda: 'foo output'
        context = view.get_context_data()
        self.assertEqual(context['command_output'], 'foo output')
