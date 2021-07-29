from ...plugin import Plugin


class TocPlugin(Plugin):
    priority = 80
    profile = {
        "type": "object",
        "properties": {
            "selector": {"type": "string"},
        },
    }

    def process_markup(self, markup):
        config = markup.document.config.get(self.name, {})
        if not config:
            return

        # Prepare context
        selector = config.get("selector", "h2, h3")

        # Update markup
        markup.add_style("https://unpkg.com/tocbot@4.12.3/dist/tocbot.css")
        markup.add_style("style.css")
        markup.add_script("https://unpkg.com/tocbot@4.12.3/dist/tocbot.min.js")
        markup.add_script("script.js", selector=selector)
        markup.add_markup(
            "markup.html",
            target="#livemark-left",
        )
