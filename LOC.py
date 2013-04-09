import re
import sublime
import sublime_plugin


class LocCommand(sublime_plugin.EventListener):
    def on_modified(self, view):
        chars = view.size()
        region = sublime.Region(0, chars)
        contents = view.substr(region)

        # total number of lines
        loc = len(view.lines(region))

        sloc = 0
        # find all non-empty lines
        pattern = re.compile(r"^\s*(\S+).*$", re.MULTILINE)
        for m in pattern.finditer(contents):
            syntax = view.scope_name(m.start(1))
            # does the line start with a comment?
            if syntax.find('comment') < 0:
                sloc += 1

        view.set_status("loc", "Lines: %d (SLOC: %d)" % (loc, sloc))
