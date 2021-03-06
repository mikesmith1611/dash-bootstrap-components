from pathlib import Path

import dash_core_components as dcc
import dash_html_components as html

from ...api_doc import ApiDoc
from ...helpers import (
    ExampleContainer,
    HighlightedSource,
    load_source_with_environment,
)
from ...metadata import get_component_metadata
from .simple import tab1_content, tab2_content
from .simple import tabs as tabs_simple

HERE = Path(__file__).parent

tabs_simple_source = (HERE / "simple.py").read_text()
tabs_active_source = (HERE / "active_tab.py").read_text()
tabs_card_source = (HERE / "card.py").read_text()


def get_content(app):
    return [
        html.H2("Tabs", className="display-4"),
        html.P(
            "A self-contained tabs component with Bootstrap styles.",
            className="lead",
        ),
        html.H4("Tabs as children"),
        html.P(
            dcc.Markdown(
                "The easiest way to use `Tabs` is to pass it one or more "
                "`Tab` components as children. Use the `label` argument to "
                "specify the label in the tab. `Tabs` will automatically "
                "switch between tabs for you by displaying and hiding the "
                "content of each `Tab` below the tab pane."
            )
        ),
        ExampleContainer(tabs_simple),
        HighlightedSource(tabs_simple_source),
        html.H4("Tabs with callback"),
        html.P(
            dcc.Markdown(
                "You can also use the `active_tab` prop of `Tabs` in a "
                "callback to switch between tabs. This is useful if you want "
                "to have content recalculated / recomputed when you switch "
                "tabs, or if you want to have the active tab affect something "
                "on the page that isn't positioned directly below the tab "
                "pane."
            )
        ),
        ExampleContainer(
            load_source_with_environment(
                tabs_active_source,
                "tabs",
                {
                    "app": app,
                    "tab1_content": tab1_content,
                    "tab2_content": tab2_content,
                },
            )
        ),
        HighlightedSource(tabs_active_source),
        html.H4("Tabs in Cards"),
        html.P(
            dcc.Markdown(
                "Use `card=True` when placing your `Tabs` inside a "
                "`CardHeader`. You must use a callback to insert the tab "
                "content into the card body rather than relying on the tabs "
                "as children approach outlined above."
            )
        ),
        ExampleContainer(
            load_source_with_environment(
                tabs_card_source, "card", {"app": app}
            )
        ),
        HighlightedSource(tabs_card_source),
        ApiDoc(
            get_component_metadata("src/components/tabs/Tabs.js"),
            component_name="Tabs",
        ),
        ApiDoc(
            get_component_metadata("src/components/tabs/Tab.js"),
            component_name="Tab",
        ),
    ]
