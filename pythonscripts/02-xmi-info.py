import xmi
import json
from rich import print
from rich.console import Console

XMI = "RACFURY.XMIT"
xmi_object = xmi.open_file(XMI)

console = Console()

js = json.loads(xmi_object.get_json())
console.clear()

for key in js:
    if key in ['file', 'CONFIG']:
        # let's skip these for the demo
        continue
    console.print(f"Displaying {key} record for {XMI}")
    console.print(js[key])
    goon = console.input("[dim]ENTER for the next record[/]")
