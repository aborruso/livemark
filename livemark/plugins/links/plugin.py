from copy import deepcopy
from ...plugin import Plugin


class LinksPlugin(Plugin):
    name = "links"
    priority = 10
    profile = {
        "type": "object",
        "properties": {
            "items": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "name": {"type": "string"},
                        "path": {"type": "string"},
                    },
                },
            },
        },
    }

    # Context

    @Plugin.property
    def items(self):
        github = self.document.get_plugin("github")
        items = deepcopy(self.config.get("items", []))
        if github:
            items.append({"name": "Report", "path": github.report_url})
            items.append({"name": "Fork", "path": github.fork_url})
            items.append({"name": "Edit", "path": github.edit_url})
        return items

    # Process

    def process_markup(self, markup):
        if self.items:
            markup.add_style("style.css")
            markup.add_markup("markup.html", target="#livemark-right")
