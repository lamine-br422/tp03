from __future__ import annotations
from pathlib import Path
from typing import Any, Dict
from ui.web_ui import WebUI


from interfaces.storage_interface import StorageInterface
from interfaces.ui_interface import UIInterface
from storage.json_storage import JSONStorage
from ui.web_ui import WebUI


def run_application(storage: StorageInterface, ui: UIInterface) -> None:
    members = storage.load_members()
    events = storage.load_events()
    subscriptions = storage.load_subscriptions()
    donations = storage.load_donations()

    project: Dict[str, Any] = {
        "members": members,
        "events": events,
        "subscriptions": subscriptions,
        "donations": donations,
    }

    ui.show_dashboard(project)


if __name__ == "__main__":
    base_dir = Path(__file__).parent
    data_dir = base_dir / "data"
    out_file = base_dir / "site" / "madrassa.html"

    storage: StorageInterface = JSONStorage(data_dir)
    ui: UIInterface = WebUI(out_file)

    run_application(storage, ui)
