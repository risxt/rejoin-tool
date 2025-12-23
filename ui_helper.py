#!/usr/bin/env python3
"""
UI Helper for Rejoin Tool
Uses pyfiglet and rich for beautiful terminal output
"""

import sys
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.table import Table

try:
    import pyfiglet
except ImportError:
    pyfiglet = None

console = Console()

def print_banner(title="REJOIN TOOL", version="1.0.0"):
    """Print a fancy banner"""
    if pyfiglet:
        fig = pyfiglet.Figlet(font='slant')
        banner_text = fig.renderText(title)
    else:
        banner_text = f"=== {title} ==="
    
    console.print(Panel(
        Text(banner_text, style="bold green"),
        title=f"Version: {version}",
        border_style="green"
    ))

def print_packages(packages):
    """Print packages in a nice table"""
    table = Table(title="Discovered Packages", border_style="cyan")
    table.add_column("#", style="yellow", justify="center")
    table.add_column("Package Name", style="white")
    
    for i, pkg in enumerate(packages, 1):
        table.add_row(str(i), pkg)
    
    console.print(table)

def print_status(package, status, running=True):
    """Print package status"""
    if running:
        console.print(f"  [green]✓[/green] {package} - [green]Running[/green]")
    else:
        console.print(f"  [red]✗[/red] {package} - [red]NOT RUNNING![/red]")

def print_info(message):
    """Print info message"""
    console.print(f"[yellow][i][/yellow] {message}")

def print_error(message):
    """Print error message"""
    console.print(f"[red][!][/red] {message}")

def print_success(message):
    """Print success message"""
    console.print(f"[green][✓][/green] {message}")

if __name__ == "__main__":
    # Test the UI elements
    print_banner()
    print_packages(["com.roblox.clientv", "com.roblox.clientw", "com.roblox.clientx"])
    print_info("This is an info message")
    print_error("This is an error message")
    print_success("This is a success message")
