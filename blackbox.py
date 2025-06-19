from rich.console import Console
from time import sleep
import random

console = Console()

def simulate_hack():
    console.print("[bold cyan]Initializing BlackBox V1...[/bold cyan]")
    sleep(1)
    console.print("[green]Connecting to target...[/green]")
    sleep(1)

    target = random.choice(["govnet.sec", "xcorp.infra", "cloudlink.io"])
    console.print(f"[yellow]Target locked: {target}[/yellow]")
    sleep(1.5)

    console.print("[bold magenta]Launching exploit chain...[/bold magenta]")
    for i in range(5):
        console.print(f"[red]→ Breaching Layer {i+1}[/red]")
        sleep(0.7)

    console.print("[bold green]Access granted.[/bold green]")
    sleep(0.5)
    console.print("[blue]Dumping credentials:[/blue]")
    sleep(0.8)

    creds = {
        "admin@xcorp.infra": "r00tPass!321",
        "it@govnet.sec": "admin1234!",
        "ops@cloudlink.io": "P@ssw0rd!"
    }
    for user, pwd in creds.items():
        console.print(f"[white]- {user} : {pwd}[/white]")
        sleep(0.5)

    console.print("\n[bold red]WARNING: You are being traced...[/bold red]")
    for i in range(5, 0, -1):
        console.print(f"Trace in: {i}...")
        sleep(1)

    console.print("[green]Trace evaded. BlackBox cloaked.[/green]")
