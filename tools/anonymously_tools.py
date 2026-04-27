"""Anonymity and privacy tools module for hackingtool.

This module provides tools for anonymous browsing, VPN management,
proxy configuration, and related privacy utilities.
"""

from tools.base_tool import HackingTool, HackingToolsCollection


class Anonsurf(HackingTool):
    """AnonSurf - Anonymous mode for Kali Linux."""

    TITLE = "AnonSurf"
    DESCRIPTION = "Anonymize the entire system via Tor"
    INSTALL_COMMANDS = [
        "git clone https://github.com/Und3rf10w/kali-anonsurf.git",
        "cd kali-anonsurf && chmod +x installer.sh && sudo ./installer.sh",
    ]
    PROJECT_URL = "https://github.com/Und3rf10w/kali-anonsurf"

    def __init__(self):
        super().__init__(installable=True, runnable=True)

    def run(self):
        """Launch AnonSurf interactive menu."""
        import subprocess
        subprocess.call(["anonsurf"])


class Multitor(HackingTool):
    """MultiTor - Use multiple Tor instances with a load balancing."""

    TITLE = "MultITor"
    DESCRIPTION = "Multi-threaded Tor proxy with load balancing"
    INSTALL_COMMANDS = [
        "git clone https://github.com/bhavesh-pardhi/multitor.git",
        "cd multitor && chmod +x setup.sh && sudo ./setup.sh",
    ]
    PROJECT_URL = "https://github.com/bhavesh-pardhi/multitor"

    def __init__(self):
        super().__init__(installable=True, runnable=True)

    def run(self):
        """Launch MultITor."""
        import subprocess
        subprocess.call(["multitor", "--help"])


class Anonip(HackingTool):
    """Anonip - IP address anonymizer for log files."""

    TITLE = "Anonip"
    DESCRIPTION = "Anonymize IP addresses in log files"
    INSTALL_COMMANDS = ["pip3 install anonip"]
    PROJECT_URL = "https://github.com/DigitaleGesellschaft/anonip"

    def __init__(self):
        super().__init__(installable=True, runnable=True)

    def run(self):
        """Show anonip usage."""
        import subprocess
        subprocess.call(["anonip", "--help"])


class TorBrowser(HackingTool):
    """Tor Browser - Anonymous web browsing."""

    TITLE = "Tor Browser"
    DESCRIPTION = "Anonymous web browser using the Tor network"
    INSTALL_COMMANDS = [
        "sudo apt-get install -y torbrowser-launcher",
    ]
    PROJECT_URL = "https://www.torproject.org"

    def __init__(self):
        super().__init__(installable=True, runnable=True)

    def run(self):
        """Launch Tor Browser."""
        import subprocess
        subprocess.Popen(["torbrowser-launcher"])


class Proxychain(HackingTool):
    """ProxyChains - Route traffic through proxy servers."""

    TITLE = "ProxyChains"
    DESCRIPTION = "Force any TCP connection through proxy servers"
    INSTALL_COMMANDS = [
        "sudo apt-get install -y proxychains4",
    ]
    PROJECT_URL = "https://github.com/haad/proxychains"

    def __init__(self):
        super().__init__(installable=True, runnable=False)

    def run(self):
        """Show proxychains configuration info.

        Note: proxychains4 config is typically at /etc/proxychains4.conf.
        Edit that file to add your proxy servers before use.
        """
        import subprocess
        # Print the config file location as a helpful reminder
        print("[*] ProxyChains config file: /etc/proxychains4.conf")
        subprocess.call(["proxychains4", "-h"])
